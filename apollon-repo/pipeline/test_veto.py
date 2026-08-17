#!/usr/bin/env python3
"""
TESTS DU VETO — APOLLON, Section Risque
=======================================

Écrit en réponse à la faute bloquante G-2 du ré-audit Astra 009 :

    « `np.isfinite(x) and x > seuil` vaut False sur NaN → "ne dépasse pas"
      → "passe". Sur 18 idées de test : les 5 violations bien formées
      bloquent, mais 7 entrées malformées sur 11 passent. Une idée sans
      taille, sans stop et sans corrélation reçoit le motif "aucune limite
      de risque dépassée". »

Le principe que ces tests protègent tient en une phrase : LE MODE DE
DÉFAILLANCE D'UN CONTRÔLE N'EST PAS QU'IL REFUSE À TORT, C'EST QU'IL
ACCEPTE EN SILENCE. Un veto qui échoue en mode passant est pire que
l'absence de veto, parce qu'il produit une trace écrite d'autorisation.

Trois familles de cas :
  A. une idée CONFORME passe — le contrôle n'est pas un refus systématique ;
  B. chacune des CINQ limites, violée isolément, bloque avec le bon motif ;
  C. toute entrée MALFORMÉE bloque — champ absent, null, NaN, ±inf, chaîne,
     liste, booléen, négatif aberrant, hors domaine, entrée non-dict.
Plus une famille D au niveau du FICHIER source : absent, JSON corrompu,
racine non-objet, clé `idees` absente, `idees` non-liste, `idees` vide.

Usage :
    python3 test_veto.py            (silencieux si tout passe, code 0)
    python3 test_veto.py -v         (détail de chaque cas)
"""

from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from apollon_risque import (                                   # noqa: E402
    LIMITE_CORRELATION, LIMITE_PERTE_STRESS_PCT, LIMITE_TAILLE_PCT,
    LIMITE_VAR_POSITION_PCT, MIN_SEANCES_PAIRE, MOTIF_ABERRANT, MOTIF_ABSENT,
    MOTIF_MESURE, est_nombre_fini, lire_idees_transmises, valider_schema_idee,
    veto,
)

VERBEUX = "-v" in sys.argv or "--verbose" in sys.argv
_ECHECS: list[str] = []
_PASSES = 0


# ══════════════════════════════════════════════════════════════════════════
# CADRE DE MESURE — identique à celui de l'exécution réelle
# ══════════════════════════════════════════════════════════════════════════

NOM_PAIRE = "Paire de test"

LIMITES = {
    "LIMITE_VAR_POSITION_PCT": LIMITE_VAR_POSITION_PCT,
    "LIMITE_TAILLE_PCT": LIMITE_TAILLE_PCT,
    "LIMITE_CORRELATION": LIMITE_CORRELATION,
    "LIMITE_PERTE_STRESS_PCT": LIMITE_PERTE_STRESS_PCT,
    "MIN_SEANCES_PAIRE": MIN_SEANCES_PAIRE,
}

# σ_position et σ_marché sont fixés à valeurs égales : β = ρ exactement.
# Les tests portent alors sur la LOGIQUE du veto et non sur la valeur d'un
# ratio de volatilités, qui est testé séparément (test_beta_corrige_rho).
MESURES = {
    "date_arrete": "2026-08-14",
    "var_retenue_pct": -1.66,
    "var_limite_fondee": True,
    "pire_episode_pct": -30.94,
    "cointegrations": {NOM_PAIRE: {"sigma_increment": 0.01, "n_obs": 2000}},
    "sigma_marche_par_paire": {NOM_PAIRE: 0.01},
}

# Seuil effectif de perte au stop : min(plafond dur 2,0 ; |VaR retenue| 1,66)
SEUIL_STOP_EFFECTIF = min(LIMITE_VAR_POSITION_PCT, abs(MESURES["var_retenue_pct"]))


def idee_conforme(**remplacements) -> dict:
    """
    Idée bien formée, sous toutes les limites. Sert de base à tous les cas :
    chaque test ne modifie QU'UN champ, de sorte qu'un blocage ne puisse
    être attribué qu'à ce champ.
    """
    o = {
        "id": "test_20260814",
        "paire": NOM_PAIRE,
        "verdict": "TRANSMISE",
        "statut_risque": "EN_ATTENTE_VETO",
        "taille_pct_nav": 3.0,
        "perte_au_stop_pct": -0.50,
        "n_obs": 2000,
        "echantillon_contient_stress": True,
        "criteres": {
            "5_correlation_marche_actions": {"passe": True, "valeur": 0.20},
            # PIÈGE VOLONTAIRE : ce champ existe et vaut 3,0. L'ancien code
            # s'en servait de valeur de repli quand `taille_pct_nav` n'était
            # pas exploitable. Aucun test ne doit plus jamais le voir passer.
            "6_taille_sous_limite": {"passe": True, "valeur": 3.0},
        },
    }
    for cle, val in remplacements.items():
        if val is _SUPPRIMER:
            o.pop(cle, None)
        else:
            o[cle] = val
    return o


class _Supprimer:
    pass


_SUPPRIMER = _Supprimer()


def rendre_veto(idee) -> dict:
    v = veto([idee], MESURES, LIMITES)
    assert len(v) == 1, f"un verdict attendu, {len(v)} rendu(s)"
    return v[0]


def verifier(nom: str, condition: bool, detail: str = "") -> None:
    global _PASSES
    if condition:
        _PASSES += 1
        if VERBEUX:
            print(f"  ok   {nom}")
    else:
        _ECHECS.append(f"{nom} — {detail}")
        print(f"  ÉCHEC {nom} — {detail}")


def attendre_bloquee(nom: str, idee, fragment_motif: str) -> None:
    """L'idée doit être BLOQUÉE et le motif doit contenir `fragment_motif`."""
    v = rendre_veto(idee)
    motifs = " || ".join(v["motifs"])
    verifier(f"{nom} · bloquée", v["veto"] is True,
             f"verdict veto={v['veto']}, motifs={motifs!r}")
    verifier(f"{nom} · motif « {fragment_motif} »",
             any(fragment_motif in m for m in v["motifs"]),
             f"motifs obtenus : {motifs!r}")
    verifier(f"{nom} · pas de motif « aucune limite »",
             not any("aucune limite" in m.lower() for m in v["motifs"]),
             f"motifs obtenus : {motifs!r}")


def attendre_passante(nom: str, idee) -> None:
    v = rendre_veto(idee)
    verifier(f"{nom} · passe", v["veto"] is False,
             f"bloquée à tort, motifs : {v['motifs']}")
    verifier(f"{nom} · schéma conforme", v.get("schema_conforme") is True,
             "schéma déclaré non conforme")
    verifier(f"{nom} · cinq limites évaluées",
             len(v["limites_evaluees"]) == 5,
             f"{len(v['limites_evaluees'])} limite(s) évaluée(s) : "
             f"{sorted(v['limites_evaluees'])}")


# ══════════════════════════════════════════════════════════════════════════
# A. PRÉDICAT DE BASE
# ══════════════════════════════════════════════════════════════════════════

def test_predicat_nombre_fini() -> None:
    print("\nA. est_nombre_fini — le prédicat qui manquait")
    for v in (0, 1, -1, 3.0, -0.5, 1e-9):
        verifier(f"A · {v!r} est un nombre fini", est_nombre_fini(v) is True)
    for v in (None, float("nan"), float("inf"), float("-inf"), "9.0", "",
              [9.0], (9.0,), {"valeur": 9.0}, True, False, complex(1, 0)):
        verifier(f"A · {v!r} n'est PAS un nombre fini",
                 est_nombre_fini(v) is False,
                 "le prédicat a accepté une valeur non exploitable")


# ══════════════════════════════════════════════════════════════════════════
# B. UNE IDÉE CONFORME PASSE
# ══════════════════════════════════════════════════════════════════════════

def test_idee_conforme_passe() -> None:
    print("\nB. Idée conforme")
    attendre_passante("B1 idée conforme", idee_conforme())
    v = rendre_veto(idee_conforme())
    verifier("B2 · aucun motif", v["motifs"] == [], f"motifs : {v['motifs']}")
    # les cas limites EXACTS ne bloquent pas : la limite est stricte (>)
    attendre_passante("B3 taille exactement au plafond",
                      idee_conforme(taille_pct_nav=LIMITE_TAILLE_PCT))
    attendre_passante("B4 corrélation exactement au seuil",
                      idee_conforme(criteres={
                          "5_correlation_marche_actions": {"valeur": LIMITE_CORRELATION},
                          "6_taille_sous_limite": {"valeur": 3.0}}))
    attendre_passante("B5 profondeur exactement au minimum",
                      idee_conforme(n_obs=MIN_SEANCES_PAIRE))
    attendre_passante("B6 corrélation NÉGATIVE forte (couverture, pas doublon)",
                      idee_conforme(criteres={
                          "5_correlation_marche_actions": {"valeur": -0.95},
                          "6_taille_sous_limite": {"valeur": 3.0}}))


# ══════════════════════════════════════════════════════════════════════════
# C. LES CINQ LIMITES, VIOLÉES ISOLÉMENT
# ══════════════════════════════════════════════════════════════════════════

def test_cinq_limites() -> None:
    print("\nC. Les cinq limites, violées une à une")

    # C1 — perte au stop au-delà de min(plafond dur ; |VaR retenue|)
    attendre_bloquee("C1 perte au stop",
                     idee_conforme(perte_au_stop_pct=-(SEUIL_STOP_EFFECTIF + 0.5)),
                     "perte au stop")

    # C2 — taille au-delà du plafond de charte §4.1
    attendre_bloquee("C2 taille",
                     idee_conforme(taille_pct_nav=LIMITE_TAILLE_PCT + 1.0),
                     "taille")

    # C3 — corrélation signée au-delà du seuil de charte §4.2
    attendre_bloquee("C3 corrélation signée",
                     idee_conforme(criteres={
                         "5_correlation_marche_actions":
                             {"valeur": LIMITE_CORRELATION + 0.15},
                         "6_taille_sous_limite": {"valeur": 3.0}}),
                     "corrélation signée")

    # C4 — perte sous le pire épisode vécu. Avec β = ρ = 0,60 et un épisode
    #      de −30,94 %, une taille de 20 % donne 3,71 % > 2,0 %.
    attendre_bloquee("C4 perte sous stress",
                     idee_conforme(taille_pct_nav=20.0, criteres={
                         "5_correlation_marche_actions": {"valeur": 0.60},
                         "6_taille_sous_limite": {"valeur": 3.0}}),
                     "perte sous le pire épisode vécu")

    # C5 — profondeur d'échantillon de la paire
    attendre_bloquee("C5 profondeur d'échantillon",
                     idee_conforme(n_obs=MIN_SEANCES_PAIRE - 1),
                     "profondeur d'échantillon")

    # C5bis — échantillon sans épisode de stress : motif autonome
    attendre_bloquee("C5bis échantillon sans stress",
                     idee_conforme(echantillon_contient_stress=False),
                     "ne contient AUCUN épisode de stress")


# ══════════════════════════════════════════════════════════════════════════
# D. ENTRÉES MALFORMÉES — LA FAUTE G-2
# ══════════════════════════════════════════════════════════════════════════

def test_donnees_malformees() -> None:
    print("\nD. Entrées malformées — aucune ne doit passer")

    # D1 — l'idée creuse de l'audit : ni taille, ni stop, ni corrélation
    creuse = {"paire": "Idée creuse", "verdict": "TRANSMISE"}
    v = rendre_veto(creuse)
    verifier("D1 idée creuse · bloquée", v["veto"] is True,
             f"motifs : {v['motifs']}")
    verifier("D1 idée creuse · aucune limite évaluée",
             set(v["limites_evaluees"]) == {"schema"},
             f"limites évaluées : {sorted(v['limites_evaluees'])}")
    verifier("D1 idée creuse · motifs DONNEE_MANQUANTE sur les cinq champs",
             sum(1 for m in v["motifs"] if m.startswith(MOTIF_ABSENT)) >= 5,
             f"motifs : {v['motifs']}")
    verifier("D1 idée creuse · pas de « aucune limite de risque dépassée »",
             not any("aucune limite" in m.lower() for m in v["motifs"]),
             f"motifs : {v['motifs']}")

    # D2 à D6 — taille : absente, null, NaN, inf, chaîne, liste, booléen
    attendre_bloquee("D2 taille absente",
                     idee_conforme(taille_pct_nav=_SUPPRIMER),
                     f"{MOTIF_ABSENT}: taille_pct")
    attendre_bloquee("D3 taille null",
                     idee_conforme(taille_pct_nav=None),
                     f"{MOTIF_ABSENT}: taille_pct")
    attendre_bloquee("D4 taille NaN",
                     idee_conforme(taille_pct_nav=float("nan")),
                     f"{MOTIF_ABSENT}: taille_pct")
    attendre_bloquee("D5 taille +inf",
                     idee_conforme(taille_pct_nav=float("inf")),
                     f"{MOTIF_ABSENT}: taille_pct")
    attendre_bloquee("D6 taille chaîne « 9.0 »",
                     idee_conforme(taille_pct_nav="9.0"),
                     f"{MOTIF_ABSENT}: taille_pct")
    attendre_bloquee("D7 taille liste [9.0]",
                     idee_conforme(taille_pct_nav=[9.0]),
                     f"{MOTIF_ABSENT}: taille_pct")
    attendre_bloquee("D8 taille booléenne True",
                     idee_conforme(taille_pct_nav=True),
                     f"{MOTIF_ABSENT}: taille_pct")

    # LE PIÈGE HISTORIQUE : la chaîne "9.0" ne doit PAS être remplacée par
    # criteres.6_taille_sous_limite = 3,0. On vérifie que la valeur de repli
    # n'apparaît NULLE PART dans le verdict.
    v = rendre_veto(idee_conforme(taille_pct_nav="9.0"))
    verifier("D6bis · aucune substitution silencieuse par criteres",
             "taille" not in v["limites_evaluees"],
             "une limite de taille a été évaluée sur une valeur de repli : "
             f"{v['limites_evaluees'].get('taille')}")

    # D9 à D11 — valeurs numériquement aberrantes
    attendre_bloquee("D9 taille négative aberrante",
                     idee_conforme(taille_pct_nav=-5.0),
                     f"{MOTIF_ABERRANT}: taille_pct")
    attendre_bloquee("D10 taille supérieure à 100 %",
                     idee_conforme(taille_pct_nav=4000.0),
                     f"{MOTIF_ABERRANT}: taille_pct")
    attendre_bloquee("D11 corrélation hors [−1 ; 1]",
                     idee_conforme(criteres={
                         "5_correlation_marche_actions": {"valeur": 1.5},
                         "6_taille_sous_limite": {"valeur": 3.0}}),
                     f"{MOTIF_ABERRANT}: correlation")

    # D12 à D14 — corrélation absente sous toutes ses formes
    attendre_bloquee("D12 bloc criteres absent",
                     idee_conforme(criteres=_SUPPRIMER),
                     f"{MOTIF_ABSENT}: correlation")
    attendre_bloquee("D13 corrélation null",
                     idee_conforme(criteres={
                         "5_correlation_marche_actions": {"valeur": None}}),
                     f"{MOTIF_ABSENT}: correlation")
    attendre_bloquee("D14 corrélation NaN",
                     idee_conforme(criteres={
                         "5_correlation_marche_actions": {"valeur": float("nan")}}),
                     f"{MOTIF_ABSENT}: correlation")
    attendre_bloquee("D15 criteres non-dict",
                     idee_conforme(criteres=["5_correlation_marche_actions"]),
                     f"{MOTIF_ABSENT}: correlation")

    # AUCUN REPLI sur `5_correlation_portefeuille` : l'ancien code l'essayait
    attendre_bloquee("D16 pas de repli sur 5_correlation_portefeuille",
                     idee_conforme(criteres={
                         "5_correlation_portefeuille": {"valeur": 0.10},
                         "6_taille_sous_limite": {"valeur": 3.0}}),
                     f"{MOTIF_ABSENT}: correlation")

    # D17 à D19 — perte au stop
    attendre_bloquee("D17 perte au stop absente",
                     idee_conforme(perte_au_stop_pct=_SUPPRIMER),
                     f"{MOTIF_ABSENT}: perte_stop_pct")
    attendre_bloquee("D18 perte au stop null",
                     idee_conforme(perte_au_stop_pct=None),
                     f"{MOTIF_ABSENT}: perte_stop_pct")
    # AUCUN REPLI sur `perte_max_pct` : l'ancien code l'essayait
    attendre_bloquee("D19 pas de repli sur perte_max_pct",
                     idee_conforme(perte_au_stop_pct=_SUPPRIMER,
                                   perte_max_pct=-0.4),
                     f"{MOTIF_ABSENT}: perte_stop_pct")

    # D20 à D22 — profondeur et stress
    attendre_bloquee("D20 n_obs absent",
                     idee_conforme(n_obs=_SUPPRIMER),
                     f"{MOTIF_ABSENT}: n_obs_paire")
    attendre_bloquee("D21 n_obs chaîne",
                     idee_conforme(n_obs="2000"),
                     f"{MOTIF_ABSENT}: n_obs_paire")
    attendre_bloquee("D22 drapeau de stress absent",
                     idee_conforme(echantillon_contient_stress=_SUPPRIMER),
                     f"{MOTIF_ABSENT}: echantillon_contient_stress")
    attendre_bloquee("D23 drapeau de stress null",
                     idee_conforme(echantillon_contient_stress=None),
                     f"{MOTIF_ABSENT}: echantillon_contient_stress")
    attendre_bloquee("D24 drapeau de stress en chaîne « oui »",
                     idee_conforme(echantillon_contient_stress="oui"),
                     f"{MOTIF_ABSENT}: echantillon_contient_stress")

    # D25 à D27 — nom
    attendre_bloquee("D25 nom absent",
                     idee_conforme(paire=_SUPPRIMER),
                     f"{MOTIF_ABSENT}: nom")
    attendre_bloquee("D26 nom vide",
                     idee_conforme(paire="   "),
                     f"{MOTIF_ABSENT}: nom")
    attendre_bloquee("D27 nom numérique",
                     idee_conforme(paire=42),
                     f"{MOTIF_ABSENT}: nom")

    # D28 à D30 — l'entrée elle-même n'est pas un objet
    for i, brute in enumerate(["une chaîne", 42, [1, 2, 3], None], start=28):
        v = rendre_veto(brute)
        verifier(f"D{i} entrée {type(brute).__name__} · bloquée",
                 v["veto"] is True, f"motifs : {v['motifs']}")
        verifier(f"D{i} entrée {type(brute).__name__} · motif d'absence",
                 any(m.startswith(MOTIF_ABSENT) for m in v["motifs"]),
                 f"motifs : {v['motifs']}")


# ══════════════════════════════════════════════════════════════════════════
# E. MESURES INDISPONIBLES CÔTÉ RISQUE — le veto ne s'auto-dispense pas
# ══════════════════════════════════════════════════════════════════════════

def test_mesures_indisponibles() -> None:
    print("\nE. Mesures indisponibles côté Risque")

    # E1 — β non mesurable (σ_position absent) : la limite de stress ne peut
    #      pas être évaluée. Une limite non évaluée n'est pas satisfaite.
    m = dict(MESURES, cointegrations={})
    v = veto([idee_conforme()], m, LIMITES)[0]
    verifier("E1 σ_position absent · bloquée", v["veto"] is True,
             f"motifs : {v['motifs']}")
    verifier("E1 · motif MESURE_INDISPONIBLE",
             any(m_.startswith(MOTIF_MESURE) for m_ in v["motifs"]),
             f"motifs : {v['motifs']}")

    # E2 — σ_marché absent
    m = dict(MESURES, sigma_marche_par_paire={})
    v = veto([idee_conforme()], m, LIMITES)[0]
    verifier("E2 σ_marché absent · bloquée", v["veto"] is True,
             f"motifs : {v['motifs']}")

    # E3 — pire épisode de stress non mesuré
    m = dict(MESURES, pire_episode_pct=None)
    v = veto([idee_conforme()], m, LIMITES)[0]
    verifier("E3 pire épisode non mesuré · bloquée", v["veto"] is True,
             f"motifs : {v['motifs']}")

    # E4 — VaR NON FONDÉE : le seuil retombe sur le plafond dur, sans erreur
    m = dict(MESURES, var_limite_fondee=False, var_retenue_pct=float("nan"))
    v = veto([idee_conforme()], m, LIMITES)[0]
    verifier("E4 VaR non fondée · idée conforme passe encore",
             v["veto"] is False, f"motifs : {v['motifs']}")
    verifier("E4 · seuil retombé sur le plafond dur",
             v["limites_evaluees"]["perte_au_stop_vs_var"]["seuil_pct"]
             == LIMITE_VAR_POSITION_PCT,
             str(v["limites_evaluees"]["perte_au_stop_vs_var"]))


# ══════════════════════════════════════════════════════════════════════════
# F. G-6 — β CORRIGE ρ
# ══════════════════════════════════════════════════════════════════════════

def test_beta_corrige_rho() -> None:
    print("\nF. G-6 — la limite de stress applique β, pas ρ")
    # σ_position = 3 × σ_marché ⇒ β = 3 ρ. Avec ρ = 0,25 et taille 10 %,
    # perte en ρ = 30,94 × 0,10 × 0,25 = 0,773 % (sous la limite de 2 %)
    # perte en β = 30,94 × 0,10 × 0,75 = 2,320 % (AU-DESSUS)
    m = dict(MESURES,
             cointegrations={NOM_PAIRE: {"sigma_increment": 0.03}},
             sigma_marche_par_paire={NOM_PAIRE: 0.01})
    idee = idee_conforme(taille_pct_nav=10.0, criteres={
        "5_correlation_marche_actions": {"valeur": 0.25},
        "6_taille_sous_limite": {"valeur": 3.0}})
    v = veto([idee], m, LIMITES)[0]
    ps = v["limites_evaluees"]["perte_sous_stress"]
    verifier("F1 · bloquée par la limite de stress en β", v["veto"] is True,
             f"motifs : {v['motifs']}")
    verifier("F2 · β = 3 ρ", abs(ps["beta"]["beta"] - 0.75) < 1e-9,
             f"β obtenu : {ps['beta']['beta']}")
    verifier("F3 · l'ancienne formule en ρ ne bloquait PAS",
             ps["ancienne_methode_en_rho_POUR_MEMOIRE"] < LIMITE_PERTE_STRESS_PCT
             < ps["perte_estimee_pct"],
             f"ρ : {ps['ancienne_methode_en_rho_POUR_MEMOIRE']}, "
             f"β : {ps['perte_estimee_pct']}")
    verifier("F4 · facteur de sous-estimation publié",
             abs(ps["facteur_sous_estimation_ancienne_methode"] - 3.0) < 1e-9,
             str(ps["facteur_sous_estimation_ancienne_methode"]))


# ══════════════════════════════════════════════════════════════════════════
# G. LA SOURCE — fichier absent, corrompu, schéma invalide, liste vide
# ══════════════════════════════════════════════════════════════════════════

def test_source() -> None:
    print("\nG. Source d'idées — traitée et déclarée dans tous les cas")
    with tempfile.TemporaryDirectory() as d:
        rep = Path(d)

        # G1 — fichier absent
        s = lire_idees_transmises(rep / "inexistant.json")
        verifier("G1 fichier absent · statut ABSENT", s["statut"] == "ABSENT",
                 s["statut"])
        verifier("G1 · NON examinable", s["examinable"] is False, str(s))
        verifier("G1 · motif écrit", bool(s.get("motif")), str(s))

        # G2 — JSON corrompu
        p = rep / "corrompu.json"
        p.write_text('{"idees": [ {"paire": ', encoding="utf-8")
        s = lire_idees_transmises(p)
        verifier("G2 JSON corrompu · statut ILLISIBLE",
                 s["statut"] == "ILLISIBLE", s["statut"])
        verifier("G2 · NON examinable", s["examinable"] is False, str(s))

        # G3 — racine JSON non-objet
        p = rep / "liste.json"
        p.write_text("[1, 2, 3]", encoding="utf-8")
        s = lire_idees_transmises(p)
        verifier("G3 racine non-objet · statut SCHEMA_INVALIDE",
                 s["statut"] == "SCHEMA_INVALIDE", s["statut"])

        # G4 — clé `idees` absente
        p = rep / "sans_idees.json"
        p.write_text('{"date_donnees": "2026-08-14"}', encoding="utf-8")
        s = lire_idees_transmises(p)
        verifier("G4 clé idees absente · statut SCHEMA_INVALIDE",
                 s["statut"] == "SCHEMA_INVALIDE", s["statut"])
        verifier("G4 · NON examinable", s["examinable"] is False, str(s))

        # G5 — `idees` non-liste
        p = rep / "idees_dict.json"
        p.write_text('{"idees": {"a": 1}}', encoding="utf-8")
        s = lire_idees_transmises(p)
        verifier("G5 idees non-liste · statut SCHEMA_INVALIDE",
                 s["statut"] == "SCHEMA_INVALIDE", s["statut"])

        # G6 — `idees` vide : état LÉGITIME, examinable, rien à examiner
        p = rep / "vide.json"
        p.write_text('{"idees": []}', encoding="utf-8")
        s = lire_idees_transmises(p)
        verifier("G6 idees vide · statut OK", s["statut"] == "OK", s["statut"])
        verifier("G6 · EXAMINABLE (rien à examiner ≠ pas pu examiner)",
                 s["examinable"] is True, str(s))
        verifier("G6 · 0 soumise", s["n_soumises"] == 0, str(s))

        # G7 — entrée non-dict dans la liste : soumise au veto, donc bloquée
        p = rep / "entree_pourrie.json"
        p.write_text('{"idees": ["ceci n\'est pas une idée"]}', encoding="utf-8")
        s = lire_idees_transmises(p)
        verifier("G7 entrée non-dict · soumise au veto", s["n_soumises"] == 1,
                 str(s))
        v = veto(s["idees"], MESURES, LIMITES)
        verifier("G7 · bloquée", v[0]["veto"] is True, str(v))

        # G8 — idée sans verdict NI statut : non triable ⇒ soumise ⇒ bloquée
        p = rep / "sans_verdict.json"
        p.write_text(json.dumps({"idees": [{"paire": "X"}]}), encoding="utf-8")
        s = lire_idees_transmises(p)
        verifier("G8 sans verdict ni statut · soumise au veto",
                 s["n_soumises"] == 1, str(s))
        verifier("G8 · bloquée",
                 veto(s["idees"], MESURES, LIMITES)[0]["veto"] is True, str(s))

        # G9 — idée au verdict amont définitif : NON soumise, mais DÉCLARÉE
        p = rep / "refusee.json"
        p.write_text(json.dumps({"idees": [
            {"paire": "Y", "verdict": "REFUSEE", "statut_risque": "CLOSE"}]}),
            encoding="utf-8")
        s = lire_idees_transmises(p)
        verifier("G9 verdict amont définitif · non soumise",
                 s["n_soumises"] == 0 and s["n_non_soumises"] == 1, str(s))
        verifier("G9 · déclarée nommément",
                 s["non_soumises"][0]["nom"] == "Y", str(s["non_soumises"]))


# ══════════════════════════════════════════════════════════════════════════
# H. LE VALIDATEUR LUI-MÊME
# ══════════════════════════════════════════════════════════════════════════

def test_validateur() -> None:
    print("\nH. valider_schema_idee")
    ok, motifs, canon = valider_schema_idee(idee_conforme())
    verifier("H1 idée conforme · valide", ok is True, str(motifs))
    verifier("H1 · canonique complet",
             set(canon) >= {"nom", "taille_pct", "correlation",
                            "perte_stop_pct", "n_obs_paire",
                            "echantillon_contient_stress"}, str(canon))
    verifier("H2 perte au stop ramenée en valeur absolue",
             canon["perte_stop_pct"] == 0.50, str(canon))
    ok, motifs, canon = valider_schema_idee({})
    verifier("H3 idée vide · invalide", ok is False, str(motifs))
    verifier("H3 · six motifs, un par champ requis", len(motifs) == 6,
             f"{len(motifs)} motif(s) : {motifs}")
    verifier("H3 · aucun canonique produit", canon == {}, str(canon))


# ══════════════════════════════════════════════════════════════════════════

def main() -> int:
    print("=" * 76)
    print("TESTS DU VETO — apollon_risque.py")
    print("=" * 76)
    print("Un contrôle qui échoue en mode PASSANT est pire que l'absence de")
    print("contrôle : il produit une trace écrite d'autorisation.")
    test_predicat_nombre_fini()
    test_idee_conforme_passe()
    test_cinq_limites()
    test_donnees_malformees()
    test_mesures_indisponibles()
    test_beta_corrige_rho()
    test_source()
    test_validateur()
    print("\n" + "=" * 76)
    if _ECHECS:
        print(f"ÉCHEC — {len(_ECHECS)} contrôle(s) en défaut sur "
              f"{_PASSES + len(_ECHECS)} :")
        for e in _ECHECS:
            print(f"  · {e}")
        print("=" * 76)
        return 1
    print(f"TOUS LES CONTRÔLES PASSENT — {_PASSES} vérifications.")
    print("Aucune entrée malformée ne franchit le veto. Aucune substitution")
    print("silencieuse. Aucune limite non évaluée déclarée satisfaite.")
    print("=" * 76)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
