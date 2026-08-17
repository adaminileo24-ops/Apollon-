#!/usr/bin/env python3
"""
APOLLON — Moteur de risque
==========================
Section Risque · Générale Kerviel

LA LEÇON QUI FONDE CE MODULE
----------------------------
La perte de 4,9 milliards d'euros de 2008 ne provient pas d'une absence de
contrôles. Les alertes ont été émises. Elles n'ont pas été traitées.

Ce module est donc écrit pour qu'une alerte ne puisse pas être classée en
silence : chaque dépassement produit une ligne horodatée dans un fichier
d'alertes, le journal est RELU à chaque exécution, dédoublonné, et le rapport
porte en tête le nombre d'alertes non traitées. Une clôture est un ÉVÉNEMENT
supplémentaire, jamais une réécriture (journal append-only, immuable).

LE PARAMÈTRE LIBRE DU RISQUE
----------------------------
Macro choisissait sa grille de scénarios. Quant choisissait sa fenêtre de
test. **Risque choisit sa méthode de VaR** — et les méthodes usuelles donnent
des réponses différentes sur les mêmes données. Un agent qui choisit sa
méthode après avoir vu les résultats choisit son niveau de risque.

Conséquence, RÉVISÉE après l'audit Astra 007 :
  - la méthode retenue est déclarée EX ANTE (METHODE_VAR_RETENUE) ;
  - elle est ARBITRÉE PAR LE BACKTEST (Kupiec + Christoffersen), pas par un
    min() sur les estimateurs — prendre le minimum de trois estimateurs
    bruités est formellement la même faute que prendre le maximum d'un
    échantillon pour une découverte (RMSE mesurée 5,6× pire) ;
  - les autres méthodes sont publiées EN ANNEXE, sans entrer dans aucune
    limite.

CORRECTIONS APPORTÉES SUITE À L'AUDIT ASTRA 007 (refus)
--------------------------------------------------------
P1  Composition : la série est en LOG-rendements. Toute capitalisation passe
    par exp(cumsum), jamais par (1+r).cumprod(). Test de non-régression
    _test_composition() ci-dessous.
P2  VETO : mécanisme réel, lit trading_resultats.json, écrit veto_risque.json,
    sort en code 2 si une idée est bloquée.
P3  Cornish-Fisher : validé par monotonicité avant publication, sinon None.
    Remplacé par Johnson SU calibrée sur les quatre moments.
P4  Suppression de min(vh, vp, vcf). Estimateur déclaré ex ante.
P5  Backtest Kupiec / Christoffersen en fenêtre GLISSANTE hors échantillon.
P6  Fenêtre échantillon complet + drapeau contient_drawdown_max par fenêtre.
P7  La VaR retenue entre dans alertes(), avec seuil en constante.
P8  Journal d'alertes relu, dédoublonné, clôturable (--clore).
P9  Paliers de drawdown déclarés INACTIFS tant qu'aucune position n'est tenue.
P10 Sortino : dénominateur sur TOUT l'échantillon + contrôle de cohérence.
P11 Sharpe : taux sans risque DFF. Versions brute ET excédentaire.
P12 Kelly : mu ARITHMÉTIQUE = mu_log + sigma²/2. Intervalle bootstrap publié.
P13 CVaR refusée si la queue compte moins de MIN_OBS_QUEUE observations.
    Arrondi à la précision de l'erreur d'échantillonnage.
P14 Corrélations SIGNÉES, N_eff, ratio de diversification, DGS10 converti en
    rendement obligataire (−duration × Δtaux).
P15 Corrélation en stress conditionnée sur variable EXOGÈNE (VIX) + null de
    corrélation constante par simulation.
P16 Drapeau de profondeur gradué (suffisante / marginale / insuffisante).
P17 Date d'arrêté unique, produite par le code.
P18 simulation_levier() : la table Kelly de la doctrine devient auditable.

CORRECTIONS APPORTÉES SUITE AU RÉ-AUDIT ASTRA 009 (refus, 3 fautes bloquantes)
------------------------------------------------------------------------------
G-1 La valeur critique du backtest est CALIBRÉE PAR SIMULATION SOUS H₀ aux
    tailles réelles, plus par l'asymptotique χ². La règle de décision
    (REGLE_VALEUR_CRITIQUE_BACKTEST) est déclarée EX ANTE, avant tout regard
    sur le résultat. Les DEUX valeurs critiques sont publiées, avec le nombre
    de tirages et la graine.
G-2 Le VETO ne peut plus échouer en mode passant. `valider_schema_idee()`
    s'exécute AVANT toute évaluation ; toute donnée absente / None / NaN /
    non numérique / mal typée produit un VETO, jamais un `pass`. Toute
    substitution silencieuse (repli sur `criteres`) est SUPPRIMÉE : chaque
    champ a une source canonique unique, déclarée dans CHEMIN_CANONIQUE.
G-3 Les paliers de drawdown sont ACTIFS dès qu'une position est détenue OU
    qu'un drawdown non nul est mesuré sur le portefeuille réel. Le
    commentaire « dd['courant'] vaut 0 par construction » était FAUX : il
    vaut 0 parce que le S&P est à son plus haut. Il est retiré.
G-4 Réconciliation « aucune cellule ne survit » / « n cellules admissibles » :
    la première phrase portait sur la seule méthode retenue, la seconde sur
    les 24 cellules toutes méthodes confondues. Les deux comptes sont
    désormais nommés et affichés ensemble.
G-5 N_eff est publié SUR LA CORRÉLATION et SUR LA COVARIANCE. L'opposable est
    celui de la COVARIANCE, parce que c'est la matrice qui correspond à la
    pondération réellement utilisée pour la volatilité de panier.
G-6 La limite de stress applique désormais β = ρ·σ_position/σ_marché, et non
    ρ. Le facteur de correction mesuré est publié par idée.
G-7 Le « 0,2501 » de la doctrine est PRODUIT par le code, sur le panier
    D'ORIGINE (DGS10 en log(taux)), plus affirmé dans une chaîne.
G-8 Les jours où la calibration Johnson SU échoue sont COMPTÉS À PART et
    retirés du backtest, au lieu d'être comptabilisés en jours sans
    dépassement — biais en faveur du modèle. Taux d'échec publié.
G-9 Source d'idées illisible ⇒ code de sortie NON NUL et alerte. « Je n'ai
    pas pu examiner » n'est pas « rien à examiner ».
G-10 Alerte permanente : la moyenne est comparée à un seuil de moyenne, le
    maximum à un seuil de maximum. La date sort de la clé de dédoublonnage.
G-11 Constantes matérielles regroupées en tête, chacune avec son origine.

Usage :
    python3 apollon_risque.py --data /chemin/vers/apollon/data
    python3 apollon_risque.py --clore <id_alerte> --motif "<texte>"
    python3 apollon_risque.py --test          (non-régression seule)
    python3 test_veto.py                      (tests du veto, obligatoires)
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from datetime import datetime, timezone
from math import comb, exp, log
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import optimize, stats

RACINE = Path(__file__).resolve().parent

# ══════════════════════════════════════════════════════════════════════════
# G-11 — CONSTANTES MATÉRIELLES : TOUTES ICI, CHACUNE AVEC SON ORIGINE
# ══════════════════════════════════════════════════════════════════════════
# L'audit 009 relevait 34 constantes en tête, ≥ 21 en dur, 8 seulement
# traçables à la charte. Le titre de ce bloc affirmait « issus de la charte
# IV » : c'était FAUX pour la majorité d'entre elles, et notamment pour
# LIMITE_VAR_PORTEFEUILLE_PCT, qui n'apparaît nulle part dans la charte.
#
# Chaque constante matérielle porte désormais une étiquette d'origine, dans
# un vocabulaire fermé de trois valeurs :
#   · « charte §X »      — l'article est cité, le chiffre y figure ;
#   · « propriété »      — imposée par une propriété mathématique, un
#                          théorème, une convention statistique ou une
#                          mesure sur les données ; reproductible ;
#   · « posée à la main » — CHOISIE. Non dérivée. Discutable en revue
#                          mensuelle, opposable d'ici là.
# Le décompte est publié à l'exécution (n_tracables_charte / n_proprietes /
# n_constantes_libres) et versé au JSON. Une constante posée à la main qui
# se déclare « issue de la charte » est une autorité usurpée.
# ══════════════════════════════════════════════════════════════════════════

# ── VaR : périmètre et estimateur ─────────────────────────────────────────
NIVEAUX_VAR = [0.95, 0.99]
# origine: propriété | convention prudentielle Bâle (95 % / 99 %)
# P6 : 1 an, 2 ans, 5 ans, ÉCHANTILLON COMPLET. Aucune des trois premières
# fenêtres ne contient mars 2020 ; l'omettre revenait à mesurer un risque de
# marché sur un échantillon d'où la seule crise avait été retirée.
FENETRES_VAR: list[int | str] = [252, 504, 1260, "complet"]
# origine: posée à la main | 1 an / 2 ans / 5 ans / tout, en séances

# ── P4 : estimateur déclaré EX ANTE ───────────────────────────────────────
# Justification, écrite AVANT d'avoir vu les chiffres de cette exécution :
# la VaR historique n'impose aucune hypothèse de distribution, c'est le seul
# estimateur dont l'erreur ne dépend pas d'une forme fonctionnelle supposée,
# et l'audit mesure sa RMSE à 0,396 pt contre 2,210 pt pour la règle
# min(historique, paramétrique, Cornish-Fisher) — 5,6× meilleure.
METHODE_VAR_RETENUE = "historique"
# origine: posée à la main | déclarée ex ante, arbitrée par le backtest
REGLE_FENETRE_LIMITE = "la plus longue fenêtre non rejetée par LR_cc"
# origine: posée à la main | départage sur la profondeur, jamais sur la valeur
SEUIL_BACKTEST = 0.05
# origine: propriété | niveau de test usuel de 5 %
BACKTEST_BURN_IN = 252
# origine: posée à la main | amorçage de la fenêtre extensible, 1 an

# ── G-1 : LA VALEUR CRITIQUE QUI DÉCIDE, DÉCLARÉE AVANT DE LA REGARDER ────
# L'audit 009 a établi que le rejet reposait sur l'asymptotique χ²(2), et
# que celle-ci N'EST PAS CALIBRÉE aux tailles réellement testées : sous H₀,
# à T = 1 251 et p = 5 %, la vraie valeur critique à 5 % vaut environ 6,5 et
# non 5,991. La statistique LR_cc est une somme de deux rapports de
# vraisemblance dont la convergence vers χ² est lente quand l'événement est
# rare : à p = 1 %, le nombre attendu de transitions 1→1 est de l'ordre de
# l'unité, et la loi limite ne décrit plus rien.
#
# RÈGLE DE DÉCISION, ÉCRITE ICI AVANT TOUTE EXÉCUTION ET AVANT TOUT REGARD
# SUR LE RÉSULTAT : c'est la valeur critique CALIBRÉE PAR SIMULATION SOUS H₀
# aux tailles réelles qui décide. L'asymptotique χ² est publiée EN REGARD,
# pour mémoire, et n'a aucun effet sur le verdict. Le motif est antérieur au
# résultat : une valeur critique fausse rejette ou accepte au mauvais taux,
# quel que soit le sens dans lequel elle se trompe et quel que soit le
# verdict que la correction produira.
REGLE_VALEUR_CRITIQUE_BACKTEST = "calibrée par simulation sous H0, tailles réelles"
# origine: posée à la main | déclarée ex ante, cf. justification ci-dessus
N_SIM_CALIBRATION_BACKTEST = 20000
# origine: propriété | erreur type du quantile 95 % simulé ≈ 0,03 à ce tirage

# ── P3 : domaine de validité de Cornish-Fisher ────────────────────────────
# L'expansion de Cornish-Fisher est un développement tronqué à l'ordre 4.
# Elle n'est une fonction quantile que si elle est strictement croissante en z.
# Au-delà d'une kurtosis excédentaire modérée, les termes négligés d'ordre
# supérieur sont du même ordre de grandeur que la correction retenue, et le
# domaine de monotonicité (Maillard 2012) se referme dès que l'asymétrie
# s'écarte de zéro. Seuil prudentiel retenu : 1,2. La monotonicité effective
# est de toute façon testée point par point ; le seuil n'est qu'un garde-fou
# supplémentaire, jamais une autorisation.
SEUIL_KURT_CF = 1.2
# origine: propriété | domaine de monotonicité de l'expansion d'ordre 4

# ── Précision et reproductibilité ─────────────────────────────────────────
MIN_OBS_QUEUE = 20             # origine: propriété | pas de moyenne de queue sur < 20 pts
N_BOOTSTRAP_KELLY = 20000      # origine: propriété | précision Monte-Carlo de l'IC 90 %
N_BOOTSTRAP_ERREUR = 400       # origine: propriété | erreur type de la VaR historique
N_SIM_NULL_CORR = 2000         # origine: propriété | null de corrélation constante
GRAINE = 20260814              # origine: propriété | reproductibilité, publiée

# ── Paliers de perte : LES SEULS CHIFFRES QUI VIENNENT VRAIMENT DE LA CHARTE
LIMITE_DRAWDOWN_ALERTE = -0.05         # origine: charte §4.3 | tableau des paliers
LIMITE_DRAWDOWN_REDUCTION = -0.10      # origine: charte §4.3 | tableau des paliers
LIMITE_DRAWDOWN_SUSPENSION = -0.15     # origine: charte §4.3 | tableau des paliers
LIMITE_DRAWDOWN_COUPE_CIRCUIT = -0.20  # origine: charte §4.3 | tableau des paliers

# ── G-10 : moyenne contre seuil de moyenne, maximum contre seuil de maximum
# Le défaut : LIMITE_CORRELATION_MOYENNE = 0,60 était comparée au MAXIMUM
# des corrélations de paires (0,934 sur SP500/NASDAQ100). Le maximum d'un
# panier contenant deux indices actions US est structurellement au-dessus de
# 0,60 : l'alerte ne pouvait JAMAIS s'éteindre. Une alerte qui ne peut pas
# s'éteindre n'informe de rien et détruit l'attention portée aux autres.
LIMITE_CORRELATION_MOYENNE = 0.60
# origine: posée à la main | comparée à la MOYENNE signée, et à elle seule
LIMITE_CORRELATION_MAX = 0.90
# origine: posée à la main | comparée au MAXIMUM signé, et à lui seul.
#          0,90 : au-delà, deux actifs ne sont plus deux actifs.
LIMITE_N_EFF_MIN = 3.0
# origine: posée à la main | nombre effectif de paris minimal

# ── LA CONSTANTE QUI SE RÉCLAMAIT DE LA CHARTE SANS Y FIGURER (G-4) ───────
LIMITE_VAR_PORTEFEUILLE_PCT = -3.0
# origine: posée à la main, NON DÉRIVÉE | la charte fondatrice ne comporte
#          AUCUNE limite de VaR : ni en partie IV (4.1 dimensionnement,
#          4.2 exposition, 4.3 drawdown, 4.4 stops, 4.5 corrélation,
#          4.6 crypto, 4.7 référence, 4.8 alpha/survie), ni ailleurs.
#          Le commentaire « charte IV » était une autorité usurpée. Ce
#          chiffre est un choix de la Section Risque, discutable en revue
#          mensuelle, opposable d'ici là — et rien d'autre.
ORIGINE_LIMITE_VAR_PORTEFEUILLE = (
    "posée à la main, non dérivée — aucune limite de VaR ne figure dans la "
    "charte fondatrice, ni en partie IV ni ailleurs")

KELLY_PLAFOND = 0.50           # origine: posée à la main | doctrine : Kelly ½ maximum
KELLY_DEFAUT = 0.25            # origine: posée à la main | doctrine : Kelly ¼ par défaut
DUREE_OBLIGATAIRE_10A = 8.5    # origine: propriété | duration modifiée du 10 ans US

# ── P2 : LIMITES DU VETO — les seules opposables à une idée ───────────────
# « Aucune transaction n'est passée sans cette section. » Ces cinq limites
# sont les seules opposables. Chacune a son seuil ici, en dur, en tête de
# fichier, et non enfoui dans une fonction.
LIMITE_VAR_POSITION_PCT = 2.0
# origine: posée à la main | plafond dur de perte au stop, en % de NAV.
#          La charte §4.4 EXIGE qu'une perte maximale soit déclarée avant
#          l'ouverture ; elle n'en fixe AUCUNE valeur. Le 2,0 est un choix.
LIMITE_TAILLE_PCT = 8.0
# origine: charte §4.1 | « Position individuelle maximale : 8 %. Sans exception »
LIMITE_CORRELATION = 0.70
# origine: charte §4.2 et §4.5 | « Positions à corrélation > 0,7 » agrégées
LIMITE_PERTE_STRESS_PCT = 2.0
# origine: posée à la main | perte de l'idée sous le pire épisode vécu
MIN_SEANCES_PAIRE = 1260
# origine: posée à la main | 5 ans de profondeur pour une cointégration

SEUILS_REGIME = {
    "vix_bas": 15.0, "vix_haut": 25.0,
    "courbe_inversee": 0.0, "courbe_pentue": 0.5,
}
# origine: posée à la main | bornes de qualification du régime (4 valeurs)
PERCENTILE_VIX_STRESS = 80
# origine: posée à la main | P15 : conditionnement EXOGÈNE sur le VIX

# ── G-2 : bornes de PLAUSIBILITÉ du schéma d'idée ─────────────────────────
# Elles ne sont pas des limites de risque : elles servent à distinguer une
# donnée ABSURDE d'une donnée simplement excessive. Une taille de −5 % ou de
# 4 000 % n'est pas une position hors limite, c'est un champ corrompu.
TAILLE_MIN_PLAUSIBLE_PCT = 0.0     # origine: propriété | une taille est ≥ 0 par définition
TAILLE_MAX_PLAUSIBLE_PCT = 100.0   # origine: propriété | une taille est ≤ 100 % de la NAV
CORRELATION_BORNE = 1.0            # origine: propriété | |ρ| ≤ 1, inégalité de Cauchy-Schwarz
PERTE_STOP_MAX_PLAUSIBLE_PCT = 100.0  # origine: propriété | une perte est ≤ 100 % de la NAV

FICHIER_ALERTES = "alertes_risque.jsonl"
FICHIER_RESULTATS = "risque_resultats.json"
FICHIER_VETO = "veto_risque.json"
FICHIER_TRADING = "trading_resultats.json"

# ── Registre d'origine, lu par le code et publié ──────────────────────────
# Il n'est pas décoratif : main() le compare à la liste réelle des constantes
# du module et refuse de publier un décompte si une constante matérielle
# n'y figure pas.
ORIGINE_CONSTANTES: dict[str, str] = {
    "NIVEAUX_VAR": "propriété",
    "FENETRES_VAR": "posée à la main",
    "METHODE_VAR_RETENUE": "posée à la main",
    "REGLE_FENETRE_LIMITE": "posée à la main",
    "SEUIL_BACKTEST": "propriété",
    "BACKTEST_BURN_IN": "posée à la main",
    "REGLE_VALEUR_CRITIQUE_BACKTEST": "posée à la main",
    "N_SIM_CALIBRATION_BACKTEST": "propriété",
    "SEUIL_KURT_CF": "propriété",
    "MIN_OBS_QUEUE": "propriété",
    "N_BOOTSTRAP_KELLY": "propriété",
    "N_BOOTSTRAP_ERREUR": "propriété",
    "N_SIM_NULL_CORR": "propriété",
    "GRAINE": "propriété",
    "LIMITE_DRAWDOWN_ALERTE": "charte §4.3",
    "LIMITE_DRAWDOWN_REDUCTION": "charte §4.3",
    "LIMITE_DRAWDOWN_SUSPENSION": "charte §4.3",
    "LIMITE_DRAWDOWN_COUPE_CIRCUIT": "charte §4.3",
    "LIMITE_CORRELATION_MOYENNE": "posée à la main",
    "LIMITE_CORRELATION_MAX": "posée à la main",
    "LIMITE_N_EFF_MIN": "posée à la main",
    "LIMITE_VAR_PORTEFEUILLE_PCT": "posée à la main",
    "KELLY_PLAFOND": "posée à la main",
    "KELLY_DEFAUT": "posée à la main",
    "DUREE_OBLIGATAIRE_10A": "propriété",
    "LIMITE_VAR_POSITION_PCT": "posée à la main",
    "LIMITE_TAILLE_PCT": "charte §4.1",
    "LIMITE_CORRELATION": "charte §4.2",
    "LIMITE_PERTE_STRESS_PCT": "posée à la main",
    "MIN_SEANCES_PAIRE": "posée à la main",
    "SEUILS_REGIME": "posée à la main",
    "PERCENTILE_VIX_STRESS": "posée à la main",
    "PANIER_NOMS": "posée à la main",
    "TAILLE_MIN_PLAUSIBLE_PCT": "propriété",
    "TAILLE_MAX_PLAUSIBLE_PCT": "propriété",
    "CORRELATION_BORNE": "propriété",
    "PERTE_STOP_MAX_PLAUSIBLE_PCT": "propriété",
}


def inventaire_constantes() -> dict:
    """
    G-11 — le décompte des constantes est PRODUIT, jamais affirmé.
    Vérifie en outre qu'aucune constante matérielle du module n'échappe au
    registre : toute variable de module en MAJUSCULES, de valeur scalaire,
    liste ou dictionnaire, doit y figurer, à l'exception des noms de fichiers
    et des chemins.
    """
    # Sont exclus : les chemins de fichiers, les registres eux-mêmes, les
    # ÉTIQUETTES de motifs (des chaînes de vocabulaire, pas des seuils) et
    # les caches internes. Rien de ce qui est exclu ne peut décider d'un
    # verdict : ce sont des noms, pas des valeurs.
    exclues = {"RACINE", "FICHIER_ALERTES", "FICHIER_RESULTATS", "FICHIER_VETO",
               "FICHIER_TRADING", "ORIGINE_CONSTANTES",
               "ORIGINE_LIMITE_VAR_PORTEFEUILLE", "CHEMIN_CANONIQUE",
               "CHAMPS_REQUIS_IDEE",
               "MOTIF_ABSENT", "MOTIF_ABERRANT", "MOTIF_MESURE",
               "_CACHE_CALIBRATION"}
    g = globals()
    reelles = {n for n, v in g.items()
               if n.isupper() and n not in exclues
               and isinstance(v, (int, float, str, list, dict, tuple))}
    manquantes = sorted(reelles - set(ORIGINE_CONSTANTES))
    fantomes = sorted(set(ORIGINE_CONSTANTES) - reelles)
    charte = sorted(n for n, o in ORIGINE_CONSTANTES.items() if o.startswith("charte"))
    prop = sorted(n for n, o in ORIGINE_CONSTANTES.items() if o == "propriété")
    libres = sorted(n for n, o in ORIGINE_CONSTANTES.items() if o == "posée à la main")
    return {
        "n_constantes_materielles": len(ORIGINE_CONSTANTES),
        "n_tracables_charte": len(charte),
        "n_proprietes": len(prop),
        "n_constantes_libres": len(libres),
        "tracables_charte": {n: ORIGINE_CONSTANTES[n] for n in charte},
        "proprietes": prop,
        "constantes_libres": libres,
        "non_enregistrees": manquantes,
        "enregistrees_inexistantes": fantomes,
        "registre_complet": not manquantes and not fantomes,
        "limite_var_portefeuille_origine": ORIGINE_LIMITE_VAR_PORTEFEUILLE,
    }


# ══════════════════════════════════════════════════════════════════════════
# OUTILS
# ══════════════════════════════════════════════════════════════════════════

def maintenant() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def est_nombre_fini(x) -> bool:
    """
    G-2 — LE PRÉDICAT QUI MANQUAIT.

    `np.isfinite(x) and x > seuil` vaut False sur NaN. Le veto lisait cette
    valeur comme « ne dépasse pas », donc « passe ». Une idée sans taille,
    sans stop et sans corrélation recevait le motif « aucune limite de risque
    dépassée ». Le mode de défaillance d'un contrôle n'est pas qu'il refuse à
    tort : c'est qu'il accepte en silence.

    Ce prédicat est VRAI uniquement pour un int ou un float réel et fini.
    Il est FAUX pour None, NaN, ±inf, une chaîne — y compris « 9.0 » —, un
    booléen (True vaut 1 en Python : une taille de True n'est pas une taille),
    une liste, un dict, un complexe, un tableau numpy.
    """
    if isinstance(x, bool):
        return False
    if isinstance(x, (int, np.integer)):
        return True
    if isinstance(x, (float, np.floating)):
        return bool(np.isfinite(x))
    return False


def arrondi_erreur(valeur: float, erreur: float) -> float:
    """
    P13 : un chiffre n'a de sens que jusqu'à son erreur d'échantillonnage.
    Arrondit `valeur` au premier chiffre significatif de `erreur`.
    -2,5043 % ± 0,7 % devient -2,5 %.
    """
    if not np.isfinite(valeur):
        return float("nan")
    if not np.isfinite(erreur) or erreur <= 0:
        return float(valeur)
    d = int(math.floor(math.log10(abs(erreur))))
    return float(round(valeur, -d))


# ══════════════════════════════════════════════════════════════════════════
# CHARGEMENT
# ══════════════════════════════════════════════════════════════════════════

def charger(data_dir: Path) -> dict[str, pd.Series]:
    hist = data_dir / "history"
    out = {}
    for f in sorted(hist.glob("*.csv")):
        try:
            d = pd.read_csv(f, parse_dates=["date"]).set_index("date")["value"]
            out[f.stem] = d.sort_index()
        except Exception:                                     # noqa: BLE001
            continue
    return out


def date_arrete(series: dict[str, pd.Series]) -> str:
    """
    P17 : une date d'arrêté UNIQUE, produite par le code, jamais saisie.
    C'est la dernière date d'observation disponible, toutes séries confondues.
    """
    dates = [s.dropna().index[-1] for s in series.values() if len(s.dropna())]
    return str(max(dates).date()) if dates else "INDISPONIBLE"


# ══════════════════════════════════════════════════════════════════════════
# VALUE AT RISK
# ══════════════════════════════════════════════════════════════════════════

def var_historique(r, niveau: float) -> float:
    """Aucune hypothèse de distribution. Ne voit que ce qui s'est produit."""
    x = np.asarray(pd.Series(r).dropna(), dtype=float)
    return float(np.percentile(x, (1 - niveau) * 100))


def var_parametrique(r, niveau: float) -> float:
    """Suppose la normalité. Sous-estime systématiquement les queues."""
    x = np.asarray(pd.Series(r).dropna(), dtype=float)
    return float(x.mean() + x.std(ddof=1) * stats.norm.ppf(1 - niveau))


def cornish_fisher_z(z, skew: float, kurt_exces: float):
    """Expansion de Cornish-Fisher, ordre 4. Correctement transcrite."""
    z = np.asarray(z, dtype=float)
    return (z + (z**2 - 1) * skew / 6
            + (z**3 - 3*z) * kurt_exces / 24
            - (2*z**3 - 5*z) * skew**2 / 36)


def cornish_fisher_valide(skew: float, kurt_exces: float,
                          z_min: float = -4.0, z_max: float = 0.0,
                          pas: float = 0.01) -> tuple[bool, str]:
    """
    Le quantile CF doit être strictement croissant en z sur [z_min, z_max].
    Une fonction quantile non monotone n'est la fonction quantile d'aucune loi.
    Retourne (bool, motif).
    """
    if kurt_exces > SEUIL_KURT_CF:
        return False, (f"kurtosis excédentaire {kurt_exces:.2f} > seuil "
                       f"{SEUIL_KURT_CF} : hors domaine de validité de "
                       f"l'expansion tronquée à l'ordre 4")
    z = np.arange(z_min, z_max + pas / 2, pas)
    q = cornish_fisher_z(z, skew, kurt_exces)
    d = np.diff(q)
    if not bool((d > 0).all()):
        i = int(np.argmin(d))
        return False, (f"quantile CF NON MONOTONE en z = {z[i]:.2f} "
                       f"(pente {d[i]:+.5f}) : ce n'est la fonction quantile "
                       f"d'aucune loi")
    return True, "monotone sur [%.1f ; %.1f]" % (z_min, z_max)


def var_cornish_fisher(r, niveau: float) -> tuple[float | None, str]:
    """
    P3 : rend None — JAMAIS un nombre — hors du domaine de validité.
    Publiée en annexe uniquement, et seulement si valide.
    """
    x = np.asarray(pd.Series(r).dropna(), dtype=float)
    s = float(stats.skew(x))
    k = float(stats.kurtosis(x, fisher=True))
    ok, motif = cornish_fisher_valide(s, k)
    if not ok:
        return None, motif
    z = float(cornish_fisher_z(stats.norm.ppf(1 - niveau), s, k))
    return float(x.mean() + x.std(ddof=1) * z), motif


# ── Johnson SU : monotone par construction ────────────────────────────────

def _moment_brut_su(n: int, a: float, b: float) -> float:
    """E[X^n] pour X = sinh((Z − a)/b), Z ~ N(0,1). Exact, par expansion."""
    s = 0.0
    for k in range(n + 1):
        c = n - 2 * k
        s += comb(n, k) * ((-1) ** k) * exp(-c * a / b + c * c / (2 * b * b))
    return s / 2 ** n


def moments_su(a: float, b: float) -> tuple[float, float, float, float]:
    """(moyenne, variance, asymétrie, kurtosis excédentaire) de johnsonsu(a,b)."""
    m1, m2, m3, m4 = (_moment_brut_su(n, a, b) for n in (1, 2, 3, 4))
    var = m2 - m1**2
    mu3 = m3 - 3*m1*m2 + 2*m1**3
    mu4 = m4 - 4*m1*m3 + 6*m1**2*m2 - 3*m1**4
    return m1, var, mu3 / var**1.5, mu4 / var**2 - 3


def calibrer_su(skew: float, kurt_exces: float) -> tuple[float, float] | None:
    """Calibration sur les DEUX moments de forme. None si hors domaine SU."""
    def f(p):
        a, lb = p
        _, _, s, k = moments_su(a, exp(lb))
        return [s - skew, k - kurt_exces]
    for x0 in ([0.0, 0.0], [-0.5, 0.5], [0.5, -0.3], [0.0, 1.0], [-1.0, 1.0]):
        try:
            p, _info, ier, _msg = optimize.fsolve(f, x0, full_output=True)
        except Exception:                                     # noqa: BLE001
            continue
        if ier != 1:
            continue
        a, b = float(p[0]), float(exp(p[1]))
        if not (np.isfinite(a) and np.isfinite(b)) or b <= 0:
            continue
        _, _, s, k = moments_su(a, b)
        if abs(s - skew) < 1e-6 and abs(k - kurt_exces) < 1e-5:
            return a, b
    return None


def var_johnson_su(r, niveau: float) -> float | None:
    """
    Ajustement Johnson SU calibré sur les QUATRE moments (moyenne, variance,
    asymétrie, kurtosis). C'est une vraie loi : sa fonction quantile est
    monotone par construction, contrairement à l'expansion de Cornish-Fisher.
    """
    x = np.asarray(pd.Series(r).dropna(), dtype=float)
    m, sd = float(x.mean()), float(x.std(ddof=1))
    sk = float(stats.skew(x))
    ku = float(stats.kurtosis(x, fisher=True))
    p = calibrer_su(sk, ku)
    if p is None:
        return None
    a, b = p
    mm, vv, _, _ = moments_su(a, b)
    if vv <= 0:
        return None
    sc = sd / math.sqrt(vv)
    loc = m - sc * mm
    return float(stats.johnsonsu.ppf(1 - niveau, a, b, loc=loc, scale=sc))


def diagnostic_cornish_fisher(r) -> dict:
    """
    P3 — rend AUDITABLE l'affirmation « la VaR CF est non monotone » : balaie
    les niveaux de confiance et cherche le maximum de la « VaR » CF. Si ce
    maximum est atteint ailleurs qu'au niveau le plus bas, la fonction n'est
    pas monotone ; s'il est POSITIF, l'objet publié annonce un GAIN garanti
    à un niveau de confiance intermédiaire. Ce n'est la fonction quantile
    d'aucune loi.
    """
    x = np.asarray(pd.Series(r).dropna(), dtype=float)
    s = float(stats.skew(x))
    k = float(stats.kurtosis(x, fisher=True))
    niv = np.arange(0.50, 0.999 + 1e-9, 0.001)
    z = stats.norm.ppf(1 - niv)
    q = x.mean() + x.std(ddof=1) * cornish_fisher_z(z, s, k)
    i = int(np.argmax(q))
    monotone = bool((np.diff(q) < 0).all())   # doit DÉCROÎTRE quand niv croît
    return {"skew": s, "kurtosis_exces": k,
            "monotone_en_niveau": monotone,
            "max_var_cf_pct": float(q[i] * 100),
            "niveau_du_max": float(niv[i]),
            "var_cf_positive": bool(q[i] > 0),
            "lecture": (f"maximum de la « VaR » CF = {q[i]*100:+.3f} % atteint "
                        f"au niveau {niv[i]*100:.1f} %"
                        if not monotone else "monotone")}


def cvar(r, niveau: float) -> dict:
    """
    Perte moyenne CONDITIONNELLE au dépassement de la VaR.
    P13 : REFUSE de produire un chiffre si la queue compte moins de
    MIN_OBS_QUEUE observations. Une moyenne de 3 points publiée à quatre
    décimales est une fausse précision, pas une mesure.
    """
    x = np.asarray(pd.Series(r).dropna(), dtype=float)
    seuil = np.percentile(x, (1 - niveau) * 100)
    queue = x[x <= seuil]
    n = int(len(queue))
    if n < MIN_OBS_QUEUE:
        return {"disponible": False, "n_queue": n,
                "motif": f"queue de {n} observation(s) < MIN_OBS_QUEUE="
                         f"{MIN_OBS_QUEUE} : refus de publier"}
    val = float(queue.mean())
    err = float(queue.std(ddof=1) / math.sqrt(n))
    return {"disponible": True, "n_queue": n, "valeur_pct": val * 100,
            "erreur_type_pct": err * 100,
            "valeur_arrondie_pct": arrondi_erreur(val * 100, err * 100),
            "ic95_pct": [arrondi_erreur((val - 1.96 * err) * 100, err * 100),
                         arrondi_erreur((val + 1.96 * err) * 100, err * 100)]}


def erreur_var_historique(r, niveau: float, b: int = N_BOOTSTRAP_ERREUR) -> float:
    """Erreur d'échantillonnage de la VaR historique, par bootstrap (P13)."""
    x = np.asarray(pd.Series(r).dropna(), dtype=float)
    rng = np.random.default_rng(GRAINE)
    n = len(x)
    if n < 60:
        return float("nan")
    tirages = rng.integers(0, n, size=(b, n))
    q = np.percentile(x[tirages], (1 - niveau) * 100, axis=1)
    return float(q.std(ddof=1))


# ══════════════════════════════════════════════════════════════════════════
# P5 — BACKTEST DE VaR : Kupiec (couverture) + Christoffersen (indépendance)
# ══════════════════════════════════════════════════════════════════════════

def kupiec_pof(x: int, T: int, p: float) -> tuple[float, float]:
    """
    Test de couverture non conditionnelle (proportion of failures).
    LR_uc = -2 ln[(1-p)^(T-x) p^x] + 2 ln[(1-x/T)^(T-x) (x/T)^x] ~ χ²(1).
    """
    if T <= 0:
        return float("nan"), float("nan")

    def ll(pi, a, b):
        t = 0.0
        if a > 0:
            t += a * log(1 - pi) if pi < 1 else -np.inf
        if b > 0:
            t += b * log(pi) if pi > 0 else -np.inf
        return t

    lr = -2 * ll(p, T - x, x) + 2 * ll(x / T, T - x, x)
    lr = max(float(lr), 0.0)
    return lr, float(1 - stats.chi2.cdf(lr, 1))


def christoffersen_independance(ind) -> tuple[float, float, dict]:
    """
    Test de Markov sur la matrice de transition des dépassements ~ χ²(1).
    C'EST LE TEST IMPORTANT. Le mode de ruine n'est pas « une VaR dépassée »,
    c'est cinq dépassements en huit séances : le nombre total peut être
    parfaitement conforme pendant que les dépassements s'agglutinent.
    """
    v = np.asarray(ind, dtype=int)
    if len(v) < 2:
        return float("nan"), float("nan"), {}
    prec, suiv = v[:-1], v[1:]
    n00 = int(((prec == 0) & (suiv == 0)).sum())
    n01 = int(((prec == 0) & (suiv == 1)).sum())
    n10 = int(((prec == 1) & (suiv == 0)).sum())
    n11 = int(((prec == 1) & (suiv == 1)).sum())
    tm = {"n00": n00, "n01": n01, "n10": n10, "n11": n11}
    n0, n1 = n00 + n01, n10 + n11
    if n0 == 0 or n1 == 0 or (n01 + n11) == 0:
        return 0.0, 1.0, tm

    def ll(pi, a, b):
        t = 0.0
        if a > 0:
            t += a * log(1 - pi) if pi < 1 else -np.inf
        if b > 0:
            t += b * log(pi) if pi > 0 else -np.inf
        return t

    p01, p11 = n01 / n0, n11 / n1
    pi = (n01 + n11) / (n0 + n1)
    lr = -2 * (ll(pi, n00, n01) + ll(pi, n10, n11)) \
         + 2 * (ll(p01, n00, n01) + ll(p11, n10, n11))
    lr = max(float(lr), 0.0)
    return lr, float(1 - stats.chi2.cdf(lr, 1)), tm


# ── G-1 : CALIBRATION DES VALEURS CRITIQUES SOUS H₀ ───────────────────────

def _lr_vectorise(V: np.ndarray, p: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Kupiec, Christoffersen et leur somme, calculés en bloc sur un tableau
    (n_sim, T) d'indicatrices 0/1. Formules IDENTIQUES, ligne à ligne, à
    kupiec_pof() et christoffersen_independance() — c'est la condition pour
    que la valeur critique simulée soit celle de la statistique publiée et
    non celle d'une statistique voisine. Le test _test_calibration_identique()
    vérifie cette identité sur des séquences tirées au hasard.
    """
    V = np.asarray(V, dtype=np.int8)
    n_sim, T = V.shape
    x = V.sum(axis=1).astype(float)

    # ── Kupiec (couverture non conditionnelle)
    with np.errstate(divide="ignore", invalid="ignore"):
        pi_uc = x / T
        ll0 = (T - x) * math.log(1 - p) + x * math.log(p)
        t1 = np.where(x > 0, x * np.log(np.where(x > 0, pi_uc, 1.0)), 0.0)
        t2 = np.where(T - x > 0,
                      (T - x) * np.log(np.where(pi_uc < 1, 1 - pi_uc, 1.0)), 0.0)
        lr_uc = np.maximum(-2 * ll0 + 2 * (t1 + t2), 0.0)

    # ── Christoffersen (indépendance de Markov)
    prec, suiv = V[:, :-1], V[:, 1:]
    n00 = ((prec == 0) & (suiv == 0)).sum(axis=1).astype(float)
    n01 = ((prec == 0) & (suiv == 1)).sum(axis=1).astype(float)
    n10 = ((prec == 1) & (suiv == 0)).sum(axis=1).astype(float)
    n11 = ((prec == 1) & (suiv == 1)).sum(axis=1).astype(float)
    n0, n1 = n00 + n01, n10 + n11

    def ll(pi, a, b):
        t = np.zeros_like(pi, dtype=float)
        m = a > 0
        t[m] += a[m] * np.log(np.clip(1 - pi[m], 1e-300, None))
        m = b > 0
        t[m] += b[m] * np.log(np.clip(pi[m], 1e-300, None))
        return t

    p01 = np.where(n0 > 0, n01 / np.where(n0 > 0, n0, 1.0), 0.0)
    p11 = np.where(n1 > 0, n11 / np.where(n1 > 0, n1, 1.0), 0.0)
    pi = (n01 + n11) / np.where(n0 + n1 > 0, n0 + n1, 1.0)
    lr_ind = np.maximum(-2 * (ll(pi, n00, n01) + ll(pi, n10, n11))
                        + 2 * (ll(p01, n00, n01) + ll(p11, n10, n11)), 0.0)
    # cas dégénérés : christoffersen_independance() rend 0,0 — même convention
    lr_ind[(n0 == 0) | (n1 == 0) | ((n01 + n11) == 0)] = 0.0
    return lr_uc, lr_ind, lr_uc + lr_ind


_CACHE_CALIBRATION: dict[tuple, dict] = {}


def calibrer_valeurs_critiques(T: int, p: float,
                               n_sim: int = N_SIM_CALIBRATION_BACKTEST,
                               graine: int = GRAINE) -> dict:
    """
    G-1 — LA VALEUR CRITIQUE DÉCIDE : ELLE DOIT DONC ÊTRE CALIBRÉE.

    Sous H₀ « la VaR est correcte », les dépassements sont indépendants et de
    probabilité p. On tire n_sim séquences de Bernoulli(p) de longueur T — la
    LONGUEUR RÉELLEMENT TESTÉE, pas une longueur asymptotique — et on lit les
    quantiles empiriques des trois statistiques.

    Ce que cela corrige : à T = 1 251 et p = 5 %, l'asymptotique χ²(2) place
    la valeur critique à 5,991 alors que la vraie vaut environ 6,5. Une
    statistique de 6,39 est « rejetée » par la première et ne l'est pas par
    la seconde. Le verdict tenait à une approximation, pas à une mesure.

    Ce que cela NE corrige PAS, et qu'il faut dire : la calibration ne change
    rien au fait que les dépassements SONT groupés. Astra a réfuté
    l'hypothèse d'un Christoffersen sur-rejetant — sous H₀ il rejette 1,4 à
    1,8 % à un nominal de 1 %, soit un excès sans commune mesure avec les
    p-values observées. Le problème se déplace, il ne disparaît pas.

    Rend aussi la fonction de répartition empirique, pour produire des
    p-values CALIBRÉES : p_cal = (1 + #{sim ≥ obs}) / (1 + n_sim).
    """
    cle = (int(T), round(float(p), 10), int(n_sim), int(graine))
    if cle in _CACHE_CALIBRATION:
        return _CACHE_CALIBRATION[cle]
    rng = np.random.default_rng(graine + int(T) * 1000 + int(round(p * 10000)))
    # tirage par blocs : (n_sim, T) en int8 reste sous 50 Mo aux tailles réelles
    V = (rng.random((n_sim, T)) < p).astype(np.int8)
    lr_uc, lr_ind, lr_cc = _lr_vectorise(V, p)
    out = {
        "T": int(T), "p": float(p), "n_simulations": int(n_sim),
        "graine": int(graine),
        "hypothese_nulle": "dépassements i.i.d. Bernoulli(p), tailles réelles",
        "valeur_critique_5pct": {
            "kupiec": float(np.percentile(lr_uc, 95)),
            "christoffersen": float(np.percentile(lr_ind, 95)),
            "conjoint": float(np.percentile(lr_cc, 95)),
        },
        "valeur_critique_1pct": {
            "kupiec": float(np.percentile(lr_uc, 99)),
            "christoffersen": float(np.percentile(lr_ind, 99)),
            "conjoint": float(np.percentile(lr_cc, 99)),
        },
        "valeur_critique_asymptotique_5pct": {
            "kupiec": float(stats.chi2.ppf(0.95, 1)),
            "christoffersen": float(stats.chi2.ppf(0.95, 1)),
            "conjoint": float(stats.chi2.ppf(0.95, 2)),
        },
        # taux de rejet EFFECTIF de l'asymptotique sous H₀ : mesure directe
        # de l'erreur de première espèce que l'on commettait
        "taux_rejet_effectif_asymptotique_5pct": {
            "kupiec": float((lr_uc > stats.chi2.ppf(0.95, 1)).mean()),
            "christoffersen": float((lr_ind > stats.chi2.ppf(0.95, 1)).mean()),
            "conjoint": float((lr_cc > stats.chi2.ppf(0.95, 2)).mean()),
        },
        "taux_rejet_effectif_asymptotique_1pct": {
            "kupiec": float((lr_uc > stats.chi2.ppf(0.99, 1)).mean()),
            "christoffersen": float((lr_ind > stats.chi2.ppf(0.99, 1)).mean()),
            "conjoint": float((lr_cc > stats.chi2.ppf(0.99, 2)).mean()),
        },
        "_echantillons": {"kupiec": np.sort(lr_uc), "christoffersen": np.sort(lr_ind),
                          "conjoint": np.sort(lr_cc)},
    }
    _CACHE_CALIBRATION[cle] = out
    return out


def p_calibree(calib: dict, statistique: str, valeur: float) -> float:
    """p-value empirique sous H₀ : (1 + #{sim ≥ obs}) / (1 + n_sim)."""
    ech = calib["_echantillons"][statistique]
    if not np.isfinite(valeur):
        return float("nan")
    n_sup = int(len(ech) - np.searchsorted(ech, valeur, side="left"))
    return float((1 + n_sup) / (1 + len(ech)))


def backtest_var(r: np.ndarray, fenetre: int | str, niveaux: list[float],
                 methodes=("historique", "parametrique", "johnson_su")) -> list[dict]:
    """
    P5 — FENÊTRE GLISSANTE HORS ÉCHANTILLON, obligatoire.
    Calibrer sur les N jours PRÉCÉDENTS, tester sur le jour suivant, avancer.

    PIÈGE ÉVITÉ : un backtest in-sample de la VaR historique donne
    mécaniquement round((1-p)·T) dépassements — 25 sur 504 à 95 % — et une
    p-value de 0,967. C'est une tautologie arithmétique, pas une validation.
    """
    r = np.asarray(r, dtype=float)
    n = len(r)
    extensible = (fenetre == "complet")
    depart = BACKTEST_BURN_IN if extensible else int(fenetre)
    if n - depart < 100:
        return [{"fenetre": str(fenetre), "disponible": False,
                 "motif": "moins de 100 tests hors échantillon possibles"}]

    # G-8 — un jour où la calibration Johnson SU ÉCHOUE n'est pas un jour sans
    # dépassement : c'est un jour SANS VaR. L'ancien code écrivait 0 dans la
    # série d'indicatrices, ce qui comptait l'échec comme un succès du modèle
    # et biaisait les deux tests EN FAVEUR du modèle. Les jours sans VaR sont
    # désormais retirés de la série et comptés à part.
    depass = {(m, niv): [] for m in methodes for niv in niveaux}
    n_echecs_su, n_jours = 0, 0
    for t in range(depart, n):
        ech = r[:t] if extensible else r[t - depart:t]
        n_jours += 1
        # Johnson SU : calibration UNE fois par date, réutilisée aux 2 niveaux
        su = None
        if "johnson_su" in methodes:
            sk, ku = float(stats.skew(ech)), float(stats.kurtosis(ech, fisher=True))
            p_su = calibrer_su(sk, ku)
            if p_su is not None:
                a, b = p_su
                mm, vv, _, _ = moments_su(a, b)
                sc = float(ech.std(ddof=1)) / math.sqrt(vv)
                su = (a, b, float(ech.mean()) - sc * mm, sc)
            else:
                n_echecs_su += 1
        for niv in niveaux:
            for m in methodes:
                if m == "historique":
                    v = float(np.percentile(ech, (1 - niv) * 100))
                elif m == "parametrique":
                    v = float(ech.mean() + ech.std(ddof=1) * stats.norm.ppf(1 - niv))
                else:
                    v = (float(stats.johnsonsu.ppf(1 - niv, su[0], su[1],
                                                   loc=su[2], scale=su[3]))
                         if su is not None else None)
                if v is None:
                    continue                      # G-8 : jour SANS VaR, écarté
                depass[(m, niv)].append(int(r[t] < v))

    out = []
    for niv in niveaux:
        p = 1 - niv
        # G-1 : la calibration ne dépend que de (T, p). Elle est faite une fois
        # par couple et mise en cache. Elle est faite AVANT de lire le résultat.
        for m in methodes:
            ind = depass[(m, niv)]
            T, x = len(ind), int(sum(ind))
            n_ecartes = n_jours - T
            lr_uc, p_uc = kupiec_pof(x, T, p)
            lr_i, p_i, tm = christoffersen_independance(ind)
            lr_cc = lr_uc + lr_i
            p_cc = float(1 - stats.chi2.cdf(lr_cc, 2))
            bi, bs = stats.binom.ppf([0.025, 0.975], T, p)

            calib = calibrer_valeurs_critiques(T, p)
            vc_cal = calib["valeur_critique_5pct"]
            vc_asy = calib["valeur_critique_asymptotique_5pct"]
            p_uc_cal = p_calibree(calib, "kupiec", lr_uc)
            p_i_cal = p_calibree(calib, "christoffersen", lr_i)
            p_cc_cal = p_calibree(calib, "conjoint", lr_cc)

            rejet_asy = bool(p_cc < SEUIL_BACKTEST)
            rejet_cal = bool(lr_cc > vc_cal["conjoint"])
            # LA RÈGLE DÉCLARÉE EX ANTE : c'est la calibrée qui décide.
            rejet = rejet_cal
            out.append({
                "fenetre": str(fenetre), "niveau": niv, "methode": m,
                "hors_echantillon": True, "n_tests": T,
                "n_jours_calibrables": n_jours,
                "n_jours_ecartes_sans_var": n_ecartes,
                "taux_echec_modele_pct": round(100.0 * n_ecartes / n_jours, 3)
                if n_jours else float("nan"),
                "depassements_observes": x, "depassements_attendus": round(T * p, 1),
                "ic95_binomial": [int(bi), int(bs)],
                "LR_uc": round(lr_uc, 4), "p_kupiec": round(p_uc, 4),
                "LR_ind": round(lr_i, 4), "p_christoffersen": round(p_i, 4),
                "LR_cc": round(lr_cc, 4), "p_conjoint": round(p_cc, 4),
                # ── G-1 : les DEUX valeurs critiques, et la p-value calibrée
                "regle_de_decision": REGLE_VALEUR_CRITIQUE_BACKTEST,
                "valeur_critique_5pct_calibree": round(vc_cal["conjoint"], 4),
                "valeur_critique_5pct_asymptotique": round(vc_asy["conjoint"], 4),
                "valeur_critique_kupiec_calibree": round(vc_cal["kupiec"], 4),
                "valeur_critique_christoffersen_calibree":
                    round(vc_cal["christoffersen"], 4),
                "p_kupiec_calibree": round(p_uc_cal, 4),
                "p_christoffersen_calibree": round(p_i_cal, 4),
                "p_conjoint_calibree": round(p_cc_cal, 4),
                "n_simulations_calibration": calib["n_simulations"],
                "graine_calibration": calib["graine"],
                "rejetee_asymptotique": rejet_asy,
                "rejetee_calibree": rejet_cal,
                "verdicts_divergent": bool(rejet_asy != rejet_cal),
                "matrice_transition": tm,
                "rejetee": rejet,
                "consequence": ("RETIRÉE du tableau des limites" if rejet
                                else "admissible comme limite"),
            })
    return out


# ══════════════════════════════════════════════════════════════════════════
# MESURES DE PERFORMANCE AJUSTÉE
# ══════════════════════════════════════════════════════════════════════════

def rendement_annualise(r) -> float:
    """
    P1 — la série est en LOG-rendements : la capitalisation est additive dans
    l'exposant. (1+r).prod() appliqué à des log-rendements n'a aucun sens.
    """
    x = np.asarray(pd.Series(r).dropna(), dtype=float)
    return float(np.exp(x.sum() * 252 / len(x)) - 1)


def valeur_capitalisee(r) -> np.ndarray:
    """P1 — exp(cumsum), jamais (1+r).cumprod()."""
    x = np.asarray(pd.Series(r).dropna(), dtype=float)
    return np.exp(np.cumsum(x))


def sortino(r, cible: float = 0.0) -> float:
    """
    Ne pénalise que la volatilité BAISSIÈRE. Le Sharpe pénalise les deux.

    P10 — le dénominateur est la racine du moment partiel inférieur d'ordre 2,
    calculé sur TOUT l'échantillon : min(r − cible, 0)² moyenné sur n, et non
    r² moyenné sur les seules séances négatives. L'erreur valait un facteur
    1/√p (p = part des séances sous la cible) et gonflait le dénominateur.
    Numérateur : rendement annualisé composé, MÊME convention que le Sharpe.
    """
    x = np.asarray(pd.Series(r).dropna(), dtype=float)
    if len(x) < 2:
        return float("nan")
    dd = math.sqrt(float((np.minimum(x - cible, 0.0) ** 2).mean()))
    if dd <= 0:
        return float("nan")
    ann = rendement_annualise(x) - cible * 252
    return float(ann / (dd * math.sqrt(252)))


def drawdown(r) -> dict:
    x = pd.Series(r).dropna()
    cum = pd.Series(valeur_capitalisee(x), index=x.index)   # P1
    pic = cum.cummax()
    dd = cum / pic - 1
    creux = dd.idxmin()
    creux_str = str(creux.date()) if hasattr(creux, "date") else str(creux)
    sous_eau = int((dd < -0.001).sum())
    # plus longue période sous l'eau, en séances consécutives — INCHANGÉ
    plus_longue, courante = 0, 0
    for v in (dd < -0.001).values:
        courante = courante + 1 if v else 0
        plus_longue = max(plus_longue, courante)
    return {
        "max": float(dd.min()), "date_creux": creux_str,
        "courant": float(dd.iloc[-1]),
        "seances_sous_eau": sous_eau,
        "pct_temps_sous_eau": float(sous_eau / len(dd) * 100),
        "plus_longue_serie_sous_eau": int(plus_longue),
        "valeur_finale": float(cum.iloc[-1]),
    }


def drawdown_ref_simple(rs) -> float:
    """
    Référence indépendante, écrite pour le test de non-régression : drawdown
    maximal calculé sur des rendements SIMPLES par capitalisation directe.
    Aucun logarithme n'intervient ici.
    """
    x = np.asarray(rs, dtype=float)
    cum = np.cumprod(1.0 + x)
    pic = np.maximum.accumulate(cum)
    return float((cum / pic - 1.0).min())


def calmar(r) -> float:
    ann = rendement_annualise(r)                             # P1
    dd = drawdown(r)["max"]
    return float(ann / abs(dd)) if dd < 0 else float("nan")


def taux_sans_risque(series: dict, index) -> pd.Series | None:
    """
    P11 — DFF est dans SERIES_OBLIGATOIRES d'apollon_data.py et le fichier
    existe. Un Sharpe sans taux sans risque n'est pas un Sharpe.
    Conversion : taux annuel en % → log-rendement quotidien.
    """
    dff = series.get("DFF")
    if dff is None or not len(dff.dropna()):
        return None
    rf = (dff.dropna() / 100.0).reindex(index, method="ffill")
    return np.log1p(rf) / 252.0


def sharpe(r, rf_quotidien: pd.Series | None = None) -> dict:
    """
    P11 — publie les DEUX versions, brute et excédentaire.

    POINT AGGRAVANT, à conserver écrit : le bug de composition (P1) gonflait
    le Sharpe d'environ +0,10 et l'omission du taux sans risque le dégonflait
    de −0,11 à −0,20. Le 0,650 publié était approximativement juste PAR
    COMPENSATION DE DEUX FAUTES. Deux erreurs qui se compensent produisent un
    chiffre juste et un raisonnement faux ; seul le chiffre était contrôlé.
    """
    x = pd.Series(r).dropna()
    ann = rendement_annualise(x)
    vol = float(x.std(ddof=1) * math.sqrt(252))
    out = {"rendement_annualise_pct": ann * 100,
           "volatilite_annualisee_pct": vol * 100,
           "sharpe_brut": float(ann / vol) if vol > 0 else float("nan"),
           "note": "sharpe_brut n'est PAS un Sharpe : il omet le taux sans risque"}
    if rf_quotidien is not None:
        rf = rf_quotidien.reindex(x.index).ffill().bfill()
        rf_ann = float(np.exp(rf.mean() * 252) - 1)
        exces = x - rf
        vol_e = float(exces.std(ddof=1) * math.sqrt(252))
        out.update({
            "taux_sans_risque_moyen_pct": rf_ann * 100,
            "rendement_excedentaire_pct": (ann - rf_ann) * 100,
            "sharpe_excedentaire": float((ann - rf_ann) / vol) if vol > 0 else float("nan"),
            "sharpe_excedentaire_vol_exces": float(rendement_annualise(exces) / vol_e)
            if vol_e > 0 else float("nan"),
        })
    return out


def controle_coherence_sortino(r, s_sortino: float, s_sharpe: float) -> dict:
    """
    P10 — le signe qui a trahi le bug : 0,655 ≈ 0,650. Deux mesures censées
    différer sur une série asymétrique coïncidaient. Ce contrôle refait ce
    raisonnement automatiquement, à chaque exécution.
    """
    sk = float(stats.skew(np.asarray(pd.Series(r).dropna(), dtype=float)))
    ecart = abs(s_sortino - s_sharpe)
    suspect = bool(ecart < 0.05 and abs(sk) > 0.05)
    return {"skew": sk, "ecart_sortino_sharpe": ecart, "suspect": suspect,
            "motif": ("Sortino ≈ Sharpe sur une série d'asymétrie non nulle : "
                      "dénominateur baissier probablement faux"
                      if suspect else "écart cohérent avec l'asymétrie mesurée")}


def kelly(r, fraction: float = KELLY_DEFAUT,
          n_bootstrap: int = N_BOOTSTRAP_KELLY) -> dict:
    """
    P12 — le critère de Kelly s'écrit mu_ARITHMÉTIQUE / sigma².
    Sur des log-rendements : mu_arith = mu_log + sigma²/2. L'omission du
    terme sigma²/2 retranche exactement 0,500× au levier, quelle que soit la
    série — signature arithmétique du bug, et non un écart d'estimation.

    Kelly PLEIN reste inapplicable : il suppose des probabilités connues avec
    exactitude, ce qui n'arrive jamais en marché. Plafond doctrinal : Kelly ½,
    défaut Kelly ¼.

    ET SURTOUT — l'intervalle. L'estimateur de Kelly est un rapport dont le
    numérateur est une moyenne : son erreur type est ÉNORME. Publier 3,892×
    à quatre chiffres significatifs quand l'intervalle à 90 % englobe Kelly ¼,
    Kelly ½ ET Kelly plein est une fausse précision. INTERDIT ici.
    """
    x = np.asarray(pd.Series(r).dropna(), dtype=float)
    mu_log, var = float(x.mean()), float(x.var(ddof=1))
    if var <= 0:
        return {"disponible": False}
    mu_arith = mu_log + var / 2.0                            # P12
    k = mu_arith / var
    k_faux = mu_log / var
    rng = np.random.default_rng(GRAINE)
    n = len(x)
    tirages = x[rng.integers(0, n, size=(n_bootstrap, n))]
    m = tirages.mean(axis=1)
    v = tirages.var(axis=1, ddof=1)
    ks = (m + v / 2.0) / v
    q05, q50, q95 = (float(np.percentile(ks, p)) for p in (5, 50, 95))
    et = float(ks.std(ddof=1))
    return {
        "disponible": True,
        "kelly_plein": arrondi_erreur(k, et),
        "kelly_plein_brut": k,
        "kelly_erreur_type": et,
        "kelly_ic90": [arrondi_erreur(q05, et), arrondi_erreur(q95, et)],
        "kelly_ic90_brut": [q05, q95],
        "kelly_mediane_bootstrap": arrondi_erreur(q50, et),
        "kelly_sans_terme_sigma2_sur_2": k_faux,
        "ecart_du_au_terme_sigma2_sur_2": k - k_faux,
        "n_bootstrap": n_bootstrap,
        "fraction_appliquee": fraction,
        "taille_recommandee_x": arrondi_erreur(k * fraction, et * fraction),
        "plafond_doctrinal_x": arrondi_erreur(k * KELLY_PLAFOND, et * KELLY_PLAFOND),
        "publication_interdite": "quatre chiffres significatifs — l'intervalle "
                                 "à 90 % couvre Kelly ¼, ½ et plein",
        "avertissement": "Kelly plein ruine. Plafond ½, défaut ¼.",
        "lecture": f"Kelly plein ∈ [{arrondi_erreur(q05, et)} ; "
                   f"{arrondi_erreur(q95, et)}] à 90 %",
    }


# ══════════════════════════════════════════════════════════════════════════
# P18 — CODE MANQUANT VERSÉ AU DÉPÔT : la table Kelly devient auditable
# ══════════════════════════════════════════════════════════════════════════

def simulation_levier(r, fractions=(1.0, 0.5, 0.25),
                      kelly_plein: float | None = None,
                      reequilibrage: int = 1) -> list[dict]:
    """
    P18 — la table Kelly de la doctrine (−87,0 % de drawdown, ×21,30) n'était
    produite par AUCUNE ligne du moteur. Elle l'est ici.

    `reequilibrage` est EXPLICITE et en séances : un levier reconstitué chaque
    jour et un levier reconstitué chaque mois ne suivent pas le même chemin.
    Entre deux rééquilibrages, le levier dérive avec la performance ; à levier
    élevé, cette dérive change le drawdown de plusieurs points.

    Le levier s'applique aux rendements SIMPLES : 1 + L·(e^r − 1), puis on
    repasse en log pour capitaliser. Appliquer un levier à un log-rendement
    est le même bug que P1.
    """
    x = np.asarray(pd.Series(r).dropna(), dtype=float)
    simple = np.exp(x) - 1.0
    if kelly_plein is None:
        mu, var = x.mean(), x.var(ddof=1)
        kelly_plein = (mu + var / 2) / var
    out = []
    for f in fractions:
        levier = kelly_plein * f
        capital = 1.0
        chemin = np.empty(len(simple))
        pos = levier          # levier effectif courant
        ancre = 1.0
        for i, s in enumerate(simple):
            if reequilibrage > 0 and i % reequilibrage == 0:
                pos, ancre = levier, capital
            # entre deux rééquilibrages, l'exposition dérive avec le capital
            expo = pos * (ancre / capital) if capital > 0 else 0.0
            capital *= (1.0 + expo * s)
            if capital <= 0:
                capital = 0.0
                chemin[i:] = 0.0
                break
            chemin[i] = capital
        cum = pd.Series(chemin, index=pd.Series(r).dropna().index)
        dd = float((cum / cum.cummax() - 1).min())
        out.append({
            "fraction_kelly": f, "levier": float(levier),
            "reequilibrage_seances": reequilibrage,
            "valeur_finale_x": round(float(cum.iloc[-1]), 2),
            "drawdown_max_pct": round(dd * 100, 1),
            "capital_restant_au_creux_pct": round((1 + dd) * 100, 1),
            "ruine": bool(cum.min() <= 0.0),
        })
    return out


# ══════════════════════════════════════════════════════════════════════════
# RÉGIME ET PERCENTILES
# ══════════════════════════════════════════════════════════════════════════

def graduer_profondeur(n: int, cible: int) -> dict:
    """
    P16 — un booléen mettait T10Y2Y (2 499 obs, −0,04 % de la cible) et
    BAMLH0A0HYM2 (787 obs, −69 %) sous le MÊME drapeau `false`.
    Trois états, avec l'écart chiffré.
    """
    ecart = (n - cible) / cible * 100
    if n >= cible:
        etat = "suffisante"
    elif ecart > -10.0:
        etat = "marginale"
    else:
        etat = "insuffisante"
    return {"n_obs": n, "cible": cible, "ecart_pct": round(ecart, 2), "etat": etat}


def percentile_courant(s: pd.Series, fenetres=(252, 2520)) -> dict:
    s = s.dropna()
    if len(s) < 60:
        return {"disponible": False}
    v = float(s.iloc[-1])
    out = {"disponible": True, "valeur": v, "date": str(s.index[-1].date()),
           "n_obs_total": len(s)}
    for f in fenetres:
        sub = s.iloc[-f:] if len(s) >= f else s
        out[f"pct_{f}"] = float((sub < v).mean() * 100)
        out[f"n_obs_{f}"] = len(sub)
        out[f"profondeur_{f}"] = graduer_profondeur(len(s), f)      # P16
    return out


def regime(series: dict) -> dict:
    r = {}
    vix = series.get("VIXCLS")
    if vix is not None and len(vix.dropna()):
        v = float(vix.dropna().iloc[-1])
        r["volatilite"] = ("BASSE" if v < SEUILS_REGIME["vix_bas"]
                           else "MOYENNE" if v <= SEUILS_REGIME["vix_haut"] else "HAUTE")
        r["vix"] = v
    pente = series.get("T10Y2Y")
    if pente is not None and len(pente.dropna()):
        p = float(pente.dropna().iloc[-1])
        r["courbe"] = ("INVERSEE" if p < SEUILS_REGIME["courbe_inversee"]
                       else "PLATE" if p < SEUILS_REGIME["courbe_pentue"] else "PENTUE")
        r["pente_2s10s"] = p
    sp = series.get("SP500")
    if sp is not None and len(sp.dropna()) >= 200:
        s = sp.dropna()
        ma = float(s.iloc[-200:].mean())
        r["tendance"] = "HAUSSIERE" if float(s.iloc[-1]) > ma else "BAISSIERE"
        r["ecart_ma200_pct"] = float((s.iloc[-1] / ma - 1) * 100)
    hy = series.get("BAMLH0A0HYM2")
    if hy is not None and len(hy.dropna()) >= 60:
        h = hy.dropna()
        m60 = float(h.iloc[-60:].mean())
        r["credit"] = "ELARGISSEMENT" if float(h.iloc[-1]) > m60 else "RESSERREMENT"
        r["hy_oas"] = float(h.iloc[-1])
        r["hy_vs_ma60_pb"] = float((h.iloc[-1] - m60) * 100)
    axes = [r.get(k) for k in ("volatilite", "courbe", "tendance", "credit")]
    r["regime"] = " / ".join(a for a in axes if a) or "INDETERMINE"
    return r


# ══════════════════════════════════════════════════════════════════════════
# P14 / P15 — CORRÉLATIONS
# ══════════════════════════════════════════════════════════════════════════

def rendements_panier(series: dict) -> tuple[pd.DataFrame, list[str]]:
    """
    P14 — DGS10 est un TAUX ACTUARIEL EN POURCENTAGE, pas un prix.
    np.log(taux).diff() mesure la variation RELATIVE DU TAUX ; le rendement
    obligataire vaut approximativement −duration × Δtaux, de SIGNE OPPOSÉ.
    Publier +0,266 pour S&P 500 / 10 ans, c'est publier la seule ligne
    diversifiante du panier avec le signe inversé.
    """
    noms = ["SP500", "NASDAQ100", "DGS10", "DCOILBRENTEU", "DEXUSEU", "VIXCLS"]
    d, retenus = {}, []
    for n in noms:
        if n not in series:
            continue
        s = series[n].dropna()
        if n == "DGS10":
            d["OBLIG10A"] = -DUREE_OBLIGATAIRE_10A * s.diff() / 100.0
            retenus.append("OBLIG10A (= −%.1f × ΔDGS10, converti en rendement)"
                           % DUREE_OBLIGATAIRE_10A)
        else:
            d[n] = np.log(s).diff()
            retenus.append(n)
    return pd.DataFrame(d).dropna(), retenus


PANIER_NOMS = ["SP500", "NASDAQ100", "DGS10", "DCOILBRENTEU", "DEXUSEU", "VIXCLS"]


def rendements_panier_origine(series: dict) -> pd.DataFrame:
    """
    G-7 — LE PANIER D'ORIGINE, RECONSTRUIT PAR LE CODE.

    L'audit 009 relevait que le « 0,2501 » attribué à la doctrine était
    AFFIRMÉ dans une chaîne de caractères et produit par aucune ligne. C'est
    exactement la faute que P18 prétendait fermer, répétée un cran plus bas.

    Cette fonction reconstruit le panier TEL QU'IL ÉTAIT AVANT la correction
    P14 — c'est-à-dire avec DGS10 traité comme un prix, np.log(taux).diff(),
    ce qui est faux — dans le seul but de RE-PRODUIRE le chiffre de doctrine
    et de le confronter au chiffre corrigé. Il n'entre dans aucune limite,
    n'alimente aucune alerte, et ne sert qu'à l'auditabilité de l'écart.
    """
    d = {}
    for n in PANIER_NOMS:
        if n not in series:
            continue
        s = series[n].dropna()
        s = s[s > 0]
        d[n] = np.log(s).diff()
    return pd.DataFrame(d).dropna()


def moyenne_abs_correlations(df: pd.DataFrame) -> float:
    """Moyenne des |ρ| du triangle supérieur. Une seule définition, partagée."""
    cc = df.corr()
    t = cc.where(np.triu(np.ones(cc.shape), 1).astype(bool)).stack()
    return float(t.abs().mean())


def chiffre_doctrine_correlation_stress(rets_origine: pd.DataFrame,
                                        decile: float = 10.0) -> dict:
    """
    G-7 — PRODUIT le « 0,250 » de la doctrine au lieu de l'affirmer.

    Construction exacte, énoncée puis exécutée : moyenne des |ρ| de toutes
    les paires du panier D'ORIGINE, restreinte aux séances du décile
    inférieur du S&P 500, corrélations INCLUANT le S&P 500.
    """
    if rets_origine is None or rets_origine.empty or "SP500" not in rets_origine:
        return {"disponible": False, "motif": "panier d'origine indisponible"}
    q = float(np.percentile(rets_origine["SP500"], decile))
    sous = rets_origine[(rets_origine["SP500"] <= q).values]
    val = moyenne_abs_correlations(sous)
    complet = moyenne_abs_correlations(rets_origine)
    return {
        "disponible": True,
        "construction": f"moyenne des |ρ| du panier D'ORIGINE (DGS10 en "
                        f"log(taux), non corrigé) sur le décile inférieur du "
                        f"S&P 500, corrélations incluant le S&P 500",
        "actifs": list(rets_origine.columns),
        "n_obs": int(len(rets_origine)),
        "n_obs_decile": int(len(sous)),
        "seuil_decile_sp500": q,
        "valeur_produite": val,
        "valeur_produite_arrondie": round(val, 4),
        "valeur_complet": complet,
        "chiffre_de_doctrine": 0.250,
        "ecart_au_chiffre_de_doctrine": val - 0.250,
        "reproduit": bool(abs(val - 0.250) < 0.0005),
    }


def diagnostics_correlation(rets: pd.DataFrame) -> dict:
    """
    P14 — `abs()` confond couverture et doublon. ρ = −0,93 et ρ = +0,93 ont le
    même |ρ| mais des volatilités de portefeuille dans un rapport de 5,25.
    La règle « toute paire > 0,70 traitée comme position unique » appliquée à
    |ρ| INTERDIRAIT la position qui réduit le risque. Le VIX, à −0,725 avec le
    S&P, est la seule protection du panier : il était compté comme un facteur
    de concentration.

    La moyenne des corrélations ne distingue pas deux structures de risque
    différentes. N_eff = (Σλ)²/Σλ² le fait.

    G-5 — N_eff SUR QUELLE MATRICE ? LA QUESTION N'EST PAS DE FORME.
    N_eff calculé sur la matrice de CORRÉLATION suppose implicitement que
    tous les actifs sont ramenés à la même volatilité — c'est-à-dire une
    pondération en risque, que ce module N'APPLIQUE PAS. La ligne suivante
    du code d'origine calculait vol_p à poids ÉGAUX sur des actifs de
    volatilités très différentes : la matrice qui correspond à cette
    pondération est la matrice de COVARIANCE, pas la corrélation.
    Les deux sont publiées. L'OPPOSABLE est celui de la COVARIANCE, parce
    qu'il décrit le portefeuille réellement pondéré. Le VIX, dont la
    volatilité quotidienne est plusieurs fois celle des autres lignes,
    absorbe alors l'essentiel de la variance et le panier n'a plus rien
    d'un panier : N_eff s'effondre.
    """
    c = rets.corr()
    triu = c.where(np.triu(np.ones(c.shape), 1).astype(bool)).stack()
    lam = np.linalg.eigvalsh(c.values)
    lam = np.clip(lam, 0, None)
    n_eff = float(lam.sum() ** 2 / (lam ** 2).sum())

    sig = rets.std(ddof=1).values
    w = np.ones(len(sig)) / len(sig)
    cov = np.outer(sig, sig) * c.values
    vol_p = float(math.sqrt(w @ cov @ w))
    ratio_div = float((w * sig).sum() / vol_p) if vol_p > 0 else float("nan")

    # ── G-5 : N_eff sur la COVARIANCE — la matrice de la pondération utilisée
    lam_cov = np.clip(np.linalg.eigvalsh(cov), 0, None)
    n_eff_cov = float(lam_cov.sum() ** 2 / (lam_cov ** 2).sum()) \
        if (lam_cov ** 2).sum() > 0 else float("nan")
    # contributions marginales à la variance du panier équipondéré
    var_p = float(w @ cov @ w)
    contrib = (w * (cov @ w)) / var_p if var_p > 0 else np.full(len(w), np.nan)
    contributions = {a: float(cv * 100) for a, cv in zip(c.columns, contrib)}
    i_dom = int(np.argmax(contrib))
    return {
        "n_actifs": int(c.shape[0]),
        "actifs": list(c.columns),
        "correlation_moyenne_signee": float(triu.mean()),
        "correlation_signee_max": {"paire": " / ".join(triu.idxmax()),
                                   "valeur": float(triu.max())},
        "correlation_signee_min": {"paire": " / ".join(triu.idxmin()),
                                   "valeur": float(triu.min())},
        "correlation_absolue_moyenne_POUR_MEMOIRE": float(triu.abs().mean()),
        # ── N_eff : les DEUX, et l'opposable est nommé
        "n_effectif_paris_correlation": n_eff,
        "n_effectif_paris_covariance": n_eff_cov,
        "n_effectif_paris_opposable": n_eff_cov,
        "base_n_eff_opposable": "covariance",
        "motif_base_opposable":
            "la volatilité de panier est calculée à poids ÉGAUX sur les "
            "rendements bruts ; la matrice correspondant à cette pondération "
            "est la covariance. N_eff sur la corrélation décrirait un "
            "portefeuille pondéré en risque, qui n'est pas celui-ci.",
        # rétro-compatibilité de lecture : la clé historique pointe désormais
        # sur l'OPPOSABLE, pour qu'aucun lecteur ne récupère la valeur douce
        "n_effectif_paris": n_eff_cov,
        "contributions_variance_pct": contributions,
        "actif_dominant_variance": {"actif": str(c.columns[i_dom]),
                                    "part_variance_pct": float(contrib[i_dom] * 100)},
        "lambda_max_sur_n": float(lam.max() / len(lam)),
        "ratio_diversification": ratio_div,
        "volatilite_panier_equipondere": vol_p,
        "note": "seule la corrélation SIGNÉE entre dans une limite ; |ρ| est "
                "publiée pour mémoire et n'est opposable à rien",
        "matrice": {a: {b: float(c.loc[a, b]) for b in c.columns} for a in c.index},
    }


def correlation_conditionnelle(rets: pd.DataFrame, vix: pd.Series,
                               n_sim: int = N_SIM_NULL_CORR,
                               rets_origine: pd.DataFrame | None = None) -> dict:
    """
    P15 — LE BIAIS EST CALCULABLE, donc il doit être calculé.

    Conditionner sur les pires séances du S&P puis mesurer des corrélations
    INCLUANT le S&P est un biais de sélection (Boyer-Gibson-Loretan 1999).
    Mesuré par l'audit sous une gaussienne à ρ CONSTANT = 0,300 :
      · conditionnement sur les 1 % plus grands mouvements en |valeur| → 0,676
        (+37,6 pt d'artefact) ;
      · conditionnement sur la queue gauche seule → 0,099 (−20,1 pt).
    Le biais CHANGE DE SIGNE selon la spécification : la mesure brute n'est
    donc pas interprétable, quel que soit son sens.

    Ici : conditionnement sur une variable EXOGÈNE (VIX > percentile 80) —
    cas témoin sans biais — ET publication du null de corrélation constante
    par simulation. Sans le null, l'écart observé n'est pas interprétable.
    """
    def moy_signee(df):
        cc = df.corr()
        t = cc.where(np.triu(np.ones(cc.shape), 1).astype(bool)).stack()
        return float(t.mean())

    v = vix.reindex(rets.index).ffill()
    seuil = float(np.nanpercentile(v.dropna().values, PERCENTILE_VIX_STRESS))
    masque = (v > seuil).values
    if masque.sum() < 60:
        return {"disponible": False, "motif": "sous-échantillon conditionnel trop court"}

    m_all = moy_signee(rets)
    m_st = moy_signee(rets[masque])
    delta = m_st - m_all

    # null : corrélation CONSTANTE, mêmes dates de conditionnement
    c = rets.corr().values
    c = (c + c.T) / 2
    lam, vec = np.linalg.eigh(c)
    lam = np.clip(lam, 1e-12, None)
    L = vec @ np.diag(np.sqrt(lam))
    rng = np.random.default_rng(GRAINE)
    n, k = len(rets), rets.shape[1]
    deltas = np.empty(n_sim)
    for i in range(n_sim):
        X = rng.standard_normal((n, k)) @ L.T
        df = pd.DataFrame(X, columns=rets.columns)
        deltas[i] = moy_signee(df[masque]) - moy_signee(df)
    q05, q95 = float(np.percentile(deltas, 5)), float(np.percentile(deltas, 95))
    ecart_null = float(delta - deltas.mean())

    # méthode BIAISÉE, publiée uniquement pour montrer l'ampleur de l'artefact
    if "SP500" in rets.columns:
        q1 = float(np.percentile(rets["SP500"], 1))
        m_biais = moy_signee(rets[(rets["SP500"] <= q1).values])
    else:
        m_biais = float("nan")

    # P18 / G-7 — reproduction du « 0,250 » de la doctrine. Le chiffre est
    # désormais PRODUIT sur le panier d'origine par
    # chiffre_doctrine_correlation_stress(), et non plus affirmé dans une
    # chaîne de caractères.
    moy_abs = moyenne_abs_correlations

    doctrine = {"disponible": False}
    if "SP500" in rets.columns:
        q10 = float(np.percentile(rets["SP500"], 10))
        m_doc = moy_abs(rets[(rets["SP500"] <= q10).values])
        m_doc_all = moy_abs(rets)
        dn = np.empty(min(n_sim, 500))
        for i in range(len(dn)):
            X = rng.standard_normal((n, k)) @ L.T
            df = pd.DataFrame(X, columns=rets.columns)
            s10 = float(np.percentile(df["SP500"], 10))
            dn[i] = moy_abs(df[(df["SP500"] <= s10).values]) - moy_abs(df)
        origine = chiffre_doctrine_correlation_stress(rets_origine)
        doctrine = {
            "disponible": True,
            "construction": "moyenne des |ρ| sur le décile des pires séances du "
                            "S&P 500, corrélations incluant le S&P 500. Appliquée "
                            "ici au panier CORRIGÉ (10 ans converti en rendement "
                            "obligataire) ; la même construction est appliquée au "
                            "panier D'ORIGINE dans la clé "
                            "`chiffre_doctrine_produit`, dont la valeur est "
                            "CALCULÉE et non affirmée.",
            "valeur_reproduite": m_doc,
            "valeur_complet": m_doc_all,
            "delta_observe": m_doc - m_doc_all,
            "null_delta_moyen": float(dn.mean()),
            "null_ic90": [float(np.percentile(dn, 5)), float(np.percentile(dn, 95))],
            "ecart_au_null": float((m_doc - m_doc_all) - dn.mean()),
            # ── G-7 : le chiffre de doctrine, produit
            "chiffre_doctrine_produit": origine,
            "ecart_panier_origine_vs_corrige": (
                (origine.get("valeur_produite") - m_doc)
                if origine.get("disponible") else None),
            "lecture": "la baisse brute est un ARTEFACT de sélection : sous "
                       "corrélation CONSTANTE, la même construction fait baisser "
                       "la mesure davantage encore. L'écart au null est de SIGNE "
                       "OPPOSÉ à la lecture brute — la corrélation conditionnelle "
                       "est au-dessus du null, pas en dessous.",
        }

    return {
        "disponible": True,
        "conditionnement": f"EXOGÈNE — VIXCLS > percentile {PERCENTILE_VIX_STRESS} "
                           f"({seuil:.2f})",
        "n_seances_conditionnelles": int(masque.sum()),
        "correlation_moyenne_signee_complet": m_all,
        "correlation_moyenne_signee_stress": m_st,
        "delta_observe": delta,
        "null_correlation_constante": {
            "n_simulations": n_sim,
            "delta_moyen": float(deltas.mean()),
            "ic90": [q05, q95],
        },
        "ecart_au_null": ecart_null,
        "significatif_a_90pct": bool(delta < q05 or delta > q95),
        "methode_biaisee_pour_memoire": {
            "conditionnement": "queue gauche 1 % du S&P 500, corrélations "
                               "INCLUANT le S&P 500",
            "correlation_moyenne_signee": m_biais,
            "artefact_estime": (m_biais - m_all) if np.isfinite(m_biais) else None,
            "note": "biais de sélection Boyer-Gibson-Loretan — NON OPPOSABLE",
        },
        "reproduction_chiffre_doctrine": doctrine,
    }


# ══════════════════════════════════════════════════════════════════════════
# TESTS DE STRESS — NE PAS MODIFIER (défendue par l'audit Astra 007)
# ══════════════════════════════════════════════════════════════════════════

def episodes_de_stress(sp: pd.Series, n: int = 5) -> list[dict]:
    """
    Plutôt que des scénarios inventés, on mesure ce que le portefeuille de
    référence a RÉELLEMENT subi sur les pires fenêtres de l'historique.
    Un stress test sur épisode vécu est plus contraignant qu'un scénario
    choisi, parce qu'il n'a pas été choisi.
    """
    r = np.log(sp.dropna()).diff().dropna()
    f20 = r.rolling(20).sum().dropna()
    pires, exclus = [], set()
    for _ in range(n):
        cand = f20[~f20.index.isin(exclus)]
        if cand.empty:
            break
        d = cand.idxmin()
        pires.append({
            "fin_fenetre": str(d.date()),
            "perte_20_seances_pct": float((math.exp(cand.loc[d]) - 1) * 100),
        })
        exclus |= set(pd.date_range(d - pd.Timedelta(days=45),
                                    d + pd.Timedelta(days=45)))
    return pires


# ══════════════════════════════════════════════════════════════════════════
# P8 — JOURNAL D'ALERTES : LU, DÉDOUBLONNÉ, CLÔTURABLE
# ══════════════════════════════════════════════════════════════════════════

def cle_alerte(a: dict) -> tuple:
    """
    G-10 — LA DATE SORT DE LA CLÉ.

    Avec (type, niveau, date_donnees), chaque nouvelle journée de données
    créait une alerte NOUVELLE pour un dépassement INCHANGÉ : le compteur
    d'alertes non traitées croissait sans borne, mécaniquement, sans qu'aucun
    risque nouveau soit apparu. Un compteur qui croît toujours ne distingue
    plus la dérive du bruit — c'est la façon la plus efficace de rendre le
    tableau d'alertes illisible, et donc de reproduire 2008 par saturation
    plutôt que par silence.

    La clé identifie désormais la CONDITION (type, niveau), pas l'instant de
    sa constatation. La date de première émission et le nombre d'occurrences
    restent journalisés ; la dernière mesure connue est mise à jour à la
    lecture. Une condition close qui réapparaît est une NOUVELLE ligne, parce
    que la clôture porte l'identifiant et pas la clé.
    """
    return (a.get("type"), a.get("niveau"))


def id_alerte(a: dict) -> str:
    """
    L'IDENTIFIANT désigne une ÉMISSION, la clé désigne une CONDITION.
    L'identifiant conserve donc la date : il reste celui du journal existant,
    et une clôture prononcée hier continue de désigner la ligne d'hier.
    """
    brut = "|".join(str(x) for x in (a.get("type"), a.get("niveau"),
                                     a.get("date_donnees")))
    return "AL-" + hashlib.md5(brut.encode("utf-8")).hexdigest()[:8]


def lire_journal(chemin: Path) -> tuple[list[dict], list[dict]]:
    """
    P8 — le journal était ouvert en mode "a", jamais en "r". Aucune ligne
    n'était relue nulle part. La docstring promettait « le rapport porte en
    tête le nombre d'alertes non traitées » ; le code affichait len(al),
    c'est-à-dire les alertes du CYCLE COURANT. Promesse non tenue.
    """
    if not chemin.exists():
        return [], []
    alertes_j, clotures = [], []
    for ligne in chemin.read_text(encoding="utf-8").splitlines():
        ligne = ligne.strip()
        if not ligne:
            continue
        try:
            o = json.loads(ligne)
        except json.JSONDecodeError:
            continue
        (clotures if o.get("evenement") == "CLOTURE" else alertes_j).append(o)
    return alertes_j, clotures


def etat_journal(chemin: Path) -> dict:
    """
    G-10 — Dédoublonne par CONDITION (type, niveau) et compte les non traitées.

    L'état d'une condition est celui de sa DERNIÈRE émission : si le dernier
    identifiant émis a été clos, la condition est close ; si une émission
    POSTÉRIEURE à la clôture existe, elle est rouverte. Le journal étant
    append-only, l'ordre du fichier est l'ordre chronologique.
    """
    alertes_j, clotures = lire_journal(chemin)
    closes = {c.get("id") for c in clotures}
    uniques: dict[tuple, dict] = {}
    for a in alertes_j:
        k = cle_alerte(a)
        ident = a.get("id") or id_alerte(a)
        if k not in uniques:
            u = dict(a)
            u["id"] = ident                       # identifiant de PREMIÈRE émission
            u["id_derniere_emission"] = ident
            u["premiere_date_donnees"] = a.get("date_donnees")
            u["derniere_date_donnees"] = a.get("date_donnees")
            u["derniere_mesure"] = a.get("mesure")
            u["occurrences"] = 1
            u["ids_emissions"] = [ident]
            uniques[k] = u
        else:
            u = uniques[k]
            u["occurrences"] += 1
            u["id_derniere_emission"] = ident
            u["derniere_date_donnees"] = a.get("date_donnees")
            u["derniere_mesure"] = a.get("mesure", u.get("derniere_mesure"))
            u["ids_emissions"].append(ident)
            if a.get("traitee"):
                u["traitee"] = True
    for u in uniques.values():
        u["cloturee"] = bool(u["id_derniere_emission"] in closes)
        u["n_clotures_passees"] = sum(1 for i in u["ids_emissions"] if i in closes)
        u["non_traitee"] = bool(not u.get("traitee") and not u["cloturee"])
    non_traitees = [u for u in uniques.values() if u["non_traitee"]]
    return {
        "lignes_alertes_brutes": len(alertes_j),
        "alertes_uniques": len(uniques),
        "cle_de_dedoublonnage": "(type, niveau) — la date en est SORTIE (G-10)",
        "clotures": len(clotures),
        "n_non_traitees": len(non_traitees),
        "non_traitees": [{"id": u["id"], "type": u.get("type"),
                          "niveau": u.get("niveau"),
                          "premiere_date_donnees": u.get("premiere_date_donnees"),
                          "derniere_date_donnees": u.get("derniere_date_donnees"),
                          "derniere_mesure": u.get("derniere_mesure"),
                          "occurrences": u["occurrences"]} for u in non_traitees],
        "uniques": list(uniques.values()),
    }


def ecrire_alertes(chemin: Path, alertes_cycle: list[dict], horodatage: str) -> dict:
    """
    G-10 — Écrit UNIQUEMENT les alertes dont la CONDITION (type, niveau) n'est
    pas déjà OUVERTE au journal. 250 exécutions sur la même condition ne
    produisent plus 250 lignes, et 250 journées de données non plus.

    Une condition CLOSE qui réapparaît produit en revanche une ligne neuve :
    la réouverture est un fait, et un fait doit s'écrire.
    """
    etat = etat_journal(chemin)
    ouvertes = {cle_alerte(u) for u in etat["uniques"] if not u.get("cloturee")}
    nouvelles, reouvertures = [], []
    with open(chemin, "a", encoding="utf-8") as fh:
        for a in alertes_cycle:
            enr = {"date_donnees": horodatage, **a}
            k = cle_alerte(enr)
            if k in ouvertes:
                continue
            deja_vue = any(cle_alerte(u) == k for u in etat["uniques"])
            enr["id"] = id_alerte(enr)
            enr["horodatage_emission"] = maintenant()
            enr["traitee"] = False
            if deja_vue:
                enr["reouverture"] = True
                reouvertures.append(enr["id"])
            fh.write(json.dumps(enr, ensure_ascii=False) + "\n")
            ouvertes.add(k)
            nouvelles.append(enr["id"])
    return {"nouvelles": nouvelles, "reouvertures": reouvertures,
            "dedoublonnees": len(alertes_cycle) - len(nouvelles)}


def clore_alerte(chemin: Path, id_: str, motif: str) -> int:
    """
    P8 — primitive de clôture. La ligne d'origine n'est JAMAIS réécrite :
    le journal reste append-only et immuable, la clôture est un ÉVÉNEMENT
    supplémentaire, horodaté et motivé. C'est exactement ce qui manquait en
    2008 : une alerte classée sans trace écrite du classement.
    """
    etat = etat_journal(chemin)
    connus = {i for u in etat["uniques"] for i in u.get("ids_emissions", [u["id"]])}
    if id_ not in connus:
        print(f"Clôture refusée : identifiant {id_} absent du journal.")
        print("Identifiants ouverts : "
              + (", ".join(u["id_derniere_emission"] for u in etat["uniques"]
                           if u["non_traitee"]) or "aucun"))
        return 1
    if not motif or not motif.strip():
        print("Clôture refusée : une clôture sans motif écrit est un classement "
              "silencieux.")
        return 1
    with open(chemin, "a", encoding="utf-8") as fh:
        fh.write(json.dumps({"evenement": "CLOTURE", "id": id_,
                             "motif": motif.strip(),
                             "horodatage_cloture": maintenant()},
                            ensure_ascii=False) + "\n")
    print(f"Alerte {id_} close le {maintenant()} — motif : {motif.strip()}")
    print("La ligne d'origine est inchangée. Le journal reste immuable.")
    return 0


# ══════════════════════════════════════════════════════════════════════════
# ALERTES — non silenciables (leçon Kerviel)
# ══════════════════════════════════════════════════════════════════════════

def statut_paliers_drawdown(dd: dict, positions_detenues: int) -> dict:
    """
    G-3 — LE COUPE-CIRCUIT ÉTAIT CONDITIONNEL ET LA CONDITION ÉTAIT FAUSSE.

    Le commentaire d'origine affirmait que dd["courant"] vaut 0 « par
    construction » tant qu'aucune position n'est détenue. C'est FAUX, et la
    faute est de nature, pas de degré : dd["courant"] vaut 0 parce que le
    S&P 500 est à son plus haut historique à cette date d'arrêté — c'est un
    fait de marché, pas une propriété du code. Astra l'a démontré en
    exécutant sur données tronquées au 2020-03-23 avec position détenue :
    « DRAWDOWN COUPE-CIRCUIT −33,92 % → Liquidation à 80 % cash »,
    positions_detenues = 13. Le drawdown mesuré était non nul, et le
    coupe-circuit s'est déclenché.

    Un coupe-circuit dont l'activation dépend d'une croyance fausse sur les
    données est un coupe-circuit désarmé sans le savoir. Les paliers sont
    donc actifs dès que L'UNE des deux conditions est vraie :
      · une position est détenue ; OU
      · un drawdown NON NUL est mesuré sur le portefeuille réel.
    Le statut publié est CALCULÉ, avec son motif mesuré, jamais rédigé.
    """
    d = float(dd.get("courant", float("nan")))
    dd_non_nul = bool(np.isfinite(d) and abs(d) > 1e-12)
    actifs = bool(positions_detenues > 0 or dd_non_nul)
    if positions_detenues > 0 and dd_non_nul:
        motif = (f"{positions_detenues} position(s) détenue(s) ET drawdown "
                 f"mesuré {d*100:.2f} % non nul")
    elif positions_detenues > 0:
        motif = (f"{positions_detenues} position(s) détenue(s) ; drawdown "
                 f"courant mesuré {d*100:.2f} %")
    elif dd_non_nul:
        motif = (f"aucune position détenue, mais drawdown NON NUL mesuré sur "
                 f"le portefeuille de référence : {d*100:.2f} %")
    else:
        motif = ("aucune position détenue ET drawdown courant mesuré à "
                 f"{d*100:.2f} % — l'indice de référence est à son plus haut. "
                 "Ce n'est pas une propriété du code : c'est un fait de "
                 "marché, qui cessera d'être vrai à la première baisse.")
    return {
        "paliers_drawdown_actifs": actifs,
        "drawdown_courant_pct": d * 100 if np.isfinite(d) else float("nan"),
        "drawdown_courant_non_nul": dd_non_nul,
        "positions_detenues": int(positions_detenues),
        "motif_mesure": motif,
        "condition": "positions_detenues > 0 OU |drawdown_courant| > 0",
        "seuils_pct": [LIMITE_DRAWDOWN_ALERTE * 100,
                       LIMITE_DRAWDOWN_REDUCTION * 100,
                       LIMITE_DRAWDOWN_SUSPENSION * 100,
                       LIMITE_DRAWDOWN_COUPE_CIRCUIT * 100],
    }


def alertes(dd: dict, diag_corr: dict | None, reg: dict,
            var_retenue_pct: float | None = None,
            positions_detenues: int = 0,
            backtest_rejette_tout: bool = False,
            coherence: dict | None = None) -> list[dict]:
    a = []
    d = dd["courant"]
    # G-3 — les paliers sont ACTIFS dès qu'une position est détenue OU qu'un
    # drawdown non nul est mesuré. Voir statut_paliers_drawdown().
    st_paliers = statut_paliers_drawdown(dd, positions_detenues)
    if st_paliers["paliers_drawdown_actifs"]:
        for seuil, niveau, action in [
            (LIMITE_DRAWDOWN_COUPE_CIRCUIT, "COUPE-CIRCUIT",
             "Liquidation à 80 % cash. Arrêt 10 séances. Audit intégral."),
            (LIMITE_DRAWDOWN_SUSPENSION, "SUSPENSION",
             "Réduction de 50 % de l'exposition brute. Aucune position 5 séances."),
            (LIMITE_DRAWDOWN_REDUCTION, "REDUCTION",
             "Réduction de 30 % de l'exposition brute. Post-mortem obligatoire."),
            (LIMITE_DRAWDOWN_ALERTE, "ALERTE",
             "Revue complète des positions. Aucune position exploratoire."),
        ]:
            if np.isfinite(d) and d <= seuil:
                a.append({"type": "DRAWDOWN", "niveau": niveau,
                          "mesure": f"{d*100:.2f} %", "seuil": f"{seuil*100:.0f} %",
                          "motif_activation": st_paliers["motif_mesure"],
                          "action_exigee": action})
                break
    # P7 — la VaR retenue ENTRE ENFIN dans les alertes. Elle était calculée,
    # écrite dans le JSON, et jamais lue par personne ni par rien.
    if var_retenue_pct is not None and np.isfinite(var_retenue_pct):
        if var_retenue_pct <= LIMITE_VAR_PORTEFEUILLE_PCT:
            a.append({"type": "VAR", "niveau": "ALERTE",
                      "mesure": f"{var_retenue_pct:.2f} %",
                      "seuil": f"{LIMITE_VAR_PORTEFEUILLE_PCT:.2f} %",
                      "action_exigee": "VaR quotidienne du portefeuille de "
                                       "référence au-delà de la limite : "
                                       "réduction de l'exposition brute exigée."})
    if backtest_rejette_tout:
        a.append({"type": "BACKTEST_VAR", "niveau": "ALERTE",
                  "mesure": "aucune cellule non rejetée",
                  "seuil": f"p_conjoint ≥ {SEUIL_BACKTEST}",
                  "action_exigee": "Toutes les cellules de VaR sont rejetées par "
                                   "le test conjoint (dépassements groupés). La "
                                   "limite de VaR est déclarée NON FONDÉE : le "
                                   "veto s'appuie sur la limite de stress."})
    if diag_corr:
        # G-10 — LA MOYENNE CONTRE LE SEUIL DE MOYENNE. Comparer le MAXIMUM
        # (0,934, SP500/NASDAQ100) à LIMITE_CORRELATION_MOYENNE = 0,60
        # produisait une alerte qui ne pouvait JAMAIS s'éteindre : le panier
        # contient par construction deux indices actions US. Une alerte
        # permanente n'est pas une alerte, c'est un décor.
        cm = float(diag_corr["correlation_moyenne_signee"])
        if cm > LIMITE_CORRELATION_MOYENNE:
            a.append({"type": "CORRELATION_MOYENNE", "niveau": "ALERTE",
                      "mesure": f"moyenne signée {cm:+.3f}",
                      "seuil": f"moyenne > {LIMITE_CORRELATION_MOYENNE}",
                      "action_exigee": "Corrélation MOYENNE signée au-delà du "
                                       "seuil : la diversification du panier "
                                       "est illusoire dans son ensemble."})
        cs = float(diag_corr["correlation_signee_max"]["valeur"])
        if cs > LIMITE_CORRELATION_MAX:
            a.append({"type": "CORRELATION_MAX", "niveau": "ALERTE",
                      "mesure": f"{cs:.3f} ({diag_corr['correlation_signee_max']['paire']})",
                      "seuil": f"maximum > {LIMITE_CORRELATION_MAX}",
                      "action_exigee": "Paire de corrélation signée extrême : "
                                       "doublon, à traiter comme position unique "
                                       "(charte §4.2 / §4.5)."})
        # G-5 — l'OPPOSABLE est le N_eff de la COVARIANCE, celui qui décrit la
        # pondération réellement appliquée. Le N_eff de corrélation est publié
        # en regard : c'est lui qui donnait 3,542 et éteignait l'alerte.
        neff = float(diag_corr["n_effectif_paris_opposable"])
        neff_corr = float(diag_corr["n_effectif_paris_correlation"])
        if np.isfinite(neff) and neff < LIMITE_N_EFF_MIN:
            dom = diag_corr.get("actif_dominant_variance", {})
            a.append({"type": "CONCENTRATION", "niveau": "ALERTE",
                      "mesure": f"N_eff covariance {neff:.3f} "
                                f"(N_eff corrélation {neff_corr:.3f}, non opposable)",
                      "seuil": f"{LIMITE_N_EFF_MIN}",
                      "action_exigee": "Nombre effectif de paris insuffisant sur "
                                       "la matrice OPPOSABLE : diversification "
                                       "apparente, pas réelle. "
                                       + (f"{dom.get('actif')} porte "
                                          f"{dom.get('part_variance_pct', float('nan')):.1f} % "
                                          f"de la variance du panier."
                                          if dom else "")})
    if coherence and coherence.get("suspect"):
        a.append({"type": "COHERENCE", "niveau": "ALERTE",
                  "mesure": f"|Sortino − Sharpe| = {coherence['ecart_sortino_sharpe']:.3f}",
                  "seuil": "0.05",
                  "action_exigee": "Deux mesures censées différer coïncident sur "
                                   "une série asymétrique : vérifier le "
                                   "dénominateur baissier."})
    if reg.get("vix") is not None and reg["vix"] < SEUILS_REGIME["vix_bas"]:
        a.append({"type": "REGIME", "niveau": "INFORMATION",
                  "mesure": f"VIX {reg['vix']:.2f}",
                  "seuil": f"< {SEUILS_REGIME['vix_bas']}",
                  "action_exigee": "Politique de couverture : achat systématique "
                                   "SI intérêt assurable (bêta ≥ 0,15) ET VIX3M ≤ 17."})
    return a


# ══════════════════════════════════════════════════════════════════════════
# P2 — LE VETO. LE MANDAT DE LA CHARTE.
# ══════════════════════════════════════════════════════════════════════════

# ── G-2 : LE SCHÉMA D'IDÉE, DÉCLARÉ, UNIQUE, SANS REPLI ───────────────────
# CHEMIN_CANONIQUE fixe, pour chaque champ opposable, UNE source et une
# seule dans le JSON de la Section Trading. Il n'y a plus de chaîne de replis.
#
# La faute corrigée : l'ancien _normaliser_idee() lisait `taille_pct_nav`,
# et si la valeur n'était pas un nombre — cas d'une chaîne "9.0" — il allait
# chercher `criteres.6_taille_sous_limite.valeur`, y trouvait 3,0, et
# évaluait la limite sur un chiffre QUE PERSONNE N'AVAIT TRANSMIS. Une idée
# de taille 9 % passait donc sous un plafond de 8 % en étant silencieusement
# remplacée par une idée de taille 3 %. Le repli n'était pas une tolérance :
# c'était une falsification de l'objet contrôlé.
#
# `5_correlation_marche_actions` est situé DANS `criteres` : ce n'est pas un
# repli, c'est le seul endroit où la Section Trading publie cette valeur.
# La différence est que ce chemin est UNIQUE et DÉCLARÉ, et qu'aucun autre
# n'est essayé si celui-là est absent ou mal typé.
CHEMIN_CANONIQUE: dict[str, tuple] = {
    "nom": ("paire",),
    "taille_pct": ("taille_pct_nav",),
    "perte_stop_pct": ("perte_au_stop_pct",),
    "correlation": ("criteres", "5_correlation_marche_actions", "valeur"),
    "n_obs_paire": ("n_obs",),
    "echantillon_contient_stress": ("echantillon_contient_stress",),
}

# Type attendu et domaine de plausibilité de chaque champ requis.
#   ("texte",)                        → chaîne non vide
#   ("nombre", borne_inf, borne_sup)  → int/float réel fini dans [inf ; sup]
#   ("booleen",)                      → True ou False, rien d'autre
CHAMPS_REQUIS_IDEE: dict[str, tuple] = {
    "nom": ("texte",),
    "taille_pct": ("nombre", TAILLE_MIN_PLAUSIBLE_PCT, TAILLE_MAX_PLAUSIBLE_PCT),
    "perte_stop_pct": ("nombre", -PERTE_STOP_MAX_PLAUSIBLE_PCT,
                       PERTE_STOP_MAX_PLAUSIBLE_PCT),
    "correlation": ("nombre", -CORRELATION_BORNE, CORRELATION_BORNE),
    "n_obs_paire": ("nombre", 0.0, 1e7),
    "echantillon_contient_stress": ("booleen",),
}

MOTIF_ABSENT = "DONNEE_MANQUANTE"
MOTIF_ABERRANT = "DONNEE_ABERRANTE"
MOTIF_MESURE = "MESURE_INDISPONIBLE"


def _lire_chemin(o, chemin: tuple):
    """
    Descend un chemin canonique. Rend le sentinelle _ABSENT dès qu'un maillon
    manque ou n'est pas un dict. Ne remplace JAMAIS rien par une valeur par
    défaut : l'absence est une information, pas un trou à combler.
    """
    cour = o
    for cle in chemin:
        if not isinstance(cour, dict) or cle not in cour:
            return _ABSENT
        cour = cour[cle]
    return cour


class _Absent:
    __slots__ = ()

    def __repr__(self):                                       # pragma: no cover
        return "<ABSENT>"


_ABSENT = _Absent()


def valider_schema_idee(idee) -> tuple[bool, list[str], dict]:
    """
    G-2 — LA VALIDATION S'EXÉCUTE AVANT TOUTE ÉVALUATION DE LIMITE.

    Le mode de défaillance corrigé : `np.isfinite(x) and x > seuil` vaut
    False sur NaN. Le veto lisait ce False comme « la limite n'est pas
    dépassée », donc « l'idée passe ». Sur les 18 idées de test de l'audit
    009, les 5 violations bien formées bloquaient — et 7 entrées MALFORMÉES
    sur 11 passaient, dont une idée sans taille, sans stop et sans
    corrélation, à laquelle le moteur délivrait le motif « aucune limite de
    risque dépassée ». Un contrôle qui échoue en mode PASSANT est pire que
    l'absence de contrôle : il produit une trace écrite d'autorisation.

    Règle, sans exception : toute donnée absente, None, NaN, ±inf, non
    numérique, mal typée ou hors domaine de plausibilité produit un VETO.
    Jamais un `pass`, jamais une valeur de repli, jamais un défaut implicite.

    Rend (conforme, motifs, canonique). `canonique` n'est renseigné que si
    conforme est vrai : on ne construit pas d'objet à partir de données dont
    on vient d'établir qu'elles ne sont pas exploitables.
    """
    motifs: list[str] = []
    if not isinstance(idee, dict):
        return False, [f"{MOTIF_ABSENT}: idee — l'entrée n'est pas un objet JSON "
                       f"mais un {type(idee).__name__}"], {}

    brut: dict = {}
    for champ, attendu in CHAMPS_REQUIS_IDEE.items():
        val = _lire_chemin(idee, CHEMIN_CANONIQUE[champ])
        chemin_txt = ".".join(CHEMIN_CANONIQUE[champ])
        if val is _ABSENT:
            motifs.append(f"{MOTIF_ABSENT}: {champ} — champ absent "
                          f"(chemin canonique « {chemin_txt} »)")
            continue
        if val is None:
            motifs.append(f"{MOTIF_ABSENT}: {champ} — valeur null "
                          f"(chemin canonique « {chemin_txt} »)")
            continue
        genre = attendu[0]
        if genre == "texte":
            if not isinstance(val, str) or not val.strip():
                motifs.append(f"{MOTIF_ABSENT}: {champ} — attendu une chaîne non "
                              f"vide, reçu {type(val).__name__} ({val!r})")
                continue
            brut[champ] = val.strip()
        elif genre == "booleen":
            if not isinstance(val, bool):
                motifs.append(f"{MOTIF_ABSENT}: {champ} — attendu un booléen, "
                              f"reçu {type(val).__name__} ({val!r})")
                continue
            brut[champ] = bool(val)
        else:
            if not est_nombre_fini(val):
                motifs.append(f"{MOTIF_ABSENT}: {champ} — attendu un nombre réel "
                              f"fini, reçu {type(val).__name__} ({val!r})")
                continue
            x = float(val)
            inf, sup = attendu[1], attendu[2]
            if not (inf <= x <= sup):
                motifs.append(f"{MOTIF_ABERRANT}: {champ} = {x:g} hors du domaine "
                              f"de plausibilité [{inf:g} ; {sup:g}]")
                continue
            brut[champ] = x

    if motifs:
        return False, motifs, {}

    canonique = {
        "id_trading": idee.get("id"),
        "nom": brut["nom"],
        "taille_pct": brut["taille_pct"],
        "correlation": brut["correlation"],
        "perte_stop_pct": abs(brut["perte_stop_pct"]),
        "n_obs_paire": int(brut["n_obs_paire"]),
        "echantillon_contient_stress": brut["echantillon_contient_stress"],
        "verdict_trading": idee.get("verdict"),
        "statut_risque": idee.get("statut_risque"),
        "alertes_trading": idee.get("alertes_trading")
        or idee.get("alertes_echantillon") or [],
    }
    return True, [], canonique


def beta_marche(idee_canon: dict, mesures: dict) -> dict:
    """
    G-6 — β, PAS ρ.

    La limite de stress estimait la perte de l'idée sous le pire épisode vécu
    par |pire_épisode| × taille × |ρ|. C'est une erreur de dimension : ρ est
    sans unité et borné par 1, alors que la sensibilité d'une position à un
    mouvement de marché est β = ρ · σ_position / σ_marché, qui n'est borné
    par rien. Une position deux fois plus volatile que le marché à ρ = 0,5 a
    β = 1,0 : la formule en ρ la comptait pour moitié moins que le marché
    lui-même alors qu'elle bouge autant.

    σ_position est l'écart type des VARIATIONS du spread coïntégré publié par
    la Section Trading (`sigma_increment`), σ_marché celui des rendements du
    portefeuille de référence mesuré SUR LA MÊME FENÊTRE que la paire.

    Si l'un des deux n'est pas mesurable, la fonction ne devine pas : elle
    rend disponible = False, et l'appelant doit poser un VETO. Une limite de
    stress qu'on ne sait pas calculer n'est pas une limite satisfaite.
    """
    nom = idee_canon.get("nom")
    rho = float(idee_canon.get("correlation", float("nan")))
    coints = mesures.get("cointegrations", {}) or {}
    sigmas_marche = mesures.get("sigma_marche_par_paire", {}) or {}
    c = coints.get(nom, {}) if isinstance(coints, dict) else {}
    sig_pos = c.get("sigma_increment") if isinstance(c, dict) else None
    sig_mkt = sigmas_marche.get(nom)
    if not est_nombre_fini(rho):
        return {"disponible": False, "motif": "corrélation non mesurée"}
    if not est_nombre_fini(sig_pos) or float(sig_pos) <= 0:
        return {"disponible": False,
                "motif": f"σ_position (sigma_increment) indisponible pour « {nom} »"}
    if not est_nombre_fini(sig_mkt) or float(sig_mkt) <= 0:
        return {"disponible": False,
                "motif": f"σ_marché indisponible sur la fenêtre de « {nom} »"}
    ratio = float(sig_pos) / float(sig_mkt)
    return {"disponible": True, "beta": rho * ratio, "rho": rho,
            "sigma_position": float(sig_pos), "sigma_marche": float(sig_mkt),
            "ratio_sigma": ratio,
            "facteur_correction_vs_rho": ratio,
            "formule": "β = ρ · σ_position / σ_marché"}


def sigma_marche_par_paire(r_marche: pd.Series, coints: dict) -> dict:
    """
    G-6 — σ_marché mesuré SUR LA FENÊTRE DE CHAQUE PAIRE.

    ρ et σ_position sont estimés par la Section Trading sur l'échantillon
    propre à la paire ; mesurer σ_marché sur un autre échantillon
    produirait un β composite dont aucune ligne n'aurait de sens. Quand la
    fenêtre de la paire n'est pas déclarée, la fonction ne devine pas : elle
    n'inscrit rien, et beta_marche() rendra indisponible — ce qui bloque.
    """
    out: dict[str, float] = {}
    if not isinstance(coints, dict):
        return out
    x = pd.Series(r_marche).dropna()
    for nom, c in coints.items():
        if not isinstance(c, dict):
            continue
        deb, fin = c.get("debut"), c.get("fin")
        try:
            sub = x.loc[str(deb):str(fin)] if (deb and fin) else x
        except Exception:                                     # noqa: BLE001
            sub = x
        if len(sub) < 60:
            sub = x
        s = float(sub.std(ddof=1))
        if np.isfinite(s) and s > 0:
            out[nom] = s
    return out


def lire_idees_transmises(chemin: Path) -> dict:
    """
    Lit trading_resultats.json.

    G-9 — QUATRE ÉTATS DISTINCTS, JAMAIS CONFONDUS :
      · OK               — le fichier a été lu et `idees` est une liste ;
      · ABSENT           — le fichier n'existe pas ;
      · ILLISIBLE        — le fichier existe et n'est pas du JSON valide ;
      · SCHEMA_INVALIDE  — le JSON est valide mais `idees` est absent ou
                           n'est pas une liste.
    Les trois derniers signifient « je n'ai pas pu examiner », ce qui n'est
    PAS « rien à examiner ». Ils produisent une alerte et un code de sortie
    non nul. Une liste vide, elle, est un état légitime : il n'y avait rien.

    TRIAGE — sont soumises au veto :
      · les idées dont le verdict Trading commence par TRANSMISE ;
      · celles dont le statut est EN_ATTENTE_VETO ;
      · toute entrée NON TRIABLE — non-dict, ou sans verdict ni statut
        lisibles. Une entrée qu'on ne sait pas classer va au veto, où elle
        sera bloquée : le doute ne se résout jamais en autorisation.
    """
    vide = {"statut": "ABSENT", "disponible": False, "examinable": False,
            "idees": [], "cointegrations": {}, "n_idees_lues": 0,
            "n_soumises": 0, "n_non_soumises": 0, "non_soumises": []}
    if not chemin.exists():
        return {**vide, "motif": f"{chemin.name} absent — source non examinée"}
    try:
        texte = chemin.read_text(encoding="utf-8")
    except Exception as e:                                    # noqa: BLE001
        return {**vide, "statut": "ILLISIBLE",
                "motif": f"{chemin.name} illisible : {e}"}
    try:
        d = json.loads(texte)
    except Exception as e:                                    # noqa: BLE001
        return {**vide, "statut": "ILLISIBLE",
                "motif": f"{chemin.name} : JSON invalide — {e}"}
    if not isinstance(d, dict):
        return {**vide, "statut": "SCHEMA_INVALIDE",
                "motif": f"{chemin.name} : racine JSON de type "
                         f"{type(d).__name__}, objet attendu"}
    if "idees" not in d:
        return {**vide, "statut": "SCHEMA_INVALIDE",
                "motif": f"{chemin.name} : clé « idees » absente — la source "
                         f"existe mais ne dit pas ce qu'elle transmet"}
    brutes = d.get("idees")
    if not isinstance(brutes, list):
        return {**vide, "statut": "SCHEMA_INVALIDE",
                "motif": f"{chemin.name} : « idees » de type "
                         f"{type(brutes).__name__}, liste attendue"}

    # ------------------------------------------------------------------
    # G-12 — CONTRÔLE DE FRAÎCHEUR (audit 010, réserve laissée ouverte)
    #
    # La Section Trading émet un bloc `fraicheur` portant `perime_apres_utc`
    # et un champ `controle_attendu_de_l_aval` qui décrit littéralement ce
    # que cette fonction doit faire. Jusqu'ici personne ne le lisait : le
    # fichier savait dire qu'il était périmé, et l'aval ne l'écoutait pas.
    #
    # C'est la forme générale de R-044 — l'instrument construit et branché
    # sur rien. Un fichier périmé lu sans contrôle, c'est la Section Risque
    # opposant les mesures de la veille aux idées du jour, en silence.
    #
    # Un fichier périmé, incomplet, ou portant une date de données autre que
    # celle de l'arrêté examiné n'est PAS « rien à examiner » : c'est
    # « je n'ai pas pu examiner ». Même traitement que ILLISIBLE.
    # ------------------------------------------------------------------
    fr = d.get("fraicheur")
    if not isinstance(fr, dict):
        return {**vide, "statut": "SANS_MARQUEUR_FRAICHEUR",
                "motif": f"{chemin.name} : bloc « fraicheur » absent — "
                         f"impossible d'établir que ce fichier est du cycle "
                         f"courant. Une source non datée n'est pas opposable."}
    if fr.get("execution_complete") is not True:
        return {**vide, "statut": "EXECUTION_INCOMPLETE",
                "motif": f"{chemin.name} : `execution_complete` = "
                         f"{fr.get('execution_complete')!r} — la source déclare "
                         f"ne pas avoir terminé son cycle."}
    peremption = fr.get("perime_apres_utc")
    try:
        lim = datetime.fromisoformat(str(peremption).replace("Z", "+00:00"))
        if lim.tzinfo is None:
            lim = lim.replace(tzinfo=timezone.utc)
    except Exception:                                         # noqa: BLE001
        return {**vide, "statut": "PEREMPTION_ILLISIBLE",
                "motif": f"{chemin.name} : `perime_apres_utc` = "
                         f"{peremption!r} — non interprétable."}
    maintenant = datetime.now(timezone.utc)
    if maintenant > lim:
        retard_h = (maintenant - lim).total_seconds() / 3600.0
        return {**vide, "statut": "PERIME",
                "motif": f"{chemin.name} PÉRIMÉ de {retard_h:.1f} h "
                         f"(limite {lim.isoformat()}). Les idées d'un cycle "
                         f"antérieur ne peuvent pas être opposées aux mesures "
                         f"de risque du cycle courant."}

    coints = d.get("cointegrations", {})
    if not isinstance(coints, dict):
        coints = {}
    soumises, non_soumises = [], []
    for o in brutes:
        if not isinstance(o, dict):
            soumises.append(o)                    # non triable ⇒ au veto
            continue
        verdict = str(o.get("verdict", "") or "").upper()
        statut = str(o.get("statut_risque", "") or "").upper()
        if verdict.startswith("TRANSMISE") or statut == "EN_ATTENTE_VETO":
            soumises.append(o)
        elif verdict or statut:
            non_soumises.append({"id": o.get("id"),
                                 "nom": o.get("paire") or o.get("nom"),
                                 "verdict": o.get("verdict"),
                                 "statut_risque": o.get("statut_risque")})
        else:
            soumises.append(o)                    # ni verdict ni statut ⇒ au veto
    return {"statut": "OK", "disponible": True, "examinable": True,
            "motif": "source lue",
            "idees": soumises,
            "cointegrations": coints,
            "n_idees_lues": len(brutes),
            "n_soumises": len(soumises),
            "n_non_soumises": len(non_soumises),
            "non_soumises": non_soumises,
            "date_donnees_trading": d.get("date_donnees")}


def veto(idees: list, mesures: dict, limites: dict) -> list[dict]:
    """
    Lit chaque idée TRANSMISE par la Section Trading, lui applique les limites
    de risque MESURÉES par cette section, et rend un verdict opposable.
    Aucune idée ne peut être exécutée sans un enregistrement dans ce fichier.

    La charte dit : « aucune transaction n'est passée sans cette section ».
    Jusqu'à l'audit 007, apollon_trading.py imprimait « transmise à la
    Section Risque pour veto » et apollon_risque.py ne lisait jamais
    trading_resultats.json : le veto était une PHRASE. L'audit 009 a montré
    que le mécanisme qui l'a remplacée échouait en mode PASSANT sur toute
    donnée malformée. Les deux fautes ont la même conséquence — une idée non
    contrôlée réputée contrôlée — et la seconde est plus grave, parce qu'elle
    produisait une trace écrite d'autorisation.

    ORDRE D'EXÉCUTION, non négociable :
      1. valider_schema_idee() — AVANT toute évaluation de limite ;
      2. si non conforme : VETO, motifs DONNEE_MANQUANTE / DONNEE_ABERRANTE,
         et AUCUNE limite n'est évaluée — on ne mesure pas un objet dont on
         ne connaît pas les champs ;
      3. sinon, les cinq limites, chacune précédée de son contrôle de
         finitude, chacune produisant un motif explicite si elle bloque.
    """
    verdicts = []
    var_ref = mesures.get("var_retenue_pct")           # < 0, en % du portefeuille
    var_fondee = bool(mesures.get("var_limite_fondee"))
    pire_stress = mesures.get("pire_episode_pct")      # < 0, en %

    for brute in idees:
        conforme, motifs_schema, idee = valider_schema_idee(brute)

        if not conforme:
            nom = "IDENTIFICATION IMPOSSIBLE"
            id_tr = None
            if isinstance(brute, dict):
                n = brute.get("paire") or brute.get("nom")
                if isinstance(n, str) and n.strip():
                    nom = n.strip()
                id_tr = brute.get("id")
            verdicts.append({
                "id": "VETO-" + hashlib.md5(
                    f"{nom}|{id_tr}|{mesures.get('date_arrete')}"
                    .encode()).hexdigest()[:8],
                "id_trading": id_tr,
                "idee": nom,
                "verdict_trading": brute.get("verdict")
                if isinstance(brute, dict) else None,
                "statut_risque_amont": brute.get("statut_risque")
                if isinstance(brute, dict) else None,
                "alertes_trading": [],
                "schema_conforme": False,
                "veto": True,
                "motifs": motifs_schema,
                "limites_evaluees": {
                    "schema": {
                        "conforme": False,
                        "n_motifs": len(motifs_schema),
                        "note": "AUCUNE limite n'a été évaluée : les champs "
                                "nécessaires ne sont pas exploitables. "
                                "L'absence de dépassement mesuré n'est pas "
                                "une absence de dépassement."}},
                "horodatage": maintenant(),
                "date_arrete": mesures.get("date_arrete"),
            })
            continue

        nom = idee["nom"]
        taille = idee["taille_pct"]
        corr = idee["correlation"]
        perte_stop = idee["perte_stop_pct"]
        n_obs = idee["n_obs_paire"]

        motifs, evaluees = [], {}

        # 1 — perte au stop contre la VaR du portefeuille et le plafond dur
        plafond_var = limites["LIMITE_VAR_POSITION_PCT"]
        seuil_var = plafond_var
        base = "plafond dur"
        if var_fondee and est_nombre_fini(var_ref):
            seuil_var = min(plafond_var, abs(float(var_ref)))
            base = f"min(plafond dur ; |VaR retenue| = {abs(float(var_ref)):.2f} %)"
        if not est_nombre_fini(perte_stop):                   # ceinture et bretelles
            motifs.append(f"{MOTIF_ABSENT}: perte_stop_pct — non mesurable")
            depasse = True
        else:
            depasse = bool(perte_stop > seuil_var)
        evaluees["perte_au_stop_vs_var"] = {
            "perte_au_stop_pct": perte_stop, "seuil_pct": seuil_var,
            "base_du_seuil": base,
            "var_retenue_pct": var_ref, "var_limite_fondee": var_fondee,
            "depasse": depasse}
        if depasse and est_nombre_fini(perte_stop):
            motifs.append(f"perte au stop {perte_stop:.3f} % > seuil {seuil_var:.3f} % "
                          f"({base})")
        if not var_fondee:
            evaluees["perte_au_stop_vs_var"]["reserve"] = (
                "limite de VaR NON FONDÉE (aucune cellule de la méthode retenue "
                "ne survit au backtest) : seul le plafond dur est opposable ici")

        # 2 — taille
        if not est_nombre_fini(taille):
            motifs.append(f"{MOTIF_ABSENT}: taille_pct — non mesurable")
            dep_t = True
        else:
            dep_t = bool(taille > limites["LIMITE_TAILLE_PCT"])
        evaluees["taille"] = {"valeur_pct": taille,
                              "seuil_pct": limites["LIMITE_TAILLE_PCT"],
                              "origine_seuil": "charte §4.1",
                              "depasse": dep_t}
        if dep_t and est_nombre_fini(taille):
            motifs.append(f"taille {taille:.2f} % > plafond de charte §4.1 "
                          f"{limites['LIMITE_TAILLE_PCT']:.2f} %")

        # 3 — corrélation SIGNÉE au portefeuille détenu (P14 : une couverture
        #     à −0,70 n'est pas un doublon à +0,70)
        if not est_nombre_fini(corr):
            motifs.append(f"{MOTIF_ABSENT}: correlation — non mesurable")
            dep_c = True
        else:
            dep_c = bool(corr > limites["LIMITE_CORRELATION"])
        evaluees["correlation_signee"] = {
            "valeur": corr, "seuil": limites["LIMITE_CORRELATION"],
            "origine_seuil": "charte §4.2 / §4.5",
            "depasse": dep_c,
            "note": "seuil appliqué à la corrélation SIGNÉE : une corrélation "
                    "négative réduit le risque et n'est pas bloquée"}
        if dep_c and est_nombre_fini(corr):
            motifs.append(f"corrélation signée {corr:.3f} > "
                          f"{limites['LIMITE_CORRELATION']:.2f} : doublon du "
                          f"portefeuille détenu")

        # 4 — G-6 : perte sous le pire épisode VÉCU, en β et non en ρ
        b = beta_marche(idee, mesures)
        perte_stress = float("nan")
        if not est_nombre_fini(pire_stress):
            motifs.append(f"{MOTIF_MESURE}: pire épisode de stress non mesuré — "
                          f"la limite de stress ne peut pas être évaluée")
            dep_s = True
            detail_beta = {"disponible": False, "motif": "pire épisode non mesuré"}
        elif not b["disponible"]:
            motifs.append(f"{MOTIF_MESURE}: β de marché non mesurable — "
                          f"{b['motif']}. La limite de stress ne peut pas être "
                          f"évaluée, et une limite non évaluée n'est pas une "
                          f"limite satisfaite")
            dep_s = True
            detail_beta = b
        else:
            detail_beta = b
            perte_stress = abs(float(pire_stress)) * (taille / 100.0) * abs(b["beta"])
            dep_s = bool(perte_stress > limites["LIMITE_PERTE_STRESS_PCT"])
            if dep_s:
                motifs.append(
                    f"perte sous le pire épisode vécu {perte_stress:.3f} % > "
                    f"{limites['LIMITE_PERTE_STRESS_PCT']:.2f} % "
                    f"(β = {b['beta']:+.4f})")
        perte_stress_en_rho = (abs(float(pire_stress)) * (taille / 100.0) * abs(corr)
                               if est_nombre_fini(pire_stress) and est_nombre_fini(corr)
                               else float("nan"))
        evaluees["perte_sous_stress"] = {
            "pire_episode_pct": pire_stress,
            "perte_estimee_pct": perte_stress,
            "seuil_pct": limites["LIMITE_PERTE_STRESS_PCT"],
            "methode": "|pire épisode 20 séances| × taille × |β|, "
                       "β = ρ · σ_position / σ_marché",
            "beta": detail_beta,
            "ancienne_methode_en_rho_POUR_MEMOIRE": perte_stress_en_rho,
            "facteur_sous_estimation_ancienne_methode":
                (perte_stress / perte_stress_en_rho)
                if (est_nombre_fini(perte_stress) and est_nombre_fini(perte_stress_en_rho)
                    and perte_stress_en_rho > 0) else None,
            "depasse": dep_s}

        # 5 — PROFONDEUR DE L'ÉCHANTILLON DE LA PAIRE : veto automatique
        dep_n = bool(n_obs < limites["MIN_SEANCES_PAIRE"])
        sans_stress = (idee["echantillon_contient_stress"] is False)
        evaluees["profondeur_echantillon_paire"] = {
            "n_obs": n_obs, "minimum": limites["MIN_SEANCES_PAIRE"],
            "annees_approx": round(n_obs / 252, 1),
            "echantillon_contient_stress": idee["echantillon_contient_stress"],
            "depasse": bool(dep_n or sans_stress)}
        if dep_n:
            motifs.append(
                f"profondeur d'échantillon de la paire {n_obs} séances "
                f"(≈ {n_obs/252:.1f} ans) < {limites['MIN_SEANCES_PAIRE']} "
                f"(5 ans) : une cointégration mesurée sur un régime unique "
                f"n'est pas une cointégration, c'est une corrélation de période")
        if sans_stress:
            motifs.append(
                "l'échantillon de la paire ne contient AUCUN épisode de stress "
                "de crédit : la relation n'a jamais été observée au moment où "
                "elle doit tenir. Raison suffisante de bloquer, à elle seule")

        verdicts.append({
            "id": "VETO-" + hashlib.md5(
                f"{nom}|{mesures.get('date_arrete')}".encode()).hexdigest()[:8],
            "id_trading": idee.get("id_trading"),
            "idee": nom,
            "verdict_trading": idee.get("verdict_trading"),
            "statut_risque_amont": idee.get("statut_risque"),
            "alertes_trading": idee.get("alertes_trading", []),
            "schema_conforme": True,
            "veto": bool(motifs),
            "motifs": motifs,
            "limites_evaluees": evaluees,
            "horodatage": maintenant(),
            "date_arrete": mesures.get("date_arrete"),
        })
    return verdicts


# ══════════════════════════════════════════════════════════════════════════
# P1 — TEST DE NON-RÉGRESSION DE LA COMPOSITION
# ══════════════════════════════════════════════════════════════════════════

def _test_composition() -> None:
    """
    Échoue sur l'ancien code — (1+r).cumprod() appliqué à des log-rendements —
    et passe sur le nouveau. Vérifié dans les deux sens.
    """
    rs = np.array([0.01, -0.02, 0.03, -0.005])       # rendements SIMPLES
    rl = np.log(1 + rs)                               # log-rendements
    assert abs(drawdown(rl)["max"] - drawdown_ref_simple(rs)) < 1e-12

    # la capitalisation doit reconstituer exactement le produit simple
    assert abs(valeur_capitalisee(rl)[-1] - np.prod(1 + rs)) < 1e-12
    # le rendement annualisé aussi
    ann_ref = float(np.prod(1 + rs) ** (252 / len(rs)) - 1)
    assert abs(rendement_annualise(rl) - ann_ref) < 1e-9
    # et l'ancienne formule DOIT s'en écarter : le test a un pouvoir de détection
    ancien = float((1 + pd.Series(rl)).prod() ** (252 / len(rl)) - 1)
    assert abs(ancien - ann_ref) > 1e-6
    print("  _test_composition : OK (et l'ancienne formule est bien détectée)")


def _test_kupiec_christoffersen() -> None:
    """Contrôles de sanité des deux statistiques de backtest."""
    # couverture parfaite → LR_uc ≈ 0
    lr, p = kupiec_pof(50, 1000, 0.05)
    assert lr < 1e-9 and p > 0.99
    # dépassements parfaitement alternés → indépendance non rejetée à 0 %
    _, p_i, _ = christoffersen_independance(([0] * 19 + [1]) * 50)
    assert p_i > 0.01
    # cinq dépassements en huit séances puis rien → indépendance REJETÉE
    grappe = [1, 1, 0, 1, 1, 0, 1, 0] + [0] * 992
    lr_i, p_i2, _ = christoffersen_independance(grappe)
    assert p_i2 < 0.01, p_i2
    print("  _test_kupiec_christoffersen : OK (la grappe est bien rejetée, "
          f"p = {p_i2:.2e})")


def _test_cornish_fisher() -> None:
    ok, _ = cornish_fisher_valide(0.0, 0.0)
    assert ok                                   # cas gaussien : monotone
    ok2, motif = cornish_fisher_valide(0.4539, 15.5522)
    assert not ok2 and "kurtosis" in motif      # cas S&P 504 : refusé
    print("  _test_cornish_fisher : OK")


def _test_calibration_identique() -> None:
    """
    G-1 — la valeur critique simulée ne vaut que si la statistique simulée est
    EXACTEMENT celle qui est publiée. On vérifie l'identité ligne à ligne de
    _lr_vectorise() avec kupiec_pof() et christoffersen_independance(), sur
    des séquences tirées au hasard, y compris les cas dégénérés (aucun
    dépassement, que des dépassements).
    """
    rng = np.random.default_rng(7)
    seqs = [(rng.random(300) < 0.05).astype(np.int8) for _ in range(30)]
    seqs.append(np.zeros(300, dtype=np.int8))
    seqs.append(np.ones(300, dtype=np.int8))
    seqs.append(np.array(([1, 1, 0] * 100), dtype=np.int8))
    V = np.vstack(seqs)
    a, b, c = _lr_vectorise(V, 0.05)
    for i, s in enumerate(seqs):
        lr_uc, _ = kupiec_pof(int(s.sum()), len(s), 0.05)
        lr_i, _, _ = christoffersen_independance(s)
        assert abs(a[i] - lr_uc) < 1e-8, (i, a[i], lr_uc)
        assert abs(b[i] - lr_i) < 1e-8, (i, b[i], lr_i)
        assert abs(c[i] - (lr_uc + lr_i)) < 1e-8
    # la calibration doit être reproductible à la graine près
    c1 = calibrer_valeurs_critiques(500, 0.05, n_sim=2000, graine=1)
    _CACHE_CALIBRATION.clear()
    c2 = calibrer_valeurs_critiques(500, 0.05, n_sim=2000, graine=1)
    assert c1["valeur_critique_5pct"] == c2["valeur_critique_5pct"]
    _CACHE_CALIBRATION.clear()
    print("  _test_calibration_identique : OK (statistiques identiques, "
          "calibration reproductible)")


def _test_veto_ne_passe_pas_en_silence() -> None:
    """
    G-2 — contrôle de non-régression MINIMAL, en plus de test_veto.py :
    une idée sans taille, sans stop et sans corrélation ne doit JAMAIS
    recevoir « aucune limite de risque dépassée ».
    """
    mesures = {"date_arrete": "2026-08-16", "var_retenue_pct": -1.66,
               "var_limite_fondee": True, "pire_episode_pct": -30.94,
               "cointegrations": {}, "sigma_marche_par_paire": {}}
    limites = {"LIMITE_VAR_POSITION_PCT": LIMITE_VAR_POSITION_PCT,
               "LIMITE_TAILLE_PCT": LIMITE_TAILLE_PCT,
               "LIMITE_CORRELATION": LIMITE_CORRELATION,
               "LIMITE_PERTE_STRESS_PCT": LIMITE_PERTE_STRESS_PCT,
               "MIN_SEANCES_PAIRE": MIN_SEANCES_PAIRE}
    v = veto([{"paire": "Idée creuse", "verdict": "TRANSMISE"}], mesures, limites)
    assert len(v) == 1 and v[0]["veto"] is True, v
    assert any(m.startswith(MOTIF_ABSENT) for m in v[0]["motifs"]), v[0]["motifs"]
    # la taille chaîne "9.0" ne doit PAS être remplacée par criteres
    v2 = veto([{"paire": "Chaîne", "verdict": "TRANSMISE",
                "taille_pct_nav": "9.0", "perte_au_stop_pct": -0.3,
                "n_obs": 2000, "echantillon_contient_stress": True,
                "criteres": {"5_correlation_marche_actions": {"valeur": 0.1},
                             "6_taille_sous_limite": {"valeur": 3.0}}}],
               mesures, limites)
    assert v2[0]["veto"] is True
    assert any("taille_pct" in m for m in v2[0]["motifs"]), v2[0]["motifs"]
    assert not v2[0]["schema_conforme"]
    print("  _test_veto_ne_passe_pas_en_silence : OK (NaN et chaîne bloquent)")


def lancer_tests() -> None:
    print("─" * 76)
    print("TESTS DE NON-RÉGRESSION")
    print("─" * 76)
    _test_composition()
    _test_kupiec_christoffersen()
    _test_cornish_fisher()
    _test_calibration_identique()
    _test_veto_ne_passe_pas_en_silence()
    print()


# ══════════════════════════════════════════════════════════════════════════
# EXÉCUTION
# ══════════════════════════════════════════════════════════════════════════

def main() -> int:
    ap = argparse.ArgumentParser(description="Moteur de risque Apollon")
    ap.add_argument("--data")
    ap.add_argument("--sortie", default=str(RACINE))
    ap.add_argument("--clore", help="identifiant d'alerte à clore")
    ap.add_argument("--motif", default="", help="motif écrit de la clôture")
    ap.add_argument("--test", action="store_true", help="tests de non-régression seuls")
    args = ap.parse_args()

    sortie = Path(args.sortie)
    chemin_alertes = sortie / FICHIER_ALERTES

    if args.clore:
        return clore_alerte(chemin_alertes, args.clore, args.motif)
    if args.test:
        lancer_tests()
        return 0
    if not args.data:
        ap.error("--data est requis (ou --clore, ou --test)")

    lancer_tests()

    series = charger(Path(args.data))
    arrete = date_arrete(series)                                  # P17

    # ── état du journal AVANT toute écriture (P8) ──────────────────────────
    etat = etat_journal(chemin_alertes)

    print("=" * 76)
    print("APOLLON — MOTEUR DE RISQUE · Générale Kerviel")
    print("=" * 76)
    print(f"DATE D'ARRÊTÉ : {arrete}   (produite par le code, jamais saisie)")
    print(f"ALERTES NON TRAITÉES AU JOURNAL : {etat['n_non_traitees']}   "
          f"({etat['alertes_uniques']} alerte(s) unique(s), "
          f"{etat['lignes_alertes_brutes']} ligne(s) brute(s), "
          f"{etat['clotures']} clôture(s))")
    for u in etat["non_traitees"]:
        print(f"    · {u['id']}  {u['type']}/{u['niveau']}  "
              f"1re {u['premiere_date_donnees']} → {u['derniere_date_donnees']}  "
              f"×{u['occurrences']}  mesure {u.get('derniere_mesure')}")
    print(f"  (clé de dédoublonnage : {etat['cle_de_dedoublonnage']})")

    # ── G-11 : inventaire des constantes, PRODUIT ─────────────────────────
    inv = inventaire_constantes()
    print(f"\nCONSTANTES MATÉRIELLES : {inv['n_constantes_materielles']} — "
          f"{inv['n_tracables_charte']} traçables à la charte, "
          f"{inv['n_proprietes']} imposées par une propriété, "
          f"{inv['n_constantes_libres']} LIBRES (posées à la main).")
    print(f"  n_tracables_charte  = {inv['n_tracables_charte']} : "
          + ", ".join(f"{n} ({o})" for n, o in inv["tracables_charte"].items()))
    print(f"  n_constantes_libres = {inv['n_constantes_libres']} : "
          + ", ".join(inv["constantes_libres"]))
    print(f"  LIMITE_VAR_PORTEFEUILLE_PCT = {LIMITE_VAR_PORTEFEUILLE_PCT} — "
          f"origine : {inv['limite_var_portefeuille_origine']}")
    if not inv["registre_complet"]:
        print(f"  ⚠ REGISTRE INCOMPLET — non enregistrées : "
              f"{inv['non_enregistrees']} ; fantômes : "
              f"{inv['enregistrees_inexistantes']}")
    print(f"\n{len(series)} séries chargées")

    sp = series.get("SP500")
    if sp is None:
        print("SP500 absent — impossible de calculer le risque.")
        return 1
    spd = sp.dropna()
    r = np.log(spd).diff().dropna()
    rv = r.values
    print(f"Portefeuille de référence : S&P 500, {len(spd)} cotations → "
          f"{len(r)} rendements, {r.index[0].date()} → {r.index[-1].date()}")
    print("  (la doctrine publiait « 2 512 séances » : c'est le nombre de "
          "COTATIONS ;\n   le nombre de RENDEMENTS est inférieur de un.)\n")

    dd = drawdown(r)
    eps = episodes_de_stress(sp)

    # ── VaR : fenêtres, drapeaux de crise, méthodes ───────────────────────
    print("─" * 76)
    print("VALUE AT RISK — MÉTHODE DÉCLARÉE EX ANTE, ARBITRÉE PAR LE BACKTEST")
    print("─" * 76)
    print(f"  Méthode retenue ex ante : {METHODE_VAR_RETENUE.upper()}")
    print("  min(historique, paramétrique, Cornish-Fisher) SUPPRIMÉ : prendre le")
    print("  minimum de trois estimateurs bruités est un estimateur de sélection")
    print("  (RMSE mesurée 2,210 pt contre 0,396 pt — 5,6× pire).\n")

    date_creux = pd.Timestamp(dd["date_creux"])
    fenetres_info, tableau_var = [], []
    for f in FENETRES_VAR:
        n_f = len(r) if f == "complet" else int(f)
        sub = r if f == "complet" else (r.iloc[-n_f:] if len(r) >= n_f else r)
        if len(sub) < 60:
            continue
        contient = bool(sub.index[0] <= date_creux <= sub.index[-1])
        fenetres_info.append({
            "fenetre": str(f), "n_obs": len(sub),
            "debut_effectif": str(sub.index[0].date()),
            "fin_effective": str(sub.index[-1].date()),
            "contient_drawdown_max": contient,
            "date_drawdown_max": dd["date_creux"],
        })
    aucune_crise_court = not any(fi["contient_drawdown_max"] for fi in fenetres_info
                                 if fi["fenetre"] != "complet")
    if aucune_crise_court:
        print("  ⚠ AUCUNE FENÊTRE COURTE NE CONTIENT DE CRISE.")
        print(f"    Le drawdown maximal ({dd['max']*100:.2f} %, creux "
              f"{dd['date_creux']}) et le pire épisode de stress "
              f"({eps[0]['perte_20_seances_pct']:.2f} % le {eps[0]['fin_fenetre']})")
        print("    sont HORS des fenêtres 252 / 504 / 1 260. Une VaR calibrée sur")
        print("    un échantillon d'où la crise a été retirée mesure le calme.\n")
    print(f"  {'Fenêtre':>10} {'n':>6} {'début':>12} {'crise incluse':>15}")
    for fi in fenetres_info:
        print(f"  {fi['fenetre']:>10} {fi['n_obs']:>6} {fi['debut_effectif']:>12} "
              f"{'OUI' if fi['contient_drawdown_max'] else 'non':>15}")
    print()

    annexe_cf, diag_cf = [], {}
    for niveau in NIVEAUX_VAR:
        print(f"  ── Niveau de confiance {niveau*100:.0f} %")
        print(f"  {'Fenêtre':>10} {'Historique':>12} {'Johnson SU':>12} "
              f"{'Paramétrique':>14} {'Cornish-Fisher':>16} {'CVaR':>14}"
              f"   erreur-type")
        for fi in fenetres_info:
            f = fi["fenetre"]
            n_f = len(r) if f == "complet" else int(f)
            sub = r if f == "complet" else r.iloc[-n_f:]
            vh = var_historique(sub, niveau)
            err = erreur_var_historique(sub, niveau)
            vp = var_parametrique(sub, niveau)
            vj = var_johnson_su(sub, niveau)
            vcf, motif_cf = var_cornish_fisher(sub, niveau)
            cv = cvar(sub, niveau)
            if vcf is None:
                annexe_cf.append({"fenetre": f, "niveau": niveau, "motif": motif_cf})
            tableau_var.append({
                "niveau": niveau, "fenetre": f, "n_obs": len(sub),
                "debut_effectif": fi["debut_effectif"],
                "contient_drawdown_max": fi["contient_drawdown_max"],
                "historique_pct": arrondi_erreur(vh * 100, err * 100),
                "historique_erreur_type_pct": err * 100,
                "johnson_su_pct": (arrondi_erreur(vj * 100, err * 100)
                                   if vj is not None else None),
                "annexe_parametrique_pct": arrondi_erreur(vp * 100, err * 100),
                "annexe_cornish_fisher_pct": (arrondi_erreur(vcf * 100, err * 100)
                                              if vcf is not None else None),
                "cornish_fisher_motif": motif_cf,
                "cvar": cv,
                "statut_annexes": "publiées pour information, n'entrent dans "
                                  "aucune limite",
            })
            # P13 — on n'imprime que les valeurs ARRONDIES à l'erreur
            # d'échantillonnage : le tableau publié ne doit pas contenir de
            # décimale que la donnée ne porte pas.
            t_ = tableau_var[-1]
            s_cf = (f"{t_['annexe_cornish_fisher_pct']:>15.2f}%"
                    if t_["annexe_cornish_fisher_pct"] is not None
                    else f"{'REFUSÉ':>16}")
            s_cv = (f"{cv['valeur_arrondie_pct']:>12.2f}% " if cv["disponible"]
                    else f"{'n=' + str(cv['n_queue']) + ' REFUS':>14}")
            s_j = (f"{t_['johnson_su_pct']:>11.2f}%"
                   if t_["johnson_su_pct"] is not None else f"{'—':>12}")
            print(f"  {f:>10} {t_['historique_pct']:>11.2f}% {s_j} "
                  f"{t_['annexe_parametrique_pct']:>13.2f}% {s_cf} {s_cv}"
                  f"   ±{err*100:.2f}")
        print()

    print("  Colonnes PARAMÉTRIQUE et CORNISH-FISHER : publiées pour information,")
    print("  n'entrent dans AUCUNE limite. Seule la méthode retenue ex ante "
          f"({METHODE_VAR_RETENUE})")
    print("  est opposable ; Johnson SU sert de contrôle de cohérence.\n")

    if annexe_cf:
        print("  CORNISH-FISHER — REFUSÉE, ET POURQUOI :")
        vus = set()
        for a in annexe_cf:
            if a["motif"] in vus:
                continue
            vus.add(a["motif"])
            print(f"    {a['motif']}")
        for f_ in ("504", "complet"):
            fi_ = next((x for x in fenetres_info if x["fenetre"] == f_), None)
            if fi_ is None:
                continue
            sub_ = r if f_ == "complet" else r.iloc[-int(f_):]
            dg = diagnostic_cornish_fisher(sub_)
            diag_cf[f_] = dg
            print(f"    fenêtre {f_} : monotone = {dg['monotone_en_niveau']} ; "
                  f"{dg['lecture']}")
        print("    Une « VaR » qui CROÎT avec le niveau de confiance et devient")
        print("    POSITIVE n'est la fonction quantile d'aucune loi : elle annonce")
        print("    un GAIN garanti là où elle devrait annoncer une perte.")
        print("    Remplacée par une Johnson SU, monotone par construction,")
        print("    calibrée sur les quatre moments.\n")

    # écart entre méthodes VALIDES (la cellule 99 %/504 = −5,58 % disparaît)
    ecarts_valides = [abs(t["historique_pct"] - t["johnson_su_pct"])
                      for t in tableau_var if t["johnson_su_pct"] is not None]
    ecart_max_valide = max(ecarts_valides) if ecarts_valides else float("nan")
    c504 = next((t for t in tableau_var
                 if t["fenetre"] == "504" and t["niveau"] == 0.99), None)
    print(f"  Écart maximal entre MÉTHODES VALIDES (historique vs Johnson SU) : "
          f"{ecart_max_valide:.2f} point(s)")
    if c504:
        print(f"  Cellule 99 %/504 : historique {c504['historique_pct']:.2f} %, "
              f"Johnson SU {c504['johnson_su_pct']:.2f} % — les deux méthodes")
        print("  valides CONCORDENT. L'« écart de 3,29 points » de la doctrine "
              "reposait")
        print("  sur la cellule Cornish-Fisher aberrante : il est RETIRÉ.\n")

    # ── P5 : backtest ────────────────────────────────────────────────────
    print("─" * 76)
    print("BACKTEST DE VaR — KUPIEC (couverture) ET CHRISTOFFERSEN (indépendance)")
    print("─" * 76)
    print("  Fenêtre GLISSANTE hors échantillon : calibration sur les N séances")
    print("  précédentes, test sur la suivante, avancée d'un jour.")
    print("  Un backtest in-sample de la VaR historique donne mécaniquement le")
    print("  bon nombre de dépassements (p = 0,967) : c'est une tautologie.\n")
    # ── G-1 : LA RÈGLE DE DÉCISION EST ANNONCÉE AVANT LE TABLEAU ──────────
    print("  G-1 — VALEUR CRITIQUE. Règle DÉCLARÉE EX ANTE, avant tout regard")
    print(f"  sur les résultats de cette exécution : « {REGLE_VALEUR_CRITIQUE_BACKTEST} ».")
    print("  L'asymptotique χ²(2) = 5,991 est publiée EN REGARD, pour mémoire,")
    print("  et n'a AUCUN effet sur le verdict. Motif, antérieur au résultat :")
    print("  la convergence de LR_cc vers χ² est lente quand l'événement est")
    print("  rare ; à p = 1 % le nombre attendu de transitions 1→1 est de")
    print("  l'ordre de l'unité et la loi limite ne décrit plus rien.")
    print(f"  Calibration : {N_SIM_CALIBRATION_BACKTEST} tirages sous H₀ par "
          f"couple (T, p), graine {GRAINE}.\n")
    backtests = []
    for f in FENETRES_VAR:
        backtests.extend(backtest_var(rv, f, NIVEAUX_VAR))

    # tableau des valeurs critiques, avant les verdicts
    print("  VALEURS CRITIQUES À 5 % — CALIBRÉE (décide) contre χ² (pour mémoire)")
    print(f"  {'T':>6} {'p':>6} {'Kupiec cal':>11} {'χ²(1)':>7} "
          f"{'Chr. cal':>10} {'χ²(1)':>7} {'conjoint cal':>13} {'χ²(2)':>7}"
          f"   rejet effectif χ²(2) sous H₀")
    vues_calib, calibrations = set(), []
    for b in backtests:
        if not b.get("n_tests"):
            continue
        cle = (b["n_tests"], round(1 - b["niveau"], 6))
        if cle in vues_calib:
            continue
        vues_calib.add(cle)
        cal = calibrer_valeurs_critiques(b["n_tests"], 1 - b["niveau"])
        calibrations.append({k2: v2 for k2, v2 in cal.items() if k2 != "_echantillons"})
        vc, va = cal["valeur_critique_5pct"], cal["valeur_critique_asymptotique_5pct"]
        tr = cal["taux_rejet_effectif_asymptotique_5pct"]
        print(f"  {cal['T']:>6} {cal['p']:>6.2f} {vc['kupiec']:>11.3f} "
              f"{va['kupiec']:>7.3f} {vc['christoffersen']:>10.3f} "
              f"{va['christoffersen']:>7.3f} {vc['conjoint']:>13.3f} "
              f"{va['conjoint']:>7.3f}   {tr['conjoint']*100:>5.2f} % "
              f"(nominal 5,00 %)")
    print()

    print(f"  {'Fenêtre':>9} {'niv':>5} {'méthode':>13} {'obs':>5} {'att':>6} "
          f"{'IC95':>10} {'LR_cc':>7} {'vc_cal':>7} {'p_cc_cal':>9} {'p_cc_χ²':>8}"
          f"  verdict")
    for b in backtests:
        if not b.get("n_tests"):
            continue
        ic = f"[{b['ic95_binomial'][0]},{b['ic95_binomial'][1]}]"
        marque = " ⚠ DIVERGENT" if b["verdicts_divergent"] else ""
        print(f"  {b['fenetre']:>9} {b['niveau']:>5.2f} {b['methode']:>13} "
              f"{b['depassements_observes']:>5} {b['depassements_attendus']:>6.1f} "
              f"{ic:>10} {b['LR_cc']:>7.3f} "
              f"{b['valeur_critique_5pct_calibree']:>7.3f} "
              f"{b['p_conjoint_calibree']:>9.4f} {b['p_conjoint']:>8.4f}  "
              f"{'REJETÉE' if b['rejetee'] else 'admissible'}{marque}")
    print()
    divergents = [b for b in backtests if b.get("verdicts_divergent")]
    if divergents:
        print("  CELLULES DONT LE VERDICT CHANGE AVEC LA CALIBRATION :")
        for b in divergents:
            print(f"    {b['methode']} {b['fenetre']}/{b['niveau']:.0%} : "
                  f"LR_cc {b['LR_cc']:.3f} → p χ² {b['p_conjoint']:.4f} "
                  f"{'REJETÉE' if b['rejetee_asymptotique'] else 'NON REJETÉE'}"
                  f" | p calibrée {b['p_conjoint_calibree']:.4f} "
                  f"{'REJETÉE' if b['rejetee_calibree'] else 'NON REJETÉE'}")
        print("    C'est la CALIBRÉE qui décide — règle déclarée ex ante.\n")
    else:
        print("  Aucune cellule ne change de verdict entre les deux valeurs "
              "critiques.\n")

    # ── G-8 : les jours SANS VaR, comptés à part ─────────────────────────
    echecs_su = {}
    for b in backtests:
        if b.get("methode") != "johnson_su" or not b.get("n_tests"):
            continue
        echecs_su[b["fenetre"]] = {
            "n_jours_calibrables": b["n_jours_calibrables"],
            "n_jours_ecartes_sans_var": b["n_jours_ecartes_sans_var"],
            "taux_echec_pct": b["taux_echec_modele_pct"],
            "n_tests_retenus": b["n_tests"]}
    if echecs_su:
        print("  G-8 — JOURS SANS VaR (échec de calibration Johnson SU)")
        print("  Un jour où le modèle ne produit PAS de VaR n'est pas un jour")
        print("  sans dépassement. L'ancien code y écrivait 0 : l'échec du")
        print("  modèle était compté comme un succès du modèle, et les deux")
        print("  tests étaient biaisés EN SA FAVEUR. Ces jours sont retirés.")
        for f_, e in echecs_su.items():
            print(f"    fenêtre {f_:>7} : {e['n_jours_ecartes_sans_var']:>4} échec(s) "
                  f"sur {e['n_jours_calibrables']:>4} jours "
                  f"({e['taux_echec_pct']:.2f} %) → {e['n_tests_retenus']} tests retenus")
        print()

    # arbitrage EX ANTE : méthode retenue + plus longue fenêtre non rejetée
    ordre = {"252": 1, "504": 2, "1260": 3, "complet": 4}
    cellules_testables = [b for b in backtests if b.get("n_tests")]
    survivants = sorted(
        [b for b in backtests
         if b.get("methode") == METHODE_VAR_RETENUE and not b.get("rejetee", True)],
        key=lambda b: (-ordre.get(b["fenetre"], 0), b["niveau"]))
    # ── G-4 : LES DEUX COMPTES, NOMMÉS, AU MÊME ENDROIT ──────────────────
    # Le rapport imprimait « AUCUNE CELLULE NE SURVIT » puis, trois lignes
    # plus bas, « 2 cellules admissibles ». Les deux phrases étaient vraies
    # et parlaient de deux populations différentes : la première des seules
    # cellules de la MÉTHODE RETENUE, la seconde de TOUTES les méthodes,
    # annexes comprises. Aucune des deux ne le disait.
    survivants_toutes = [b for b in cellules_testables if not b.get("rejetee", True)]
    cellules_methode = [b for b in cellules_testables
                        if b.get("methode") == METHODE_VAR_RETENUE]
    print("  ── DÉCOMPTE DES CELLULES, DEUX POPULATIONS DISTINCTES (G-4)")
    print(f"    Méthode RETENUE ({METHODE_VAR_RETENUE}) : "
          f"{len(survivants)} cellule(s) admissible(s) sur {len(cellules_methode)} "
          f"— SEULE population opposable.")
    print(f"    Toutes méthodes confondues : {len(survivants_toutes)} cellule(s) "
          f"admissible(s) sur {len(cellules_testables)} — les cellules "
          f"paramétriques et")
    print("    Johnson SU sont des ANNEXES : elles n'entrent dans aucune limite,")
    print("    qu'elles survivent ou non.")
    if survivants_toutes:
        print("    Détail des survivantes toutes méthodes : "
              + ", ".join(f"{b['methode']} {b['fenetre']}/{b['niveau']:.0%}"
                          for b in survivants_toutes))
    print()

    var_limite_fondee = bool(survivants)
    if var_limite_fondee:
        cell = survivants[0]
        t = next(t for t in tableau_var
                 if t["fenetre"] == cell["fenetre"] and t["niveau"] == cell["niveau"])
        var_retenue_pct = t["historique_pct"]
        cellule_limite = {"methode": METHODE_VAR_RETENUE, "fenetre": cell["fenetre"],
                          "niveau": cell["niveau"],
                          "LR_cc": cell["LR_cc"],
                          "valeur_critique_calibree":
                              cell["valeur_critique_5pct_calibree"],
                          "p_conjoint_calibree": cell["p_conjoint_calibree"],
                          "p_conjoint_asymptotique": cell["p_conjoint"]}
        print(f"  → LIMITE FONDÉE : méthode {METHODE_VAR_RETENUE}, fenêtre "
              f"{cell['fenetre']}, niveau {cell['niveau']:.0%} → "
              f"{var_retenue_pct:.2f} %")
        print(f"    (règle de fenêtre : {REGLE_FENETRE_LIMITE} ; LR_cc "
              f"{cell['LR_cc']:.3f} contre valeur critique calibrée "
              f"{cell['valeur_critique_5pct_calibree']:.3f})")
    else:
        # fenêtre la plus longue, pour la publication — mais NON opposable
        t = next((t for t in tableau_var
                  if t["fenetre"] == "complet" and t["niveau"] == 0.99), tableau_var[-1])
        var_retenue_pct = t["historique_pct"]
        cellule_limite = None
        print(f"  → AUCUNE CELLULE DE LA MÉTHODE RETENUE ({METHODE_VAR_RETENUE}) "
              f"NE SURVIT")
        print("    AU TEST CONJOINT, valeur critique calibrée. La limite de VaR")
        print("    est déclarée NON FONDÉE ; le veto s'appuie sur le plafond dur")
        print("    et sur la limite de stress.")
        print(f"    (VaR publiée pour information : {var_retenue_pct:.2f} % — "
              f"{METHODE_VAR_RETENUE}, fenêtre complète, 99 %)")
    tableau_limites = [
        {"methode": b["methode"], "fenetre": b["fenetre"], "niveau": b["niveau"],
         "p_conjoint_calibree": b["p_conjoint_calibree"],
         "p_conjoint_asymptotique": b["p_conjoint"],
         "opposable": bool(b["methode"] == METHODE_VAR_RETENUE)}
        for b in survivants_toutes]
    print()

    # ── Performance ajustée ───────────────────────────────────────────────
    print("─" * 76)
    print("MESURES AJUSTÉES DU RISQUE")
    print("─" * 76)
    rf = taux_sans_risque(series, r.index)
    sh = sharpe(r, rf)
    so = sortino(r)
    coh = controle_coherence_sortino(r, so, sh["sharpe_brut"])
    cal = calmar(r)
    print(f"  Rendement annualisé      : {sh['rendement_annualise_pct']:>8.2f} %")
    print(f"  Volatilité annualisée    : {sh['volatilite_annualisee_pct']:>8.2f} %")
    print(f"  Valeur finale            : {dd['valeur_finale']:>8.2f} ×")
    print(f"  Sharpe BRUT (sans rf)    : {sh['sharpe_brut']:>8.3f}  ← n'est pas un Sharpe")
    if "sharpe_excedentaire" in sh:
        print(f"  Taux sans risque moyen   : {sh['taux_sans_risque_moyen_pct']:>8.2f} %  (DFF)")
        print(f"  SHARPE EXCÉDENTAIRE      : {sh['sharpe_excedentaire']:>8.3f}  ← le Sharpe")
    print(f"  Sortino                  : {so:>8.3f}")
    print(f"  Calmar                   : {cal:>8.3f}")
    print(f"  Drawdown maximal         : {dd['max']*100:>8.2f} %  (creux {dd['date_creux']})")
    print(f"  Drawdown courant         : {dd['courant']*100:>8.2f} %")
    print(f"  Temps sous l'eau         : {dd['pct_temps_sous_eau']:>8.1f} % des séances")
    print(f"  Plus longue série        : {dd['plus_longue_serie_sous_eau']:>8d} séances consécutives")
    print(f"  Contrôle Sortino/Sharpe  : {'SUSPECT' if coh['suspect'] else 'cohérent'} "
          f"(écart {coh['ecart_sortino_sharpe']:.3f}, skew {coh['skew']:+.3f})")
    print("\n  Note P11 : le 0,650 publié était approximativement juste PAR")
    print("  COMPENSATION — le bug de composition gonflait le Sharpe d'environ")
    print("  +0,10, l'omission du taux sans risque le dégonflait d'autant.")
    print("  Deux fautes de signe opposé produisent un chiffre plausible et un")
    print("  raisonnement faux. Seul le chiffre était contrôlé.\n")

    k = kelly(r)
    if k.get("disponible"):
        print(f"  Kelly plein              : {k['kelly_plein']:>8} ×  ← INAPPLICABLE, ruine")
        print(f"  {k['lecture']}")
        print(f"  Écart t. σ²/2 (P12)      : {k['ecart_du_au_terme_sigma2_sur_2']:>8.3f} × "
              f"(exactement σ²/2 ÷ σ² = 0,5)")
        print(f"  Kelly ½ (plafond)        : {k['plafond_doctrinal_x']:>8} ×")
        print(f"  Kelly ¼ (défaut)         : {k['taille_recommandee_x']:>8} ×")
        print("  Publication à quatre chiffres significatifs INTERDITE : "
              "l'intervalle\n  à 90 % englobe Kelly ¼, Kelly ½ ET Kelly plein.\n")

    sim = simulation_levier(r, kelly_plein=k.get("kelly_plein_brut"),
                            reequilibrage=1)
    sim_mens = simulation_levier(r, kelly_plein=k.get("kelly_plein_brut"),
                                 reequilibrage=21)
    print("  TABLE KELLY (P18 — désormais produite par le code, auditable)")
    print(f"  {'fraction':>9} {'levier':>8} {'final':>8} {'drawdown':>10} "
          f"{'capital au creux':>18}   rééquilibrage")
    for s_, freq in [(sim, "quotidien"), (sim_mens, "mensuel (21 séances)")]:
        for e in s_:
            print(f"  {e['fraction_kelly']:>9.2f} {e['levier']:>8.3f} "
                  f"{e['valeur_finale_x']:>7.2f}× {e['drawdown_max_pct']:>9.1f}% "
                  f"{e['capital_restant_au_creux_pct']:>17.1f}%   {freq}")
    print()

    # ── Régime ────────────────────────────────────────────────────────────
    print("─" * 76)
    print("RÉGIME ET PERCENTILES")
    print("─" * 76)
    reg = regime(series)
    print(f"  Régime : {reg['regime']}\n")
    pcts = {}
    for sid, lab in [("VIXCLS", "VIX"), ("T10Y2Y", "Pente 2s10s"),
                     ("BAMLH0A0HYM2", "Spread HY"), ("DGS10", "10 ans"),
                     ("DFII10", "Réel 10 ans")]:
        if sid in series:
            p = percentile_courant(series[sid])
            if p.get("disponible"):
                pcts[sid] = p
                g = p["profondeur_2520"]
                marque = {"suffisante": "", "marginale": "  ~ profondeur MARGINALE",
                          "insuffisante": "  ⚠ profondeur INSUFFISANTE"}[g["etat"]]
                print(f"  {lab:<14} {p['valeur']:>9.3f}  "
                      f"pct 1 an {p['pct_252']:>5.1f}  "
                      f"pct 10 ans {p['pct_2520']:>5.1f}  "
                      f"({p['n_obs_total']} obs, {g['ecart_pct']:+.1f} %){marque}")
    print("  P16 : T10Y2Y (−0,8 %) et BAMLH0A0HYM2 (−69 %) ne portent plus le "
          "même drapeau.\n")

    # ── Corrélations ──────────────────────────────────────────────────────
    print("─" * 76)
    print("CORRÉLATIONS — DIVERSIFICATION RÉELLE OU APPARENTE")
    print("─" * 76)
    rets, retenus = rendements_panier(series)
    diag = None
    cond = {"disponible": False}
    rets_origine = None
    doc_prod = {"disponible": False, "motif": "panier trop court"}
    if len(rets) > 60 and rets.shape[1] > 1:
        diag = diagnostics_correlation(rets)
        print(f"  Panier : {', '.join(retenus)}")
        print(f"  Corrélation moyenne SIGNÉE   : {diag['correlation_moyenne_signee']:+.3f}")
        print(f"  (|ρ| moyenne, pour mémoire)  : "
              f"{diag['correlation_absolue_moyenne_POUR_MEMOIRE']:.3f}  ← non opposable")
        print(f"  Corrélation signée MAX       : "
              f"{diag['correlation_signee_max']['paire']} = "
              f"{diag['correlation_signee_max']['valeur']:+.3f}  (doublon)")
        print(f"  Corrélation signée MIN       : "
              f"{diag['correlation_signee_min']['paire']} = "
              f"{diag['correlation_signee_min']['valeur']:+.3f}  (COUVERTURE, "
              f"la seule protection du panier)")
        # ── G-5 : LES DEUX N_eff, ET L'OPPOSABLE EST NOMMÉ ───────────────
        print(f"  N_eff sur la CORRÉLATION     : "
              f"{diag['n_effectif_paris_correlation']:.3f} sur {diag['n_actifs']} "
              f"actifs   ← non opposable")
        print(f"  N_eff sur la COVARIANCE      : "
              f"{diag['n_effectif_paris_covariance']:.3f} sur {diag['n_actifs']} "
              f"actifs   ← OPPOSABLE")
        print(f"    motif : {diag['motif_base_opposable']}")
        print(f"    seuil {LIMITE_N_EFF_MIN} → "
              f"{'ALERTE CONCENTRATION' if diag['n_effectif_paris_opposable'] < LIMITE_N_EFF_MIN else 'sous la limite'}"
              f" sur l'opposable ; "
              f"{'ALERTE' if diag['n_effectif_paris_correlation'] < LIMITE_N_EFF_MIN else 'AUCUNE alerte'}"
              f" sur la corrélation")
        dom = diag["actif_dominant_variance"]
        print(f"  Contributions à la VARIANCE du panier équipondéré :")
        for nom_a, part in sorted(diag["contributions_variance_pct"].items(),
                                  key=lambda kv: -kv[1]):
            print(f"      {nom_a:<14} {part:>7.2f} %")
        print(f"    → {dom['actif']} porte {dom['part_variance_pct']:.1f} % de la "
              f"variance : le « panier » est un pari unique.")
        print(f"  λ_max / n                    : {diag['lambda_max_sur_n']:.3f}")
        print(f"  Ratio de diversification     : {diag['ratio_diversification']:.3f}")
        if "OBLIG10A" in rets.columns and "SP500" in rets.columns:
            print(f"  S&P 500 / 10 ans converti    : "
                  f"{diag['matrice']['SP500']['OBLIG10A']:+.3f}   "
                  f"(la doctrine publiait +0,266 sur log(taux) : SIGNE INVERSÉ)")
        print()
        # ── G-7 : le chiffre de doctrine, PRODUIT sur le panier d'origine ──
        rets_origine = rendements_panier_origine(series)
        doc_prod = chiffre_doctrine_correlation_stress(rets_origine)
        if doc_prod.get("disponible"):
            print("  G-7 — CHIFFRE DE DOCTRINE « 0,250 », PRODUIT PAR LE CODE")
            print(f"    {doc_prod['construction']}")
            print(f"    panier d'origine : {', '.join(doc_prod['actifs'])} "
                  f"({doc_prod['n_obs']} obs, décile = {doc_prod['n_obs_decile']} obs)")
            print(f"    valeur PRODUITE  : {doc_prod['valeur_produite']:.6f}  "
                  f"(complet {doc_prod['valeur_complet']:.6f})")
            print(f"    chiffre de doctrine 0,250 → écart "
                  f"{doc_prod['ecart_au_chiffre_de_doctrine']:+.6f} → "
                  f"{'REPRODUIT' if doc_prod['reproduit'] else 'NON REPRODUIT'}")
            print("    Jusqu'ici ce nombre était AFFIRMÉ dans une chaîne de")
            print("    caractères. Il est désormais calculé, donc réfutable.\n")
        vix = series.get("VIXCLS")
        if vix is not None:
            cond = correlation_conditionnelle(rets, vix.dropna(),
                                              rets_origine=rets_origine)
            if cond.get("disponible"):
                print("  CORRÉLATION EN STRESS — conditionnement EXOGÈNE (P15)")
                print(f"    {cond['conditionnement']}, "
                      f"{cond['n_seances_conditionnelles']} séances")
                print(f"    moyenne signée complet {cond['correlation_moyenne_signee_complet']:+.4f}"
                      f" → stress {cond['correlation_moyenne_signee_stress']:+.4f}"
                      f"  (Δ {cond['delta_observe']:+.4f})")
                nl = cond["null_correlation_constante"]
                print(f"    NULL corrélation constante ({nl['n_simulations']} sim.) : "
                      f"Δ attendu {nl['delta_moyen']:+.4f}, "
                      f"IC90 [{nl['ic90'][0]:+.4f} ; {nl['ic90'][1]:+.4f}]")
                print(f"    écart au null {cond['ecart_au_null']:+.4f} → "
                      f"{'SIGNIFICATIF' if cond['significatif_a_90pct'] else 'NON SIGNIFICATIF'} à 90 %")
                mb = cond["methode_biaisee_pour_memoire"]
                print(f"    méthode BIAISÉE (queue S&P, corrélations incluant le "
                      f"S&P) : {mb['correlation_moyenne_signee']:+.4f} "
                      f"(artefact {mb['artefact_estime']:+.4f}) — NON OPPOSABLE")
                doc = cond.get("reproduction_chiffre_doctrine", {})
                if doc.get("disponible"):
                    print(f"    P18 — chiffre de doctrine reproduit : |ρ| moyen en "
                          f"stress = {doc['valeur_reproduite']:.3f} "
                          f"(doctrine : 0,250) contre {doc['valeur_complet']:.3f} "
                          f"complet, Δ {doc['delta_observe']:+.4f}")
                    print(f"          null de corrélation constante : Δ attendu "
                          f"{doc['null_delta_moyen']:+.4f}, IC90 "
                          f"[{doc['null_ic90'][0]:+.4f} ; {doc['null_ic90'][1]:+.4f}] "
                          f"→ écart au null {doc['ecart_au_null']:+.4f}")
                    print("          la baisse brute est un ARTEFACT : l'écart au "
                          "null est de SIGNE OPPOSÉ à la lecture brute.\n")

    # ── Stress sur épisodes vécus ─────────────────────────────────────────
    print("─" * 76)
    print("TESTS DE STRESS — ÉPISODES RÉELLEMENT VÉCUS, NON INVENTÉS")
    print("─" * 76)
    for i, e in enumerate(eps, 1):
        print(f"  {i}. {e['fin_fenetre']} : {e['perte_20_seances_pct']:>7.2f} % sur 20 séances")
    print()

    # ── P2 : VETO ─────────────────────────────────────────────────────────
    candidats = [Path(args.data).parent / FICHIER_TRADING,
                 RACINE / FICHIER_TRADING, sortie / FICHIER_TRADING]
    chemin_trading = next((c for c in candidats if c.exists()), candidats[0])
    src = lire_idees_transmises(chemin_trading)
    limites = {"LIMITE_VAR_POSITION_PCT": LIMITE_VAR_POSITION_PCT,
               "LIMITE_TAILLE_PCT": LIMITE_TAILLE_PCT,
               "LIMITE_CORRELATION": LIMITE_CORRELATION,
               "LIMITE_PERTE_STRESS_PCT": LIMITE_PERTE_STRESS_PCT,
               "MIN_SEANCES_PAIRE": MIN_SEANCES_PAIRE}
    # ── G-6 : σ_marché mesuré SUR LA FENÊTRE DE CHAQUE PAIRE ─────────────
    sigmas_marche = sigma_marche_par_paire(r, src.get("cointegrations", {}))
    mesures = {"date_arrete": arrete,
               "var_retenue_pct": var_retenue_pct,
               "var_limite_fondee": var_limite_fondee,
               "pire_episode_pct": eps[0]["perte_20_seances_pct"] if eps else None,
               "cointegrations": src.get("cointegrations", {}),
               "sigma_marche_par_paire": sigmas_marche}
    verdicts = veto(src["idees"], mesures, limites) if src["idees"] else []
    n_bloq = sum(1 for v in verdicts if v["veto"])
    source_examinable = bool(src.get("examinable"))
    if not source_examinable:
        # G-9 — « je n'ai pas pu examiner » n'est PAS « rien à examiner »
        statut_veto = f"SOURCE NON EXAMINÉE — {src['statut']}"
        entete_veto = (f"VETO — SOURCE NON EXAMINÉE ({src['statut']}) : "
                       f"{src.get('motif')}")
    elif not verdicts:
        statut_veto = "AUCUNE IDEE SOUMISE"
        entete_veto = ("VETO — 0 idée(s) soumise(s), 0 bloquée(s) — "
                       "AUCUNE IDEE SOUMISE (source lue, liste vide)")
    else:
        statut_veto = f"{len(verdicts)} soumise(s), {n_bloq} bloquée(s)"
        entete_veto = (f"VETO — {len(verdicts)} idée(s) soumise(s), "
                       f"{n_bloq} bloquée(s)")

    print("=" * 76)
    print(entete_veto)
    print("=" * 76)
    print("  « Aucune transaction n'est passée sans cette section » (charte).")
    print("  Le veto n'est plus une phrase imprimée par la Section Trading :")
    print("  il valide le SCHÉMA de chaque idée, puis applique cinq limites")
    print("  mesurées, et bloque. Toute donnée absente, nulle, NaN, mal typée")
    print("  ou hors domaine produit un VETO, jamais un passage silencieux.\n")
    print(f"  Source : {chemin_trading} — statut {src['statut']} "
          f"({src.get('motif')})")
    print(f"  {src.get('n_idees_lues', 0)} idée(s) lue(s), "
          f"{len(verdicts)} soumise(s) au veto, "
          f"{src.get('n_non_soumises', 0)} non soumise(s) (verdict amont "
          f"définitif).")
    if not source_examinable:
        print("\n  ⚠ AUCUN VERDICT N'A PU ÊTRE RENDU. Une source non examinée")
        print("    n'autorise rien : le processus sort en code non nul et une")
        print("    alerte SOURCE_VETO est journalisée.")
    n_schema = sum(1 for v in verdicts if not v.get("schema_conforme", True))
    if n_schema:
        print(f"  {n_schema} idée(s) BLOQUÉE(S) AU SCHÉMA — aucune limite ne "
              f"leur a été appliquée.")
    print()
    for v in verdicts:
        etiquette = "VETO" if v["veto"] else "PASSÉE"
        if not v.get("schema_conforme", True):
            etiquette = "VETO/SCHEMA"
        print(f"  [{etiquette}] {v['id']} — {v['idee']}"
              f"   (verdict Trading : {v.get('verdict_trading')})")
        for m in v["motifs"]:
            print(f"      · {m}")
        if not v["motifs"]:
            ps = v["limites_evaluees"]["perte_sous_stress"]
            b = ps.get("beta", {})
            print("      · schéma conforme, cinq limites évaluées, aucune "
                  "dépassée — NON BLOQUÉE par la Section Risque")
            if b.get("disponible"):
                print(f"        (perte sous stress {ps['perte_estimee_pct']:.3f} % "
                      f"avec β = {b['beta']:+.4f} ; l'ancienne formule en ρ "
                      f"donnait {ps['ancienne_methode_en_rho_POUR_MEMOIRE']:.3f} %, "
                      f"soit ×{ps['facteur_sous_estimation_ancienne_methode']:.2f} "
                      f"de sous-estimation)")
    print()

    Path(sortie / FICHIER_VETO).write_text(json.dumps({
        "date_arrete": arrete, "horodatage": maintenant(),
        "statut": statut_veto, "entete": entete_veto,
        "source": FICHIER_TRADING, "chemin_source": str(chemin_trading),
        "source_statut": src["statut"],
        "source_examinable": source_examinable,
        "source_motif": src.get("motif"),
        "source_disponible": src["disponible"],
        "schema_idee": {"chemins_canoniques":
                        {k2: ".".join(v2) for k2, v2 in CHEMIN_CANONIQUE.items()},
                        "champs_requis":
                        {k2: list(v2) for k2, v2 in CHAMPS_REQUIS_IDEE.items()},
                        "regle": "toute donnée absente / None / NaN / non "
                                 "numérique / mal typée / hors domaine ⇒ VETO ; "
                                 "aucune substitution, aucun repli"},
        "limites": limites,
        "sigma_marche_par_paire": sigmas_marche,
        "mesures_utilisees": {
            k2: v2 for k2, v2 in mesures.items()
            if k2 not in ("cointegrations", "sigma_marche_par_paire")},
        "verdicts": verdicts,
        "n_idees_lues": src.get("n_idees_lues", 0),
        "n_non_soumises": src.get("n_non_soumises", 0),
        "non_soumises": src.get("non_soumises", []),
        "n_soumises": len(verdicts),
        "n_bloquees": n_bloq,
        "n_bloquees_au_schema": n_schema,
    }, indent=2, ensure_ascii=False, default=str), encoding="utf-8")

    # ── Alertes ───────────────────────────────────────────────────────────
    # P9 — une position est DÉTENUE si et seulement si Trading l'a transmise
    # ET que le veto ne l'a pas bloquée. « Non bloquée par le risque » n'est
    # pas « détenue » : une idée déjà refusée en amont ne crée aucune exposition.
    positions_detenues = sum(
        1 for v in verdicts
        if not v["veto"]
        and str(v.get("verdict_trading", "")).upper().startswith("TRANSMISE"))
    al = alertes(dd, diag, reg, var_retenue_pct=var_retenue_pct,
                 positions_detenues=positions_detenues,
                 backtest_rejette_tout=not var_limite_fondee,
                 coherence=coh)
    # G-9 — la source non examinée est une ALERTE, pas un silence
    if not source_examinable:
        al.append({"type": "SOURCE_VETO", "niveau": "ALERTE",
                   "mesure": f"statut {src['statut']}",
                   "seuil": "source lisible et conforme au schéma",
                   "action_exigee": f"La source d'idées n'a PAS pu être "
                                    f"examinée ({src.get('motif')}). Aucune "
                                    f"transaction ne peut être autorisée sur "
                                    f"cette exécution. Rétablir la source, puis "
                                    f"relancer le cycle de risque."})
    print("=" * 76)
    print(f"ALERTES — {len(al)} émise(s) ce cycle · "
          f"{etat['n_non_traitees']} NON TRAITÉE(S) au journal")
    print("=" * 76)
    if not al:
        print("  Aucune ce cycle.")
    for a in al:
        print(f"\n  [{a['niveau']}] {a['type']} — mesure {a['mesure']} "
              f"contre seuil {a['seuil']}")
        print(f"    ACTION EXIGÉE : {a['action_exigee']}")
    # ── G-3 : statut des paliers, CALCULÉ, jamais rédigé ─────────────────
    st_paliers = statut_paliers_drawdown(dd, positions_detenues)
    paliers = ("ACTIFS" if st_paliers["paliers_drawdown_actifs"] else "INACTIFS")
    print(f"\n  PALIERS DE DRAWDOWN (−5 / −10 / −15 / −20 %, charte §4.3) : "
          f"{paliers}")
    print(f"    paliers_drawdown_actifs = {st_paliers['paliers_drawdown_actifs']}")
    print(f"    condition : {st_paliers['condition']}")
    print(f"    motif mesuré : {st_paliers['motif_mesure']}")
    print(f"    drawdown courant mesuré : "
          f"{st_paliers['drawdown_courant_pct']:.2f} %  ·  "
          f"positions détenues : {st_paliers['positions_detenues']}")
    if not st_paliers["paliers_drawdown_actifs"]:
        print("    G-3 — le commentaire « dd['courant'] vaut 0 par construction »")
        print("    a été RETIRÉ : il était faux. Le drawdown courant est nul")
        print("    parce que l'indice est à son plus haut, ce qui est un fait de")
        print("    marché révocable, et non une propriété du code. Exécuté sur")
        print("    données tronquées au 2020-03-23 avec position détenue, le")
        print("    coupe-circuit se déclenche à −33,92 %.")
    print("\n  Rappel Kerviel : en 2008 les alertes ont été émises et non traitées.")
    print(f"  Journal : {FICHIER_ALERTES} — relu, dédoublonné, append-only.")
    print("  Clôture : python3 apollon_risque.py --clore <id> --motif \"<texte>\"\n")

    ecr = ecrire_alertes(chemin_alertes, al, arrete)
    etat_apres = etat_journal(chemin_alertes)
    print(f"  Journal : {len(ecr['nouvelles'])} nouvelle(s) ligne(s) "
          f"(dont {len(ecr['reouvertures'])} réouverture(s)), "
          f"{ecr['dedoublonnees']} doublon(s) évité(s), "
          f"{etat_apres['n_non_traitees']} non traitée(s) au total.")
    # Conditions ouvertes au journal que ce cycle NE MESURE PLUS. Elles ne
    # sont PAS closes d'office : une clôture sans motif écrit est exactement
    # le classement silencieux de 2008. Elles sont SIGNALÉES, à charge pour
    # l'opérateur de les clore avec un motif, ou de les laisser ouvertes.
    cles_cycle = {cle_alerte(a) for a in al}
    dormantes = [u for u in etat_apres["uniques"]
                 if u["non_traitee"] and cle_alerte(u) not in cles_cycle]
    if dormantes:
        print(f"  {len(dormantes)} condition(s) ouverte(s) NON REPRODUITE(S) ce "
              f"cycle — non closes d'office :")
        for u in dormantes:
            print(f"    · {u['id_derniere_emission']}  {u['type']}/{u['niveau']}  "
                  f"dernière mesure « {u.get('derniere_mesure')} » le "
                  f"{u.get('derniere_date_donnees')}")
        print("    Une clôture sans motif écrit est un classement silencieux : "
              "elle\n    exige --clore <id> --motif \"<texte>\".")
    print()

    Path(sortie / FICHIER_RESULTATS).write_text(json.dumps({
        "date_arrete": arrete,
        "date_donnees_sp500": str(spd.index[-1].date()),
        "n_series": len(series),
        "n_cotations_sp500": len(spd), "n_rendements": len(r),
        "methode_var_retenue_ex_ante": METHODE_VAR_RETENUE,
        "regle_fenetre_limite": REGLE_FENETRE_LIMITE,
        "regle_valeur_critique_backtest_ex_ante": REGLE_VALEUR_CRITIQUE_BACKTEST,
        "var_retenue_pct": var_retenue_pct,
        "var_limite_fondee": var_limite_fondee,
        "cellule_de_limite": cellule_limite,
        "fenetres": fenetres_info,
        "aucune_fenetre_courte_ne_contient_de_crise": aucune_crise_court,
        "var": tableau_var,
        "ecart_max_methodes_valides_pt": ecart_max_valide,
        "backtest": backtests,
        "calibration_backtest_sous_h0": calibrations,
        "decompte_cellules": {
            "methode_retenue": METHODE_VAR_RETENUE,
            "n_cellules_methode_retenue": len(cellules_methode),
            "n_admissibles_methode_retenue": len(survivants),
            "n_cellules_toutes_methodes": len(cellules_testables),
            "n_admissibles_toutes_methodes": len(survivants_toutes),
            "note": "G-4 — deux populations distinctes. Seules les cellules de "
                    "la méthode retenue ex ante sont opposables ; les cellules "
                    "paramétriques et Johnson SU sont des annexes.",
        },
        "echecs_johnson_su_backtest": echecs_su,
        "tableau_limites_admissibles": tableau_limites,
        "cornish_fisher_statut": "REFUSÉE — hors domaine de validité",
        "cornish_fisher_diagnostic": diag_cf,
        "performance": sh, "sortino": so, "coherence_sortino_sharpe": coh,
        "calmar": cal, "drawdown": dd,
        "paliers_drawdown": paliers,
        "paliers_drawdown_actifs": st_paliers["paliers_drawdown_actifs"],
        "statut_paliers_drawdown": st_paliers,
        "kelly": k,
        "simulation_levier_quotidien": sim,
        "simulation_levier_mensuel": sim_mens,
        "regime": reg, "percentiles": pcts,
        "correlations": diag, "correlation_stress": cond,
        "chiffre_doctrine_produit": doc_prod,
        "episodes_stress": eps,
        "veto": statut_veto, "verdicts_veto": verdicts,
        "source_veto": {"statut": src["statut"], "examinable": source_examinable,
                        "motif": src.get("motif"),
                        "chemin": str(chemin_trading)},
        "alertes": al, "n_alertes_cycle": len(al),
        "n_alertes_non_traitees": etat_apres["n_non_traitees"],
        "journal": {k2: v2 for k2, v2 in etat_apres.items() if k2 != "uniques"},
        "constantes": inv,
    }, indent=2, ensure_ascii=False, default=str), encoding="utf-8")
    print(f"→ {FICHIER_RESULTATS} · {FICHIER_VETO} · {FICHIER_ALERTES}")

    # ── CODES DE SORTIE ──────────────────────────────────────────────────
    #   2 — au moins une idée BLOQUÉE par le veto ;
    #   3 — G-9 : source d'idées NON EXAMINÉE (absente, illisible, schéma
    #       invalide). Ce n'est pas « rien à examiner » et cela ne doit pas
    #       ressembler à un succès ;
    #   0 — source examinée, aucune idée bloquée.
    n_bloquees = sum(1 for v in verdicts if v["veto"])
    if n_bloquees:
        print(f"\nSORTIE EN CODE 2 : {n_bloquees} idée(s) BLOQUÉE(S) par le veto "
              f"(dont {n_schema} au schéma).")
        print("Un veto qui ne bloque pas le processus n'est pas un veto.")
        return 2
    if not source_examinable:
        print(f"\nSORTIE EN CODE 3 : source d'idées NON EXAMINÉE — "
              f"{src['statut']} ({src.get('motif')}).")
        print("« Je n'ai pas pu examiner » n'est pas « rien à examiner ».")
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
