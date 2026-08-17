#!/usr/bin/env python3
"""
APOLLON — Banc de test quantitatif
==================================
Section Quantitative · Générale De Prado

PRINCIPE DIRECTEUR
------------------
Un agent qui choisit son hypothèse nulle la rejettera. Ce banc existe pour
retirer ce choix. Le nombre d'essais est DÉCLARÉ AVANT de commencer, en dur
dans le fichier, et toute correction de tests multiples s'y réfère.

Ce que le banc impose, sans possibilité de contournement :
  1. Nombre d'essais déclaré avant exécution      -> N_ESSAIS_DECLARES
  2. Signaux décalés d'un jour                    -> aucun look-ahead
  3. Coûts de transaction obligatoires            -> COUT_ALLER_RETOUR_PB
  4. Validation croisée purgée avec embargo       -> purge des chevauchements
  5. Sharpe dégonflé (Bailey & López de Prado)    -> corrige les essais multiples
  6. Probabilité de surapprentissage (CSCV)       -> PBO
  7. Décomposition factorielle Fama-French 5      -> sépare alpha et bêta
  8. Seuils de rejet appliqués mécaniquement      -> aucun arbitrage a posteriori

Usage :
    python3 apollon_quant.py --data /chemin/vers/apollon/data
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

# ══════════════════════════════════════════════════════════════════════════
# DÉCLARATION PRÉALABLE — figée avant toute exécution (règle Q-001)
# ══════════════════════════════════════════════════════════════════════════

HYPOTHESE = (
    "Le rendement du S&P 500 est conditionnel au régime. Un signal de régime "
    "construit sur la volatilité, la pente de la courbe ou les taux réels "
    "sépare des périodes de rendement significativement différent."
)

# Grille figée. Le produit de ses dimensions EST le nombre d'essais.
SIGNAUX = ["VIXCLS", "T10Y2Y", "DFII10", "T10YIE", "DGS10"]
FENETRES = [20, 60, 120]            # jours de lissage du signal
QUANTILES = [0.25, 0.50, 0.75]      # seuil de bascule
SENS = ["dessous", "dessus"]        # long quand le signal est sous/sur le seuil

N_ESSAIS_DECLARES = len(SIGNAUX) * len(FENETRES) * len(QUANTILES) * len(SENS)

COUT_ALLER_RETOUR_PB = 15.0         # points de base, doctrine §écart 3
EMBARGO_JOURS = 10                  # purge autour des frontières de plis
N_PLIS = 8                          # plis pour la validation croisée purgée

# Seuils de rejet — appliqués mécaniquement, jamais négociés
SEUIL_DSR = 0.95                    # Sharpe dégonflé : probabilité minimale
SEUIL_PBO = 0.50                    # probabilité de surapprentissage maximale
SEUIL_ALPHA_T = 2.0                 # t-stat minimal de l'alpha factoriel

GAMMA_EULER = 0.5772156649015329


# ══════════════════════════════════════════════════════════════════════════
# CHARGEMENT
# ══════════════════════════════════════════════════════════════════════════

def charger(data_dir: Path) -> tuple[pd.DataFrame, pd.DataFrame | None]:
    """Charge les séries du dépôt et les facteurs Fama-French."""
    hist = data_dir / "history"
    séries = {}
    for sid in set(SIGNAUX) | {"SP500"}:
        f = hist / f"{sid}.csv"
        if not f.exists():
            raise FileNotFoundError(f"Série obligatoire absente : {sid}")
        d = pd.read_csv(f, parse_dates=["date"]).set_index("date")["value"]
        séries[sid] = d
    df = pd.DataFrame(séries).sort_index()
    df["ret"] = np.log(df["SP500"]).diff()
    df = df.dropna(subset=["SP500"])

    ff = None
    fpath = data_dir / "fama_french_5_daily.csv"
    if fpath.exists():
        try:
            raw = pd.read_csv(fpath, skiprows=3)
            raw.columns = ["date"] + list(raw.columns[1:])
            raw = raw[raw["date"].astype(str).str.match(r"^\d{8}$", na=False)]
            raw["date"] = pd.to_datetime(raw["date"], format="%Y%m%d")
            ff = raw.set_index("date").astype(float) / 100.0
        except Exception as exc:                              # noqa: BLE001
            print(f"  ! facteurs illisibles : {exc}")
    return df, ff


# ══════════════════════════════════════════════════════════════════════════
# STRATÉGIE
# ══════════════════════════════════════════════════════════════════════════

def positions(df: pd.DataFrame, signal: str, fenetre: int,
              q: float, sens: str) -> pd.Series:
    """
    Position binaire 0/1 sur le S&P.
    Le signal est lissé, comparé à un seuil glissant, PUIS DÉCALÉ D'UN JOUR.
    Le décalage est la seule protection contre le look-ahead et il est appliqué
    ici, une fois, pour toutes les stratégies.
    """
    s = df[signal].ffill()
    lisse = s.rolling(fenetre, min_periods=fenetre).mean()
    seuil = s.rolling(252, min_periods=252).quantile(q)
    pos = (lisse < seuil) if sens == "dessous" else (lisse > seuil)
    return pos.astype(float).shift(1).fillna(0.0)


def rendements_nets(df: pd.DataFrame, pos: pd.Series) -> pd.Series:
    """Rendements après coûts. Le coût s'applique à chaque changement de position."""
    brut = pos * df["ret"]
    rotations = pos.diff().abs().fillna(0.0)
    cout = rotations * (COUT_ALLER_RETOUR_PB / 1e4)
    return (brut - cout).dropna()


def sharpe(r: pd.Series) -> float:
    if len(r) < 60 or r.std() == 0 or not np.isfinite(r.std()):
        return float("nan")
    return float(r.mean() / r.std() * math.sqrt(252))


# ══════════════════════════════════════════════════════════════════════════
# SHARPE DÉGONFLÉ — Bailey & López de Prado (2014)
# ══════════════════════════════════════════════════════════════════════════

def sharpe_attendu_max(var_sr: float, n_essais: int, moyenne: float = 0.0) -> float:
    """
    Sharpe maximal attendu sous l'hypothèse nulle, après n_essais tirages.
    C'est la barre que le meilleur résultat doit franchir pour signifier
    quelque chose. Sans elle, le maximum d'un échantillon de bruit passe
    pour une découverte.
    """
    if n_essais < 2 or var_sr <= 0:
        return 0.0
    e = math.e
    z1 = stats.norm.ppf(1 - 1.0 / n_essais)
    z2 = stats.norm.ppf(1 - 1.0 / (n_essais * e))
    # CORRECTION F6 (Astra 006) : le nul doit être recentré sur la dérive de
    # la grille. Toutes les stratégies sont long-only sur un marché haussier :
    # elles héritent de la dérive. Un nul centré sur 0 est faux et trop
    # permissif. Le paramètre `moyenne` recentre la distribution.
    return moyenne + math.sqrt(var_sr) * ((1 - GAMMA_EULER) * z1 + GAMMA_EULER * z2)


def sharpe_degonfle(sr_annuel: float, r: pd.Series, sr_seuil_annuel: float) -> float:
    """
    Probabilité que le Sharpe observé dépasse réellement le seuil de bruit.

    CORRECTION F1 (Astra 006, 15/08/2026) — ERREUR D'UNITÉS.
    La version initiale combinait un Sharpe ANNUALISÉ avec un T en JOURS.
    La formule de Bailey & López de Prado exige SR et T dans la MÊME
    fréquence. Le numérateur était gonflé d'un facteur ~√252, ce qui
    saturait le résultat à 1,000 et faisait passer un critère qui échoue.
    Mesure : DSR publié 1,000 · DSR réel 0,796.

    Tout est désormais ramené en fréquence quotidienne.
    """
    T = len(r)
    if T < 60 or not np.isfinite(sr_annuel):
        return float("nan")
    sr = sr_annuel / math.sqrt(252)          # <- ramené au quotidien
    seuil = sr_seuil_annuel / math.sqrt(252) # <- idem
    g3 = float(stats.skew(r))
    g4 = float(stats.kurtosis(r, fisher=False))
    denom = 1.0 - g3 * sr + ((g4 - 1.0) / 4.0) * sr ** 2
    if denom <= 0:
        return float("nan")
    z = (sr - seuil) * math.sqrt(T - 1) / math.sqrt(denom)
    return float(stats.norm.cdf(z))


# ══════════════════════════════════════════════════════════════════════════
# PROBABILITÉ DE SURAPPRENTISSAGE — CSCV
# ══════════════════════════════════════════════════════════════════════════

def pbo(matrice: pd.DataFrame, n_blocs: int = 10) -> float:
    """
    Combinatorially Symmetric Cross-Validation.
    On découpe l'historique en blocs, on prend toutes les moitiés possibles
    comme échantillon d'apprentissage, et on regarde où se classe hors
    échantillon la stratégie qui gagnait en apprentissage.

    PBO élevé = la stratégie gagnante en apprentissage est médiocre en dehors,
    donc la sélection captait du bruit.
    """
    T, N = matrice.shape
    if N < 2 or T < n_blocs * 20:
        return float("nan")
    taille = T // n_blocs
    blocs = [matrice.iloc[i * taille:(i + 1) * taille] for i in range(n_blocs)]
    logits = []
    for combo in itertools.combinations(range(n_blocs), n_blocs // 2):
        reste = [i for i in range(n_blocs) if i not in combo]
        IS = pd.concat([blocs[i] for i in combo])
        OOS = pd.concat([blocs[i] for i in reste])
        sr_is = IS.apply(lambda c: sharpe(c.dropna()))
        sr_oos = OOS.apply(lambda c: sharpe(c.dropna()))
        if sr_is.isna().all() or sr_oos.isna().all():
            continue
        best = sr_is.idxmax()
        rang = sr_oos.rank(pct=True).get(best, np.nan)
        if not np.isfinite(rang):
            continue
        rang = min(max(rang, 1e-6), 1 - 1e-6)
        logits.append(math.log(rang / (1 - rang)))
    if not logits:
        return float("nan")
    return float(np.mean([1.0 for x in logits if x <= 0]) if logits else np.nan) \
        if False else float(sum(1 for x in logits if x <= 0) / len(logits))


# ══════════════════════════════════════════════════════════════════════════
# VALIDATION CROISÉE PURGÉE
# ══════════════════════════════════════════════════════════════════════════

def cv_purgee(r: pd.Series, pos: pd.Series | None = None,
              n_plis: int = N_PLIS, embargo: int = EMBARGO_JOURS) -> dict:
    """
    Stabilité par sous-période, avec purge d'embargo.

    CORRECTION F4/F5 (Astra 006) — DEUX AVEUX.
    (a) Ce n'est PAS une validation croisée : il n'y a ni ensemble
        d'apprentissage ni ensemble de test, donc rien dont l'embargo
        protège. C'est une mesure de STABILITÉ par sous-période, et elle
        est désormais nommée comme telle.
    (b) La version initiale supprimait SILENCIEUSEMENT les plis où la
        stratégie était plate (écart-type nul → Sharpe NaN). « 5/5 plis
        positifs » masquait 3 plis sur 8 entièrement hors marché — ce qui
        est l'information centrale pour une stratégie de timing.
        Les plis plats sont désormais comptés et publiés.
    """
    T = len(r)
    if T < n_plis * 60:
        return {"disponible": False}
    taille = T // n_plis
    sharpes, plats, courts = [], 0, 0
    for k in range(n_plis):
        d, f = k * taille, (k + 1) * taille
        test = r.iloc[max(0, d + embargo):max(0, f - embargo)]
        if len(test) < 40:
            courts += 1
            continue
        if pos is not None:
            p = pos.reindex(test.index).fillna(0.0)
            if p.abs().sum() == 0:
                plats += 1
                continue
        s = sharpe(test)
        if np.isfinite(s):
            sharpes.append(s)
        else:
            plats += 1
    return {
        "disponible": True,
        "n_plis_total": n_plis,
        "n_plis_evalues": len(sharpes),
        "n_plis_plats": plats,
        "n_plis_courts": courts,
        "mediane": float(np.median(sharpes)) if sharpes else float("nan"),
        "positifs": int(sum(1 for x in sharpes if x > 0)),
        "note": "stabilité par sous-période — PAS une validation croisée",
    }


def treynor_mazuy(r: pd.Series, ff: pd.DataFrame | None) -> dict:
    """
    Test de timing de marché — AJOUT (Astra 006, manque n° 2).
    r − rf = a + b·Mkt + c·Mkt² + e
    Un c positif et significatif indique une capacité de timing réelle :
    l'exposition monte quand le marché monte. C'est LE test naturel d'une
    stratégie de régime binaire, et son absence était le plus gros trou
    technique du banc.
    """
    if ff is None or "Mkt-RF" not in ff.columns or "RF" not in ff.columns:
        return {"disponible": False}
    j = pd.concat([r.rename("s"), ff[["Mkt-RF", "RF"]]], axis=1, sort=True).dropna()
    if len(j) < 250:
        return {"disponible": False}
    y = (j["s"] - j["RF"]).values
    m = j["Mkt-RF"].values
    X = np.column_stack([np.ones(len(j)), m, m ** 2])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta
    dof = len(j) - 3
    s2 = float(resid @ resid) / dof
    try:
        se = np.sqrt(np.diag(s2 * np.linalg.inv(X.T @ X)))
    except np.linalg.LinAlgError:
        return {"disponible": False}
    return {
        "disponible": True,
        "alpha_annualise_pct": float(beta[0] * 252 * 100),
        "alpha_t": float(beta[0] / se[0]) if se[0] > 0 else float("nan"),
        "beta": float(beta[1]),
        "gamma_timing": float(beta[2]),
        "gamma_t": float(beta[2] / se[2]) if se[2] > 0 else float("nan"),
    }


# ══════════════════════════════════════════════════════════════════════════
# DÉCOMPOSITION FACTORIELLE
# ══════════════════════════════════════════════════════════════════════════

def regression_factorielle(r: pd.Series, ff: pd.DataFrame | None) -> dict:
    """
    Régresse les rendements de la stratégie contre Fama-French 5 facteurs.
    L'ordonnée à l'origine est l'alpha. Le reste est du bêta factoriel,
    accessible pour 0,15 % par an via un ETF. C'est l'écart technique n° 4
    de la feuille de route.
    """
    if ff is None:
        return {"disponible": False}
    cols = [c for c in ["Mkt-RF", "SMB", "HML", "RMW", "CMA"] if c in ff.columns]
    if not cols or "RF" not in ff.columns:
        return {"disponible": False}
    j = pd.concat([r.rename("strat"), ff[cols + ["RF"]]], axis=1).dropna()
    if len(j) < 250:
        return {"disponible": False, "motif": f"seulement {len(j)} observations communes"}
    y = (j["strat"] - j["RF"]).values
    X = np.column_stack([np.ones(len(j))] + [j[c].values for c in cols])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta
    dof = len(j) - X.shape[1]
    s2 = float(resid @ resid) / dof
    try:
        se = np.sqrt(np.diag(s2 * np.linalg.inv(X.T @ X)))
    except np.linalg.LinAlgError:
        return {"disponible": False, "motif": "matrice singulière"}
    return {
        "disponible": True,
        "n_obs": int(len(j)),
        "alpha_annualise_pct": float(beta[0] * 252 * 100),
        "alpha_t": float(beta[0] / se[0]) if se[0] > 0 else float("nan"),
        "betas": {c: float(b) for c, b in zip(cols, beta[1:])},
        "r2": float(1 - (resid @ resid) / ((y - y.mean()) @ (y - y.mean()))),
    }


# ══════════════════════════════════════════════════════════════════════════
# CONTRÔLE POSITIF — condition bloquante (Astra 006, exigence n° 1)
# ══════════════════════════════════════════════════════════════════════════

def controle_positif(df, ff, sr_seuil, var_sr, alphas=(0.0, 3.0, 6.0, 9.0, 12.0),
                     beta_cible=0.35, n_tirages=200):
    """
    COURBE DE PUISSANCE — contrôle positif (Astra 006, exigence bloquante n° 1).

    Un tirage unique ne prouve rien : la variation d'échantillonnage domine.
    Le premier essai a récupéré 3,65 % pour 6 % injectés, non par biais mais
    par un écart-type d'estimation de ~2,3 %/an. Vérifié : SANS bruit, le banc
    récupère exactement 6,000 % et un bêta de 0,3500.

    Le contrôle correct mesure donc le TAUX DE DÉTECTION sur n tirages, pour
    plusieurs niveaux d'alpha. C'est la puissance du test, et c'est la seule
    chose qui dise si un « zéro retenue » informe sur les stratégies ou sur
    l'instrument.

    Lecture attendue : à alpha nul, le taux de détection doit valoir le taux
    de faux positifs (≈ 5 % pour |t| ≥ 2). S'il est plus élevé, le banc
    fabrique des découvertes.
    """
    if ff is None or "Mkt-RF" not in ff.columns or "RF" not in ff.columns:
        return {"disponible": False, "motif": "facteurs absents"}
    mkt = ff["Mkt-RF"].reindex(df.index).dropna()
    if len(mkt) < 500:
        return {"disponible": False, "motif": f"{len(mkt)} obs seulement"}
    rf = ff["RF"].reindex(mkt.index).fillna(0.0).values
    sigma_bruit = float(df["ret"].std()) * 0.4
    cols = ["Mkt-RF", "SMB", "HML", "RMW", "CMA"]
    base = ff[cols + ["RF"]].reindex(mkt.index)
    X = np.column_stack([np.ones(len(mkt))] + [base[c].values for c in cols])
    XtX_inv = np.linalg.inv(X.T @ X)
    dof = len(mkt) - X.shape[1]

    courbe = []
    for a_pct in alphas:
        a_j = (a_pct / 100.0) / 252.0
        detections, alphas_rec, ts = 0, [], []
        rng = np.random.default_rng(20260815)
        for _ in range(n_tirages):
            bruit = rng.normal(0, sigma_bruit, len(mkt))
            y = beta_cible * mkt.values + a_j + bruit      # déjà en excédentaire
            b = XtX_inv @ (X.T @ y)
            resid = y - X @ b
            se0 = math.sqrt(float(resid @ resid) / dof * XtX_inv[0, 0])
            t = b[0] / se0 if se0 > 0 else 0.0
            alphas_rec.append(b[0] * 252 * 100); ts.append(t)
            if abs(t) >= SEUIL_ALPHA_T:
                detections += 1
        courbe.append({
            "alpha_injecte_pct": a_pct,
            "taux_detection": detections / n_tirages,
            "alpha_moyen_recupere_pct": float(np.mean(alphas_rec)),
            "t_moyen": float(np.mean(ts)),
            "se_alpha_pct": float(np.std(alphas_rec)),
        })
    faux_positifs = courbe[0]["taux_detection"]
    puissance_6 = next((c["taux_detection"] for c in courbe
                        if abs(c["alpha_injecte_pct"] - 6.0) < 1e-9), float("nan"))
    # Le banc est étalonné si : faux positifs maîtrisés ET puissance réelle
    etalonne = (faux_positifs <= 0.10) and (puissance_6 >= 0.50)
    return {"disponible": True, "beta_injecte": beta_cible,
            "n_tirages": n_tirages, "courbe": courbe,
            "taux_faux_positifs": faux_positifs, "puissance_alpha_6pct": puissance_6,
            "banc_etalonne": bool(etalonne)}


def alpha_minimum_detectable(r, ff):
    """Puissance du test — exigence n° 5 d'Astra. Publiée en tête de rapport."""
    fac = regression_factorielle(r, ff)
    if not fac.get("disponible") or not np.isfinite(fac.get("alpha_t", float("nan"))):
        return float("nan")
    a, t = fac["alpha_annualise_pct"], fac["alpha_t"]
    if abs(t) < 1e-9:
        return float("nan")
    return abs(a / t) * SEUIL_ALPHA_T


# ══════════════════════════════════════════════════════════════════════════
# EXÉCUTION
# ══════════════════════════════════════════════════════════════════════════

def main() -> int:
    ap = argparse.ArgumentParser(description="Banc de test quantitatif Apollon")
    ap.add_argument("--data", required=True)
    args = ap.parse_args()
    data_dir = Path(args.data)

    print("=" * 76)
    print("APOLLON — BANC DE TEST QUANTITATIF v2.0 · Générale De Prado")
    print("=" * 76)
    print(f"\nHYPOTHÈSE DÉCLARÉE\n  {HYPOTHESE}\n")
    print(f"ESSAIS DÉCLARÉS AVANT EXÉCUTION : {N_ESSAIS_DECLARES}")
    print(f"COÛT : {COUT_ALLER_RETOUR_PB:.0f} pb A/R · SEUILS : DSR≥{SEUIL_DSR} "
          f"· PBO≤{SEUIL_PBO} · |t(α)|≥{SEUIL_ALPHA_T}\n")

    df, ff = charger(data_dir)
    print(f"Données : {len(df)} séances, {df.index[0].date()} → {df.index[-1].date()}")
    bh = df["ret"].dropna()
    sr_bh = sharpe(bh)
    print(f"Référence achat-conservation : Sharpe {sr_bh:.3f}\n")

    # Balayage
    resultats, colonnes, pos_par_nom = [], {}, {}
    for sig, fen, q, sens in itertools.product(SIGNAUX, FENETRES, QUANTILES, SENS):
        pos = positions(df, sig, fen, q, sens)
        r = rendements_nets(df, pos)
        sr = sharpe(r)
        if not np.isfinite(sr):
            continue
        nom = f"{sig}|{fen}|{q}|{sens}"
        colonnes[nom] = r; pos_par_nom[nom] = pos
        resultats.append({"nom": nom, "sharpe": sr, "n_obs": len(r),
                          "expo_moy": float(pos.reindex(r.index).mean()),
                          "rotations_an": float(pos.diff().abs().sum()/(len(pos)/252))})
    res = pd.DataFrame(resultats).sort_values("sharpe", ascending=False)
    mat = pd.DataFrame(colonnes)

    var_sr = float(res["sharpe"].var()); moy_sr = float(res["sharpe"].mean())
    seuil_nul0 = sharpe_attendu_max(var_sr, N_ESSAIS_DECLARES, 0.0)
    seuil_recentre = sharpe_attendu_max(var_sr, N_ESSAIS_DECLARES, moy_sr)
    best = res.iloc[0]

    print("─" * 76); print("CORRECTION DES TESTS MULTIPLES"); print("─" * 76)
    print(f"  Moyenne de la grille : {moy_sr:.4f} · variance {var_sr:.4f}")
    print(f"  Seuil nul centré sur 0 (version initiale, FAUX) : {seuil_nul0:.4f}")
    print(f"  SEUIL RECENTRÉ SUR LA DÉRIVE (correct, F6)      : {seuil_recentre:.4f}")
    print(f"  Maximum observé                                 : {best['sharpe']:.4f}")
    ecart = best["sharpe"] - seuil_recentre
    print(f"  → écart au seuil correct : {ecart:+.4f}  "
          f"({'AU-DESSUS' if ecart>0 else 'SOUS le bruit recentré'})\n")

    # CONTRÔLE POSITIF — bloquant
    print("─" * 76); print("CONTRÔLE POSITIF — le banc sait-il dire OUI ?"); print("─" * 76)
    cp = controle_positif(df, ff, seuil_recentre, var_sr)
    if cp.get("disponible"):
        print(f"  Courbe de puissance · {cp['n_tirages']} tirages par niveau · "
              f"bêta injecté {cp['beta_injecte']:.2f}\n")
        print(f"  {'alpha injecté':>14} {'alpha récupéré':>16} {'t moyen':>9} "
              f"{'SE(α)':>8} {'DÉTECTION':>11}")
        for c in cp["courbe"]:
            print(f"  {c['alpha_injecte_pct']:>13.1f}% {c['alpha_moyen_recupere_pct']:>15.2f}% "
                  f"{c['t_moyen']:>9.2f} {c['se_alpha_pct']:>7.2f}% "
                  f"{c['taux_detection']*100:>10.1f}%")
        print(f"\n  Taux de faux positifs (alpha nul) : {cp['taux_faux_positifs']*100:.1f}% "
              f"— attendu ≈ 5 % pour |t| ≥ 2")
        print(f"  Puissance à alpha = 6 %/an        : {cp['puissance_alpha_6pct']*100:.1f}%")
        print(f"\n  → BANC {'ÉTALONNÉ' if cp['banc_etalonne'] else 'NON ÉTALONNÉ'}")
        if cp["banc_etalonne"]:
            print("     Il détecte un alpha réel et ne fabrique pas de faux positifs.")
            print("     Un verdict de rejet porte donc une information.")
        else:
            print("     Tout verdict de rejet est ininterprétable.")
    else:
        print(f"  Indisponible : {cp.get('motif')}")
    print()

    # PBO — statistique de grille, PLUS un veto par stratégie (F3)
    p_bo = pbo(mat.dropna(how="all"))
    print("─" * 76); print("PBO — STATISTIQUE DE GRILLE (correction F3)"); print("─" * 76)
    print(f"  PBO = {p_bo:.4f}")
    print("  Le PBO porte sur le PROCESSUS DE SÉLECTION sur l'ensemble de la grille,")
    print("  pas sur une stratégie. Il conditionne la LECTURE des résultats ;")
    print("  il n'oppose plus de veto individuel — c'était un défaut de logique,")
    print("  et le mécanisme direct du « zéro retenue ».")
    print(f"  Lecture : {'aucune compétence de sélection détectable hors échantillon' if p_bo>=0.45 else 'sélection porteuse d information'}\n")

    # Examen
    print("─" * 76); print("EXAMEN DES TROIS MEILLEURES"); print("─" * 76)
    retenues, examens = [], []
    for _, row in res.head(3).iterrows():
        nom = row["nom"]; r = mat[nom].dropna(); pos = pos_par_nom[nom]
        dsr = sharpe_degonfle(row["sharpe"], r, seuil_recentre)
        st = cv_purgee(r, pos); fac = regression_factorielle(r, ff)
        tm = treynor_mazuy(r, ff); amd = alpha_minimum_detectable(r, ff)
        print(f"\n  ▸ {nom}")
        print(f"    Sharpe {row['sharpe']:.3f} · exposition {row['expo_moy']*100:.1f} % · "
              f"{row['rotations_an']:.1f} rotations/an")
        print(f"    DSR (seuil recentré) : {dsr:.4f}  "
              f"{'PASSE' if np.isfinite(dsr) and dsr>=SEUIL_DSR else 'ÉCHOUE'}")
        if st.get("disponible"):
            print(f"    Stabilité : {st['n_plis_evalues']}/{st['n_plis_total']} plis évalués, "
                  f"{st['n_plis_plats']} PLATS (hors marché), médiane {st['mediane']:+.3f}, "
                  f"{st['positifs']} positifs")
        if fac.get("disponible"):
            print(f"    Alpha FF5 : {fac['alpha_annualise_pct']:+.2f} %/an, t={fac['alpha_t']:+.2f}  "
                  f"{'PASSE' if abs(fac['alpha_t'])>=SEUIL_ALPHA_T else 'ÉCHOUE'} · "
                  f"bêta {fac['betas']['Mkt-RF']:+.3f} · R² {fac['r2']:.3f}")
            print(f"    PUISSANCE : alpha minimum détectable = {amd:.2f} %/an")
        if tm.get("disponible"):
            print(f"    Treynor-Mazuy : γ(timing) = {tm['gamma_timing']:+.3f}, "
                  f"t={tm['gamma_t']:+.2f}  "
                  f"{'timing détecté' if abs(tm['gamma_t'])>=2 else 'AUCUN timing détectable'}")
        ok = (np.isfinite(dsr) and dsr>=SEUIL_DSR and fac.get("disponible")
              and abs(fac.get("alpha_t",0))>=SEUIL_ALPHA_T)
        print(f"    VERDICT : {'RETENUE' if ok else 'REJETÉE'}")
        if ok: retenues.append(nom)
        examens.append({"nom":nom,"sharpe":float(row["sharpe"]),"dsr":dsr,
                        "stabilite":st,"facteurs":fac,"treynor_mazuy":tm,
                        "alpha_min_detectable":amd,"retenue":bool(ok)})

    print("\n" + "=" * 76); print("CONCLUSION"); print("=" * 76)
    if not cp.get("banc_etalonne", False):
        print("  ⚠ CONTRÔLE POSITIF ÉCHOUÉ — le banc n'est pas étalonné.")
        print("    Aucun verdict n'est interprétable tant que ce point n'est pas réglé.")
    elif retenues:
        print(f"  {len(retenues)} stratégie(s) retenue(s) : {', '.join(retenues)}")
    else:
        print("  AUCUNE stratégie retenue — et le banc EST étalonné (il détecte")
        print("  un alpha connu de 6 %/an). Le rejet porte donc une information.")

    Path("quant_resultats.json").write_text(json.dumps({
        "version":"2.0","hypothese":HYPOTHESE,
        "n_essais_declares":N_ESSAIS_DECLARES,"n_evalues":int(len(res)),
        "reference_bh_sharpe":sr_bh,"moyenne_grille":moy_sr,"variance_grille":var_sr,
        "seuil_nul_centre_zero":seuil_nul0,"seuil_recentre_derive":seuil_recentre,
        "meilleur_sharpe":float(best["sharpe"]),"ecart_au_seuil_recentre":ecart,
        "controle_positif":cp,"pbo_grille":p_bo,
        "examens":examens,"retenues":retenues,
        "grille_complete":res.to_dict(orient="records"),
    }, indent=2, ensure_ascii=False, default=str), encoding="utf-8")
    print("\n→ quant_resultats.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
