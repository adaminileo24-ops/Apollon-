#!/usr/bin/env python3
"""BANC DE TEST DE LA COLLECTE — la couche qui n'avait jamais été testée.

Quatre cycles perdus sur `apollon_data.py` (E-052, E-054, E-056, E-057).
Chaque faute est ici un cas de test. Un banc dont les cas viennent des
fautes réellement commises est un registre exécutable.

    python3 test_collecte.py
    python3 -O test_collecte.py      # R-046 : même comportement exigé
"""
from __future__ import annotations

import importlib.util
import pathlib
import sys
import tempfile
import traceback

BASE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(BASE))

from simulateur_fred import SimulateurFred, MENSUELLES     # noqa: E402

_RESULTATS: list[tuple[str, bool, str]] = []


def cas(titre):
    def deco(fn):
        def run():
            try:
                fn()
                _RESULTATS.append((titre, True, ""))
                print(f"  [OK ] {titre}")
            except AssertionError as e:
                _RESULTATS.append((titre, False, str(e)))
                print(f"  [ÉCHEC] {titre}\n          {e}")
            except Exception as e:                          # noqa: BLE001
                _RESULTATS.append((titre, False, f"{type(e).__name__}: {e}"))
                print(f"  [ÉCHEC] {titre}\n          {type(e).__name__}: {e}")
                traceback.print_exc()
        run.titre = titre
        _CAS.append(run)
        return run
    return deco


_CAS: list = []


def charger(mode: str = "nominal", **kw):
    """Charge une instance NEUVE d'apollon_data avec le simulateur branché."""
    spec = importlib.util.spec_from_file_location(
        f"_ad_{len(_CAS)}_{mode}", BASE / "apollon_data.py")
    ad = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = ad
    spec.loader.exec_module(ad)
    sim = SimulateurFred(mode, **kw)
    ad.requests = sim
    ad.FRED_KEY = "a" * 32
    return ad, sim


# =====================================================================
# 1. E-052 — la forme de la réponse
# =====================================================================

@cas("1a  réponse nominale => observations exploitables, '.' ignorés")
def t_nominal():
    ad, _ = charger()
    r = ad.fred("DGS10", "2016-01-01")
    assert len(r) > 2400, f"{len(r)} observations, attendu ~2500"
    assert all(isinstance(v, float) for _, v in r), "valeurs non converties"


@cas("1b  E-052 : forme inattendue => repli déclaré, JAMAIS une liste vide")
def t_forme_inattendue():
    ad, sim = charger("forme_millesime")
    r = ad.fred("PAYEMS", "2016-01-01", vintage=True)
    assert r, ("une réponse de forme inconnue a produit une liste vide : "
               "c'est exactement E-052")
    assert len(sim.appels) >= 2, "le repli n'a pas été tenté"


@cas("1c  JSON malformé => liste vide ET message, pas d'exception qui remonte")
def t_json_malforme():
    ad, _ = charger("json_malforme")
    assert ad.fred("DGS10", "2016-01-01") == []


@cas("1d  HTTP 500 => liste vide, la collecte continue")
def t_http_500():
    ad, _ = charger("http_500")
    assert ad.fred("DGS10", "2016-01-01") == []


# =====================================================================
# 2. E-054 / E-056 — LE MILLÉSIME NE PEUT JAMAIS FAIRE PERDRE UNE SÉRIE
# =====================================================================

@cas("2a  E-054 : série jamais révisée => AUCUNE requête millésime")
def t_pas_de_millesime_hors_perimetre():
    ad, sim = charger()
    ad.fred("DGS10", "2016-01-01", vintage=True)
    ots = [a.get("output_type") for a in sim.appels]
    assert 4 not in ots, (
        f"millésime demandé sur une série jamais révisée : {ots}. "
        f"Il ne supprime aucun biais et tronque l'historique (E-054).")


@cas("2b  E-056 : millésime VIDE => repli, la série n'est JAMAIS perdue")
def t_millesime_vide():
    ad, sim = charger("millesime_vide")
    for sid in sorted(MENSUELLES):
        r = ad.fred(sid, "2016-01-01", vintage=True)
        assert r, (f"{sid} PERDUE sur millésime vide — c'est E-056, "
                   f"les quatre séries de noyau disparues du dépôt")
        assert len(r) > 100, f"{sid} : {len(r)} obs seulement"


@cas("2c  E-054 : millésime TRONQUÉ (12 %) => repli sur la version complète")
def t_millesime_tronque():
    ad, _ = charger("millesime_tronque")
    r = ad.fred("PAYEMS", "2016-01-01", vintage=True)
    assert len(r) > 100, f"troncature non rattrapée : {len(r)} obs"


@cas("2d  PROPRIÉTÉ : sur les 5 modes, --vintage ne perd JAMAIS d'observation")
def t_propriete_millesime():
    """Le cas 2b teste un mode. Celui-ci teste la PROPRIÉTÉ sur tous.

    R-058 — un garde-fou se teste sur le cas le plus dégradé. Écrire un
    test par mode connu laisse passer le mode suivant ; écrire la
    propriété la ferme définitivement.
    """
    modes = ["nominal", "millesime_vide", "millesime_tronque", "forme_millesime"]
    for mode in modes:
        for sid in ("CPIAUCSL", "PAYEMS", "DGS10", "SP500"):
            ad, _ = charger(mode)
            avec = ad.fred(sid, "2016-01-01", vintage=True)
            ad2, _ = charger(mode)
            sans = ad2.fred(sid, "2016-01-01", vintage=False)
            assert len(avec) >= 0.80 * len(sans), (
                f"mode {mode}, {sid} : --vintage rend {len(avec)} obs contre "
                f"{len(sans)} sans. Une option d'amélioration ne peut jamais "
                f"faire perdre une donnée (R-058).")


# =====================================================================
# 3. LE CALENDRIER
# =====================================================================

@cas("3a  le calendrier demande explicitement les dates FUTURES")
def t_calendrier_parametre():
    ad, sim = charger()
    ad.calendrier_publications()
    req = [a for a in sim.appels if "releases/dates" in a["url"]]
    assert req, "aucune requête calendrier"
    assert req[0].get("include_release_dates_with_no_data") == "true", (
        "sans ce paramètre l'API ne renvoie QUE le passé, et le critère "
        "« catalyseur daté » reste mort par construction")


@cas("3b  seules les publications suivies sont retenues")
def t_calendrier_filtre():
    ad, _ = charger()
    ev = ad.calendrier_publications()
    assert ev, "calendrier vide"
    assert all(e["release_id"] in ad.RELEASES_SUIVIES for e in ev)
    assert any(e["futur"] for e in ev), "aucune date future retenue"


@cas("3c  calendrier sans date future => déclaré INUTILISABLE, pas silencieux")
def t_calendrier_passe():
    ad, _ = charger("calendrier_passe")
    with tempfile.TemporaryDirectory() as d:
        ad.DATA = pathlib.Path(d)
        cr = ad.archiver_calendrier(ad.calendrier_publications())
    assert cr["calendrier_utilisable"] is False
    assert cr["motif_si_inutilisable"], "aucun motif publié"


@cas("3d  le calendrier ne peut pas faire tomber la collecte")
def t_calendrier_robuste():
    for mode in ("http_500", "json_malforme"):
        ad, _ = charger(mode)
        assert ad.calendrier_publications() == [], f"mode {mode}"


# =====================================================================
# 4. E-057 — COHÉRENCE ENTRE COLLECTE ET DÉCLARATION
# =====================================================================

@cas("4a  E-057 : toute série collectée est déclarée côté Macro")
def t_coherence_declaration():
    ad, _ = charger()
    spec = importlib.util.spec_from_file_location("_am", BASE / "apollon_macro.py")
    am = importlib.util.module_from_spec(spec)
    sys.modules["_am"] = am
    spec.loader.exec_module(am)

    sans_sens = sorted(set(ad.SERIES) - set(am.SENS_SERIE))
    assert not sans_sens, (
        f"séries collectées SANS SENS DÉCLARÉ : {sans_sens}. Elles bloquent "
        f"la production du brief (E-007). La déclaration précède la "
        f"collecte (R-056).")

    sans_conv = sorted(s for s in ad.SERIES
                       if s not in am.CONVENTION
                       and s not in getattr(am, "MATURITE_OBLIGATION", {}))
    assert not sans_conv, f"séries sans convention de P&L : {sans_conv}"


@cas("4b  les séries obligatoires du collecteur sont dans sa liste de collecte")
def t_obligatoires_collectees():
    ad, _ = charger()
    absentes = sorted(set(ad.SERIES_OBLIGATOIRES) - set(ad.SERIES))
    assert not absentes, f"déclarées obligatoires mais jamais collectées : {absentes}"


# =====================================================================
# 5. CLÉ ABSENTE
# =====================================================================

@cas("5a  clé absente => message actionnable, pas une trace obscure")
def t_cle_absente():
    ad, _ = charger()
    ad.FRED_KEY = ""
    try:
        ad.fred("DGS10", "2016-01-01")
    except RuntimeError as e:
        assert "FRED_API_KEY" in str(e) and "fredaccount" in str(e)
        return
    raise AssertionError("aucune erreur levée sans clé")


# =====================================================================

def main() -> int:
    print("=" * 78)
    print("BANC DE TEST DE LA COLLECTE — simulateur FRED/ALFRED, hors réseau")
    print("=" * 78)
    for c in _CAS:
        c()
    ok = sum(1 for _, b, _ in _RESULTATS if b)
    print("=" * 78)
    print(f"{ok}/{len(_RESULTATS)} contrôles passés")
    print("=" * 78)
    if ok != len(_RESULTATS):
        for t, b, m in _RESULTATS:
            if not b:
                print(f"  ÉCHEC : {t}\n          {m}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
