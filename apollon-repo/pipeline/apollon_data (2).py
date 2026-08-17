#!/usr/bin/env python3
"""
APOLLON — Pipeline de données
=============================
Collecte les séries de marché et macro, calcule le régime, archive l'historique.

Tourne sur VOTRE machine (le conteneur cloud n'a pas accès aux API financières).

Installation
------------
    pip install requests pandas

Clé FRED (gratuite, 30 secondes)
--------------------------------
    https://fredaccount.stlouisfed.org/apikeys
    export FRED_API_KEY="votre_cle"        # ajoutez-le à votre ~/.zshrc

Usage
-----
    python3 apollon_data.py                # instantané du jour
    python3 apollon_data.py --history 5    # + 5 ans d'historique
    python3 apollon_data.py --factors      # + facteurs Fama-French

Sorties (dans ./data/)
----------------------
    snapshot_YYYY-MM-DD.json    instantané machine
    snapshot_YYYY-MM-DD.md      instantané lisible
    history/<SERIE>.csv         historique accumulé, jamais écrasé
    regime_log.csv              journal du régime, une ligne par exécution
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import os
import sys
import zipfile
from datetime import date, datetime, timedelta
from pathlib import Path

try:
    import requests
except ImportError:
    sys.exit("Manque requests.  ->  pip install requests pandas")

BASE = Path(__file__).resolve().parent
DATA = BASE / "data"
HIST = DATA / "history"
for d in (DATA, HIST):
    d.mkdir(parents=True, exist_ok=True)

FRED_KEY = os.environ.get("FRED_API_KEY", "").strip()
FRED_URL = "https://api.stlouisfed.org/fred/series/observations"

# --- SÉRIES OBLIGATOIRES (règle R-028) --------------------------------------
# Toute série de cette liste absente de la collecte interdit la production d'un
# brief. Une lacune sur l'une d'elles n'est jamais une « réserve de méthode » :
# c'est un échec de collecte. Origine : faute F-5 de la note Astra 005 — cinq
# séries déclarées indisponibles étaient obtenables en une requête, dont deux
# chez le fournisseur de rang 1 du fonds.
SERIES_OBLIGATOIRES = {
    "DGS2", "DGS10", "DGS30", "T10Y2Y", "DFII10", "T10YIE",
    "CPIAUCSL", "CPILFESL", "UNRATE", "PAYEMS",
    "VIXCLS", "VXVCLS", "SP500", "DFF",
}

# ---------------------------------------------------------------- séries FRED
# code FRED -> (libellé, unité, section propriétaire)
SERIES: dict[str, tuple[str, str, str]] = {
    # M1 — Banques centrales & taux
    "DFF":            ("Fed funds effectif",            "%",    "M1"),
    "DGS2":           ("Treasury 2 ans",                "%",    "M1"),
    "DGS10":          ("Treasury 10 ans",               "%",    "M1"),
    "DGS30":          ("Treasury 30 ans",               "%",    "M1"),
    "T10Y2Y":         ("Pente 2s10s",                   "%",    "M1"),
    "DFII10":         ("Taux réel 10 ans (TIPS)",       "%",    "M1"),
    "T10YIE":         ("Point mort inflation 10 ans",   "%",    "M1"),
    "T5YIFR":         ("Point mort 5 ans dans 5 ans",   "%",    "M1"),
    # M2 — Cycle & données
    "CPIAUCSL":       ("CPI global",                    "idx",  "M2"),
    "CPILFESL":       ("CPI cœur",                      "idx",  "M2"),
    "UNRATE":         ("Taux de chômage",               "%",    "M2"),
    "PAYEMS":         ("Emploi non agricole",           "milliers", "M2"),
    "INDPRO":         ("Production industrielle",       "idx",  "M2"),
    # M3 — Énergie & matières premières
    "DCOILBRENTEU":   ("Brent",                         "$",    "M3"),
    "DCOILWTICO":     ("WTI",                           "$",    "M3"),
    # M4 — Devises
    "DEXUSEU":        ("EUR/USD",                       "",     "M4"),
    "DEXJPUS":        ("USD/JPY",                       "",     "M4"),
    "DTWEXBGS":       ("Indice dollar large",           "idx",  "M4"),
    # RISQUE — régime
    "VIXCLS":         ("VIX 30 jours",                  "",     "RISQUE"),
    "VXVCLS":         ("VIX3M — 3 mois",                "",     "RISQUE"),
    "VXDCLS":         ("VXD — Dow",                     "",     "RISQUE"),
    "OVXCLS":         ("OVX — volatilité pétrole",      "",     "RISQUE"),
    "BAMLH0A0HYM2":   ("Spread haut rendement OAS",     "%",    "RISQUE"),
    "BAMLC0A0CM":     ("Spread investment grade OAS",   "%",    "RISQUE"),
    "SP500":          ("S&P 500",                       "idx",  "RISQUE"),
    "NASDAQ100":      ("Nasdaq 100",                    "idx",  "RISQUE"),
}


# ---------------------------------------------------------------- collecte
def fred(series_id: str, start: str | None = None,
         vintage: bool = False) -> list[tuple[str, float]]:
    """Retourne [(date, valeur), ...] pour une série FRED.

    `vintage=True` demande les valeurs TELLES QUE CONNUES à l'époque
    (ALFRED), et non la version révisée d'aujourd'hui. Voir le bloc
    ci-dessous : sans cela, tout test hors échantillon sur une série
    révisable est optimiste.
    """
    if not FRED_KEY:
        raise RuntimeError(
            "FRED_API_KEY absente.\n"
            "  1. https://fredaccount.stlouisfed.org/apikeys  (gratuit)\n"
            '  2. export FRED_API_KEY="votre_cle"'
        )
    params = {
        "series_id": series_id,
        "api_key": FRED_KEY,
        "file_type": "json",
        "observation_start": start or (date.today() - timedelta(days=400)).isoformat(),
    }
    # ------------------------------------------------------------------
    # BIAIS D'ANTICIPATION PAR RÉVISION — le plus discret du dispositif.
    #
    # PAYEMS, INDPRO, CPIAUCSL sont RÉVISÉES, parfois lourdement. Sans
    # paramètre temps réel, FRED renvoie la version RÉVISÉE D'AUJOURD'HUI
    # pour TOUTE l'histoire. Un signal daté du 15 mars 2024 est alors
    # calculé sur un chiffre d'emploi qui n'existait pas le 15 mars 2024.
    #
    # Le test hors échantillon de la Section Trading et le critère 16 de
    # la Section Macro mesurent tous deux des rendements futurs à partir
    # d'états passés : sur données révisées, ils SURESTIMENT.
    #
    # `vintage=True` demande à ALFRED la valeur telle qu'elle était CONNUE
    # à sa date d'observation. C'est plus lent et plus lourd, donc c'est
    # une option déclarée — mais toute conclusion tirée de séries révisées
    # doit porter la mention correspondante.
    # ------------------------------------------------------------------
    if vintage:
        # output_type=4 — « Observations, Initial Release Only » : la valeur
        # TELLE QUE PUBLIÉE la première fois, dans la structure normale
        # {date, value}.
        #
        # FAUTE CORRIGÉE, ET ELLE A COÛTÉ UN CYCLE. J'avais écrit
        # output_type=2 (« Observations by Vintage Date, All Observations »),
        # qui renvoie UNE COLONNE PAR MILLÉSIME — une structure que
        # l'analyseur ci-dessous ne sait pas lire. Il ne levait pas
        # d'exception : il ne trouvait simplement aucun champ `value`, et
        # retournait une liste VIDE pour CHAQUE série. La collecte
        # réussissait en apparence et ne ramenait rien.
        #
        # R-053 — Un changement de paramètre qui modifie la FORME de la
        # réponse doit être vérifié sur une réponse réelle, jamais déduit
        # de la documentation. Et un analyseur qui ne reconnaît aucun champ
        # doit le DIRE, pas rendre une liste vide (voir le garde-fou plus bas).
        params["output_type"] = 4

    try:
        r = requests.get(FRED_URL, params=params, timeout=25)
        r.raise_for_status()
        obs = r.json().get("observations", [])
    except Exception as exc:                                  # noqa: BLE001
        print(f"  ! {series_id}: {exc}", file=sys.stderr)
        return []
    out = []
    for o in obs:
        v = o.get("value", ".")
        if v not in (".", "", None):
            try:
                out.append((o["date"], float(v)))
            except (ValueError, KeyError):
                continue

    # R-053 — « la réponse est vide » et « je ne sais pas lire cette réponse »
    # ne peuvent pas produire le même silence. Si le serveur a renvoyé des
    # lignes et qu'aucune n'est exploitable, la forme a changé : on le dit,
    # et en mode millésime on retombe sur la requête standard plutôt que de
    # rendre une série vide qui ferait échouer tout l'aval.
    if obs and not out:
        champs = sorted({k for o in obs[:3] if isinstance(o, dict) for k in o})
        print(f"  ! {series_id}: {len(obs)} lignes reçues, AUCUNE exploitable — "
              f"champs vus : {champs}", file=sys.stderr)
        if vintage:
            print(f"    repli sur la requête standard (valeurs RÉVISÉES) "
                  f"pour {series_id}", file=sys.stderr)
            return fred(series_id, start, vintage=False)
    return out


def archive(series_id: str, rows: list[tuple[str, float]]) -> None:
    """Fusionne dans history/<serie>.csv sans jamais perdre l'existant."""
    path = HIST / f"{series_id}.csv"
    merged: dict[str, float] = {}
    if path.exists():
        with path.open(newline="", encoding="utf-8") as fh:
            for rec in csv.DictReader(fh):
                try:
                    merged[rec["date"]] = float(rec["value"])
                except (KeyError, ValueError):
                    continue
    merged.update(dict(rows))
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["date", "value"])
        for d in sorted(merged):
            w.writerow([d, merged[d]])


# ---------------------------------------------------------------- régime
def sma(values: list[float], window: int) -> float | None:
    return sum(values[-window:]) / window if len(values) >= window else None


def classify(latest: dict[str, float], series: dict[str, list[tuple[str, float]]]) -> dict:
    """Classificateur de régime — 4 axes, seuils fixés dans la doctrine."""
    r: dict[str, str | None] = {}

    # Axe 1 — volatilité
    vix = latest.get("VIXCLS")
    r["volatilite"] = None if vix is None else (
        "BASSE" if vix < 15 else "MOYENNE" if vix <= 25 else "HAUTE"
    )

    # Axe 2 — courbe
    sp = latest.get("T10Y2Y")
    r["courbe"] = None if sp is None else (
        "INVERSEE" if sp < 0 else "PLATE" if sp < 0.5 else "PENTUE"
    )

    # Axe 3 — tendance (S&P vs moyenne 200 séances)
    spx = [v for _, v in series.get("SP500", [])]
    ma200 = sma(spx, 200)
    r["tendance"] = None
    if ma200 and spx:
        r["tendance"] = "HAUSSIERE" if spx[-1] > ma200 else "BAISSIERE"
        r["_spx_vs_ma200_pct"] = round((spx[-1] / ma200 - 1) * 100, 2)

    # Axe 4 — crédit (spread courant vs moyenne 60 séances)
    hy = [v for _, v in series.get("BAMLH0A0HYM2", [])]
    ma60 = sma(hy, 60)
    r["credit"] = None
    if ma60 and hy:
        r["credit"] = "ELARGISSEMENT" if hy[-1] > ma60 else "RESSERREMENT"
        r["_hy_vs_ma60_pb"] = round((hy[-1] - ma60) * 100, 1)

    axes = [r.get("volatilite"), r.get("courbe"), r.get("tendance"), r.get("credit")]
    r["regime"] = " / ".join(a for a in axes if a) or "INDETERMINE"

    # Règle de couverture — doctrine partie III.8
    r["politique_couverture"] = None if vix is None else (
        "ACHAT SYSTEMATIQUE — protection bon marche" if vix < 15
        else "OPPORTUNISTE" if vix <= 25
        else "AUCUN ACHAT — trop chere ; vente de vol envisageable"
    )
    return r



# ------------------------------------------------- calendrier de publications
# E-050 bis — DEUX CRITÈRES DU PORTIER MACRO SONT MORTS PAR CONSTRUCTION.
# « Catalyseur identifié ET DATÉ » et « invalidation observable » ne peuvent
# être franchis par aucune donnée : le dépôt ne contenait que des séries.
# La Réserve fédérale de Saint-Louis publie pourtant les dates de publication
# À VENIR, avec la même clé. Il fallait la demander, pas la déclarer absente
# (R-028 : une lacune déclarée est une requête non lancée).
#
# PIÈGE, ET C'EST TOUT LE POINT : par défaut l'endpoint EXCLUT les dates
# futures. Sans include_release_dates_with_no_data=true, on récupère
# l'historique des publications passées et on croit avoir un calendrier.
RELEASES_URL = "https://api.stlouisfed.org/fred/releases/dates"

# Publications qui déplacent les marchés. Identifiants de RELEASE (pas de
# série) — stables, vérifiables sur fred.stlouisfed.org/releases/<id>.
RELEASES_SUIVIES = {
    10:  "Indice des prix à la consommation (CPI)",
    50:  "Situation de l'emploi (Employment Situation)",
    53:  "Produit intérieur brut (GDP)",
    13:  "Production industrielle et taux d'utilisation (G.17)",
    18:  "H.15 — taux d'intérêt sélectionnés",
    175: "Décisions du FOMC — communiqués",
}


def calendrier_publications(jours_avant: int = 400, jours_apres: int = 120) -> list[dict]:
    """Dates de publication PASSÉES ET FUTURES des releases suivies.

    Retourne [] en cas d'échec — jamais une exception : le calendrier est un
    enrichissement, il ne peut pas faire tomber la collecte des séries.
    """
    if not FRED_KEY:
        return []
    params = {
        "api_key": FRED_KEY,
        "file_type": "json",
        # SANS ce paramètre, aucune date future n'est renvoyée.
        "include_release_dates_with_no_data": "true",
        "realtime_start": (date.today() - timedelta(days=jours_avant)).isoformat(),
        "realtime_end":   (date.today() + timedelta(days=jours_apres)).isoformat(),
        "sort_order": "asc",
        "limit": 10000,
    }
    try:
        r = requests.get(RELEASES_URL, params=params, timeout=30)
        r.raise_for_status()
        brut = r.json().get("release_dates", [])
    except Exception as exc:                                  # noqa: BLE001
        print(f"  ! calendrier de publications : {exc}", file=sys.stderr)
        return []

    aujourdhui = date.today().isoformat()
    out = []
    for d in brut:
        rid = d.get("release_id")
        if rid not in RELEASES_SUIVIES:
            continue
        jour = d.get("date")
        if not jour:
            continue
        out.append({
            "release_id": rid,
            "intitule": RELEASES_SUIVIES[rid],
            "date": jour,
            "futur": jour > aujourdhui,
        })
    out.sort(key=lambda x: (x["date"], x["release_id"]))
    return out


def archiver_calendrier(evenements: list[dict]) -> dict:
    """Écrit data/calendrier_publications.csv et rend un compte-rendu.

    Le fichier est le SEUL objet du dépôt qui porte des faits datés dans le
    futur. Sans lui, le critère « catalyseur daté » ne peut pas exister.
    """
    chemin = DATA / "calendrier_publications.csv"
    fusion: dict[tuple, dict] = {}
    if chemin.exists():
        with chemin.open(newline="", encoding="utf-8") as fh:
            for ligne in csv.DictReader(fh):
                fusion[(ligne["release_id"], ligne["date"])] = ligne
    for e in evenements:
        fusion[(str(e["release_id"]), e["date"])] = {
            "release_id": str(e["release_id"]),
            "intitule": e["intitule"],
            "date": e["date"],
        }
    lignes = sorted(fusion.values(), key=lambda x: (x["date"], x["release_id"]))
    with chemin.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["release_id", "intitule", "date"])
        w.writeheader()
        w.writerows(lignes)

    aujourdhui = date.today().isoformat()
    futurs = [l for l in lignes if l["date"] > aujourdhui]
    prochaine = futurs[0] if futurs else None
    return {
        "fichier": str(chemin.relative_to(BASE)),
        "n_total": len(lignes),
        "n_futurs": len(futurs),
        "n_releases_suivies": len(RELEASES_SUIVIES),
        "prochaine_publication": prochaine,
        "calendrier_utilisable": bool(futurs),
        "motif_si_inutilisable": ("" if futurs else
            "aucune date future récupérée — vérifier que la requête porte bien "
            "include_release_dates_with_no_data=true, faute de quoi l'endpoint "
            "ne renvoie que le passé et le critère « catalyseur daté » reste mort"),
    }


# ---------------------------------------------------------------- facteurs
FF_URL = ("https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/"
          "F-F_Research_Data_5_Factors_2x3_daily_CSV.zip")


def fetch_factors() -> str | None:
    """Facteurs Fama-French 5 quotidiens — indispensables pour separer alpha et beta."""
    try:
        r = requests.get(FF_URL, timeout=60)
        r.raise_for_status()
        with zipfile.ZipFile(io.BytesIO(r.content)) as z:
            name = z.namelist()[0]
            raw = z.read(name).decode("utf-8", errors="ignore")
    except Exception as exc:                                  # noqa: BLE001
        print(f"  ! facteurs Fama-French: {exc}", file=sys.stderr)
        return None
    out = DATA / "fama_french_5_daily.csv"
    out.write_text(raw, encoding="utf-8")
    return str(out)


# ---------------------------------------------------------------- rendu
def to_markdown(snap: dict) -> str:
    L = [
        f"# Instantané Apollon — {snap['date']}",
        "",
        f"**Régime :** `{snap['regime']['regime']}`",
        f"**Politique de couverture :** {snap['regime'].get('politique_couverture') or 'n/d'}",
        "",
    ]
    alertes = snap.get("alertes_qualite") or []
    if alertes:
        L += ["> ## ⚠ ALERTES QUALITÉ — lire avant toute analyse", ">"]
        L += [f"> - {a}" for a in alertes]
        L += [">",
              "> Un percentile calculé sur une série tronquée n'a aucune valeur.",
              "> Toute analyse portant sur ces séries doit citer la profondeur réelle.",
              ""]
    L += [
        "## Axes de régime",
        "",
        "| Axe | État |",
        "|---|---|",
    ]
    for k in ("volatilite", "courbe", "tendance", "credit"):
        L.append(f"| {k.capitalize()} | {snap['regime'].get(k) or 'n/d'} |")

    for sec, titre in (("M1", "Banques centrales & taux"),
                       ("M2", "Cycle & données"),
                       ("M3", "Énergie & matières premières"),
                       ("M4", "Devises"),
                       ("RISQUE", "Risque & marchés")):
        rows = [(sid, d) for sid, d in snap["series"].items() if d["section"] == sec]
        if not rows:
            continue
        L += ["", f"## {sec} — {titre}", "",
              "| Série | Valeur | Date | Δ 1 j | Δ 20 j |", "|---|---:|---|---:|---:|"]
        for sid, d in rows:
            def f(x):
                return "—" if x is None else f"{x:+.2f}"
            L.append(f"| {d['label']} | {d['value']:.4g} {d['unit']} | "
                     f"{d['date']} | {f(d['chg_1d'])} | {f(d['chg_20d'])} |")

    L += ["", "---",
          f"*Généré le {datetime.now().isoformat(timespec='seconds')} · "
          f"source FRED · {len(snap['series'])} séries*",
          "*Document de recherche. Ne constitue pas un conseil en investissement.*"]
    return "\n".join(L)


# ---------------------------------------------------------------- main
def main() -> int:
    ap = argparse.ArgumentParser(description="Pipeline de données Apollon")
    ap.add_argument("--history", type=int, default=0,
                    help="années d'historique à récupérer (défaut : ~400 jours)")
    ap.add_argument("--factors", action="store_true",
                    help="télécharger aussi les facteurs Fama-French")
    ap.add_argument("--sans-calendrier", action="store_true",
                    help="ne pas collecter le calendrier de publications")
    ap.add_argument("--vintage", action="store_true",
                    help="valeurs telles que CONNUES à l'époque (ALFRED) plutôt "
                         "que révisées : supprime le biais d'anticipation par révision")
    args = ap.parse_args()

    start = None
    if args.history:
        start = (date.today() - timedelta(days=365 * args.history)).isoformat()

    print(f"APOLLON — collecte de {len(SERIES)} séries…\n")
    series_data: dict[str, list[tuple[str, float]]] = {}
    latest: dict[str, float] = {}
    snap_series: dict[str, dict] = {}

    alertes: list[str] = []

    for sid, (label, unit, section) in SERIES.items():
        rows = fred(sid, start, vintage=args.vintage)
        if not rows:
            print(f"  ✗ {sid:<15} {label}")
            alertes.append(f"{sid}: AUCUNE donnée récupérée")
            continue
        archive(sid, rows)
        series_data[sid] = rows
        vals = [v for _, v in rows]
        latest[sid] = vals[-1]

        # --- CONTRÔLE DE PROFONDEUR (règle R-011) -------------------------
        # FRED renvoie parfois moins d'historique que demandé, sans erreur.
        # Une profondeur silencieusement tronquée invalide tout percentile
        # calculé dessus. On la mesure, on la publie, on alerte.
        obtenu = rows[0][0]
        tronque = bool(start and obtenu > start)
        if tronque:
            alertes.append(
                f"{sid} ({label}) : demandé depuis {start}, obtenu depuis {obtenu} "
                f"— PERCENTILES NON FIABLES sur cette série"
            )

        snap_series[sid] = {
            "label": label, "unit": unit, "section": section,
            "value": vals[-1], "date": rows[-1][0],
            "chg_1d": round(vals[-1] - vals[-2], 4) if len(vals) > 1 else None,
            "chg_20d": round(vals[-1] - vals[-21], 4) if len(vals) > 20 else None,
            "debut_historique": obtenu,
            "n_observations": len(rows),
            "profondeur_tronquee": tronque,
        }
        flag = "  ⚠ TRONQUÉ" if tronque else ""
        print(f"  ✓ {sid:<15} {label:<32} {vals[-1]:>12.4g}   "
              f"({len(rows)} pts depuis {obtenu}){flag}")

    if not snap_series:
        print("\nAucune série récupérée. Vérifiez FRED_API_KEY et la connexion.",
              file=sys.stderr)
        return 1

    regime = classify(latest, series_data)
    snap = {
        "date": date.today().isoformat(),
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "regime": regime,
        "alertes_qualite": alertes,
        "series": snap_series,
    }

    # --- CONTRÔLE DES SÉRIES OBLIGATOIRES (R-028) ---------------------------
    manquantes = sorted(SERIES_OBLIGATOIRES - set(snap_series))
    snap["series_obligatoires_manquantes"] = manquantes
    snap["production_autorisee"] = not manquantes

    if alertes:
        print("\n" + "!" * 62)
        print("ALERTES QUALITÉ DES DONNÉES — à lire avant toute analyse")
        print("!" * 62)
        for a in alertes:
            print(f"  ⚠ {a}")

    if manquantes:
        print("\n" + "#" * 62)
        print("SÉRIES OBLIGATOIRES MANQUANTES — PRODUCTION DE BRIEF INTERDITE")
        print("#" * 62)
        for m in manquantes:
            print(f"  ✗ {m}")
        print("\nUne lacune sur une série obligatoire n'est pas une réserve de")
        print("méthode : c'est un échec de collecte. Corriger avant de produire.")

    if args.factors:
        print("\nFacteurs Fama-French…")
        p = fetch_factors()
        print(f"  {'✓ ' + p if p else '✗ échec'}")

    # Calendrier de publications — nourrit le critère « catalyseur daté »,
    # mort par construction tant qu'aucune date future n'existait au dépôt.
    if not args.sans_calendrier:
        print("\nCalendrier de publications (dates FUTURES incluses)…")
        cal = archiver_calendrier(calendrier_publications())
        snap["calendrier_publications"] = cal
        if cal["calendrier_utilisable"]:
            pr = cal["prochaine_publication"]
            print(f"  ✓ {cal['n_total']} dates dont {cal['n_futurs']} à venir "
                  f"sur {cal['n_releases_suivies']} publications suivies")
            print(f"    prochaine : {pr['date']} — {pr['intitule']}")
        else:
            print(f"  ✗ AUCUNE DATE FUTURE — {cal['motif_si_inutilisable']}")
            alertes.append(
                "CALENDRIER INUTILISABLE : aucune date de publication future. "
                "Le critère « catalyseur identifié et daté » de la Section Macro "
                "reste mort par construction.")

    stamp = snap["date"]
    (DATA / f"snapshot_{stamp}.json").write_text(
        json.dumps(snap, indent=2, ensure_ascii=False), encoding="utf-8")
    (DATA / f"snapshot_{stamp}.md").write_text(to_markdown(snap), encoding="utf-8")

    # journal du régime — une ligne par exécution, jamais écrasé
    log = DATA / "regime_log.csv"
    new = not log.exists()
    with log.open("a", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        if new:
            w.writerow(["date", "regime", "volatilite", "courbe", "tendance",
                        "credit", "vix", "hy_oas", "spx", "us10y", "pente_2s10s"])
        w.writerow([stamp, regime["regime"], regime.get("volatilite"),
                    regime.get("courbe"), regime.get("tendance"), regime.get("credit"),
                    latest.get("VIXCLS"), latest.get("BAMLH0A0HYM2"),
                    latest.get("SP500"), latest.get("DGS10"), latest.get("T10Y2Y")])

    print(f"\n{'=' * 62}")
    print(f"RÉGIME : {regime['regime']}")
    print(f"COUVERTURE : {regime.get('politique_couverture')}")
    print(f"{'=' * 62}")
    print(f"\n→ {DATA / f'snapshot_{stamp}.md'}")
    print(f"→ {DATA / f'snapshot_{stamp}.json'}")
    print(f"→ {log}   (journal du régime)")
    print(f"→ {HIST}/   ({len(snap_series)} séries archivées)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
