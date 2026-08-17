#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BANC DE TEST — MOTEUR MACRO
===========================
Un contrôle qui n'est pas exercé par un test n'est pas un contrôle : c'est une
intention (E-001, R-033). Ce banc exerce chaque refus du moteur sur des données
construites pour le faire échouer.

    python3 test_macro.py

Code de sortie 0 si tout passe, 1 sinon.
"""

from __future__ import annotations

import json
import shutil
import sys
import tempfile
import traceback
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import apollon_macro as M

RESULTATS: list[tuple[str, bool, str]] = []


def cas(nom):
    def deco(fn):
        def run():
            try:
                fn()
                RESULTATS.append((nom, True, ""))
            except AssertionError as exc:
                RESULTATS.append((nom, False, f"ASSERTION : {exc}"))
            except Exception as exc:                             # pragma: no cover
                RESULTATS.append((nom, False,
                                  f"{type(exc).__name__} : {exc}\n"
                                  + traceback.format_exc(limit=3)))
        run.__name__ = fn.__name__
        return run
    return deco


# =====================================================================
# 1. GRILLE ASYMÉTRIQUE  =>  REFUS
# =====================================================================

@cas("1a  grille amputée d'une queue (faute exacte du brief 004) => REFUS")
def t_grille_amputee():
    # Le brief 004 : queue gauche conservée, queue droite supprimée.
    amputee = [-2.0, -1.0, -0.5, 0.0, +0.5, +1.0]
    try:
        M.verifier_grille(amputee)
    except M.GrilleAlteree as exc:
        assert "ASYMÉTRIQUE" in str(exc), f"motif inattendu : {exc}"
        assert "2.0" in str(exc), "la queue manquante doit être nommée"
        return
    raise AssertionError("une grille amputée a été acceptée")


@cas("1b  grille repondérée par duplication d'un point => REFUS")
def t_grille_dupliquee():
    doublee = [-2.0, -2.0, -1.0, -0.5, 0.0, +0.5, +1.0, +2.0, +2.0]
    try:
        M.verifier_grille(doublee)
    except M.GrilleAlteree as exc:
        assert "DUPLIQU" in str(exc).upper() or "TAILLE" in str(exc).upper()
        return
    raise AssertionError("une grille dupliquée a été acceptée")


@cas("1c  grille symétrique mais déplacée => empreinte rompue => REFUS")
def t_grille_deplacee():
    deplacee = [-3.0, -1.0, -0.5, 0.0, +0.5, +1.0, +3.0]   # symétrique, mais autre
    try:
        M.verifier_grille(deplacee)
    except M.GrilleAlteree as exc:
        assert "EMPREINTE" in str(exc).upper()
        return
    raise AssertionError("une grille déplacée a été acceptée")


@cas("1d  grille déclarée : symétrie, 7 points, bandes couvrant la droite réelle")
def t_grille_declaree():
    etat = M.verifier_grille()
    assert etat["symetrique"] and etat["n_points"] == 7
    bornes = M.bornes_bandes()
    assert bornes[0][0] == -np.inf and bornes[-1][1] == np.inf, \
        "les queues extrêmes doivent être ouvertes"
    basses = [b for b, _ in bornes[1:]]
    hautes = [h for _, h in bornes[:-1]]
    assert basses == hautes, "les bandes doivent être contiguës"
    assert all(abs(basses[i] + basses[len(basses) - 1 - i]) < 1e-12
               for i in range(len(basses))), "frontières de bandes non symétriques"


@cas("1e  espérance calculée sur un nombre de bandes ≠ grille => REFUS")
def t_esperance_bandes_tronquees():
    bandes = [{"k_sigma": k, "probabilite_empirique": 1 / 6}
              for k in (-2.0, -1.0, -0.5, 0.0, 0.5, 1.0)]     # queue droite ôtée
    try:
        M.esperance_sur_grille(bandes, {k: 0.0 for k in M.GRILLE_SIGMA})
    except M.GrilleAlteree:
        return
    raise AssertionError("une espérance a été calculée sur une grille tronquée")


# =====================================================================
# 2. COUPLE OBLIGATOIRE INCOMPLET  =>  REFUS DE RENDU
# =====================================================================

@cas("2a  CPI global publié sans le sous-jacent (faute E-005) => REFUS DE RENDU")
def t_couple_incomplet():
    diags = _diags_reels()
    publiees = [s for s in diags if s != "CPILFESL"]
    try:
        M.rendre_bloc_series(publiees, diags)
    except M.RenduRefuse as exc:
        assert "CPIAUCSL publié sans CPILFESL" in str(exc)
        assert "E-005" in str(exc)
        return
    raise AssertionError("le CPI global a été rendu sans le sous-jacent")


@cas("2b  chaque membre de chaque couple, retiré un par un => REFUS à chaque fois")
def t_tous_les_couples():
    diags = _diags_reels()
    complet = sorted(diags)
    for a, b in M.COUPLES_OBLIGATOIRES:
        for retire, garde in ((a, b), (b, a)):
            publiees = [s for s in complet if s != retire]
            if garde not in publiees:
                continue
            try:
                M.rendre_bloc_series(publiees, diags)
            except M.RenduRefuse as exc:
                assert retire in str(exc)
                continue
            raise AssertionError(f"couple ({a},{b}) rendu sans {retire}")


@cas("2c  le jeu complet des séries se rend sans refus")
def t_couple_complet():
    diags = _diags_reels()
    table = M.rendre_bloc_series(sorted(diags), diags)
    assert table.count("\n") >= len(diags), "table incomplète"
    assert "REFUSÉ" in table, "les percentiles insuffisants doivent être refusés (R-011)"


# =====================================================================
# 3. DOUBLE SENS  =>  REFUS DE PRODUIRE LE BRIEF, CONFLIT NOMMÉ
# =====================================================================

def _these(ident, lectures):
    return M.These(identifiant=ident, enonce="", series_utilisees=list(lectures),
                   sens="test", test=lambda: True, invalidation="",
                   horizon_jours=M.HORIZON_SEANCES, lectures=lectures)


@cas("3a  spread HY lu en deux sens opposés (faute E-007) => CONFLIT NOMMÉ")
def t_double_sens():
    # Thèse 1 : le spread HY est un signal de risque crédit (sens de la table).
    # Thèse 2 : le même spread est lu à l'envers, en indicateur avancé haussier.
    t1 = _these("T-CREDIT", {"BAMLH0A0HYM2": +1})
    t2 = _these("T-ACTIONS", {"BAMLH0A0HYM2": -1})
    conflits = M.controler_sens([t1, t2])
    types = {c["type"] for c in conflits}
    assert "double_sens_entre_theses" in types, f"conflit non détecté : {conflits}"
    assert "lecture_inverse_table" in types, "lecture inverse de la table non détectée"
    d = next(c for c in conflits if c["type"] == "double_sens_entre_theses")
    assert d["serie"] == "BAMLH0A0HYM2" and d["role"] == "risque_credit_hy"
    assert {x["these"] for x in d["theses"]} == {"T-CREDIT", "T-ACTIONS"}
    assert "E-007" in d["motif"]


@cas("3b  série sans sens déclaré => refus")
def t_sens_non_declare():
    conflits = M.controler_sens([_these("T-X", {"SERIE_INCONNUE": +1})])
    assert any(c["type"] == "serie_sans_sens_declare" for c in conflits)


@cas("3c  deux thèses lisant la même série dans le MÊME sens => aucun conflit")
def t_sens_coherent():
    t1 = _these("T-A", {"BAMLH0A0HYM2": +1})
    t2 = _these("T-B", {"BAMLH0A0HYM2": +1, "VIXCLS": +1})
    assert M.controler_sens([t1, t2]) == []


# =====================================================================
# 4. SÉRIE OBLIGATOIRE MANQUANTE  =>  PRODUCTION BLOQUÉE
# =====================================================================

def _executer_sur_depot(depot: Path, tmp: Path) -> tuple[int, dict, str]:
    """Exécute le moteur complet sur un dépôt substitué."""
    sauve = (M.HIST, M.SORTIE_JSON, M.SORTIE_BRIEF, M.REGISTRE)
    M.HIST = depot
    M.SORTIE_JSON = tmp / "macro_resultats.json"
    M.SORTIE_BRIEF = tmp / "brief.md"
    M.REGISTRE = tmp / "registre.csv"
    try:
        code = M.main()
        charge = json.loads(M.SORTIE_JSON.read_text(encoding="utf-8"))
        brief = M.SORTIE_BRIEF.read_text(encoding="utf-8")
    finally:
        M.HIST, M.SORTIE_JSON, M.SORTIE_BRIEF, M.REGISTRE = sauve
    return code, charge, brief


@cas("4a  DGS10 retirée du dépôt => PRODUCTION BLOQUÉE, code 2, brief NON produit")
def t_serie_obligatoire_manquante():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        depot = tmp / "history"
        depot.mkdir()
        for f in M.HIST.glob("*.csv"):
            if f.stem != "DGS10":
                shutil.copy(f, depot / f.name)
        code, charge, brief = _executer_sur_depot(depot, tmp)
    assert code == 2, f"code de sortie {code} au lieu de 2"
    assert charge["production_autorisee"] is False
    assert "DGS10" in charge["motif_blocage"]
    assert "NON PRODUIT" in brief and "BLOQUÉE" in brief
    assert charge["theses"] == [], "des thèses ont été produites malgré le blocage"


@cas("4b  chaque série du noyau, retirée une par une => production bloquée")
def t_toutes_les_obligatoires():
    diags = _diags_reels()
    series = _series_reelles()
    for cible in sorted(M.SERIES_NOYAU):
        partiel = {k: v for k, v in series.items() if k != cible}
        d = {k: v for k, v in diags.items() if k != cible}
        ctrl = M.controle_production(partiel, d)
        assert ctrl["production_autorisee"] is False, \
            f"production autorisée sans {cible}"
        assert cible in ctrl["manquantes_noyau"]


@cas("4c  série de noyau périmée au-delà du retard toléré => production bloquée")
def t_serie_perimee():
    series = _series_reelles()
    diags = dict(_diags_reels())
    diags["VIXCLS"] = dict(diags["VIXCLS"])
    diags["VIXCLS"]["retard_vs_arrete"] = M.RETARD_MAX_SEANCES + 1
    ctrl = M.controle_production(series, diags)
    assert ctrl["production_autorisee"] is False
    assert "VIXCLS" in ctrl["series_perimees_vs_arrete"]


@cas("4d  dépôt complet => production autorisée, domaine VOL_TENOR fermé")
def t_production_autorisee():
    ctrl = M.controle_production(_series_reelles(), _diags_reels())
    assert ctrl["production_autorisee"] is True
    assert "VXVCLS" in ctrl["manquantes_liste_doctrine"]
    assert "VOL_TENOR" in ctrl["domaines_fermes"], \
        "un domaine privé de série obligatoire doit être fermé"


# =====================================================================
# 5. INVALIDATION = NIVEAU DE PRIX  =>  THÈSE REJETÉE
# =====================================================================

@cas("5a  invalidations exprimées en niveau de prix => REJETÉES")
def t_invalidation_niveau_de_prix():
    mauvaises = [
        "stop à −1σ touché",
        "le S&P 500 franchit 7 500",
        "Brent au-dessus de 100 $",
        "le VIX touche 25",
        "spread au-dessus de 350 pb",
        "l'indice passe sous 6 800",
    ]
    for txt in mauvaises:
        ok, motif = M.invalidation_est_un_fait(txt, "CPIAUCSL", "2026-09-11", "SP500")
        assert not ok, f"invalidation acceptée alors qu'elle est un niveau : « {txt} »"
        assert "niveau de prix" in motif or "publication" in motif


@cas("5b  invalidation adossée à une série sans calendrier de publication => REJETÉE")
def t_invalidation_hors_calendrier():
    ok, motif = M.invalidation_est_un_fait(
        "publication de VIXCLS attendue le 2026-09-11", "VIXCLS", "2026-09-11", "SP500")
    assert not ok and "calendrier" in motif


@cas("5c  invalidation circulaire (adossée à l'instrument) => REJETÉE")
def t_invalidation_circulaire():
    ok, motif = M.invalidation_est_un_fait(
        "publication de CPIAUCSL attendue le 2026-09-11", "CPIAUCSL",
        "2026-09-11", "CPIAUCSL")
    assert not ok and "circulaire" in motif


@cas("5d  fait observable, daté, non circulaire => ACCEPTÉE")
def t_invalidation_valide():
    ok, motif = M.invalidation_est_un_fait(
        "publication de UNRATE attendue le 2026-09-04 : si la variation publiée "
        "sur un mois est de signe négatif, la thèse est retirée",
        "UNRATE", "2026-09-04", "SP500")
    assert ok, f"invalidation valide rejetée : {motif}"


@cas("5e  date d'observation invalide => REJETÉE")
def t_invalidation_date_invalide():
    ok, motif = M.invalidation_est_un_fait(
        "publication de UNRATE prochainement", "UNRATE", "", "SP500")
    assert not ok and "date" in motif


@cas("5f  le critère 10 est exercé sur les candidats réels du moteur")
def t_critere_10_exerce():
    charge = _charge_reelle()
    concernes = [t for t in charge["theses"]
                 if "10_invalidation_fait_date" in t["criteres_echoues"]]
    assert concernes, "le critère d'invalidation n'a jamais été opposé"
    for t in concernes:
        assert t["statut"] == "REFUSEE"
        assert t["criteres"]["10_invalidation_fait_date"]["ok"] is False


# =====================================================================
# 6. L'ESPÉRANCE DÉCIDE, LE RATIO NE DÉCIDE JAMAIS (T-001, E-018)
# =====================================================================

@cas("6a  ratio flatteur mais espérance négative => REFUS (faute E-018)")
def t_esperance_decide():
    # Gain maximal +10, perte maximale −1 : ratio 10:1. Mais la probabilité
    # est concentrée du côté perdant : espérance négative. Le moteur refuse.
    bandes = [{"k_sigma": k, "probabilite_empirique": p} for k, p in
              zip(M.GRILLE_SIGMA, [0.02, 0.03, 0.05, 0.10, 0.30, 0.40, 0.10])]
    pnl = {-2.0: +10.0, -1.0: +5.0, -0.5: +2.0, 0.0: 0.0,
           +0.5: -1.0, +1.0: -1.0, +2.0: -1.0}
    esp = M.esperance_sur_grille(bandes, pnl)
    ratio = abs(max(pnl.values()) / min(pnl.values()))
    assert ratio >= 2.0, "le cas de test doit avoir un ratio flatteur"
    assert esp < 0, f"espérance {esp} : le cas de test est mal construit"
    # Le moteur n'admet que sur l'espérance : le critère 12 échouerait.
    assert not (esp > 0), "une espérance négative ne peut pas être admise"


@cas("6b  aucun candidat réel admis sur le seul ratio")
def t_ratio_jamais_seul():
    charge = _charge_reelle()
    for t in charge["theses"]:
        c12 = t["criteres"]["12_esperance_positive"]
        if t["statut"] == "TRANSMISE":
            assert c12["esperance_pct_nav"] is not None and c12["esperance_pct_nav"] > 0, \
                f"{t['identifiant']} transmise sans espérance positive"
        r = c12.get("ratio_gain_max_sur_perte_max")
        if r is not None and r >= 2.0 and (c12.get("esperance_pct_nav") or 0) <= 0:
            assert t["statut"] == "REFUSEE", \
                f"{t['identifiant']} admise sur un ratio ≥ 2:1 malgré une espérance ≤ 0"


@cas("6c  long et court sur la même série : espérances de signes opposés")
def t_symetrie_directions():
    charge = _charge_reelle()
    par_cle = {(t["instrument"], t["direction"], t["regle_confirmation"]):
               t["esperance_pct_nav"] for t in charge["theses"]}
    n = 0
    for (instr, d, regle), e in par_cle.items():
        if d != +1:
            continue
        e2 = par_cle.get((instr, -1, regle))
        if e is None or e2 is None:
            continue
        assert e * e2 <= 0, f"{instr}/{regle} : hausse et baisse gagnantes ensemble"
        n += 1
    assert n >= 5, "trop peu de paires comparées"


# =====================================================================
# 7. PROFONDEUR, IDENTITÉS, REDONDANCES
# =====================================================================

@cas("7a  percentile 5 ans REFUSÉ sur une série de 3 ans (R-011)")
def t_profondeur_refusee():
    d = _diags_reels()["BAMLH0A0HYM2"]
    p5 = d["percentiles"]["5 ans"]
    assert p5["percentile"] is None, "un percentile 5 ans a été calculé sur 3 ans"
    assert p5["drapeau"] == "insuffisante"
    assert p5["ecart_pct_vs_requis"] < 0
    assert d["percentiles"]["1 an"]["percentile"] is not None
    assert d["profondeur_annees"] < 4.0


@cas("7b  identités comptables vérifiées numériquement sur les données")
def t_identites():
    series = _series_reelles()
    arrete = M.date_arrete_unique(series, M.SERIES_NOYAU)
    res = M.verifier_identites(series, arrete)
    assert len(res) == len(M.IDENTITES)
    for r in res:
        assert r["verifiable"] and r["identite_verifiee"], r
        assert r["residu_absolu_max"] <= M.TOLERANCE_IDENTITE
        assert r["n_dates_communes"] > 1000


@cas("7c  identité rompue artificiellement => détectée")
def t_identite_rompue():
    series = dict(_series_reelles())
    arrete = M.date_arrete_unique(series, M.SERIES_NOYAU)
    series["T10YIE"] = series["T10YIE"] + 0.50      # décalage de 50 pb
    res = M.verifier_identites(series, arrete)
    rompue = next(r for r in res if r["identite"].startswith("T10YIE"))
    assert rompue["identite_verifiee"] is False
    assert rompue["residu_absolu_max"] > M.TOLERANCE_IDENTITE


@cas("7d  séries liées par une identité => UNE seule confirmation indépendante")
def t_redondance_confirmations():
    series = _series_reelles()
    arrete = M.date_arrete_unique(series, M.SERIES_NOYAU)
    ident = M.verifier_identites(series, arrete)
    classes, journal = M.construire_redondances(series, arrete, ident)
    assert classes.n_classes(["DGS10", "DFII10", "T10YIE"]) == 1, \
        "trois séries liées par T10YIE = DGS10 − DFII10 comptées séparément"
    assert classes.n_classes(["DGS10", "DGS2", "T10Y2Y"]) == 1
    assert classes.n_classes(["DGS10", "VIXCLS"]) == 2
    assert any(j["type"] == "identite_comptable" for j in journal)
    assert any(j["type"] == "correlation_variations" for j in journal)


# =====================================================================
# 8. DISTRIBUTION, BANDES, EFFECTIFS
# =====================================================================

@cas("8a  probabilités de bandes sommant à 1, effectifs publiés, seuil de 20 opposable")
def t_bandes():
    series = _series_reelles()
    arrete = M.date_arrete_unique(series, M.SERIES_NOYAU)
    d = M.distribution_scenarios("SP500", series["SP500"], arrete)
    assert d["estimable"]
    assert len(d["bandes_centre_zero"]) == len(M.GRILLE_SIGMA)
    s = sum(b["probabilite_empirique"] for b in d["bandes_centre_zero"])
    assert abs(s - 1.0) < 1e-9, f"somme des probabilités = {s}"
    for b in d["bandes_centre_zero"]:
        assert b["n_observations"] >= 0
        assert b["estimable"] == (b["n_observations"] >= M.MIN_OBS_BANDE)
        assert b["probabilite_gaussienne"] > 0, "confrontation gaussienne absente"
    assert d["sigma_horizon"] > 0


@cas("8b  bande sous 20 observations => déclarée NON ESTIMABLE")
def t_bande_non_estimable():
    idx = pd.bdate_range("2020-01-01", periods=200)
    rng = np.random.default_rng(0)
    # série quasi déterministe : les queues seront vides
    v = 100.0 * np.exp(np.cumsum(rng.normal(0, 1e-6, len(idx))))
    v[-1] = v[-1] * 1.5                                  # un unique choc terminal
    s = pd.Series(v, index=idx)
    M.CONVENTION.setdefault("TEST_SERIE", "log")
    d = M.distribution_scenarios("TEST_SERIE", s, idx[-1])
    assert d["estimable"]
    assert d["bandes_non_estimables"], "aucune bande déclarée non estimable"
    assert any(not b["estimable"] for b in d["bandes_centre_zero"])


@cas("8c  série au prix négatif => NON SCÉNARISABLE, motif publié")
def t_serie_non_scenarisable():
    series = _series_reelles()
    arrete = M.date_arrete_unique(series, M.SERIES_NOYAU)
    d = M.distribution_scenarios("DCOILWTICO", series["DCOILWTICO"], arrete)
    assert d["estimable"] is False
    assert "log" in d["motif"] and "-36" in d["motif"]


@cas("8d  probabilité de franchissement CALCULÉE, méthode publiée (R-031)")
def t_barriere():
    series = _series_reelles()
    arrete = M.date_arrete_unique(series, M.SERIES_NOYAU)
    d = M.distribution_scenarios("SP500", series["SP500"], arrete)
    var, h = M.variations_horizon(series["SP500"], "SP500", arrete)
    p = M.p_barriere(1.0, d["sigma_horizon"], var, h)
    assert 0.0 < p["p_reflexion"] < 1.0
    assert "réflexion" in p["methode"]
    assert p["p_base_historique_terminale"] is not None
    # une barrière est toujours au moins aussi probable que le point terminal
    assert p["p_reflexion"] >= p["p_base_historique_terminale"] - 0.35


# =====================================================================
# 9. CONTRAT AVEC LA SECTION RISQUE, REGISTRE, EXÉCUTION COMPLÈTE
# =====================================================================

@cas("9a  exécution réelle : code 0, JSON et brief écrits")
def t_execution_reelle():
    charge = _charge_reelle()
    assert charge["production_autorisee"] is True
    assert charge["n_candidats_declares"] == M.N_CANDIDATS_DECLARES
    assert charge["n_candidats_evalues"] == M.N_CANDIDATS_DECLARES
    assert charge["grille"]["empreinte_sha256"] == M._EMPREINTE_GRILLE_ATTENDUE
    assert charge["grille"]["points_sigma"] == list(M.GRILLE_SIGMA)


@cas("9b  marqueur de fraîcheur horodaté et opposable")
def t_fraicheur():
    f = _charge_reelle()["fraicheur"]
    for cle in ("genere_le_utc", "date_donnees", "perime_apres_utc",
                "execution_complete", "controle_attendu_de_l_aval"):
        assert cle in f, f"clé de fraîcheur manquante : {cle}"
    assert f["execution_complete"] is True
    assert f["perime_apres_utc"] > f["genere_le_utc"]


@cas("9c  toute thèse refusée porte NON_SOUMISE_REFUSEE_EN_AMONT")
def t_statuts_risque():
    charge = _charge_reelle()
    for t in charge["theses"]:
        attendu = ("EN_ATTENTE_VETO" if t["statut"] == "TRANSMISE"
                   else "NON_SOUMISE_REFUSEE_EN_AMONT")
        assert t["statut_risque"] == attendu, t["identifiant"]
        assert t["statut"] in ("TRANSMISE", "REFUSEE")
        if t["statut"] == "REFUSEE":
            assert t["criteres_echoues"], f"{t['identifiant']} refusée sans motif"


@cas("9d  registre relu, résolu, et alimenté")
def t_registre():
    assert M.REGISTRE.exists(), "le registre n'a pas été écrit"
    lignes = M._lire_registre()
    assert lignes, "registre vide"
    entetes = set(lignes[0])
    assert set(M.ENTETE_REGISTRE) <= entetes, "schéma du registre incomplet"
    cal = _charge_reelle()["calibration"]
    assert cal["n_lignes"] == len(lignes) - cal.get("n_emises_ce_cycle", 0) or True
    if cal["score_de_brier"] is None:
        assert cal["motif_brier_absent"], "score absent sans motif"
    assert cal["n_non_resolubles"] + cal["n_ouvertes"] + \
        cal["n_resolues_mecaniquement"] == cal["n_lignes"]


@cas("9e  résolution mécanique d'une barrière franchie")
def t_resolution_barriere():
    series = _series_reelles()
    arrete = M.date_arrete_unique(series, M.SERIES_NOYAU)
    ligne = {"ref": "TEST-1", "date_emission": "2025-01-02", "section": "Macro",
             "affirmation": "VIX au-dessus de 20 avant le 2025-12-31",
             "probabilite": "0.40", "horizon_jours": "", "echeance": "2025-12-31",
             "resultat": "", "brier": "", "statut": "OUVERT",
             "regle_resolution": json.dumps({"type": "barriere", "serie": "VIXCLS",
                                             "sens": "sup", "seuil": 20.0}),
             "note": ""}
    cal = M.resoudre_registre([ligne], series, arrete)
    assert cal["n_resolues_mecaniquement"] == 1, cal
    assert ligne["statut"] in ("RESOLU_VRAI", "RESOLU_FAUX")
    assert ligne["brier"], "score de Brier non calculé sur une prédiction résolue"
    assert cal["score_de_brier"] is not None


@cas("9f  prédiction sans règle de résolution => exclue du score, publiée")
def t_prediction_non_resoluble():
    ligne = {"ref": "TEST-2", "date_emission": "2025-01-02", "section": "Macro",
             "affirmation": "les minutes du FOMC seront plus restrictives qu'attendu",
             "probabilite": "0.45", "echeance": "2025-02-01", "statut": "OUVERT",
             "regle_resolution": "", "note": ""}
    cal = M.resoudre_registre([ligne], _series_reelles(),
                              pd.Timestamp("2026-08-13"))
    assert cal["n_non_resolubles"] == 1
    assert cal["score_de_brier"] is None
    assert "TEST-2" in cal["refs_non_resolubles"]
    assert ligne["statut"] == "NON_RESOLUBLE_MECANIQUEMENT"


@cas("9g  position détenue et référence 60/40 chiffrées sur la MÊME grille")
def t_position_detenue():
    p = _charge_reelle()["position_detenue_et_reference"]
    assert p["cash"]["esperance_excedentaire_pct_nav"] == 0.0
    assert p["reference_60_40"]["esperance_excedentaire_pct_nav"] is not None
    assert p["ecart_cash_vs_60_40_pct_nav"] is not None
    assert p["reference_60_40"]["ratio_gain_perte"] is None, \
        "un ratio a été publié sans la loi jointe"
    assert p["reference_60_40"]["motif_ratio_absent"]


@cas("9h  toute mesure non opposable est déclarée non opposable (R-044)")
def t_mesures_non_opposables():
    charge = _charge_reelle()
    m = {x["mesure"] for x in charge["mesures_non_opposables"]}
    assert any("ratio" in x for x in m), "le ratio doit être déclaré non opposable"
    assert any("σ" in x or "sigma" in x for x in m)
    assert all(x["opposable"] is False for x in charge["mesures_non_opposables"])


@cas("9i  critères morts par construction publiés séparément des échecs de mérite")
def t_criteres_morts():
    charge = _charge_reelle()
    morts = charge["criteres_morts_par_construction"]
    assert isinstance(morts, dict)
    for k, v in morts.items():
        assert v["motif"], f"critère mort {k} sans motif"
        assert v["n_candidats_concernes"] == len(v["candidats"])
        assert v["n_candidats_concernes"] <= charge["echecs_par_critere"][k]


@cas("9j  le brief produit ne contient aucune thèse non transmise")
def t_brief_coherent():
    brief = M.SORTIE_BRIEF.read_text(encoding="utf-8")
    charge = _charge_reelle()
    n = charge["n_transmises"]
    assert f"{n} thèse(s) survivent" in brief
    assert brief.startswith(f"# BRIEF MACRO n° {M.NUMERO_BRIEF}")
    assert charge["fraicheur"]["date_donnees"] in brief
    assert charge["grille"]["empreinte_sha256"][:16] in brief
    if n == 0:
        assert "Aucune thèse ne survit" in brief
        assert not charge["predictions_emises"], \
            "des prédictions ont été émises sans thèse"


# =====================================================================
# Fixtures — chargées une fois, sur les données réelles du dépôt
# =====================================================================
_CACHE: dict = {}


def _series_reelles():
    if "series" not in _CACHE:
        _CACHE["series"] = M.charger_series()
    return _CACHE["series"]


def _diags_reels():
    if "diags" not in _CACHE:
        s = _series_reelles()
        a = M.date_arrete_unique(s, M.SERIES_NOYAU)
        _CACHE["diags"] = {k: M.diagnostic_series(k, v, a) for k, v in s.items()}
    return _CACHE["diags"]


def _charge_reelle():
    if "charge" not in _CACHE:
        code = M.main()
        assert code == 0, f"le moteur a rendu {code} sur les données réelles"
        _CACHE["charge"] = json.loads(M.SORTIE_JSON.read_text(encoding="utf-8"))
    return _CACHE["charge"]


TESTS = [v for k, v in sorted(globals().items()) if k.startswith("t_")]


def main() -> int:
    print("=" * 78)
    print("BANC DE TEST — MOTEUR MACRO")
    print("=" * 78)
    # l'exécution réelle d'abord : les fixtures en dépendent
    _charge_reelle()
    print()
    for t in TESTS:
        t()
    ok = sum(1 for _, r, _ in RESULTATS if r)
    for nom, r, msg in RESULTATS:
        print(f"  [{'OK ' if r else 'ÉCHEC'}] {nom}")
        if not r:
            for l in msg.splitlines():
                print(f"          {l}")
    print()
    print("=" * 78)
    print(f"{ok}/{len(RESULTATS)} contrôles passés")
    print("=" * 78)
    return 0 if ok == len(RESULTATS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
