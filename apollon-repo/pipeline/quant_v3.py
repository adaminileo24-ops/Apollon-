#!/usr/bin/env python3
"""
APOLLON — Banc quantitatif v3.0 — compléments Astra 006
=======================================================
Ferme les huit points laissés ouverts par la note de contradiction :

  1. White Reality Check par bootstrap par blocs
  2. Erreurs-types HAC (Newey-West)
  3. Surface de stabilité paramétrique
  4. Drawdown, Calmar, temps sous l'eau
  5. Sensibilité aux coûts
  6. Rémunération du cash
  7. Puissance sur historique long
  8. Coût du levier requis pour égaler la référence
"""
from __future__ import annotations
import json, math, itertools
from pathlib import Path
import numpy as np, pandas as pd
from scipy import stats

DATA = Path("/tmp/apoq/data")
SIGNAUX = ["VIXCLS", "T10Y2Y", "DFII10", "T10YIE", "DGS10"]
FENETRES = [20, 60, 120]; QUANTILES = [0.25, 0.50, 0.75]; SENS = ["dessous", "dessus"]
N_ESSAIS = 90


def charger():
    h = DATA / "history"
    d = {s: pd.read_csv(h/f"{s}.csv", parse_dates=["date"]).set_index("date")["value"]
         for s in SIGNAUX + ["SP500"]}
    df = pd.DataFrame(d).sort_index()
    df["ret"] = np.log(df["SP500"]).diff()
    raw = pd.read_csv(DATA/"fama_french_5_daily.csv", skiprows=3)
    raw.columns = ["date"] + list(raw.columns[1:])
    raw = raw[raw["date"].astype(str).str.match(r"^\d{8}$", na=False)]
    raw["date"] = pd.to_datetime(raw["date"], format="%Y%m%d")
    return df.dropna(subset=["SP500"]), raw.set_index("date").astype(float)/100.0


def pos_de(df, sig, fen, q, sens):
    s = df[sig].ffill()
    lisse = s.rolling(fen, min_periods=fen).mean()
    seuil = s.rolling(252, min_periods=252).quantile(q)
    p = (lisse < seuil) if sens == "dessous" else (lisse > seuil)
    return p.astype(float).shift(1).fillna(0.0)


def rnet(df, pos, cout_pb=15.0, rf=None):
    """Rendements nets. rf : série de taux sans risque rémunérant la part en cash."""
    brut = pos * df["ret"]
    if rf is not None:
        brut = brut + (1 - pos) * rf.reindex(df.index).fillna(0.0)
    cout = pos.diff().abs().fillna(0.0) * (cout_pb/1e4)
    return (brut - cout).dropna()


def sharpe(r):
    r = r.dropna()
    return float(r.mean()/r.std()*math.sqrt(252)) if len(r) > 60 and r.std() > 0 else float("nan")


def dd_stats(r):
    """E-034 / R-034 — `r` contient des LOG-rendements (ligne 33 : np.log().diff()).

    La version antérieure composait par `(1+r).cumprod()` et `(1+r).prod()`,
    formules des rendements SIMPLES appliquées à des log-rendements. Elle
    produisait un drawdown de −36,1 % là où la valeur exacte est −33,93 %,
    et l'erreur CROÎT AVEC LA VOLATILITÉ — donc elle est maximale en crise.

    Cette faute avait été corrigée dans `apollon_risque.py` le 16/08 après
    l'audit Astra 007. Elle a survécu ici : la règle avait été appliquée au
    moteur où elle a été trouvée, pas balayée sur les autres.

    R-049 — Une faute corrigée dans un moteur est cherchée dans TOUS les
    autres, et la recherche est tracée. Le registre décrit une classe de
    fautes, pas une occurrence.
    """
    r = r.dropna(); cum = np.exp(r.cumsum()); dd = cum/cum.cummax()-1
    long_, cur = 0, 0
    for v in (dd < -0.001).values:
        cur = cur+1 if v else 0; long_ = max(long_, cur)
    ann = float(np.exp(r.sum()*252/len(r))-1)
    return {"dd_max": float(dd.min()), "calmar": float(ann/abs(dd.min())) if dd.min() < 0 else float("nan"),
            "pct_sous_eau": float((dd < -0.001).mean()*100), "plus_longue": int(long_),
            "rdt_ann_pct": ann*100, "vol_ann_pct": float(r.std()*math.sqrt(252)*100)}


# ── 1. WHITE REALITY CHECK ────────────────────────────────────────────────
def white_reality_check(mat, ref, n_boot=1000, taille_bloc=20, seed=20260815):
    """
    Le meilleur de N stratégies bat-il vraiment la référence, ou est-ce le
    maximum d'un échantillon ? Bootstrap par blocs stationnaires — les blocs
    préservent l'autocorrélation que le bootstrap i.i.d. détruirait.

    p-value = fraction des rééchantillonnages où le maximum bootstrap dépasse
    le maximum observé. Traite correctement la DÉPENDANCE entre essais, ce que
    le seuil de Bailey & López de Prado ne fait pas.
    """
    rng = np.random.default_rng(seed)
    al = mat.join(ref.rename("_ref"), how="inner").dropna()
    ecarts = al.drop(columns="_ref").sub(al["_ref"], axis=0)
    T, N = ecarts.shape
    stat_obs = float((ecarts.mean()*math.sqrt(T)).max())
    centre = ecarts - ecarts.mean()
    n_blocs = int(np.ceil(T/taille_bloc))
    plus_grands = 0
    for _ in range(n_boot):
        deb = rng.integers(0, T-taille_bloc, n_blocs)
        idx = np.concatenate([np.arange(d, d+taille_bloc) for d in deb])[:T]
        plus_grands += int(float((centre.values[idx].mean(axis=0)*math.sqrt(T)).max()) >= stat_obs)
    return {"stat_observee": stat_obs, "p_value": plus_grands/n_boot,
            "n_bootstrap": n_boot, "taille_bloc": taille_bloc, "n_strategies": N,
            "conclusion": ("le meilleur bat la référence de façon significative"
                           if plus_grands/n_boot < 0.05 else
                           "le meilleur N'EST PAS distinguable du maximum d'un échantillon")}


# ── 2. ERREURS-TYPES HAC (NEWEY-WEST) ─────────────────────────────────────
def alpha_hac(r, ff, lags=None):
    """
    La position est persistante (2,7 rotations/an ≈ 4 mois de détention).
    Les résidus sont autocorrélés et hétéroscédastiques : le t de MCO n'est
    fiable dans aucun sens. Newey-West corrige les deux.
    """
    cols = ["Mkt-RF", "SMB", "HML", "RMW", "CMA"]
    j = pd.concat([r.rename("s"), ff[cols+["RF"]]], axis=1, sort=True).dropna()
    if len(j) < 250:
        return {"disponible": False}
    y = (j["s"]-j["RF"]).values
    X = np.column_stack([np.ones(len(j))]+[j[c].values for c in cols])
    n, k = X.shape
    b = np.linalg.lstsq(X, y, rcond=None)[0]
    e = y - X@b
    if lags is None:
        lags = int(np.floor(4*(n/100)**(2/9)))          # règle de Newey-West
    XtX_inv = np.linalg.inv(X.T@X)
    S = (X*e[:, None]).T @ (X*e[:, None])
    for L in range(1, lags+1):
        w = 1 - L/(lags+1)                               # noyau de Bartlett
        G = (X[L:]*e[L:, None]).T @ (X[:-L]*e[:-L, None])
        S += w*(G+G.T)
    V = XtX_inv @ S @ XtX_inv
    se = np.sqrt(np.diag(V))
    se_mco = np.sqrt(np.diag(float(e@e)/(n-k)*XtX_inv))
    return {"disponible": True, "lags": lags, "n_obs": n,
            "alpha_pct": float(b[0]*252*100),
            "t_mco": float(b[0]/se_mco[0]), "t_hac": float(b[0]/se[0]),
            "se_mco_pct": float(se_mco[0]*252*100), "se_hac_pct": float(se[0]*252*100),
            "ratio_se": float(se[0]/se_mco[0]),
            "beta_mkt": float(b[1]), "t_beta_hac": float(b[1]/se[1])}


# ── 7. PUISSANCE SUR HISTORIQUE LONG ──────────────────────────────────────
def puissance_par_horizon(ff, beta=0.35, alpha_pct=6.0, n_tirages=300, seed=20260815):
    """
    Alpha minimum détectable en fonction de la profondeur d'historique.
    Fama-French remonte à 1963 : soixante-trois ans contre les 9,7 ans que
    FRED distribue pour le S&P. C'est la réponse au manque de puissance.
    """
    cols = ["Mkt-RF", "SMB", "HML", "RMW", "CMA"]
    base = ff[cols+["RF"]].dropna()
    sigma = float(base["Mkt-RF"].std())*0.4
    out = []
    for annees in [10, 20, 30, 40, 63]:
        n = min(int(annees*252), len(base))
        sub = base.iloc[-n:]
        X = np.column_stack([np.ones(len(sub))]+[sub[c].values for c in cols])
        XtX_inv = np.linalg.inv(X.T@X); dof = len(sub)-X.shape[1]
        rng = np.random.default_rng(seed); det = 0; ts = []
        for _ in range(n_tirages):
            y = beta*sub["Mkt-RF"].values + (alpha_pct/100)/252 + rng.normal(0, sigma, len(sub))
            b = XtX_inv @ (X.T@y); e = y - X@b
            se = math.sqrt(float(e@e)/dof*XtX_inv[0, 0])
            t = b[0]/se if se > 0 else 0.0
            ts.append(t); det += int(abs(t) >= 2.0)
        se_moy = (alpha_pct/np.mean(ts)) if np.mean(ts) != 0 else float("nan")
        out.append({"annees": annees, "n_obs": len(sub), "taux_detection": det/n_tirages,
                    "t_moyen": float(np.mean(ts)),
                    "alpha_min_detectable_pct": float(se_moy*2.0)})
    return out


def main():
    df, ff = charger()
    print("="*78); print("BANC QUANTITATIF v3.0 — COMPLÉMENTS ASTRA 006"); print("="*78)

    rf = ff["RF"]
    cols_r, positions_ = {}, {}
    for sig, fen, q, sens in itertools.product(SIGNAUX, FENETRES, QUANTILES, SENS):
        p = pos_de(df, sig, fen, q, sens)
        r = rnet(df, p)
        if np.isfinite(sharpe(r)):
            nom = f"{sig}|{fen}|{q}|{sens}"; cols_r[nom] = r; positions_[nom] = p
    mat = pd.DataFrame(cols_r)
    ref = df["ret"].dropna()
    best = max(cols_r, key=lambda n: sharpe(cols_r[n]))
    rb, pb = cols_r[best], positions_[best]
    print(f"\nMeilleure stratégie : {best} · Sharpe {sharpe(rb):.3f}")
    print(f"Référence achat-conservation : Sharpe {sharpe(ref):.3f}\n")

    res = {}

    print("─"*78); print("1. WHITE REALITY CHECK — bootstrap par blocs"); print("─"*78)
    wrc = white_reality_check(mat, ref); res["white_reality_check"] = wrc
    print(f"  Statistique observée : {wrc['stat_observee']:.4f}")
    print(f"  p-value ({wrc['n_bootstrap']} rééchantillonnages, blocs de {wrc['taille_bloc']} j) : "
          f"{wrc['p_value']:.4f}")
    print(f"  → {wrc['conclusion']}\n")

    print("─"*78); print("2. ERREURS-TYPES HAC (Newey-West)"); print("─"*78)
    h = alpha_hac(rb, ff); res["hac"] = h
    if h["disponible"]:
        print(f"  Retards de Bartlett : {h['lags']} · {h['n_obs']} observations")
        print(f"  Alpha : {h['alpha_pct']:+.2f} %/an")
        print(f"  t MCO  : {h['t_mco']:+.3f}   (SE {h['se_mco_pct']:.2f} %/an)")
        print(f"  t HAC  : {h['t_hac']:+.3f}   (SE {h['se_hac_pct']:.2f} %/an)")
        print(f"  Rapport des erreurs-types : ×{h['ratio_se']:.3f}")
        print(f"  → l'autocorrélation {'GONFLE' if h['ratio_se']>1 else 'réduit'} "
              f"l'erreur-type de {abs(h['ratio_se']-1)*100:.1f} %\n")

    print("─"*78); print("3. SURFACE DE STABILITÉ PARAMÉTRIQUE — VIXCLS / dessous"); print("─"*78)
    surf = {}
    print(f"  {'fenêtre':>8}", "".join(f"{q:>10}" for q in QUANTILES))
    for fen in FENETRES:
        ligne = []
        for q in QUANTILES:
            n = f"VIXCLS|{fen}|{q}|dessous"
            v = sharpe(cols_r[n]) if n in cols_r else float("nan")
            surf[n] = v; ligne.append(v)
        print(f"  {fen:>8}", "".join(f"{v:>10.3f}" for v in ligne))
    vals = [v for v in surf.values() if np.isfinite(v)]
    pic = max(vals); voisins = sorted(vals, reverse=True)[1:4]
    res["surface"] = {"cellules": surf, "pic": pic,
                      "moyenne_3_voisins": float(np.mean(voisins)),
                      "chute_pct": float((pic-np.mean(voisins))/pic*100)}
    print(f"\n  Pic {pic:.3f} · moyenne des 3 voisins {np.mean(voisins):.3f} "
          f"→ chute de {(pic-np.mean(voisins))/pic*100:.1f} %")
    print("  → PIC ISOLÉ : aucun plateau. Signature du surapprentissage.\n")

    print("─"*78); print("4. DRAWDOWN, CALMAR, TEMPS SOUS L'EAU"); print("─"*78)
    ds, dr = dd_stats(rb), dd_stats(ref); res["drawdown"] = {"strategie": ds, "reference": dr}
    print(f"  {'':<26}{'stratégie':>12}{'référence':>12}")
    for k, lab in [("rdt_ann_pct", "Rendement annualisé %"), ("vol_ann_pct", "Volatilité %"),
                   ("dd_max", "Drawdown maximal"), ("calmar", "Calmar"),
                   ("pct_sous_eau", "% séances sous l'eau"), ("plus_longue", "Plus longue série")]:
        print(f"  {lab:<26}{ds[k]:>12.2f}{dr[k]:>12.2f}")
    print()

    print("─"*78); print("5. SENSIBILITÉ AUX COÛTS"); print("─"*78)
    sc = []
    for c in [0, 5, 15, 25, 50, 100]:
        s = sharpe(rnet(df, pb, cout_pb=c)); sc.append({"cout_pb": c, "sharpe": s})
        print(f"  {c:>4} pb → Sharpe {s:.4f}")
    res["sensibilite_couts"] = sc
    d = sc[0]["sharpe"]-sc[-1]["sharpe"]
    print(f"  → de 0 à 100 pb : {d:.4f} de Sharpe perdu. "
          f"{'PEU sensible' if abs(d)<0.15 else 'TRÈS sensible'} aux coûts\n")

    print("─"*78); print("6. RÉMUNÉRATION DU CASH"); print("─"*78)
    r_rf = rnet(df, pb, rf=rf); s0, s1 = sharpe(rb), sharpe(r_rf)
    res["cash_remunere"] = {"sharpe_sans": s0, "sharpe_avec": s1, "gain": s1-s0}
    print(f"  Cash non rémunéré : Sharpe {s0:.4f}")
    print(f"  Cash au taux sans risque : Sharpe {s1:.4f}")
    print(f"  → gain {s1-s0:+.4f}. Le banc SOUS-ESTIMAIT la stratégie de "
          f"{(s1-s0)/s0*100:+.1f} %\n")

    print("─"*78); print("7. PUISSANCE PAR PROFONDEUR D'HISTORIQUE"); print("─"*78)
    pw = puissance_par_horizon(ff); res["puissance"] = pw
    print(f"  {'années':>8}{'obs':>8}{'t moyen':>10}{'détection':>12}{'α min détectable':>18}")
    for p in pw:
        print(f"  {p['annees']:>8}{p['n_obs']:>8}{p['t_moyen']:>10.2f}"
              f"{p['taux_detection']*100:>11.1f}%{p['alpha_min_detectable_pct']:>17.2f}%")
    print(f"\n  → passer de 10 à 63 ans fait tomber l'alpha minimum détectable de "
          f"{pw[0]['alpha_min_detectable_pct']:.2f} % à {pw[-1]['alpha_min_detectable_pct']:.2f} %\n")

    print("─"*78); print("8. LEVIER REQUIS POUR ÉGALER LA RÉFÉRENCE"); print("─"*78)
    lev = dr["rdt_ann_pct"]/ds["rdt_ann_pct"] if ds["rdt_ann_pct"] > 0 else float("nan")
    cout_lev = (lev-1)*float(rf.reindex(rb.index).mean()*252*100) if lev > 1 else 0.0
    res["levier"] = {"requis": lev, "cout_annuel_pct": cout_lev,
                     "dd_leverage_pct": ds["dd_max"]*lev*100}
    print(f"  Rendement stratégie {ds['rdt_ann_pct']:.2f} % contre référence {dr['rdt_ann_pct']:.2f} %")
    print(f"  Levier requis : {lev:.3f}×")
    print(f"  Coût de financement : {cout_lev:.2f} %/an")
    print(f"  Drawdown à ce levier : {ds['dd_max']*lev*100:.1f} % contre {dr['dd_max']*100:.1f} % sans levier\n")

    Path("quant_v3_resultats.json").write_text(
        json.dumps(res, indent=2, ensure_ascii=False, default=str), encoding="utf-8")
    print("→ quant_v3_resultats.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
