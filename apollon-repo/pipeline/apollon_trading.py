#!/usr/bin/env python3
"""
APOLLON — Portier de qualité Trading
====================================
Section Trading · Générale Aurelius
Version 4 — 16/08/2026, corrections F-2…F-9 après le réaudit Astra 010
(« VALIDÉE SOUS RÉSERVE »). Version 3 : refonte après le REFUS de l'audit 008.

CE MODULE N'A PAS LE DROIT DE DÉCLARER UNE IDÉE EXÉCUTABLE
-----------------------------------------------------------
Son verdict maximal est « TRANSMISE ». Une idée TRANSMISE sort avec
`statut_risque = "EN_ATTENTE_VETO"` — une DEMANDE de veto, jamais une
autorisation. Une idée REFUSÉE sort avec
`statut_risque = "NON_SOUMISE_REFUSEE_EN_AMONT"` : elle n'est pas soumise,
donc elle ne peut pas revenir de l'aval avec un enregistrement favorable
(CORRECTION F-8). Seule la Section Risque peut lever ou opposer le veto de
la charte. Un moteur de trading qui s'auto-autorise n'est pas un moteur de
trading, c'est un opérateur sans contrepartie.

CE QUE LE RÉAUDIT 010 A CORRIGÉ (F-2…F-9)
------------------------------------------
  F-7 UN THÉORÈME FAUX RETIRÉ DE LA DOCTRINE. Le critère 1 affirmait que
      le ratio « ne peut franchir 2:1 que si le stop est placé plus près
      que la cible, ce qui détruit l'espérance (Doob) ». FAUX : le stop
      étant ABSOLU et la cible FIXE, le ratio vaut ≈ |z₀|/(2,5−|z₀|) et
      franchit 2:1 dès |z₀| ≈ 1,71 à constantes de doctrine INCHANGÉES —
      et l'espérance y est MAXIMALE. Critères 1 et 7 non antagonistes.
      La table de franchissement est CALCULÉE à chaque exécution.
  F-6 L'ADF GLISSANT, PROMIS AU CRITÈRE 3, N'ÉTAIT CALCULÉ NULLE PART.
      Il l'est, il est publié, et il est BLOQUANT (critère 8). Le test
      hors échantillon, qui n'alimentait aucun verdict, devient le
      critère 9.
  F-3 LA DOCTRINE DE PROFONDEUR N'ÉTAIT PAS OPPOSABLE. Critère 10.
  F-8 `EN_ATTENTE_VETO` était apposé même sur les idées REFUSÉES.
  F-2 DISCRÉTISATION : passage à 20 sous-pas par séance, biais mesuré.
  F-4 DÉPASSEMENT PUBLIÉ DES DEUX CÔTÉS ; la « marge en erreurs types de
      Monte-Carlo » est retirée au profit de l'espérance sur l'IC de κ.
  F-5 UNE DEMI-VIE DONT LA RACINE UNITAIRE N'EST PAS REJETÉE N'A PAS DE
      BORNE SUPÉRIEURE. Elle est déclarée non identifiée.
  F-9 Plus aucun `assert` (ils disparaissent sous `python3 -O`) ; boucle
      encapsulée ; JSON horodaté et périssable ; garde `len > 20` fermée
      par un vocabulaire ; taille nommée.

CE QUE LE RÉAUDIT 010 A RÉFUTÉ — ET QUI N'A PAS ÉTÉ TOUCHÉ
-----------------------------------------------------------
  · les constantes de barrières (cible z = 0, stop z = ±2,5) ne sont
    ajustées sur rien ; le refus du jour est un résultat, pas un réglage ;
  · l'espérance vient de la dérive mesurée, pas du placement des barrières
    (zéro sous martingale — Doob) ;
  · la sélection des retards par BIC ;
  · le contrôle de cohérence Ornstein-Uhlenbeck ;
  · le traitement du WTI négatif ;
  · le test hors échantillon lui-même (il était propre : il ne lui
    manquait qu'un critère à alimenter).

CE QUE L'AUDIT 008 A RÉFUTÉ — ET QUI N'A PAS ÉTÉ TOUCHÉ
--------------------------------------------------------
  · valeur critique d'Engle-Granger −3,34 : CORRECTE (2 000 marches
    aléatoires → 4,80 %-5,15 % de rejets). Conservée telle quelle.
  · P = b/(a+b) : formule exacte. Conservée (elle reste utilisée comme
    CONTRÔLE analytique de la simulation à horizon infini, plus comme
    estimateur de probabilité à 30 séances).
  · estimation de la demi-vie : biais −5,0 %, correcte. Conservée ;
    seul l'intervalle de confiance manquait, il est désormais publié.
  · traitement du WTI négatif (−37,63 $ le 20/04/2020) : exemplaire.
    Observations non positives exclues ET comptées. Conservé.

CE QUI A ÉTÉ CORRIGÉ (P1…P16) — voir les blocs marqués « CORRECTION Pxx ».

Usage :
    python3 apollon_trading.py --data /chemin/vers/data
"""
from __future__ import annotations

import argparse, json, math
from datetime import datetime, timedelta
from pathlib import Path
import numpy as np, pandas as pd

# ══════════════════════════════════════════════════════════════════════════
# SEUILS — charte Partie VI, rendus mécaniques
# ══════════════════════════════════════════════════════════════════════════
RATIO_MINIMUM = 2.0            # gain max / perte max, LES DEUX QUEUES (R-030)
CORRELATION_MAX = 0.70         # au-delà : position unique (R-R3)
TAILLE_MAX_PCT = 8.0           # charte 4.1
HORIZON_SEANCES = 30           # six semaines
HORIZON_JOURS_CAL = 42         # 30 séances ≈ 42 jours calendaires

# ── CORRECTION F-9 : la taille est NOMMÉE, plus quatre littéraux 3.0 ─────
# Elle était écrite en dur à quatre endroits (simulation, portier, test hors
# échantillon, charge JSON). Quatre littéraux identiques sont quatre
# occasions de divergence silencieuse.
TAILLE_PCT_NAV = 3.0

# ── CORRECTION P2 / P10 : simulation, graine fixée et PUBLIÉE ────────────
GRAINE_SIMULATION = 12345
N_TRAJECTOIRES = 100_000
# Grille réduite pour les TABLES D'EXPLORATION (sensibilité au z d'entrée,
# au stop, à κ). Déclarée : ces tables ne décident de rien, elles publient
# une forme. Le verdict, lui, est rendu sur N_TRAJECTOIRES.
N_TRAJECTOIRES_EXPLORATION = 20_000

# ── CORRECTION F-2 / F-4 : DISCRÉTISATION ────────────────────────────────
# Le premier passage était simulé au PAS JOURNALIER. Une trajectoire qui
# franchit une barrière entre deux clôtures et revient n'était pas comptée :
# P(stop) sous-estimée (−42 % sur HY/IG, −33 % sur Brent au pas 1), espérance
# surévaluée (+26 % et +58 %). Le biais n'est pas un arrondi, il est
# systématique et d'un seul côté.
# Le pas est donc subdivisé en SOUS_PAS_PAR_SEANCE incréments d'OU exacts.
# L'erreur résiduelle d'un schéma à barrières discrètes est en O(1/√m) ;
# elle est mesurée et publiée à chaque exécution (extrapolation de Richardson
# en 1/√m entre m = 1 et m = SOUS_PAS_PAR_SEANCE), elle n'est pas postulée.
SOUS_PAS_PAR_SEANCE = 20

# ── CORRECTION P1 : barrières fixées en z ABSOLU, pas en multiples d'un σ
#    ambigu. Voir la docstring de `simuler_barrieres`.
CIBLE_Z = 0.0                  # la moyenne : c'est là que le retour va
STOP_Z_ABSOLU = 2.5            # stop au NIVEAU z = ±2,5 (borne absolue, pas un
                               # écart relatif : une entrée déjà au-delà de 2,5σ
                               # n'a plus de stop, elle est disqualifiée)
# POURQUOI 2,5 EST FIXÉ ICI, EX ANTE, ET NON CHOISI PAR PAIRE.
# Le stop est le seul paramètre libre de la structure ; le laisser flotter
# permettrait de fabriquer le critère 1 en le resserrant jusqu'à ce que le
# ratio passe. C'est exactement la faute que le module reprochait par écrit
# à sa propre version du 15/08 : « le ratio vaut 2,00 PARCE QUE j'ai écrit
# stop −1σ et cible +2σ. Un critère que l'agent règle lui-même n'est pas un
# critère. » Le stop est donc une CONSTANTE de doctrine, arrêtée avant de
# voir les données.
#
# CORRECTION F-7 — LA TABLE DE SENSIBILITÉ AU STOP N'EST PLUS RECOPIÉE ICI.
# Elle était saisie à la main à partir d'un seul cas (HY/IG au 14/08) et
# servait d'appui à une conclusion générale (« franchir 2:1 divise
# l'espérance par trois »). Une table figée dans un commentaire ne se
# vérifie pas et vieillit sans prévenir. Elle est désormais RECALCULÉE à
# chaque exécution, par paire, et imprimée (`table_sensibilite_stop`).
# Ce qui est doctrinal tient en une phrase, et elle ne dépend d'aucun cas :
# resserrer le stop pour franchir le critère 1 revient à appeler « stop »
# une fraction de σ qui n'invalide plus rien. Le refus, quand il tombe,
# reste un résultat, pas un réglage.

# ── CORRECTION P6 : la convention de coût est TRANCHÉE et DOCUMENTÉE ─────
# 15 pb ALLER-RETOUR du NOTIONNEL de la position (convention de marché :
# une commission se cite en points de base de la valeur traitée, jamais en
# points de base des capitaux propres du fonds).
#   coût en % de NAV = (COUT_ALLER_RETOUR_PB / 10 000) × taille_pct_nav
# Sous cette convention, une position de 3 % de NAV paie 0,45 pb de NAV
# par aller-retour. L'autre lecture (15 pb de NAV par aller-retour) est
# économiquement absurde : elle ferait payer le même coût à une position
# de 0,1 % et à une position de 8 %.
COUT_ALLER_RETOUR_PB = 15.0
BASE_COUT = "points de base du NOTIONNEL de la position, aller-retour"

# ── CORRECTION P8 : contrôle de profondeur, seuils explicites ────────────
PROFONDEUR_MIN_OBS = 250
PROFONDEUR_MIN_ANNEES = 5.0    # en deçà : alerte PROFONDEUR_INSUFFISANTE

# ── CORRECTION F-3 : LA PROFONDEUR EST OPPOSABLE, PLUS SEULEMENT IMPRIMÉE
# `PROFONDEUR_MIN_ANNEES` et `ECHANTILLON_SANS_STRESS` produisaient deux
# chaînes dans une liste `alertes` que rien ne lisait. HY/IG (3,00 ans,
# aucun épisode de stress dans l'échantillon) traversait le portier sans
# qu'aucun critère ne s'y oppose — pendant que la Section Risque bloquait
# sur EXACTEMENT ces deux motifs. La section qui énonce la doctrine ne s'y
# tenait pas. Ces deux marqueurs sont désormais le critère 10, BLOQUANT.
# Un échantillon sans stress ne dit rien du comportement de la paire en
# stress : la demi-vie et le σ y sont calibrés sur un seul régime.
EXIGER_STRESS_DANS_ECHANTILLON = True

# ── CORRECTION P11 : fenêtre glissante causale ───────────────────────────
FENETRE_GLISSANTE = 250        # une année de séances

# ── CORRECTION F-6 : ADF GLISSANT — DÉCLARÉ AU CRITÈRE 3, JAMAIS CALCULÉ
# Le critère 3 promettait « l'ADF glissant sur 250 séances, retards par BIC,
# remonte au-dessus de −3,04 ». Cette phrase n'existait que dans un littéral
# de chaîne : aucun ADF glissant n'était calculé nulle part. Le critère
# était franchi par la DESCRIPTION d'un test.
# C'est pourtant le seul instrument du module qui détecte une RUPTURE de
# relation : sur une paire cointégrée puis rompue, la cointégration plein
# échantillon, la demi-vie, son IC et le contrôle OU restent tous sains,
# et seul l'ADF glissant s'effondre.
# Il est donc réellement calculé, publié, et opposable (critère 8).
ADF_GLISSANT_FENETRE = 250     # séances par fenêtre
ADF_GLISSANT_PAS = 25          # une fenêtre par mois de bourse
ADF_GLISSANT_SEUIL_T = -3.04   # valeur critique Engle-Granger à 10 %
# Fenêtres « récentes » sur lesquelles le critère tranche : 24 pas de 25
# séances ≈ deux années de bourse. Constante de doctrine, arrêtée sur une
# durée, pas sur un résultat.
ADF_GLISSANT_N_FENETRES_RECENTES = 24
# Tolérance : au plus un cinquième des fenêtres récentes peut échouer à
# rejeter la racine unitaire à 10 %. Au-delà, la relation n'est pas
# « bruitée », elle est intermittente — et une relation intermittente n'est
# pas la condition nécessaire d'un pair trade. Seuil posé ex ante.
ADF_GLISSANT_FRACTION_MAX = 0.20

# ── CORRECTION F-6 : le test hors échantillon devient OPPOSABLE ──────────
# Il existait, il était propre, et il n'alimentait AUCUN critère : il
# rejetait la prédiction du modèle sans qu'aucun verdict ne s'en aperçoive.
# Désormais critère 9. Le modèle prédit trois probabilités de sortie
# (cible / stop / marché) et une espérance ; le hors échantillon les
# confronte aux réalisations. Un χ² de Pearson sur les trois issues.
HORS_ECHANTILLON_SEUIL_P = 0.01   # en deçà : le modèle est réfuté, refus
HORS_ECHANTILLON_MIN_SIGNAUX = 10 # sous ce nombre, le test n'a pas de puissance

# ── CORRECTION F-9 : marqueur de fraîcheur du fichier de sortie ──────────
# La Section Risque relisait `trading_resultats.json` sans aucun moyen de
# savoir s'il datait du jour ou de la veille. Un fichier périmé lu comme
# frais est une position prise sur des chiffres morts.
VALIDITE_SORTIE_HEURES = 36.0

# ── CORRECTION P7 : vocabulaires contrôlés, plus de chaîne libre ─────────
TYPES_INVALIDATION_ADMIS = {"test_statistique", "fait_macroeconomique",
                            "fait_microstructure", "evenement_credit"}
OBSTACLES_ARBITRAGE_ADMIS = {"contrainte_stockage", "segmentation_clientele",
                             "cout_de_portage", "contrainte_reglementaire",
                             "illiquidite"}
# ── CORRECTION F-9 : le MÉCANISME sort du texte libre ────────────────────
# Le critère 4 vérifiait `isinstance(mecanisme, str) and len(mecanisme) > 20`.
# `'x' * 21` le franchissait. Une garde de longueur n'est pas une garde de
# contenu. Le mécanisme est désormais un CODE d'un vocabulaire fermé, au
# même titre que l'obstacle ; la phrase reste, mais elle n'est plus ce qui
# fait passer le critère. Une référence non vide est également exigée.
MECANISMES_ADMIS = {
    "convergence_par_notation":        "rééquilibrage des mandats obligataires par notation",
    "borne_par_cout_de_transport":     "écart borné par le coût de transport physique",
    "borne_par_cout_de_stockage":      "écart borné par le coût de stockage",
    "arbitrage_de_livraison_physique": "arbitrage cash-and-carry sur sous-jacent livrable",
}

# ── CORRECTION P7 (critère 2) : calendrier d'événements DATÉS ────────────
# Un catalyseur est un ÉVÉNEMENT À DATE. Le retour à la moyenne n'est pas
# un événement : il n'a pas de date, il a une demi-vie. Le fonds ne dispose
# d'AUCUNE source d'événements datés dans son pipeline (`apollon_data.py`
# ne collecte que des séries FRED). Ce calendrier est donc vide, et le
# critère 2 échoue pour toutes les paires. C'est le résultat honnête :
# l'absence de source n'est pas une preuve de catalyseur.
# Format attendu : {"Nom de la paire": [(datetime, "libellé"), ...]}
CALENDRIER_CATALYSEURS: dict[str, list[tuple[datetime, str]]] = {}


class ControleInterneRompu(RuntimeError):
    """CORRECTION F-9 — remplace les `assert` du module.

    Deux contrôles centraux étaient écrits `assert` : la cohérence
    Ornstein-Uhlenbeck et l'exhaustivité des trois états de sortie.
    `python3 -O` supprime les `assert` : les deux gardes disparaissaient
    sans le moindre message sous un commutateur d'exécution banal. Vérifié.
    De plus, l'exception était levée dans la boucle sur les paires, sans
    `try` : une seule paire mal calibrée tuait le processus AVANT l'écriture
    du JSON, et la Section Risque relisait le fichier de la veille sans
    marqueur de péremption.
    Les contrôles sont désormais des `if` explicites, incompressibles, et
    l'exception est capturée paire par paire.
    """


def charger(d: Path) -> dict[str, pd.Series]:
    return {f.stem: pd.read_csv(f, parse_dates=["date"]).set_index("date")["value"].sort_index()
            for f in sorted((d / "history").glob("*.csv"))}


# ══════════════════════════════════════════════════════════════════════════
# COINTÉGRATION — Engle-Granger
# ══════════════════════════════════════════════════════════════════════════
def _adf_regression(x: np.ndarray, p: int, decalage_commun: int) -> tuple[float, float, float, int]:
    """Une régression ADF à p retards, estimée sur un ÉCHANTILLON COMMUN.

    L'échantillon est tronqué à `decalage_commun` quel que soit p : sans
    cela, comparer l'AIC/BIC entre deux valeurs de p compare deux
    vraisemblances calculées sur deux échantillons différents, ce qui n'a
    aucun sens.
    """
    dx = np.diff(x); n = len(dx)
    y = dx[decalage_commun:]
    colonnes = [np.ones(len(y)), x[decalage_commun:-1]]
    for L in range(1, p + 1):
        colonnes.append(dx[decalage_commun - L:n - L])
    X = np.column_stack(colonnes)
    m, k = X.shape
    if m - k < 20:
        return float("nan"), float("inf"), float("inf"), p
    b, *_ = np.linalg.lstsq(X, y, rcond=None)
    e = y - X @ b
    ssr = float(e @ e)
    s2 = ssr / (m - k)
    try:
        se = math.sqrt(s2 * np.linalg.inv(X.T @ X)[1, 1])
    except np.linalg.LinAlgError:
        return float("nan"), float("inf"), float("inf"), p
    t = float(b[1] / se) if se > 0 else float("nan")
    aic = m * math.log(ssr / m) + 2 * k
    bic = m * math.log(ssr / m) + k * math.log(m)
    return t, aic, bic, p


def adf(x: np.ndarray, critere: str = "BIC") -> dict:
    """
    Dickey-Fuller augmenté AVEC SÉLECTION DE RETARDS — CORRECTION P9.

    AVANT : `def adf(x, retards: int = 1)`. Le 1 n'était ni choisi ni
    justifié. Sous H0 (deux marches indépendantes à incréments MA(1) —
    la signature du bruit de microstructure sur données quotidiennes),
    ce test rejette la non-cointégration jusqu'à 82,7 % du temps pour
    θ = −0,7, contre 2,7 % avec 20 retards.

    APRÈS : p ∈ [0, p_max] avec p_max = int(12·(n/100)^0,25) (Schwert),
    sélectionné par BIC sur échantillon COMMUN, retard retenu PUBLIÉ.
    Le BIC est retenu plutôt que l'AIC parce que l'AIC SATURE p_max —
    symptôme classique de sur-paramétrage. CORRECTION F-7 : le nombre de
    paires concernées n'est plus recopié à la main dans cette docstring (il
    y était figé sur l'arrêté du 14/08 et aurait vieilli sans prévenir) ; il
    est COMPTÉ et imprimé à chaque exécution, sous la table de
    cointégration. L'AIC est publié par paire comme contrôle de robustesse.

    La valeur critique reste −3,34 (Engle-Granger, 2 variables) :
    l'audit 008 l'a explicitement validée par simulation.
    """
    x = np.asarray(x, float)
    n = len(x)
    if n - 1 < 50:
        return {"t": float("nan"), "retards": 0, "p_max": 0, "critere": critere}
    p_max = int(12 * (n / 100) ** 0.25)
    p_max = min(p_max, max(0, (n - 40) // 2))
    resultats = [_adf_regression(x, p, p_max) for p in range(0, p_max + 1)]
    resultats = [r for r in resultats if np.isfinite(r[0])]
    if not resultats:
        return {"t": float("nan"), "retards": 0, "p_max": p_max, "critere": critere}
    idx = 2 if critere == "BIC" else 1
    retenu = min(resultats, key=lambda r: r[idx])
    autre = min(resultats, key=lambda r: r[1] if critere == "BIC" else r[2])
    t_p1 = next((r[0] for r in resultats if r[3] == 1), float("nan"))
    return {"t": retenu[0], "retards": retenu[3], "p_max": p_max, "critere": critere,
            "t_critere_alternatif": autre[0], "retards_critere_alternatif": autre[3],
            "t_ancien_retards_1": t_p1}


def demi_vie_et_ic(spread: np.ndarray, racine_unitaire_rejetee: bool) -> dict:
    """
    Demi-vie de retour à la moyenne + INTERVALLE DE CONFIANCE — CORRECTION P12.

    Δs_t = c + k·s_{t−1} + ε,  h = −ln2 / k.
    Méthode delta : ∂h/∂k = ln2 / k², d'où σ_h = (ln2/k²)·σ_k.

    L'audit 008 a confirmé que l'ESTIMATION était bonne (biais −5,0 %).
    Ce qui manquait était l'intervalle. Il change la lecture : la doctrine
    éliminait 10 ans/2 ans et 30 ans/10 ans sur « 114 et 142 séances »,
    c'est-à-dire sur des estimations ponctuelles présentées comme des
    mesures. CORRECTION F-7 : l'ampleur de cet intervalle n'est plus
    décrite ici par un chiffre recopié (« un facteur 6 ») — chiffre devenu
    faux, puisque sur ces deux paires la racine unitaire n'est pas rejetée
    et que l'intervalle n'a PAS de borne supérieure. L'intervalle est
    calculé, qualifié (identifié ou non) et imprimé par paire.

    ── CORRECTION F-5 : DEUX ÉNONCÉS QUI NE PEUVENT PAS ÊTRE VRAIS ENSEMBLE
    Le `k` estimé ici est LE MÊME COEFFICIENT que celui que l'ADF teste. Le
    module le déclarait non significatif contre la valeur critique −3,34,
    puis publiait « demi-vie 113,8 [32,3 ; 195,2] » en construisant
    l'intervalle à ±1,96 σ, c'est-à-dire en supposant k normal ET
    significativement négatif. On ne peut pas à la fois ne pas rejeter la
    racine unitaire et borner la demi-vie par le haut : sous k = 0, h = ∞.
    La distribution de k n'est d'ailleurs pas normale sous H0 — c'est
    précisément pourquoi la valeur critique vaut −3,34 et non −1,96.

    Tranché : si la racine unitaire n'est PAS rejetée, la demi-vie est
    déclarée NON IDENTIFIÉE et sa borne supérieure est infinie. L'estimation
    ponctuelle reste publiée (elle sert au contrôle de cohérence OU), mais
    elle ne peut plus être lue comme une mesure encadrée.
    """
    s = np.asarray(spread, float)
    ds, sl = np.diff(s), s[:-1]
    X = np.column_stack([np.ones(len(sl)), sl])
    b, *_ = np.linalg.lstsq(X, ds, rcond=None)
    e = ds - X @ b
    m = len(ds)
    s2 = float(e @ e) / (m - 2)
    try:
        se_k = math.sqrt(s2 * np.linalg.inv(X.T @ X)[1, 1])
    except np.linalg.LinAlgError:
        return {"demi_vie": float("nan"), "ic95": [float("nan"), float("nan")],
                "k": float("nan"), "identifiee": False,
                "motif_non_identifiee": "matrice singulière"}
    k = float(b[1])
    if k >= 0:
        return {"demi_vie": float("nan"), "ic95": [float("nan"), float("nan")],
                "k": k, "se_k": se_k, "identifiee": False,
                "motif_non_identifiee": "k ≥ 0 : aucun retour à la moyenne estimé"}
    h = -math.log(2) / k
    se_h = math.log(2) / k ** 2 * se_k
    if not racine_unitaire_rejetee:
        # Borne supérieure INFINIE, représentée par None (JSON n'a pas d'infini).
        return {"demi_vie": h, "ic95": [h - 1.96 * se_h, None],
                "k": k, "se_k": se_k, "se_demi_vie": se_h,
                "identifiee": False,
                "libelle_ic": "demi-vie non identifiée (borne supérieure infinie)",
                "motif_non_identifiee": (
                    "la racine unitaire n'est pas rejetée par l'ADF (valeur "
                    "critique −3,34) : le même coefficient k ne peut pas être "
                    "déclaré non significatif et encadré à ±1,96 σ")}
    return {"demi_vie": h, "ic95": [h - 1.96 * se_h, h + 1.96 * se_h],
            "k": k, "se_k": se_k, "se_demi_vie": se_h, "identifiee": True,
            "libelle_ic": f"{h:.1f} [{h - 1.96 * se_h:.1f} ; {h + 1.96 * se_h:.1f}]"}


def adf_glissant(spread: pd.Series,
                 fenetre: int = ADF_GLISSANT_FENETRE,
                 pas: int = ADF_GLISSANT_PAS,
                 seuil_t: float = ADF_GLISSANT_SEUIL_T,
                 n_recentes: int = ADF_GLISSANT_N_FENETRES_RECENTES) -> dict:
    """
    CORRECTION F-6 — L'ADF GLISSANT, RÉELLEMENT CALCULÉ.

    Le critère 3 promettait ce test depuis deux versions ; il n'existait que
    sous forme de chaîne de caractères. Un test décrit n'est pas un test.

    Fenêtre de `fenetre` séances, avancée de `pas` en `pas`, retards
    sélectionnés par BIC dans chaque fenêtre (même procédure que l'ADF plein
    échantillon, P9). Chaque fenêtre est CAUSALE par construction : elle
    n'utilise que des observations qui la précèdent ou la composent.

    CE QU'IL DÉTECTE ET QUE RIEN D'AUTRE NE DÉTECTE : la RUPTURE de
    relation. Une paire cointégrée sur la première moitié de l'échantillon
    et rompue sur la seconde produit un dossier plein échantillon d'aspect
    irréprochable — cointégration à 5 %, demi-vie encadrée, contrôle OU
    passé, espérance positive, aucune alerte. Seul l'ADF glissant s'effondre.
    L'agrégat masque la rupture ; la fenêtre la montre.

    Publié : la série complète des t, les dates de fin de fenêtre, la
    fraction de franchissements sur l'ensemble et sur les fenêtres récentes.
    """
    x = np.asarray(spread.values, float)
    n = len(x)
    if n < fenetre + 1:
        return {"disponible": False,
                "motif": f"{n} obs < fenêtre {fenetre}",
                "fenetre": fenetre, "pas": pas}
    fins, ts, retards = [], [], []
    for t in range(fenetre, n + 1, pas):
        r = adf(x[t - fenetre:t], critere="BIC")
        fins.append(str(spread.index[t - 1].date()))
        ts.append(float(r["t"]))
        retards.append(int(r["retards"]))
    ts_arr = np.asarray(ts, float)
    finis = np.isfinite(ts_arr)
    if not finis.any():
        return {"disponible": False, "motif": "aucune fenêtre exploitable",
                "fenetre": fenetre, "pas": pas}
    franchit = ts_arr > seuil_t                 # « remonte au-dessus de −3,04 »
    recentes = ts_arr[-n_recentes:]
    franchit_rec = recentes > seuil_t
    return {"disponible": True,
            "fenetre": fenetre, "pas": pas, "seuil_t": seuil_t,
            "n_fenetres": int(len(ts_arr)),
            "n_fenetres_recentes": int(len(recentes)),
            "dates_fin_fenetre": fins,
            "t_glissants": [float(v) for v in ts_arr],
            "retards_glissants": retards,
            "t_min": float(np.nanmin(ts_arr)), "t_max": float(np.nanmax(ts_arr)),
            "t_dernier": float(ts_arr[-1]),
            "n_franchissements": int(franchit.sum()),
            "fraction_franchissements": float(franchit.mean()),
            "n_franchissements_recents": int(franchit_rec.sum()),
            "fraction_franchissements_recents": float(franchit_rec.mean())}


def episodes_de_stress(S: dict[str, pd.Series], debut, fin) -> dict:
    """
    CORRECTION P8 — l'échantillon contient-il un épisode de stress ?

    Deux marqueurs, tous deux mesurés sur les données du fonds, aucun
    postulé :
      · repli actions ≥ 20 % depuis le plus haut glissant (S&P 500) ;
      · écart de crédit haut rendement ≥ 800 pb (BAMLH0A0HYM2).
    Au moins cinq séances marquées sont exigées pour écarter un point
    isolé.

    Une demi-vie et un σ calibrés sur un régime calme ne décrivent PAS le
    comportement de la paire en régime de stress. La réserve n° 1 de la
    doctrine annonçait « la cointégration mesurée sur dix ans » sur une
    paire qui n'en a que trois.
    """
    marqueurs = []
    if "SP500" in S:
        sp = S["SP500"].loc[debut:fin]
        if len(sp) > 20:
            dd = sp / S["SP500"].loc[:fin].cummax().loc[sp.index] - 1.0
            n = int((dd <= -0.20).sum())
            if n >= 5:
                marqueurs.append(f"repli actions ≥ 20 % ({n} séances)")
    if "BAMLH0A0HYM2" in S:
        hy = S["BAMLH0A0HYM2"].loc[debut:fin]
        n = int((hy >= 8.0).sum())
        if n >= 5:
            marqueurs.append(f"écart HY ≥ 800 pb ({n} séances)")
    return {"contient_stress": bool(marqueurs), "marqueurs": marqueurs}


def cointegration(a: pd.Series, b: pd.Series, S: dict[str, pd.Series]) -> dict:
    """
    Engle-Granger. Deux séries sont cointégrées si une combinaison linéaire
    est stationnaire — c'est la condition NÉCESSAIRE d'un pair trade.
    Sans elle, l'écart n'a aucune raison de revenir, et « retour à la moyenne »
    est une croyance, pas une propriété.
    """
    j = pd.concat([a.rename("a"), b.rename("b")], axis=1, sort=True).dropna()
    n_brut = len(j)
    # Le WTI a coté NÉGATIF le 20 avril 2020 (−37,63 $). Le logarithme d'un
    # prix négatif n'existe pas. Les observations non strictement positives
    # sont écartées ET COMPTÉES — les supprimer en silence serait la faute
    # E-032 : une lacune non déclarée. [VALIDÉ PAR L'AUDIT 008 — NE PAS TOUCHER]
    j = j[(j["a"] > 0) & (j["b"] > 0)]
    n_exclues = n_brut - len(j)
    if len(j) < PROFONDEUR_MIN_OBS:
        return {"disponible": False, "motif": f"{len(j)} obs exploitables"}

    # ── CORRECTION P8 : profondeur RÉELLE, en observations ET en années ──
    debut, fin = j.index[0], j.index[-1]
    annees = float((fin - debut).days / 365.25)
    stress = episodes_de_stress(S, debut, fin)
    alertes = []
    if annees < PROFONDEUR_MIN_ANNEES:
        alertes.append(f"PROFONDEUR_INSUFFISANTE ({annees:.2f} ans < {PROFONDEUR_MIN_ANNEES})")
    if not stress["contient_stress"]:
        alertes.append("ECHANTILLON_SANS_STRESS")

    la, lb = np.log(j["a"].values), np.log(j["b"].values)
    X = np.column_stack([np.ones(len(lb)), lb])
    beta, *_ = np.linalg.lstsq(X, la, rcond=None)
    spread = la - X @ beta

    a_res = adf(spread, critere="BIC")
    t_adf_brut = a_res["t"]
    racine_unitaire_rejetee = bool(np.isfinite(t_adf_brut) and t_adf_brut < -3.34)
    # CORRECTION F-5 — l'IC de la demi-vie n'est construit que si le MÊME
    # coefficient a été déclaré significatif par le test qui le juge.
    dv = demi_vie_et_ic(spread, racine_unitaire_rejetee)
    # CORRECTION F-6 — l'ADF glissant est CALCULÉ, pas décrit.
    adf_gliss = adf_glissant(pd.Series(spread, index=j.index))

    sigma_niveau = float(spread.std())              # σ_N, écart-type du NIVEAU
    sigma_increment = float(np.diff(spread).std(ddof=1))   # σ_j, écart-type de la VARIATION

    # ── CORRECTION P3 : CONTRÔLE DE COHÉRENCE ORNSTEIN-UHLENBECK ────────
    # Pour un OU stationnaire, σ_N = σ_j / √(2κ) avec κ = ln2/h.
    # Si le rapport théorique/observé s'écarte, le calibrage OU ne tient
    # pas et TOUT ce qui en découle (dérive, probabilités) est faux.
    # C'est cette assertion, et elle seule, qui autorise à mesurer le
    # risque avec la loi stationnaire plutôt qu'avec la racine du temps.
    coh = {"applicable": False}
    if np.isfinite(dv["demi_vie"]) and dv["demi_vie"] > 0:
        kappa = math.log(2) / dv["demi_vie"]
        sigma_n_theorique = sigma_increment / math.sqrt(2 * kappa)
        rapport = sigma_n_theorique / sigma_niveau if sigma_niveau > 0 else float("nan")
        coh = {"applicable": True, "kappa": kappa,
               "sigma_n_theorique": sigma_n_theorique,
               "sigma_n_observe": sigma_niveau, "rapport": rapport,
               "borne_basse": 0.75, "borne_haute": 1.33}
        # ── CORRECTION F-9 : PLUS D'`assert` ─────────────────────────────
        # AVANT : `assert 0.75 < rapport < 1.33`. Deux défauts, tous deux
        # graves. (1) `python3 -O` supprime l'instruction : le contrôle
        # central du module disparaissait sans bruit sous un simple
        # commutateur d'exécution. (2) Levée dans la boucle sur les paires
        # sans `try`, elle tuait le processus AVANT l'écriture du JSON — et
        # la Section Risque relisait alors le fichier de la veille sans
        # savoir qu'il était périmé. Une seule paire mal calibrée effaçait
        # le travail sur toutes les autres.
        # APRÈS : vérification explicite, incompressible, qui BLOQUE la
        # paire au lieu de tuer le processus. Le contrôle garde toute sa
        # force : si la loi stationnaire ne décrit pas le spread, rien de
        # ce qui en découle n'est utilisable, et la paire est refusée.
        coherent = bool(0.75 < rapport < 1.33)
        coh["coherent"] = coherent
        if not coherent:
            coh["motif"] = (
                f"CALIBRAGE OU INCOHÉRENT : σ_N théorique {sigma_n_theorique:.6f} "
                f"vs observé {sigma_niveau:.6f} (rapport {rapport:.3f}, hors "
                f"[0,75 ; 1,33]). La loi stationnaire ne décrit pas ce spread.")
            alertes.append("CALIBRAGE_OU_INCOHERENT")
        # σ à l'horizon T d'un OU — remplace σ_j·√T (CORRECTION P3).
        sigma_horizon_ou = sigma_niveau * math.sqrt(1 - math.exp(-2 * kappa * HORIZON_SEANCES))
        coh["sigma_horizon_ou"] = sigma_horizon_ou
        coh["sigma_horizon_racine_du_temps"] = sigma_increment * math.sqrt(HORIZON_SEANCES)
        coh["facteur_surevaluation_racine_du_temps"] = (
            coh["sigma_horizon_racine_du_temps"] / sigma_horizon_ou if sigma_horizon_ou > 0 else float("nan"))

    t_adf = a_res["t"]
    return {"disponible": True, "n_obs": len(j), "n_exclues_non_positives": n_exclues,
            "debut": str(debut.date()), "fin": str(fin.date()),
            "profondeur_annees": annees,
            "echantillon_contient_stress": stress["contient_stress"],
            "marqueurs_stress": stress["marqueurs"], "alertes": alertes,
            "beta_couverture": float(beta[1]),
            "adf_t": t_adf, "adf_retards": a_res["retards"], "adf_p_max": a_res["p_max"],
            "adf_critere": a_res["critere"],
            "adf_t_aic": a_res.get("t_critere_alternatif"),
            "adf_retards_aic": a_res.get("retards_critere_alternatif"),
            "adf_t_ancien_retards_1": a_res.get("t_ancien_retards_1"),
            "cointegre_5pct": bool(np.isfinite(t_adf) and t_adf < -3.34),
            "cointegre_10pct": bool(np.isfinite(t_adf) and t_adf < -3.04),
            "demi_vie_seances": dv["demi_vie"], "demi_vie_ic95": dv["ic95"],
            "demi_vie_identifiee": dv.get("identifiee", False),
            "demi_vie_libelle": dv.get("libelle_ic",
                                       "demi-vie non identifiée (borne supérieure infinie)"),
            "demi_vie_motif_non_identifiee": dv.get("motif_non_identifiee"),
            "adf_glissant": adf_gliss,
            "z_courant": float(spread[-1] / sigma_niveau) if sigma_niveau > 0 else float("nan"),
            "spread_std": sigma_niveau, "sigma_increment": sigma_increment,
            "coherence_ou": coh,
            "serie_spread": pd.Series(spread, index=j.index),
            "log_a": pd.Series(la, index=j.index), "log_b": pd.Series(lb, index=j.index)}


# ══════════════════════════════════════════════════════════════════════════
# CORRECTION P11 — NORMALISATION CAUSALE ET TEST HORS ÉCHANTILLON
# ══════════════════════════════════════════════════════════════════════════
def z_causal(la: pd.Series, lb: pd.Series, fenetre: int = FENETRE_GLISSANTE,
             expansif: bool = False) -> pd.Series:
    """
    z estimé en FENÊTRE GLISSANTE CAUSALE — CORRECTION P11.

    AVANT : β, moyenne et σ estimés sur TOUT l'échantillon, y compris les
    observations postérieures à la date du signal. Un z dont l'écart au z
    causal a un écart-type du même ordre de grandeur que lui-même n'est pas
    un signal, c'est un signal plus du biais d'anticipation. L'écart-type
    en question est MESURÉ et imprimé par paire à chaque exécution
    (`biais_anticipation_ecart_type`) — le chiffre autrefois recopié ici
    (0,24) ne correspondait plus à aucune sortie du module.

    APRÈS : à chaque date t, β, moyenne et σ sont estimés sur les séances
    STRICTEMENT ANTÉRIEURES. Aucune information future.

    Deux variantes sont produites, parce qu'elles ne mesurent pas la même
    chose et que les confondre serait une nouvelle faute :
      · `expansif=True`  : toute l'histoire jusqu'à t−1. C'est le
        comparable direct du z plein échantillon — même information, moins
        le futur. L'écart mesure le PUR BIAIS D'ANTICIPATION.
      · `expansif=False` : fenêtre glissante de `fenetre` séances. C'est
        l'estimateur exploitable en production, qui oublie le régime
        ancien. L'écart y mélange biais d'anticipation ET changement de
        régime — il est nécessairement plus grand, et ce n'est pas une
        anomalie.
    """
    A, B = la.values, lb.values
    n = len(A)
    out = np.full(n, np.nan)
    for t in range(fenetre, n):
        deb = 0 if expansif else t - fenetre
        wa, wb = A[deb:t], B[deb:t]
        X = np.column_stack([np.ones(len(wb)), wb])
        bta, *_ = np.linalg.lstsq(X, wa, rcond=None)
        res = wa - X @ bta
        sd = res.std()
        if sd > 0:
            out[t] = (A[t] - bta[0] - bta[1] * B[t]) / sd
    return pd.Series(out, index=la.index)


def test_hors_echantillon(la: pd.Series, lb: pd.Series, taille_pct: float) -> dict:
    """
    CORRECTION P11 — calibrage sur la première moitié, mesure sur la seconde.

    La Section Quantitative a déclaré 90 essais, un Sharpe déflaté et une
    PBO. La Section Trading avait produit ZÉRO test hors échantillon sur
    une idée destinée à l'exécution. C'est le double standard de preuve du
    fonds, corrigé ici.

    Règle testée, identique à celle qui est simulée : entrée quand |z|
    franchit 1,0, cible z = 0, stop à 2,5σ au-delà de l'entrée, sortie au
    marché à J+30 si aucune barrière.
    """
    n = len(la)
    mi = n // 2
    A, B = la.values, lb.values
    X = np.column_stack([np.ones(mi), B[:mi]])
    bta, *_ = np.linalg.lstsq(X, A[:mi], rcond=None)
    res_in = A[:mi] - X @ bta
    sd = res_in.std()
    # CORRECTION F-5 — même règle qu'en plein échantillon : l'IC de la
    # demi-vie de calibrage n'est construit que si l'ADF de la période de
    # calibrage rejette la racine unitaire.
    adf_in = adf(res_in, critere="BIC")
    dv_in = demi_vie_et_ic(
        res_in, bool(np.isfinite(adf_in["t"]) and adf_in["t"] < -3.34))
    if sd <= 0:
        return {"disponible": False, "motif": "σ nul en échantillon d'entraînement"}
    s_out = (A[mi:] - bta[0] - bta[1] * B[mi:]) / sd     # z hors échantillon
    m = len(s_out)
    trades, i = [], 0
    while i < m:
        if 1.0 < abs(s_out[i]) < STOP_Z_ABSOLU:
            z0 = s_out[i]
            sens = 1.0 if z0 < 0 else -1.0
            stop = math.copysign(STOP_Z_ABSOLU, z0)
            issue, sortie_z, duree = "marche", None, HORIZON_SEANCES
            for k in range(1, HORIZON_SEANCES + 1):
                if i + k >= m:
                    duree = k - 1
                    sortie_z = s_out[i + duree] if duree >= 0 else z0
                    break
                zk = s_out[i + k]
                if (sens > 0 and zk >= CIBLE_Z) or (sens < 0 and zk <= CIBLE_Z):
                    issue, sortie_z, duree = "cible", zk, k
                    break
                if (sens > 0 and zk <= stop) or (sens < 0 and zk >= stop):
                    issue, sortie_z, duree = "stop", zk, k
                    break
            else:
                sortie_z = s_out[i + HORIZON_SEANCES] if i + HORIZON_SEANCES < m else s_out[-1]
            if sortie_z is None:
                sortie_z = s_out[min(i + duree, m - 1)]
            # P&L en % de NAV : Δz × σ (unités de spread log) × taille
            pnl = sens * (sortie_z - z0) * sd * taille_pct
            pnl -= COUT_ALLER_RETOUR_PB / 10_000.0 * taille_pct
            trades.append({"issue": issue, "z_entree": float(z0),
                           "duree": int(duree), "pnl_pct": float(pnl)})
            i += max(duree, 1)
        else:
            i += 1
    if not trades:
        return {"disponible": True, "n_trades": 0,
                "note": "aucun signal hors échantillon"}
    pnls = np.array([t["pnl_pct"] for t in trades])
    issues = [t["issue"] for t in trades]
    return {"disponible": True, "n_trades": len(trades),
            "n_obs_calibrage": mi, "n_obs_test": m,
            "demi_vie_calibrage": dv_in["demi_vie"],
            "demi_vie_calibrage_identifiee": dv_in.get("identifiee", False),
            "adf_t_calibrage": float(adf_in["t"]),
            "sigma_calibrage": float(sd),
            "n_cible": issues.count("cible"), "n_stop": issues.count("stop"),
            "n_marche": issues.count("marche"),
            "part_cible": issues.count("cible") / len(issues),
            "part_stop": issues.count("stop") / len(issues),
            "part_marche": issues.count("marche") / len(issues),
            "pnl_moyen_pct": float(pnls.mean()),
            "pnl_moyen_pb_nav": float(pnls.mean() * 100),
            "pnl_ecart_type_pct": float(pnls.std(ddof=1)) if len(pnls) > 1 else float("nan"),
            "pnl_total_pct": float(pnls.sum()),
            "part_gagnants": float((pnls > 0).mean())}


def _p_chi2(x: float, ddl: int) -> float:
    """P(χ²_ddl > x), sans SciPy. Fonction gamma incomplète régularisée
    supérieure Q(ddl/2, x/2), série et fraction continue de Lentz."""
    if not np.isfinite(x) or x < 0 or ddl <= 0:
        return float("nan")
    a, y = ddl / 2.0, x / 2.0
    if y == 0:
        return 1.0
    lg = math.lgamma(a)
    if y < a + 1.0:                                   # série pour P(a, y)
        terme, somme, n = 1.0 / a, 1.0 / a, 0
        while n < 10_000:
            n += 1
            terme *= y / (a + n)
            somme += terme
            if abs(terme) < abs(somme) * 1e-15:
                break
        return max(0.0, min(1.0, 1.0 - somme * math.exp(-y + a * math.log(y) - lg)))
    # fraction continue pour Q(a, y)
    minuscule = 1e-300
    b, c, d = y + 1.0 - a, 1.0 / minuscule, 1.0 / (y + 1.0 - a)
    h, i = d, 0
    while i < 10_000:
        i += 1
        an = -i * (i - a)
        b += 2.0
        d = an * d + b
        if abs(d) < minuscule:
            d = minuscule
        c = b + an / c
        if abs(c) < minuscule:
            c = minuscule
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < 1e-15:
            break
    return max(0.0, min(1.0, math.exp(-y + a * math.log(y) - lg) * h))


def _beta_incomplete(a: float, b: float, x: float) -> float:
    """I_x(a, b) régularisée — fraction continue de Lentz. Sans SciPy."""
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    lbeta = math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b)
    avant = math.exp(a * math.log(x) + b * math.log(1 - x) - lbeta)
    if x < (a + 1) / (a + b + 2):
        return avant * _bcf(a, b, x) / a
    return 1.0 - avant * _bcf(b, a, 1 - x) / b


def _bcf(a: float, b: float, x: float) -> float:
    minuscule = 1e-300
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c, d = 1.0, 1.0 - qab * x / qap
    if abs(d) < minuscule:
        d = minuscule
    d = 1.0 / d
    h = d
    for m in range(1, 300):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < minuscule:
            d = minuscule
        c = 1.0 + aa / c
        if abs(c) < minuscule:
            c = minuscule
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < minuscule:
            d = minuscule
        c = 1.0 + aa / c
        if abs(c) < minuscule:
            c = minuscule
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < 1e-14:
            break
    return h


def _p_student_bilaterale(t: float, ddl: int) -> float:
    """P(|T_ddl| > |t|)."""
    if not np.isfinite(t) or ddl <= 0:
        return float("nan")
    return _beta_incomplete(ddl / 2.0, 0.5, ddl / (ddl + t * t))


def _p_binomiale_exacte_bilaterale(k: int, n: int, p: float) -> float:
    """
    Test binomial EXACT bilatéral (méthode de la densité : somme des
    probabilités des issues au plus aussi vraisemblables que l'observée).
    Aucune approximation asymptotique : valable quel que soit l'effectif
    attendu — c'est précisément ce que le χ² ne garantit pas ici, où
    l'effectif attendu d'une cellule tombe sous 5.
    """
    if not (0 <= k <= n) or not (0.0 < p < 1.0) or n <= 0:
        return float("nan")
    def logp(i: int) -> float:
        return (math.lgamma(n + 1) - math.lgamma(i + 1) - math.lgamma(n - i + 1)
                + i * math.log(p) + (n - i) * math.log1p(-p))
    seuil = logp(k) + 1e-9
    total = 0.0
    for i in range(n + 1):
        li = logp(i)
        if li <= seuil:
            total += math.exp(li)
    return max(0.0, min(1.0, total))


def _p_multinomiale_exacte(obs: list[int], p: list[float]) -> float:
    """
    Test multinomial EXACT à trois cellules, par énumération (méthode de la
    densité : somme des probabilités de TOUTES les issues au plus aussi
    vraisemblables que l'observée).

    Pourquoi exact et non χ² : ici l'effectif ATTENDU d'une cellule tombe
    sous 5 — parfois sous 1 — et l'approximation asymptotique du χ² n'y a
    plus aucune validité. Le nombre d'issues à énumérer vaut (n+1)(n+2)/2,
    soit quelques centaines : le calcul exact est immédiat, il n'y a aucune
    raison de lui préférer une approximation invalide.
    """
    n = int(sum(obs))
    if n <= 0 or len(obs) != 3 or len(p) != 3:
        return float("nan")
    q = [max(v, 1e-15) for v in p]
    s = sum(q)
    q = [v / s for v in q]
    lq = [math.log(v) for v in q]
    lfac = [math.lgamma(i + 1) for i in range(n + 1)]
    ln_fac_n = lfac[n]

    def lp(v: list[int]) -> float:
        return ln_fac_n - sum(lfac[i] for i in v) + sum(i * l for i, l in zip(v, lq))

    seuil = lp(list(obs)) + 1e-9
    total = 0.0
    for i in range(n + 1):
        for j in range(n - i + 1):
            l = lp([i, j, n - i - j])
            if l <= seuil:
                total += math.exp(l)
    return max(0.0, min(1.0, total))


def confronter_hors_echantillon(hors: dict, sim: dict) -> dict:
    """
    CORRECTION F-6 — LE TEST HORS ÉCHANTILLON DEVIENT OPPOSABLE.

    Il existait, il était propre, et il n'alimentait rien : le module
    publiait « cible 29 % / stop 61 % » à côté d'un modèle qui prédisait
    « cible 82 % / stop 6 % » sans qu'aucun critère ne s'en aperçoive.
    Un test dont aucun verdict ne dépend n'est pas une preuve, c'est un
    ornement.

    DEUX tests, DÉCLARÉS EX ANTE, portant sur deux prédictions distinctes
    du modèle — on ne choisit pas le test après avoir vu le résultat :
      · la FRÉQUENCE des trois issues : test multinomial EXACT (cible /
        stop / marché) contre les trois probabilités simulées. Exact, et
        non χ², parce que l'effectif attendu d'une cellule tombe ici sous
        l'unité, ce qui prive le χ² de toute validité. Le χ² est publié
        pour mémoire, il ne tranche pas.
      · l'AMPLEUR : test de Student bilatéral sur le P&L moyen réalisé
        contre le P&L moyen prédit.
    Un test binomial exact sur le seul nombre de STOPS est publié en
    complément (l'issue qui décide du risque), sans entrer dans la règle.

    RÈGLE DE DÉCISION : deux tests déclarés ⇒ correction de BONFERRONI. Le
    modèle est réfuté si min(p) < seuil/2. C'est le contrôle correct du
    risque de première espèce familial. Prendre le min sans correction
    serait se donner deux chances de rejeter ; prendre le max reviendrait à
    laisser le test le MOINS puissant recouvrir une réfutation établie par
    l'autre — ce qui n'est pas de la prudence, c'est de la cécité.

    RÉSERVE ÉNONCÉE, NON DISSIMULÉE : les signaux hors échantillon se
    chevauchent dans le temps, donc les deux tests surestiment la
    significativité. Ils sont retenus comme tests de RUPTURE — un écart de
    cet ordre ne s'explique pas par la dépendance sérielle — et non comme
    des niveaux exacts. Le seuil global est fixé à 1 % pour cette raison.
    """
    if not hors.get("disponible") or not hors.get("n_trades"):
        return {"applicable": False,
                "motif": hors.get("note", "aucun signal hors échantillon")}
    n = int(hors["n_trades"])
    if n < HORS_ECHANTILLON_MIN_SIGNAUX:
        return {"applicable": False,
                "motif": f"{n} signaux < {HORS_ECHANTILLON_MIN_SIGNAUX} : "
                         f"le test n'a pas de puissance"}
    obs = [hors["n_cible"], hors["n_stop"], hors["n_marche"]]
    p_mod = [sim["p_cible"], sim["p_stop"], sim["p_aucune"]]
    att = [n * p for p in p_mod]
    if min(att) < 1e-9:
        return {"applicable": False, "motif": "probabilité modèle nulle"}
    chi2 = float(sum((o - a) ** 2 / a for o, a in zip(obs, att)))
    p_chi2 = _p_chi2(chi2, 2)
    # Binomial EXACT sur les stops : insensible à la petitesse des effectifs.
    p_bin = _p_binomiale_exacte_bilaterale(int(hors["n_stop"]), n, sim["p_stop"])
    # Student sur le P&L moyen réalisé contre le P&L moyen prédit.
    sd_pnl = hors.get("pnl_ecart_type_pct", float("nan"))
    if np.isfinite(sd_pnl) and sd_pnl > 0 and n > 1:
        t_pnl = ((hors["pnl_moyen_pct"] - sim["esperance_brute_pct"])
                 / (sd_pnl / math.sqrt(n)))
        p_t = _p_student_bilaterale(t_pnl, n - 1)
    else:
        t_pnl, p_t = float("nan"), float("nan")
    # Multinomial EXACT sur les trois issues : le test qui tranche la
    # FRÉQUENCE, valable quel que soit l'effectif attendu.
    p_multi = _p_multinomiale_exacte(obs, p_mod)
    # Les DEUX tests déclarés ex ante, et eux seuls, entrent dans la règle.
    tests_declares = {"multinomial_exact_trois_issues": p_multi,
                      "student_pnl_moyen": p_t}
    finis = {k: v for k, v in tests_declares.items() if np.isfinite(v)}
    seuil_bonferroni = (HORS_ECHANTILLON_SEUIL_P / len(finis)) if finis else float("nan")
    nom_retenu = min(finis, key=finis.get) if finis else None
    p_val = finis[nom_retenu] if nom_retenu else float("nan")
    return {"applicable": True,
            "n_signaux": n,
            "observe": {"cible": obs[0], "stop": obs[1], "marche": obs[2]},
            "attendu_modele": {"cible": att[0], "stop": att[1], "marche": att[2]},
            "probabilites_modele": {"cible": p_mod[0], "stop": p_mod[1],
                                    "marche": p_mod[2]},
            "p_multinomial_exact": p_multi,
            "chi2": chi2, "ddl": 2, "p_chi2": p_chi2,
            "chi2_valide": bool(min(att) >= 5.0),
            "p_binomial_exact_stops": p_bin,
            "t_pnl": t_pnl, "p_student_pnl": p_t,
            "tests_declares": tests_declares,
            "n_tests_declares": len(finis),
            "seuil_bonferroni": seuil_bonferroni,
            "test_le_plus_defavorable": nom_retenu,
            "p_valeur": p_val,
            "regle_de_selection": (
                "deux tests DÉCLARÉS EX ANTE (fréquence des issues : "
                "multinomial exact ; amplitude : Student sur le P&L moyen). "
                "Réfutation si min(p) < seuil/2 (Bonferroni). Le χ² et le "
                "binomial sur les stops sont publiés mais ne tranchent pas."),
            "seuil_p": HORS_ECHANTILLON_SEUIL_P,
            "modele_refute": bool(np.isfinite(p_val) and p_val < seuil_bonferroni),
            "pnl_moyen_hors_echantillon_pb": hors["pnl_moyen_pb_nav"],
            "pnl_moyen_predit_pb": float(sim["esperance_brute_pct"] * 100),
            "effectif_attendu_min": float(min(att)),
            "reserve": ("signaux chevauchants ET effectif attendu minimal de "
                        f"{min(att):.1f} : p-valeurs indicatives, retenues comme "
                        "test de RUPTURE et non comme niveaux exacts")}


# ══════════════════════════════════════════════════════════════════════════
# PREMIER PASSAGE À DEUX BARRIÈRES, HORIZON FINI
# ══════════════════════════════════════════════════════════════════════════
def proba_deux_barrieres_horizon_infini(cible: float, stop: float, derive: float = 0.0) -> dict:
    """
    Ruine du joueur, HORIZON INFINI. [FORMULE VALIDÉE PAR L'AUDIT 008]

        P(toucher +a avant −b) = b / (a + b)          (sans dérive)
        P = (1 − e^(2μb/σ²)) / (e^(−2μa/σ²) − e^(2μb/σ²))   (avec dérive)

    LA FORMULE EST EXACTE ET N'EST PAS TOUCHÉE. Ce qui était faux était son
    EMPLOI : elle répond à « laquelle des deux barrières en premier, si
    l'une des deux finit par être touchée », et non à « laquelle en
    30 séances ». Elle pose P(aucune barrière) = 0 par construction, alors
    que la simulation à horizon fini mesure une masse non nulle sur cet
    état. CORRECTION F-7 : la valeur de cette masse n'est plus recopiée ici
    (elle l'était depuis un arrêté antérieur, sur une paire, à la maille
    journalière — et elle est fausse à la maille retenue aujourd'hui) ;
    `p_aucune` est publiée par paire à chaque exécution.

    Elle n'est donc plus utilisée pour décider. Elle reste ici comme
    CONTRÔLE : la simulation à horizon fini doit converger vers elle quand
    T → ∞. [CORRECTION P2]

    REDÉCOUVERTE, PAS DÉCOUVERTE — CORRECTION P16.
    « Sans dérive, pour tout couple (cible, stop), l'espérance est
    exactement nulle » est le THÉORÈME D'ARRÊT OPTIONNEL DE DOOB (1953)
    appliqué à une martingale bornée. Le résultat est juste et sa
    démonstration est bonne ; l'appeler « la découverte du module » était
    une surdéclaration.

    CONVENTION LOGARITHMIQUE — CORRECTION P16, ressaisie F-7.
    Le « ratio 1,00 exactement » d'une position linéaire ne tient qu'en
    unités LOGARITHMIQUES : en unités de prix, ±d en log donne
    (e^d − 1) / (1 − e^(−d)) ≠ 1. La conversion n'est plus illustrée ici
    par un couple de pourcentages recopié à la main sur une paire ; elle
    est RECALCULÉE sur le σ mesuré de chaque paire retenue et imprimée en
    conclusion. La convention log est défendable pour un pair trade (elle
    rend la couverture β linéaire), mais une conclusion doctrinale
    d'exclusion structurelle ne peut pas être bâtie dessus sans que la
    convention soit énoncée. Elle l'est ici, et chiffrée à l'exécution.
    """
    a, b = abs(cible), abs(stop)
    if a <= 0 or b <= 0:
        return {"disponible": False}
    if abs(derive) < 1e-9:
        p_cible = b / (a + b)
    else:
        m = 2 * derive
        try:
            p_cible = (1 - math.exp(m * b)) / (math.exp(-m * a) - math.exp(m * b))
        except OverflowError:
            p_cible = 1.0 if derive > 0 else 0.0
    p_cible = min(max(p_cible, 0.0), 1.0)
    return {"disponible": True, "p_cible": p_cible, "p_stop": 1 - p_cible,
            "methode": "ruine du joueur, HORIZON INFINI — contrôle uniquement"}


def simuler_barrieres(z0: float, sigma_niveau: float, demi_vie: float,
                      taille_pct: float, cible_z: float = CIBLE_Z,
                      stop_z_absolu: float = STOP_Z_ABSOLU,
                      horizon: int = HORIZON_SEANCES,
                      n: int = N_TRAJECTOIRES,
                      graine: int = GRAINE_SIMULATION,
                      sous_pas: int = SOUS_PAS_PAR_SEANCE) -> dict:
    """
    Premier passage à DEUX BARRIÈRES et HORIZON FINI — CORRECTIONS P1, P2, P3, P10.

    ── P1 : UNE SEULE UNITÉ ────────────────────────────────────────────
    [CE PARAGRAPHE EST UN RELEVÉ HISTORIQUE, DATÉ. Les chiffres qui suivent
    décrivent UNE paire (HY/IG) à UN arrêté (14/08/2026) sous l'ancienne
    maille journalière. Ils ne sont pas un résultat général et ne doivent
    pas être relus comme tel — F-7.]
    L'ancienne version mélangeait deux écarts-types dans la même formule :
    z était normalisé par σ_N = 0,039492 (écart-type du NIVEAU) tandis que
    les barrières étaient exprimées en multiples de σ_H = σ_j·√30 =
    0,080713 (écart-type de la VARIATION). Rapport 2,0438. Conséquence
    géométrique : la « cible à +2σ » exigeait que le spread passe de
    z = −0,98 à z = +3,11, soit 4,1 écarts-types du NIVEAU d'un processus
    STATIONNAIRE DE MOYENNE NULLE. P(cible) publiée 0,8262, vraie 0,0025 :
    facteur d'erreur 330.

    POURQUOI UNE CIBLE « +2σ » N'A AUCUN SENS ICI. Un spread cointégré est
    stationnaire : sa loi limite est centrée sur zéro avec un écart-type
    σ_N. Demander +2σ_N à partir de −1σ_N, c'est demander un déplacement
    de 3σ_N — non pas dans le sens du retour à la moyenne, mais À TRAVERS
    la moyenne et bien au-delà, contre la force de rappel qui devient
    répulsive dès que le spread a franchi zéro. Le moteur du gain (le
    rappel −κx) devient l'adversaire du gain au-delà de la moyenne.
    LA DISTANCE QUE LE RAPPEL TRAVAILLE À PARCOURIR EST |z₀| : toute cible
    au-delà de zéro est un pari directionnel gratuit greffé sur un pari de
    retour à la moyenne.

    CE QUE CETTE PHRASE N'IMPLIQUE PAS — CORRECTION F-7. Elle a été lue,
    au critère 1, comme une borne sur le RATIO gain/perte. C'est faux.
    |z₀| borne la distance parcourue par la dérive, elle ne borne pas le
    rapport des deux branches : le stop est ABSOLU (z = ±2,5) et la cible
    est FIXE (z = 0), donc éloigner l'entrée allonge la branche de gain
    (|z₀|) ET raccourcit la branche de perte (2,5 − |z₀|). Le ratio vaut
    approximativement |z₀|/(2,5 − |z₀|) et franchit 2:1 dès |z₀| ≈ 1,71,
    sans toucher à aucune constante de doctrine — et l'espérance y est
    MAXIMALE, non détruite. Voir `table_franchissement_critere1`, calculée
    à chaque exécution.

    Les barrières sont donc fixées EN z ABSOLU, dans l'unique unité σ_N :
      · cible : z = 0 — la moyenne, c'est là que le retour va ;
      · stop  : z = ±2,5 (BORNE ABSOLUE du même côté que l'entrée) — un
        niveau que la loi stationnaire rend rare (masse au-delà :
        erfc(2,5/√2) sous la loi normale, calculée et imprimée en tête
        d'exécution, jamais recopiée) et qui constitue une vraie
        réfutation du retour à la moyenne :
        si le spread atteint 2,5σ, ce n'est plus un écart, c'est une
        rupture de relation.
    Conséquence : |z₀| doit être strictement inférieur à 2,5, sans quoi
    l'entrée est déjà au-delà de son propre stop et l'idée est refusée.

    ── P3 : PAS DE RACINE DU TEMPS ─────────────────────────────────────
    La dynamique simulée est celle d'un Ornstein-Uhlenbeck, la même que
    celle qui produit l'espérance. Transition EXACTE :
        x_{t+1} = x_t·e^(−κ) + σ_N·√(1 − e^(−2κ))·ε
    Aucun σ_j·√T n'apparaît. Postuler un OU pour l'espérance et une marche
    aléatoire pour le risque était une contradiction interne frontale.

    ── P2 : TROIS ÉTATS DE SORTIE, SOMME = 1 SANS NORMALISATION ────────
    cible / stop / marquage au marché à J+T. L'assertion est écrite.
    L'ancienne version posait P(aucune) = 0, exactement la faute qu'elle
    reprochait par écrit à la version antérieure. Troisième récidive
    évitée.

    ── P10 : SORTIE AU COURS EFFECTIVEMENT FRANCHI ─────────────────────
    Un stop touché en clôture est touché AU-DELÀ du niveau. Le P&L est
    calculé sur x au pas de franchissement, pas sur le niveau de barrière.

    ── F-2 : LA MAILLE N'EST PLUS JOURNALIÈRE ──────────────────────────
    Les barrières étaient testées une fois par séance. Une trajectoire qui
    franchit le stop en séance et referme du bon côté n'était pas comptée :
    le biais est SYSTÉMATIQUE et D'UN SEUL CÔTÉ — P(stop) sous-estimée,
    espérance surévaluée. Mesuré au pas journalier : P(stop) −42 % sur
    HY/IG et −33 % sur Brent, espérance +26 % et +58 %.
    La séance est donc subdivisée en `sous_pas` incréments d'OU EXACTS —
    la transition reste exacte à tout pas dt, seule la fréquence
    d'observation des barrières change. L'erreur résiduelle d'un schéma à
    barrières discrètes décroît en O(1/√m) ; elle est mesurée par
    extrapolation de Richardson en 1/√m et PUBLIÉE, pas postulée.

    ── F-4 : LE DÉPASSEMENT EST BILATÉRAL, LA PUBLICATION L'EST AUSSI ──
    Le franchissement en temps discret dépasse la barrière DES DEUX CÔTÉS :
    la sortie à la cible se fait au-delà de la cible (gain gonflé) autant
    que la sortie au stop se fait au-delà du stop (perte gonflée). Seul le
    dépassement du STOP était publié, alors que celui de la CIBLE est plus
    grand en proportion. Publier une moitié d'un biais bilatéral donne au
    lecteur l'impression d'une prudence qui n'existe pas. Les DEUX
    dépassements sont désormais publiés.
    """
    if not (np.isfinite(demi_vie) and demi_vie > 0 and sigma_niveau > 0):
        return {"disponible": False, "motif": "demi-vie ou σ non exploitables"}
    if abs(z0) >= stop_z_absolu:
        return {"disponible": False,
                "motif": f"entrée à z = {z0:+.2f}, déjà au-delà du stop "
                         f"±{stop_z_absolu:.1f}σ — pas de position possible"}
    if abs(z0 - cible_z) < 1e-9:
        return {"disponible": False, "motif": "entrée confondue avec la cible"}
    sous_pas = max(1, int(sous_pas))
    kappa = math.log(2) / demi_vie
    dt = 1.0 / sous_pas
    phi = math.exp(-kappa * dt)
    sd_pas = sigma_niveau * math.sqrt(1 - math.exp(-2 * kappa * dt))

    sens = 1.0 if z0 < 0 else -1.0      # long_spread si z < 0
    x0 = z0 * sigma_niveau
    niveau_cible = cible_z * sigma_niveau
    z_stop = math.copysign(stop_z_absolu, z0)   # même côté que l'entrée
    niveau_stop = z_stop * sigma_niveau

    rng = np.random.default_rng(graine)
    x = np.full(n, x0)
    etat = np.zeros(n, np.int8)          # 0 vivant, 1 cible, 2 stop
    sortie = np.full(n, np.nan)
    for _ in range(horizon * sous_pas):
        x = x * phi + sd_pas * rng.standard_normal(n)
        vivant = etat == 0
        if sens > 0:
            touche_c = vivant & (x >= niveau_cible)
        else:
            touche_c = vivant & (x <= niveau_cible)
        etat[touche_c] = 1; sortie[touche_c] = x[touche_c]
        vivant = etat == 0
        if sens > 0:
            touche_s = vivant & (x <= niveau_stop)
        else:
            touche_s = vivant & (x >= niveau_stop)
        etat[touche_s] = 2; sortie[touche_s] = x[touche_s]
    vivant = etat == 0
    sortie[vivant] = x[vivant]           # marquage au marché à J+T

    p_cible = float((etat == 1).mean())
    p_stop = float((etat == 2).mean())
    p_aucune = float(vivant.mean())
    # CORRECTION P2 — trois états, somme = 1 SANS normalisation.
    # CORRECTION F-9 — c'était un `assert` : supprimé par `python3 -O`, et
    # fatal au processus entier s'il se déclenchait. Vérification explicite,
    # incompressible, qui remonte une exception NOMMÉE, capturée paire par
    # paire dans la boucle principale. Le contrôle reste éliminatoire pour
    # la paire ; il ne détruit plus le travail des autres ni le fichier.
    ecart_somme = abs(p_cible + p_stop + p_aucune - 1.0)
    if ecart_somme >= 1e-12:
        raise ControleInterneRompu(
            f"états de sortie non exhaustifs : {p_cible}+{p_stop}+{p_aucune} "
            f"(écart {ecart_somme:.3e})")

    pnl = sens * (sortie - x0) * taille_pct          # % de NAV
    esperance_brute = float(pnl.mean())
    perte_au_stop = float(pnl[etat == 2].mean()) if p_stop > 0 else 0.0
    gain_a_la_cible = float(pnl[etat == 1].mean()) if p_cible > 0 else 0.0
    pnl_marche = float(pnl[vivant].mean()) if p_aucune > 0 else 0.0

    # Nominaux (aux niveaux de barrière), pour mesurer le dépassement P10.
    # CORRECTION F-4 : LES DEUX dépassements sont calculés et publiés.
    gain_nominal = abs(cible_z - z0) * sigma_niveau * taille_pct
    perte_nominale = -abs(z_stop - z0) * sigma_niveau * taille_pct
    depassement = (perte_au_stop / perte_nominale - 1.0) if perte_nominale < 0 and p_stop > 0 else 0.0
    depassement_cible = (gain_a_la_cible / gain_nominal - 1.0) if gain_nominal > 0 and p_cible > 0 else 0.0
    # Effet NET des deux dépassements sur le ratio publié au critère 1 :
    # un ratio gonflé du côté favorable et du côté défavorable ne se
    # compense pas, il se compose.
    ratio_nominal = abs(gain_nominal / perte_nominale) if perte_nominale < 0 else float("inf")
    ratio_franchi = (abs(gain_a_la_cible / perte_au_stop)
                     if (p_stop > 0 and perte_au_stop < 0 and p_cible > 0) else float("nan"))
    biais_ratio = (ratio_franchi / ratio_nominal - 1.0
                   if np.isfinite(ratio_franchi) and ratio_nominal > 0 else float("nan"))

    # Contrôle : la formule horizon infini, sur les mêmes barrières
    ctrl = proba_deux_barrieres_horizon_infini(abs(cible_z - z0), abs(z_stop - z0))

    return {"disponible": True, "sens": "long_spread" if sens > 0 else "short_spread",
            "cible_z": cible_z, "stop_z": z_stop, "z_entree": z0,
            "kappa": kappa, "sigma_niveau": sigma_niveau,
            "p_cible": p_cible, "p_stop": p_stop, "p_aucune": p_aucune,
            "esperance_brute_pct": esperance_brute,
            "gain_a_la_cible_pct": gain_a_la_cible,
            "perte_au_stop_pct": perte_au_stop,
            "pnl_marquage_marche_pct": pnl_marche,
            "gain_nominal_pct": gain_nominal, "perte_nominale_pct": perte_nominale,
            # CORRECTION F-4 — publication BILATÉRALE du dépassement.
            "depassement_du_stop": depassement,
            "depassement_de_la_cible": depassement_cible,
            "ratio_aux_niveaux_nominaux": ratio_nominal,
            "ratio_aux_cours_franchis": ratio_franchi,
            "biais_de_discretisation_sur_le_ratio": biais_ratio,
            "sous_pas_par_seance": sous_pas,
            "ecart_type_pnl_pct": float(pnl.std()),
            # CORRECTION P5 — erreur type de Monte-Carlo sur l'espérance.
            # L'ancien critère 7 tranchait sur 6,939e−18, une valeur dont le
            # SIGNE dépendait de l'ordre d'addition. Publier l'erreur type
            # rend visible si la marge est un résultat ou du bruit.
            "esperance_erreur_type_mc": float(pnl.std() / math.sqrt(n)),
            "n_trajectoires": n, "graine": graine,
            "controle_horizon_infini_p_cible": ctrl.get("p_cible"),
            "methode": (f"Ornstein-Uhlenbeck exact, deux barrières, horizon fini "
                        f"{horizon} séances × {sous_pas} sous-pas, sortie au cours "
                        f"franchi")}


# ══════════════════════════════════════════════════════════════════════════
# CORRECTION F-2 / F-4 / F-7 — TABLES CALCULÉES, PLUS AUCUNE TABLE SAISIE
# ══════════════════════════════════════════════════════════════════════════
def convergence_discretisation(z0: float, sigma_niveau: float, demi_vie: float,
                               taille_pct: float, cout_pct: float,
                               m_grossier: int = 1,
                               m_fin: int = SOUS_PAS_PAR_SEANCE,
                               n: int = N_TRAJECTOIRES_EXPLORATION) -> dict:
    """
    CORRECTION F-2 — LE BIAIS DE DISCRÉTISATION EST MESURÉ, PAS SUPPOSÉ.

    Deux simulations, même graine, même dynamique, deux fréquences
    d'observation des barrières. L'erreur d'un schéma à barrières discrètes
    est en O(1/√m) : f(m) = f(∞) + c/√m. Deux points suffisent donc à
    extrapoler f(∞) (Richardson en 1/√m) :
        f(∞) = [f(m_fin) − f(m_grossier)·√(m_grossier/m_fin)]
               / [1 − √(m_grossier/m_fin)]
    Le résidu |f(m_fin) − f(∞)| est l'erreur qui subsiste à la maille
    retenue. Il est publié. C'est LUI, et non l'erreur type de Monte-Carlo,
    qui mesure ce que la simulation ignore.
    """
    out = {"applicable": False}
    a = simuler_barrieres(z0, sigma_niveau, demi_vie, taille_pct,
                          n=n, sous_pas=m_grossier)
    b = simuler_barrieres(z0, sigma_niveau, demi_vie, taille_pct,
                          n=n, sous_pas=m_fin)
    if not (a.get("disponible") and b.get("disponible")):
        return out
    r = math.sqrt(m_grossier / m_fin)

    def extrap(va: float, vb: float) -> float:
        return (vb - va * r) / (1.0 - r)

    e_inf = extrap(a["esperance_brute_pct"], b["esperance_brute_pct"])
    p_inf = extrap(a["p_stop"], b["p_stop"])
    ra = abs(a["gain_a_la_cible_pct"] / a["perte_au_stop_pct"]) if a["perte_au_stop_pct"] < 0 else float("nan")
    rb = abs(b["gain_a_la_cible_pct"] / b["perte_au_stop_pct"]) if b["perte_au_stop_pct"] < 0 else float("nan")
    r_inf = extrap(ra, rb) if np.isfinite(ra) and np.isfinite(rb) else float("nan")
    return {"applicable": True, "n_trajectoires": n,
            "m_grossier": m_grossier, "m_retenu": m_fin,
            "p_stop": {"m_grossier": a["p_stop"], "m_retenu": b["p_stop"],
                       "extrapole_infini": p_inf,
                       "sous_estimation_au_pas_journalier_pct":
                           (a["p_stop"] / p_inf - 1.0) * 100 if p_inf > 0 else float("nan")},
            "ratio": {"m_grossier": ra, "m_retenu": rb, "extrapole_infini": r_inf},
            "esperance_brute_pb": {"m_grossier": a["esperance_brute_pct"] * 100,
                                   "m_retenu": b["esperance_brute_pct"] * 100,
                                   "extrapole_infini": e_inf * 100,
                                   "surevaluation_au_pas_journalier_pct":
                                       (a["esperance_brute_pct"] / e_inf - 1.0) * 100
                                       if e_inf != 0 else float("nan")},
            "residu_a_la_maille_retenue_pb": abs(b["esperance_brute_pct"] - e_inf) * 100,
            "esperance_nette_extrapolee_pb": (e_inf - cout_pct) * 100,
            "note": ("extrapolation de Richardson en 1/√m entre m=%d et m=%d ; "
                     "grille réduite à %d trajectoires, déclarée"
                     % (m_grossier, m_fin, n))}


def esperance_sur_ic_kappa(z0: float, sigma_niveau: float, dv_ic: list,
                           taille_pct: float, cout_pct: float,
                           n: int = N_TRAJECTOIRES) -> dict:
    """
    CORRECTION F-4 — L'INCERTITUDE QUI COMPTE EST CELLE DE κ, PAS CELLE DU
    GÉNÉRATEUR ALÉATOIRE.

    Le module publiait « la marge nette vaut 325,3 erreurs types ». Cette
    marge mesure le bruit de Monte-Carlo, c'est-à-dire la reproductibilité
    du tirage — une quantité que l'on rend arbitrairement petite en
    augmentant `n`. Elle ne dit RIEN de la fiabilité du résultat. Mise en
    regard des incertitudes réelles, elle était trompeuse :
      · discrétisation      ≈  70 erreurs types de Monte-Carlo ;
      · incertitude sur κ   ≈ 131 erreurs types de Monte-Carlo.
    Autrement dit, le chiffre publié était deux ordres de grandeur au-dessus
    de la précision effective du résultat, et il était publié SEUL.

    Ce qui est publié désormais : l'espérance nette AUX DEUX BORNES de l'IC
    à 95 % de la demi-vie que le module publie lui-même. Si le signe de
    l'espérance n'est pas stable sur cet intervalle, l'espérance n'est pas
    un résultat.
    """
    if not (isinstance(dv_ic, (list, tuple)) and len(dv_ic) == 2):
        return {"applicable": False, "motif": "IC de la demi-vie indisponible"}
    lo, hi = dv_ic
    if lo is None or hi is None or not (np.isfinite(lo) and np.isfinite(hi)) or lo <= 0:
        return {"applicable": False,
                "motif": "demi-vie non identifiée : borne supérieure infinie, "
                         "κ non borné par le bas"}
    points = {}
    for etiquette, h in (("demi_vie_basse_kappa_haut", lo),
                         ("demi_vie_haute_kappa_bas", hi)):
        s = simuler_barrieres(z0, sigma_niveau, h, taille_pct, n=n)
        if not s.get("disponible"):
            return {"applicable": False, "motif": s.get("motif")}
        points[etiquette] = {
            "demi_vie": h, "kappa": math.log(2) / h,
            "p_cible": s["p_cible"], "p_stop": s["p_stop"],
            "esperance_brute_pb": s["esperance_brute_pct"] * 100,
            "esperance_nette_pb": (s["esperance_brute_pct"] - cout_pct) * 100,
            "ratio": (abs(s["gain_a_la_cible_pct"] / s["perte_au_stop_pct"])
                      if s["perte_au_stop_pct"] < 0 else float("nan"))}
    nettes = [p["esperance_nette_pb"] for p in points.values()]
    return {"applicable": True, "ic95_demi_vie": [lo, hi],
            "ic_kappa": [math.log(2) / hi, math.log(2) / lo],
            "points": points,
            "esperance_nette_min_pb": min(nettes),
            "esperance_nette_max_pb": max(nettes),
            "signe_stable_sur_ic": bool(min(nettes) > 0 or max(nettes) < 0),
            "positive_sur_tout_ic": bool(min(nettes) > 0)}


def table_franchissement_critere1(sigma_niveau: float, demi_vie: float,
                                  taille_pct: float, cout_pct: float,
                                  z_observe: float,
                                  ratio_minimum: float = RATIO_MINIMUM,
                                  stop_z: float = STOP_Z_ABSOLU,
                                  cible_z: float = CIBLE_Z,
                                  n: int = N_TRAJECTOIRES_EXPLORATION) -> dict:
    """
    CORRECTION F-7 — LA TABLE DE FRANCHISSEMENT DU CRITÈRE 1, CALCULÉE.

    Le critère 1 portait la phrase suivante, écrite à la main :
      « Sur un spread stationnaire l'énergie du signal est bornée par |z₀| :
        ce ratio ne peut franchir 2:1 que si le stop est placé plus près que
        la cible, ce qui détruit l'espérance (Doob). »
    ELLE EST FAUSSE, et le simulateur de ce module la réfute. À CONSTANTES
    DE DOCTRINE INCHANGÉES (cible z = 0, stop z = ±2,5), en ne faisant
    varier que le seul terme que le moteur ne choisit pas — le z OBSERVÉ —
    le ratio vaut approximativement |z₀| / (stop − |z₀|) et franchit 2:1
    à |z₀| = 2·stop/3 = 1,67 (sans dépassement), soit ≈ 1,71 en discret.
    L'espérance n'y est pas détruite : elle y est MAXIMALE. Avec un stop
    ABSOLU et une cible FIXE, éloigner l'entrée allonge la branche de gain
    ET raccourcit la branche de perte : les deux effets vont dans le même
    sens.

    Conséquence doctrinale, celle-là mesurée : les critères 1 et 7 ne sont
    PAS antagonistes. Leur zone de compatibilité est la zone d'espérance
    maximale. Le refus du jour porte sur le z observé, pas sur la classe
    des pair trades.

    Cette fonction produit, pour chaque paire : la grille (z, ratio,
    P(cible), espérance nette), le |z| minimal qui ferait passer le critère
    1 (bissection sur le ratio simulé), l'espérance à ce point, et l'argmax
    de l'espérance nette sur la grille.
    """
    if not (np.isfinite(demi_vie) and demi_vie > 0 and sigma_niveau > 0):
        return {"applicable": False, "motif": "demi-vie ou σ non exploitables"}
    sens_z = -1.0 if z_observe < 0 else 1.0     # on explore du côté observé

    def mesure(absz: float) -> dict | None:
        s = simuler_barrieres(sens_z * absz, sigma_niveau, demi_vie, taille_pct, n=n)
        if not s.get("disponible") or s["p_stop"] <= 0 or s["perte_au_stop_pct"] >= 0:
            return None
        return {"z": sens_z * absz,
                "ratio": abs(s["gain_a_la_cible_pct"] / s["perte_au_stop_pct"]),
                "p_cible": s["p_cible"], "p_stop": s["p_stop"],
                "esperance_nette_pb": (s["esperance_brute_pct"] - cout_pct) * 100}

    z_analytique = ratio_minimum * abs(stop_z - cible_z) / (1.0 + ratio_minimum)
    grille_abs = sorted({round(v, 4) for v in
                         [abs(z_observe), 1.25, 1.50, z_analytique, 1.75,
                          2.00, 2.20, 2.40]
                         if 0.05 < v < stop_z - 0.02})
    lignes = [l for l in (mesure(v) for v in grille_abs) if l]
    if not lignes:
        return {"applicable": False, "motif": "aucune ligne exploitable"}

    # Bissection sur |z| : plus petit |z| dont le ratio simulé atteint le seuil.
    lo, hi = 0.05, stop_z - 0.02
    r_lo, r_hi = mesure(lo), mesure(hi)
    z_franchissement = float("nan")
    ligne_franchissement = None
    if r_lo and r_hi and r_lo["ratio"] < ratio_minimum <= r_hi["ratio"]:
        for _ in range(24):
            mid = 0.5 * (lo + hi)
            r = mesure(mid)
            if r is None:
                break
            if r["ratio"] >= ratio_minimum:
                hi, ligne_franchissement = mid, r
            else:
                lo = mid
            if hi - lo < 1e-3:
                break
        z_franchissement = hi
    meilleur = max(lignes, key=lambda l: l["esperance_nette_pb"])
    ligne_observee = min(lignes, key=lambda l: abs(abs(l["z"]) - abs(z_observe)))
    return {"applicable": True, "n_trajectoires": n,
            "cible_z": cible_z, "stop_z_absolu": stop_z,
            "ratio_minimum": ratio_minimum,
            "z_observe": z_observe,
            "formule_approchee": "ratio ≈ |z₀| / (%.2f − |z₀|)" % stop_z,
            "z_franchissement_analytique": z_analytique,
            "z_franchissement_simule": z_franchissement,
            "ligne_au_franchissement": ligne_franchissement,
            "esperance_nette_au_franchissement_pb":
                (ligne_franchissement or {}).get("esperance_nette_pb", float("nan")),
            "z_esperance_maximale": meilleur["z"],
            "esperance_nette_maximale_pb": meilleur["esperance_nette_pb"],
            "esperance_nette_au_z_observe_pb": ligne_observee["esperance_nette_pb"],
            "gain_d_esperance_au_franchissement_pct":
                ((ligne_franchissement["esperance_nette_pb"]
                  / ligne_observee["esperance_nette_pb"] - 1.0) * 100
                 if ligne_franchissement and ligne_observee["esperance_nette_pb"] > 0
                 else float("nan")),
            "criteres_1_et_7_antagonistes": bool(
                ligne_franchissement is not None
                and ligne_franchissement["esperance_nette_pb"] <= 0),
            "lignes": lignes}


def table_sensibilite_stop(z0: float, sigma_niveau: float, demi_vie: float,
                           taille_pct: float, cout_pct: float,
                           n: int = N_TRAJECTOIRES_EXPLORATION) -> list[dict]:
    """
    CORRECTION F-7 — la table de sensibilité au stop, autrefois recopiée à
    la main dans un commentaire à partir d'un seul cas, est RECALCULÉE.
    Elle documente ce que coûterait le desserrage du seul paramètre libre
    de la structure. Elle ne décide de rien : STOP_Z_ABSOLU reste une
    constante de doctrine.
    """
    out = []
    for sz in (2.50, 2.00, 1.50, 1.35, 1.10):
        if abs(z0) >= sz:
            continue
        s = simuler_barrieres(z0, sigma_niveau, demi_vie, taille_pct,
                              stop_z_absolu=sz, n=n)
        if not s.get("disponible") or s["perte_au_stop_pct"] >= 0:
            continue
        out.append({"stop_z": sz,
                    "ratio": abs(s["gain_a_la_cible_pct"] / s["perte_au_stop_pct"]),
                    "p_cible": s["p_cible"], "p_stop": s["p_stop"],
                    "esperance_nette_pb": (s["esperance_brute_pct"] - cout_pct) * 100})
    return out


# ══════════════════════════════════════════════════════════════════════════
# CORRECTION P4 — UNE SEULE QUALIFICATION, APPELÉE UNE SEULE FOIS
# ══════════════════════════════════════════════════════════════════════════
def qualifier(nom: str, c: dict, date_donnees: pd.Timestamp) -> dict:
    """
    UNIQUE fonction de qualification d'une idée — CORRECTION P4.

    LA STRUCTURE D'UNE POSITION NE PEUT PAS CRÉER UN CATALYSEUR.
    Ni un stop, ni une cible, ni un horizon ne produisent un fait
    observable dans le monde. Cette fonction est appelée UNE FOIS par
    paire, avant toute décision de structure, et son résultat est passé
    tel quel au portier. Le portier ne la rappelle jamais.

    AVANT : les critères 2 et 3 étaient réécrits entre les deux passages.
        passage 1 (linéaire)  : catalyseur = |z| > 1,5      → False
        passage 2 (stop/cible): catalyseur = demi-vie < 30  → True
        passage 1 : invalidation = |z| > 1,5                → False
        passage 2 : invalidation = « l'ADF est un nombre fini » → True
    Échecs passage 1 : ['1_ratio', '2_catalyseur', '3_invalidation'].
    Échecs passage 2 : []. Le seuil avait été déplacé, pas la preuve.
    L'unique idée transmise du fonds devait sa transmission à cette
    réécriture. « L'ADF est un nombre fini » est franchi par toute paire
    ayant produit un ADF.

    APRÈS : trois objets TYPÉS (CORRECTION P7), produits une seule fois,
    dont aucun n'est franchissable par une chaîne non vide.
    """
    # ── Critère 2 : catalyseur IDENTIFIÉ ET DATÉ ────────────────────────
    # Exige un datetime réel dans l'horizon. `bool('x')` valait True ;
    # « retour à la moyenne, demi-vie 10 séances » n'a pas de date.
    fin_horizon = date_donnees + timedelta(days=HORIZON_JOURS_CAL)
    catalyseur = None
    for dt, libelle in CALENDRIER_CATALYSEURS.get(nom, []):
        if date_donnees <= pd.Timestamp(dt) <= fin_horizon:
            catalyseur = {"date": pd.Timestamp(dt), "libelle": libelle}
            break
    motif_catalyseur = (
        "aucun événement daté dans l'horizon : le pipeline du fonds ne "
        "collecte que des séries FRED, il n'a AUCUNE source d'événements. "
        "Le retour à la moyenne n'est pas un catalyseur — il n'a pas de "
        "date, il a une demi-vie."
        if catalyseur is None else None)

    # ── Critère 3 : invalidation, FAIT OBSERVABLE, JAMAIS UN PRIX ───────
    # AVANT : « ADF remonte au-dessus de −3,04 sur 60 séances, OU STOP À
    # −1σ TOUCHÉ ». La seconde branche est exactement un niveau de prix —
    # c'est-à-dire précisément ce que la charte interdit. Supprimée.
    # ── CORRECTION F-6 : L'ÉNONCÉ N'EST PLUS UNE PROMESSE ───────────────
    # L'énoncé décrivait un ADF glissant que le module ne calculait NULLE
    # PART : le critère était franchi par la DESCRIPTION d'un test. Le test
    # est désormais exécuté (`adf_glissant`), sa série est publiée, et son
    # résultat est opposable au critère 8. L'invalidation n'est validée ici
    # que si la mesure existe réellement.
    invalidation = None
    ag = c.get("adf_glissant", {})
    if np.isfinite(c["adf_t"]) and ag.get("disponible"):
        invalidation = {
            "type": "test_statistique",
            "enonce": (f"l'ADF glissant sur {ag['fenetre']} séances, retards "
                       f"sélectionnés par BIC, pas de {ag['pas']} séances, "
                       f"remonte au-dessus de {ag['seuil_t']:.2f}"),
            "seuil": ag["seuil_t"], "frequence": f"tous les {ag['pas']} séances",
            "mesure_effectuee": True,
            "n_fenetres_calculees": ag["n_fenetres"],
            "fraction_franchissements_recents": ag["fraction_franchissements_recents"],
            "est_niveau_de_prix": False}

    # ── Critère 4 : pourquoi l'opportunité existe, STRUCTURE TYPÉE ──────
    # AVANT : chaîne libre, `bool(s)` accepte 'x'.
    # CORRECTION F-9 : `mecanisme_code` est tiré d'un VOCABULAIRE FERMÉ.
    # La garde précédente était `len(mecanisme) > 20` : `'x' * 21` la
    # franchissait. La phrase reste, pour être lue ; elle ne fait plus
    # passer le critère.
    pourquoi = None
    if "rendement" in nom.lower():
        pourquoi = {"mecanisme_code": "convergence_par_notation",
                    "mecanisme": "l'écart de qualité de crédit se referme parce que "
                                 "les mandats obligataires rééquilibrent par notation",
                    "obstacle": "segmentation_clientele",
                    "reference": "ICE BofA OAS, méthodologie de l'indice"}
    elif "Brent" in nom:
        pourquoi = {"mecanisme_code": "borne_par_cout_de_transport",
                    "mecanisme": "l'écart de qualité pétrolière est borné par le coût "
                                 "de transport transatlantique",
                    "obstacle": "contrainte_stockage",
                    "reference": "capacité de stockage de Cushing, EIA"}
    return {"catalyseur": catalyseur, "motif_absence_catalyseur": motif_catalyseur,
            "invalidation": invalidation, "pourquoi_existe": pourquoi}


# ══════════════════════════════════════════════════════════════════════════
# LE PORTIER — sept critères, tous mécaniques
# ══════════════════════════════════════════════════════════════════════════
def portier(nom: str, qualif: dict, sim: dict, correlations: dict[str, float],
            taille_pct: float, date_donnees: pd.Timestamp,
            coint: dict, confront: dict, ic_kappa: dict,
            franchissement: dict | None = None) -> dict:
    """
    Les sept critères de la charte Partie VI, appliqués mécaniquement,
    PLUS TROIS CRITÈRES D'OPPOSABILITÉ ajoutés par le réaudit 010.
    Aucun n'est cochable : chacun produit un nombre, une date ou un refus.

    CRITÈRES 8, 9, 10 — POURQUOI ILS EXISTENT (F-6, F-3)
      · 8 — ADF glissant. Il était PROMIS au critère 3 et n'était calculé
        nulle part. C'est le seul instrument du module capable de détecter
        une RUPTURE de relation : plein échantillon, une paire cointégrée
        puis rompue produit un dossier irréprochable.
      · 9 — test hors échantillon. Il existait, il était propre, il
        rejetait la prédiction du modèle, et il n'alimentait AUCUN verdict.
      · 10 — profondeur et présence de stress. Deux constantes de doctrine
        (`PROFONDEUR_MIN_ANNEES`, `ECHANTILLON_SANS_STRESS`) produisaient
        deux chaînes imprimées que rien ne lisait, pendant que la Section
        Risque bloquait sur exactement ces deux motifs. La section qui
        énonce une doctrine doit s'y tenir la première.

    Le portier NE QUALIFIE PAS : il reçoit `qualif`, produit une seule
    fois par `qualifier()`, et se contente de le vérifier (CORRECTION P4).

    LE PORTIER NE PEUT PAS DÉCLARER UNE IDÉE EXÉCUTABLE. Son verdict
    maximal est « TRANSMISE ». Une idée TRANSMISE sort en
    `EN_ATTENTE_VETO` ; une idée REFUSÉE sort en
    `NON_SOUMISE_REFUSEE_EN_AMONT` (CORRECTION F-8) — apposer
    « en attente de veto » sur une idée refusée produisait, en aval, un
    enregistrement de veto FAVORABLE (`veto: false, motifs: []`) sur une
    idée que cette section avait elle-même écartée.
    """
    # ── CORRECTION P6 : le coût n'est plus une constante morte ──────────
    cout_pct = COUT_ALLER_RETOUR_PB / 10_000.0 * taille_pct
    esperance_brute = sim["esperance_brute_pct"]
    esperance_nette = esperance_brute - cout_pct
    # Seuil de rentabilité : au-delà de combien de pb du notionnel l'idée meurt.
    seuil_rentabilite_pb_notionnel = (esperance_brute * 10_000.0 / taille_pct
                                      if taille_pct > 0 else float("nan"))

    gain_max = sim["gain_a_la_cible_pct"] if sim["p_cible"] > 0 else sim["gain_nominal_pct"]
    perte_max = sim["perte_au_stop_pct"] if sim["p_stop"] > 0 else sim["perte_nominale_pct"]
    ratio = abs(gain_max / perte_max) if perte_max < 0 else float("inf")

    corr_max = max(correlations.values()) if correlations else 0.0
    corr_pire = max(correlations, key=correlations.get) if correlations else None

    cat, inv, pq = qualif["catalyseur"], qualif["invalidation"], qualif["pourquoi_existe"]
    fin_horizon = date_donnees + timedelta(days=HORIZON_JOURS_CAL)
    cat_valide = bool(cat and isinstance(cat.get("date"), pd.Timestamp)
                      and date_donnees <= cat["date"] <= fin_horizon)
    inv_valide = bool(inv and inv.get("type") in TYPES_INVALIDATION_ADMIS
                      and inv.get("est_niveau_de_prix") is False)
    # CORRECTION F-9 — la garde `len(mecanisme) > 20` est fermée : le
    # mécanisme est un CODE d'un vocabulaire fermé, et la référence doit
    # exister. `'x' * 21` ne passe plus.
    pq_valide = bool(pq and pq.get("obstacle") in OBSTACLES_ARBITRAGE_ADMIS
                     and pq.get("mecanisme_code") in MECANISMES_ADMIS
                     and isinstance(pq.get("reference"), str)
                     and len(pq["reference"].strip()) > 0)

    # ── CORRECTION F-6 : critère 8, ADF glissant, RÉELLEMENT MESURÉ ─────
    ag = (coint or {}).get("adf_glissant", {}) or {}
    if ag.get("disponible"):
        frac_rec = ag["fraction_franchissements_recents"]
        adf_g_passe = bool(frac_rec <= ADF_GLISSANT_FRACTION_MAX)
        adf_g_valeur = frac_rec
        adf_g_detail = {
            "n_fenetres_total": ag["n_fenetres"],
            "n_fenetres_recentes": ag["n_fenetres_recentes"],
            "n_franchissements_recents": ag["n_franchissements_recents"],
            "fraction_franchissements_toutes_fenetres": ag["fraction_franchissements"],
            "t_glissant_min": ag["t_min"], "t_glissant_max": ag["t_max"],
            "t_glissant_dernier": ag["t_dernier"],
            "seuil_t": ag["seuil_t"], "fenetre": ag["fenetre"], "pas": ag["pas"]}
    else:
        adf_g_passe = False        # pas de mesure ⇒ pas de franchissement
        adf_g_valeur = None
        adf_g_detail = {"motif": ag.get("motif", "ADF glissant indisponible")}

    # ── CORRECTION F-6 : critère 9, hors échantillon OPPOSABLE ─────────
    if confront.get("applicable"):
        he_passe = not confront["modele_refute"]
        he_valeur = confront["p_valeur"]
    else:
        # Pas de test possible ⇒ pas de preuve hors échantillon. Le portier
        # refuse par défaut : l'absence de test n'est pas un test réussi.
        he_passe = False
        he_valeur = None

    # ── CORRECTION F-3 : critère 10, profondeur et stress OPPOSABLES ────
    annees = (coint or {}).get("profondeur_annees", float("nan"))
    a_du_stress = bool((coint or {}).get("echantillon_contient_stress", False))
    profondeur_ok = bool(np.isfinite(annees) and annees >= PROFONDEUR_MIN_ANNEES)
    stress_ok = bool(a_du_stress or not EXIGER_STRESS_DANS_ECHANTILLON)
    motifs_ech = []
    if not profondeur_ok:
        motifs_ech.append(f"PROFONDEUR_INSUFFISANTE ({annees:.2f} ans "
                          f"< {PROFONDEUR_MIN_ANNEES:.1f})")
    if not stress_ok:
        motifs_ech.append("ECHANTILLON_SANS_STRESS")

    # ── CORRECTION F-4 : le critère 7 ne se juge plus sur le bruit du
    # générateur mais sur l'IC de κ que le module publie lui-même.
    if ic_kappa.get("applicable"):
        esp_ic_min = ic_kappa["esperance_nette_min_pb"] / 100.0
        esp_ic_max = ic_kappa["esperance_nette_max_pb"] / 100.0
        esp_robuste = bool(ic_kappa["positive_sur_tout_ic"])
    else:
        # Demi-vie non identifiée ⇒ κ n'est pas borné par le bas ⇒ on ne
        # peut pas affirmer que l'espérance est positive. Refus par défaut.
        esp_ic_min = esp_ic_max = float("nan")
        esp_robuste = False
    esp_passe = bool(esperance_nette > 0.0 and esp_robuste)

    criteres = {
        # ── CORRECTION F-7 : LE THÉORÈME FAUX EST RETIRÉ ────────────────
        # RETIRÉ : « Sur un spread stationnaire l'énergie du signal est
        # bornée par |z₀| : ce ratio ne peut franchir 2:1 que si le stop
        # est placé plus près que la cible, ce qui détruit l'espérance
        # (Doob). » Cet énoncé est FAUX sur les deux membres, et le
        # simulateur de ce module le réfute. À constantes de doctrine
        # inchangées (cible z = 0, stop z = ±2,5), le seul terme que le
        # moteur ne choisit pas — le z OBSERVÉ — suffit à franchir 2:1, et
        # l'espérance y est MAXIMALE, pas détruite : le stop est ABSOLU,
        # donc éloigner l'entrée allonge la branche de gain et raccourcit
        # celle de perte. Doob dit que sans dérive l'espérance est nulle
        # pour TOUT couple de barrières ; il ne dit rien du ratio.
        # Ce qui le remplace n'est pas une phrase : c'est
        # `table_franchissement_critere1`, recalculée à chaque exécution.
        "1_ratio_asymetrie": {
            "valeur": ratio, "seuil": RATIO_MINIMUM, "passe": bool(ratio >= RATIO_MINIMUM),
            "ratio_aux_niveaux_nominaux": sim.get("ratio_aux_niveaux_nominaux"),
            "biais_de_discretisation_sur_le_ratio":
                sim.get("biais_de_discretisation_sur_le_ratio"),
            "z_franchissement_analytique": (franchissement or {}).get(
                "z_franchissement_analytique"),
            "z_franchissement_simule": (franchissement or {}).get(
                "z_franchissement_simule"),
            "esperance_nette_au_franchissement_pb": (franchissement or {}).get(
                "esperance_nette_au_franchissement_pb"),
            "z_esperance_maximale": (franchissement or {}).get("z_esperance_maximale"),
            "note": (
                "gain moyen à la cible / perte moyenne au stop, AU COURS "
                f"EFFECTIVEMENT FRANCHI (R-030). Le ratio vaut approximativement "
                f"|z₀|/({STOP_Z_ABSOLU:.2f}−|z₀|) et franchit "
                f"{RATIO_MINIMUM:.0f}:1 à |z₀| = "
                f"{RATIO_MINIMUM * STOP_Z_ABSOLU / (1 + RATIO_MINIMUM):.2f} "
                "(valeur analytique, sans dépassement de barrière) ; le point de "
                "franchissement effectivement simulé pour cette paire est publié "
                "ci-dessus. Le refus porte sur le z OBSERVÉ "
                f"({sim.get('z_entree', float('nan')):+.2f}), PAS sur la classe "
                "des pair trades : à constantes de doctrine inchangées, le "
                "critère est franchissable, et l'espérance nette y est maximale, "
                "pas détruite. Les critères 1 et 7 ne sont pas antagonistes.")},
        "2_catalyseur_date": {
            "valeur": str(cat["date"].date()) + " — " + cat["libelle"] if cat_valide else None,
            "passe": cat_valide,
            "note": "un ÉVÉNEMENT À DATE dans l'horizon de 30 séances. Un "
                    "datetime réel est exigé, pas une chaîne. "
                    + (qualif.get("motif_absence_catalyseur") or "")},
        "3_invalidation_observable": {
            "valeur": inv["enonce"] if inv else None, "passe": inv_valide,
            "note": "un FAIT observable, JAMAIS un niveau de prix. Type contrôlé "
                    "contre un vocabulaire fermé ; `est_niveau_de_prix` doit "
                    "être False."},
        "4_pourquoi_existe": {
            "valeur": pq["obstacle"] if pq else None, "passe": pq_valide,
            "note": "obstacle d'arbitrage NOMMÉ dans un vocabulaire fermé, "
                    "plus un mécanisme explicite. Pas de texte libre."},
        # CORRECTION P14 — RENOMMÉ. Le portefeuille est à 100 % de liquidités
        # avec un bêta de 0,00 : la corrélation AU PORTEFEUILLE est nulle par
        # construction. Ce critère mesurait la corrélation au marché actions
        # sous le nom de corrélation au portefeuille. Il est renommé ; il sera
        # remplacé par la vraie corrélation au portefeuille quand un
        # portefeuille existera.
        "5_correlation_marche_actions": {
            "valeur": corr_max, "seuil": CORRELATION_MAX,
            "passe": bool(corr_max < CORRELATION_MAX), "pire_paire": corr_pire,
            "note": "corrélation au MARCHÉ ACTIONS (S&P 500), et non au "
                    "portefeuille : le portefeuille est à 100 % de liquidités, "
                    "toute corrélation à lui est nulle par construction. "
                    "Critère de corrélation au portefeuille SUSPENDU jusqu'à "
                    "existence d'un portefeuille."},
        "6_taille_sous_limite": {
            "valeur": taille_pct, "seuil": TAILLE_MAX_PCT,
            "passe": bool(taille_pct <= TAILLE_MAX_PCT),
            "note": "plafond de 8 % en dur, quelle que soit la conviction"},
        # CORRECTION P5 + P6 — le critère 7 ne se décide plus au bruit de
        # virgule flottante. AVANT : `esperance > 0.0` sans tolérance, avec
        # une espérance de 6,939e−18 sur Brent/WTI dont le SIGNE dépendait de
        # l'ordre d'addition de la grille. Le critère « qui décide » rendait
        # un verdict réversible par permutation.
        # APRÈS : l'espérance est NETTE DES COÛTS, et le seuil est le coût
        # aller-retour lui-même — le seul seuil économiquement pertinent.
        # CORRECTION F-4 — la « marge de 325,3 erreurs types » est RETIRÉE.
        # Elle mesurait le bruit du générateur aléatoire, une quantité que
        # l'on rend arbitrairement petite en augmentant n. Face à elle, les
        # incertitudes réelles valaient ≈ 70 (discrétisation) et ≈ 131
        # (incertitude sur κ) erreurs types de Monte-Carlo. Ce qui est
        # publié désormais, et ce sur quoi le critère tranche, c'est
        # l'espérance nette AUX DEUX BORNES de l'IC à 95 % de la demi-vie
        # que ce module publie lui-même.
        "7_esperance_nette_positive": {
            "valeur": esperance_nette, "seuil": 0.0,
            "passe": esp_passe,
            "esperance_brute_pct": esperance_brute,
            "cout_pct": cout_pct,
            "esperance_nette_min_sur_ic_kappa_pct": esp_ic_min,
            "esperance_nette_max_sur_ic_kappa_pct": esp_ic_max,
            "ic95_demi_vie": ic_kappa.get("ic95_demi_vie"),
            "ic_kappa": ic_kappa.get("ic_kappa"),
            "positive_sur_tout_ic_kappa": esp_robuste,
            "motif_ic_indisponible": (None if ic_kappa.get("applicable")
                                      else ic_kappa.get("motif")),
            "erreur_type_mc_pct": sim.get("esperance_erreur_type_mc"),
            "seuil_rentabilite_pb_notionnel": seuil_rentabilite_pb_notionnel,
            "note": f"espérance NETTE des coûts ({COUT_ALLER_RETOUR_PB:.0f} pb "
                    f"{BASE_COUT}), exigée positive AU POINT ESTIMÉ ET AUX DEUX "
                    f"BORNES de l'IC à 95 % de la demi-vie. L'espérance est "
                    f"produite par la DÉRIVE MESURÉE (retour à la moyenne), "
                    f"jamais par le placement du stop : sans dérive, tout couple "
                    f"stop/cible donne zéro (Doob, 1953). L'erreur type de "
                    f"Monte-Carlo est publiée pour mémoire, elle ne tranche "
                    f"rien — elle mesure le générateur, pas le marché."},
        # ── CORRECTION F-6 : critère 8, BLOQUANT ────────────────────────
        "8_adf_glissant_stable": {
            "valeur": adf_g_valeur, "seuil": ADF_GLISSANT_FRACTION_MAX,
            "passe": adf_g_passe, **adf_g_detail,
            "note": (f"fraction des {ADF_GLISSANT_N_FENETRES_RECENTES} dernières "
                     f"fenêtres de {ADF_GLISSANT_FENETRE} séances (pas "
                     f"{ADF_GLISSANT_PAS}) où l'ADF, retards par BIC, REMONTE "
                     f"au-dessus de {ADF_GLISSANT_SEUIL_T:.2f}. C'est le test "
                     f"que le critère 3 promettait sans le calculer. Une "
                     f"relation qui ne tient que par intermittence n'est pas la "
                     f"condition nécessaire d'un pair trade. Absence de mesure "
                     f"= échec : le portier refuse par défaut.")},
        # ── CORRECTION F-6 : critère 9, hors échantillon OPPOSABLE ──────
        "9_hors_echantillon_non_refute": {
            "valeur": he_valeur, "seuil": HORS_ECHANTILLON_SEUIL_P,
            "passe": he_passe,
            "chi2": confront.get("chi2"), "ddl": confront.get("ddl"),
            "observe": confront.get("observe"),
            "attendu_modele": confront.get("attendu_modele"),
            "pnl_moyen_hors_echantillon_pb": confront.get("pnl_moyen_hors_echantillon_pb"),
            "pnl_moyen_predit_pb": confront.get("pnl_moyen_predit_pb"),
            "motif_non_applicable": (None if confront.get("applicable")
                                     else confront.get("motif")),
            "reserve": confront.get("reserve"),
            "note": (f"χ² de Pearson à 2 ddl entre les trois issues RÉALISÉES "
                     f"hors échantillon et les trois probabilités PRÉDITES par "
                     f"la simulation. p < {HORS_ECHANTILLON_SEUIL_P:.2f} ⇒ le "
                     f"modèle est réfuté sur des données qu'il n'a pas vues ⇒ "
                     f"refus. Le test existait déjà et n'alimentait rien. "
                     f"Absence de test = échec.")},
        # ── CORRECTION F-3 : critère 10, doctrine de profondeur OPPOSABLE
        "10_profondeur_et_stress": {
            "valeur": (f"{annees:.2f} ans · stress "
                       f"{'OUI' if a_du_stress else 'NON'}"
                       if np.isfinite(annees) else None),
            "seuil": PROFONDEUR_MIN_ANNEES,
            "passe": bool(profondeur_ok and stress_ok),
            "profondeur_annees": annees,
            "profondeur_suffisante": profondeur_ok,
            "echantillon_contient_stress": a_du_stress,
            "marqueurs_stress": (coint or {}).get("marqueurs_stress", []),
            "motifs": motifs_ech,
            "note": (f"profondeur ≥ {PROFONDEUR_MIN_ANNEES:.1f} ans ET au moins "
                     f"un épisode de stress DANS l'échantillon. Ces deux "
                     f"marqueurs existaient déjà et ne bloquaient rien : ils "
                     f"étaient imprimés dans une liste `alertes` que rien ne "
                     f"lisait, pendant que la Section Risque bloquait sur "
                     f"exactement ces deux motifs. Une demi-vie et un σ "
                     f"calibrés sur un seul régime ne décrivent pas la paire "
                     f"dans l'autre.")},
    }
    echecs = [k for k, v in criteres.items() if not v["passe"]]
    verdict = "TRANSMISE" if not echecs else "REFUSEE"
    # ── CORRECTION F-8 : DEUX STATUTS, PAS UN ───────────────────────────
    # AVANT : `statut_risque = "EN_ATTENTE_VETO"`, constante, apposée sur
    # TOUTES les idées — y compris les REFUSÉES. Conséquence en aval :
    # `apollon_risque.py` soumet au veto toute entrée portant ce statut, et
    # Brent/WTI — REFUSÉE par cette section — ressortait de `veto_risque.json`
    # avec `veto: false, motifs: []`. Un enregistrement FAVORABLE sur une
    # idée écartée. Le contrat produisait le contraire de ce qu'il énonçait.
    # APRÈS : `EN_ATTENTE_VETO` UNIQUEMENT sur ce qui est transmis. Une idée
    # refusée n'est pas soumise, donc elle n'est ni acquittée ni bloquée :
    # elle est NON SOUMISE. La règle « ce moteur ne peut pas déclarer une
    # idée exécutable » est intacte — le seul statut qui ouvre l'aval reste
    # une demande de veto, jamais une autorisation.
    statut = ("EN_ATTENTE_VETO" if verdict == "TRANSMISE"
              else "NON_SOUMISE_REFUSEE_EN_AMONT")
    return {"nom": nom, "criteres": criteres, "echecs": echecs,
            "ratio": ratio, "gain_max_pct": gain_max, "perte_max_pct": perte_max,
            "esperance_brute_pct": esperance_brute,
            "esperance_nette_pct": esperance_nette,
            "cout_pct": cout_pct,
            "seuil_rentabilite_pb_notionnel": seuil_rentabilite_pb_notionnel,
            "verdict": verdict,
            # LE MOTEUR DE TRADING N'A PAS LE DROIT DE DÉCLARER UNE IDÉE
            # EXÉCUTABLE : aucune branche ne produit autre chose que
            # « en attente de veto » ou « non soumise ».
            "statut_risque": statut}


def identifiant(nom: str, date_donnees: pd.Timestamp) -> str:
    slug = (nom.lower().replace("&", "").replace("/", "_").replace(" ", "_")
            .replace("é", "e").replace("è", "e").replace("ê", "e"))
    slug = "_".join(x for x in slug.split("_") if x)
    court = {"haut_rendement_investment_grade": "hy_ig",
             "brent_wti": "brent_wti", "sp_500_nasdaq_100": "spx_ndx",
             "10_ans_2_ans": "10a_2a", "30_ans_10_ans": "30a_10a"}.get(slug, slug[:24])
    return f"{court}_{date_donnees.strftime('%Y%m%d')}"


# ══════════════════════════════════════════════════════════════════════════
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--sortie", default=None)
    args = ap.parse_args()
    racine = Path(args.data)
    S = charger(racine)
    sortie_json = Path(args.sortie) if args.sortie else racine.parent / "trading_resultats.json"
    date_donnees = max(s.index[-1] for s in S.values())
    horodatage_execution = datetime.utcnow()

    print("=" * 78); print("APOLLON — PORTIER DE QUALITÉ TRADING · Générale Aurelius"); print("=" * 78)
    print(f"\n{len(S)} séries · données au {date_donnees.date()} · "
          f"portefeuille détenu : 100 % liquidités, bêta 0,00")
    print(f"Graine de simulation PUBLIÉE : {GRAINE_SIMULATION} · "
          f"{N_TRAJECTOIRES:,} trajectoires · "
          f"{SOUS_PAS_PAR_SEANCE} sous-pas par séance (F-2)".replace(",", " "))
    # Masse de la loi stationnaire au-delà du stop — CALCULÉE, jamais recopiée.
    masse_au_dela = math.erfc(STOP_Z_ABSOLU / math.sqrt(2.0))
    print(f"Stop de doctrine z = ±{STOP_Z_ABSOLU:.1f} · masse normale au-delà : "
          f"{100 * masse_au_dela:.2f} % (erfc, calculée)")
    print("Ce moteur ne peut PAS déclarer une idée exécutable : une idée "
          "TRANSMISE sort")
    print("en EN_ATTENTE_VETO, une idée REFUSÉE en "
          "NON_SOUMISE_REFUSEE_EN_AMONT (F-8).\n")

    PAIRES = [("DCOILBRENTEU", "DCOILWTICO", "Brent / WTI"),
              ("SP500", "NASDAQ100", "S&P 500 / Nasdaq 100"),
              ("DGS10", "DGS2", "10 ans / 2 ans"),
              ("BAMLH0A0HYM2", "BAMLC0A0CM", "Haut rendement / Investment grade"),
              ("DGS30", "DGS10", "30 ans / 10 ans")]

    print("─" * 78); print("COINTÉGRATION — condition NÉCESSAIRE d'un pair trade"); print("─" * 78)
    print("Sans cointégration, l'écart n'a aucune raison de revenir et")
    print("« retour à la moyenne » est une croyance, pas une propriété.")
    print("ADF : retards sélectionnés par BIC entre 0 et 12·(n/100)^0,25 (P9).\n")
    print(f"  {'Paire':<34}{'ADF t':>8}{'ret.':>5}{'5%':>5}{'demi-vie (IC95)':>32}"
          f"{'z':>7}{'n':>7}{'ans':>7}{'stress':>8}")
    coints = {}
    for a, b, lab in PAIRES:
        if a not in S or b not in S:
            print(f"  {lab:<34}{'série absente':>50}"); continue
        c = cointegration(S[a], S[b], S)
        if not c.get("disponible"):
            print(f"  {lab:<34}{c.get('motif', 'indispo'):>50}"); continue
        coints[lab] = c
        dv = c["demi_vie_seances"]; ic = c["demi_vie_ic95"]
        # CORRECTION F-5 — une demi-vie dont la racine unitaire n'est pas
        # rejetée n'a PAS de borne supérieure. On ne l'imprime plus comme si.
        if not np.isfinite(dv):
            sdv = "—"
        elif c["demi_vie_identifiee"]:
            sdv = f"{dv:.1f} [{ic[0]:.1f};{ic[1]:.1f}]"
        else:
            sdv = f"{dv:.1f} [{ic[0]:.1f};∞) NON IDENTIFIÉE"
        print(f"  {lab:<34}{c['adf_t']:>8.2f}{c['adf_retards']:>5}"
              f"{'OUI' if c['cointegre_5pct'] else 'non':>5}{sdv:>32}"
              f"{c['z_courant']:>7.2f}{c['n_obs']:>7}{c['profondeur_annees']:>7.2f}"
              f"{('OUI' if c['echantillon_contient_stress'] else 'NON'):>8}")
        if c["n_exclues_non_positives"]:
            print(f"  {'':<34}⚠ {c['n_exclues_non_positives']} obs non positives "
                  f"exclues (WTI négatif du 20/04/2020) — exclues ET COMPTÉES")
        for al in c["alertes"]:
            print(f"  {'':<34}⚠ {al}")
        co = c["coherence_ou"]
        if co.get("applicable"):
            print(f"  {'':<34}contrôle OU : σ_N théo {co['sigma_n_theorique']:.6f} vs "
                  f"obs {co['sigma_n_observe']:.6f} (rapport {co['rapport']:.4f}) — "
                  f"racine du temps surévaluait ×{co['facteur_surevaluation_racine_du_temps']:.3f}")
        print(f"  {'':<34}ADF à retards=1 (ancienne version) : {c['adf_t_ancien_retards_1']:+.2f} "
              f"· AIC p={c['adf_retards_aic']}/p_max={c['adf_p_max']} → {c['adf_t_aic']:+.2f} "
              f"· BIC p={c['adf_retards']}")
        if not c["demi_vie_identifiee"] and np.isfinite(c["demi_vie_seances"]):
            print(f"  {'':<34}⚠ {c['demi_vie_libelle']} — "
                  f"{c['demi_vie_motif_non_identifiee']}")
        ag = c["adf_glissant"]
        if ag.get("disponible"):
            print(f"  {'':<34}ADF GLISSANT ({ag['fenetre']} séances, pas {ag['pas']}, "
                  f"BIC) : {ag['n_fenetres']} fenêtres · t ∈ [{ag['t_min']:.2f} ; "
                  f"{ag['t_max']:.2f}] · dernier {ag['t_dernier']:.2f}")
            print(f"  {'':<34}  franchissements de {ag['seuil_t']:.2f} : "
                  f"{ag['n_franchissements']}/{ag['n_fenetres']} "
                  f"({100*ag['fraction_franchissements']:.1f} %) · "
                  f"{ag['n_franchissements_recents']}/{ag['n_fenetres_recentes']} "
                  f"récentes ({100*ag['fraction_franchissements_recents']:.1f} %)")
        else:
            print(f"  {'':<34}ADF GLISSANT : indisponible "
                  f"({ag.get('motif', 'motif absent')})")
    # ── CORRECTION F-7 : la saturation de l'AIC est COMPTÉE, plus décrite
    if coints:
        sat = [l for l, c in coints.items()
               if c["adf_retards_aic"] is not None
               and c["adf_retards_aic"] >= 0.8 * c["adf_p_max"]]
        print(f"\n  SÉLECTION DES RETARDS — l'AIC sature p_max (≥ 80 % de p_max) "
              f"sur {len(sat)} paire(s) sur {len(coints)} :")
        print(f"    {', '.join(sat) if sat else 'aucune'}")
        print(f"    Le BIC, lui, retient "
              f"{', '.join(str(c['adf_retards']) for c in coints.values())} retards "
              f"respectivement. C'est le motif du choix du BIC (P9), et il est "
              f"compté ici, pas recopié.")
    print("\n  Valeur critique Engle-Granger à 5 % : −3,34 "
          "[validée par l'audit 008, non modifiée]\n")

    retenus = [l for l, c in coints.items() if c["cointegre_5pct"]]
    print(f"  → {len(retenus)} paire(s) cointégrée(s) à 5 % : "
          f"{', '.join(retenus) if retenus else 'AUCUNE'}\n")

    # ── CORRECTION P13 : plus de branche `else` sur la condition nécessaire
    # AVANT : `for lab in (retenus or list(coints)[:2])` — si aucune paire
    # n'était cointégrée, le module passait les DEUX PREMIÈRES PAIRES DU
    # DICTIONNAIRE au portier. Une condition nécessaire qui possède une
    # branche `else` n'est pas une condition nécessaire.
    idees, resultats_detail, erreurs_paires = [], [], []
    if not retenus:
        print("─" * 78)
        print("AUCUNE PAIRE COINTÉGRÉE À 5 % — ARRÊT.")
        print("La cointégration est une condition NÉCESSAIRE. Il n'existe pas")
        print("de branche de repli : le module termine sans idée. L'absence")
        print("d'idée est le résultat normal d'un portier qui refuse par défaut.")
        print("─" * 78)
    else:
        print("─" * 78)
        print("PASSAGE AU PORTIER — DIX critères mécaniques, UN SEUL passage")
        print("─" * 78)
        print("Barrières en z ABSOLU (P1) : cible z = 0,00 (la moyenne) · "
              f"stop au niveau z = ±{STOP_Z_ABSOLU:.1f}, du côté de l'entrée.")
        print(f"Probabilités par SIMULATION Ornstein-Uhlenbeck exacte, horizon "
              f"{HORIZON_SEANCES} séances × {SOUS_PAS_PAR_SEANCE} sous-pas (P2, P3, F-2),")
        print("trois états de sortie, sortie au cours effectivement franchi (P10).")
        print("Critères 8 (ADF glissant), 9 (hors échantillon), 10 (profondeur "
              "et stress) : BLOQUANTS.\n")

        ret_sp = np.log(S["SP500"]).diff().dropna()
        for lab in retenus:
          # ── CORRECTION F-9 : ENCAPSULATION ────────────────────────────
          # Un contrôle interne rompu sur UNE paire ne doit pas détruire le
          # travail sur les autres, ni empêcher l'écriture du JSON — ce qui
          # laissait la Section Risque relire le fichier de la veille.
          try:
            c = coints[lab]
            co = c["coherence_ou"]
            if co.get("applicable") and not co.get("coherent", True):
                # Le contrôle OU garde toute sa force : la paire est écartée.
                print(f"\n  ▸ {lab} : ÉCARTÉE — {co['motif']}")
                erreurs_paires.append({"paire": lab, "type": "CALIBRAGE_OU_INCOHERENT",
                                       "motif": co["motif"]})
                continue
            spread = c["serie_spread"]
            r_spread = spread.diff().dropna()
            corr = {"S&P 500": abs(float(
                pd.concat([r_spread, ret_sp], axis=1, sort=True).dropna().corr().iloc[0, 1]))}

            # UNE SEULE qualification, UN SEUL appel (P4)
            qualif = qualifier(lab, c, date_donnees)

            sim = simuler_barrieres(c["z_courant"], c["spread_std"],
                                    c["demi_vie_seances"], taille_pct=TAILLE_PCT_NAV)
            if not sim.get("disponible"):
                print(f"  ▸ {lab} : simulation impossible ({sim.get('motif')})"); continue

            cout_pct = COUT_ALLER_RETOUR_PB / 10_000.0 * TAILLE_PCT_NAV

            # CORRECTION P11 — normalisation causale et test hors échantillon
            zc = z_causal(c["log_a"], c["log_b"], expansif=False)
            ze = z_causal(c["log_a"], c["log_b"], expansif=True)
            zp = (spread / c["spread_std"]).rename("plein")
            comm = pd.concat([zc.rename("causal"), ze.rename("expansif"), zp],
                             axis=1, sort=True).dropna()
            ecart = comm["plein"] - comm["causal"]
            ecart_exp = comm["plein"] - comm["expansif"]
            hors = test_hors_echantillon(c["log_a"], c["log_b"],
                                         taille_pct=TAILLE_PCT_NAV)
            # CORRECTION F-6 — le hors échantillon est CONFRONTÉ au modèle.
            confront = confronter_hors_echantillon(hors, sim)
            # CORRECTION F-4 — espérance sur l'IC de κ, et non erreurs types MC.
            ic_k = esperance_sur_ic_kappa(c["z_courant"], c["spread_std"],
                                          c["demi_vie_ic95"], TAILLE_PCT_NAV, cout_pct)
            # CORRECTION F-2 — biais de discrétisation MESURÉ.
            conv = convergence_discretisation(c["z_courant"], c["spread_std"],
                                              c["demi_vie_seances"],
                                              TAILLE_PCT_NAV, cout_pct)
            # CORRECTION F-7 — table de franchissement du critère 1, CALCULÉE.
            franch = table_franchissement_critere1(
                c["spread_std"], c["demi_vie_seances"], TAILLE_PCT_NAV, cout_pct,
                c["z_courant"])
            # CORRECTION F-7 — sensibilité au stop, RECALCULÉE, jamais recopiée.
            tab_stop = table_sensibilite_stop(c["z_courant"], c["spread_std"],
                                              c["demi_vie_seances"],
                                              TAILLE_PCT_NAV, cout_pct)

            p = portier(lab, qualif, sim, corr, taille_pct=TAILLE_PCT_NAV,
                        date_donnees=date_donnees, coint=c, confront=confront,
                        ic_kappa=ic_k, franchissement=franch)

            print(f"\n  ▸ {lab}")
            print(f"    z plein échantillon {c['z_courant']:+.4f} · z causal EXPANSIF "
                  f"{comm['expansif'].iloc[-1]:+.4f} · z causal GLISSANT "
                  f"{FENETRE_GLISSANTE} {comm['causal'].iloc[-1]:+.4f}")
            print(f"    biais d'anticipation PUR (expansif) : écart-type {ecart_exp.std():.4f} · "
                  f"|écart| > 0,2 dans {100*(ecart_exp.abs() > 0.2).mean():.1f} % des séances")
            print(f"    biais + changement de régime (glissant) : écart-type {ecart.std():.4f} · "
                  f"|écart| > 0,2 dans {100*(ecart.abs() > 0.2).mean():.1f} % des séances")
            print(f"    sens {sim['sens']} · cible z {sim['cible_z']:+.2f} · "
                  f"stop z {sim['stop_z']:+.2f}")
            print(f"    P(cible) {sim['p_cible']:.4f} · P(stop) {sim['p_stop']:.4f} · "
                  f"P(AUCUNE barrière) {sim['p_aucune']:.4f}  [somme = "
                  f"{sim['p_cible']+sim['p_stop']+sim['p_aucune']:.12f}, non normalisée]")
            # ── CORRECTION F-4 : DÉPASSEMENT PUBLIÉ DES DEUX CÔTÉS ─────
            print(f"    gain à la cible {sim['gain_a_la_cible_pct']*100:+.2f} pb NAV "
                  f"(dépassement du nominal {sim['depassement_de_la_cible']*100:+.1f} %) · "
                  f"perte au stop {sim['perte_au_stop_pct']*100:+.2f} pb NAV "
                  f"(dépassement {sim['depassement_du_stop']*100:+.1f} %)")
            print(f"    ratio aux niveaux nominaux {sim['ratio_aux_niveaux_nominaux']:.4f} → "
                  f"aux cours franchis {sim['ratio_aux_cours_franchis']:.4f} "
                  f"(biais de discrétisation {sim['biais_de_discretisation_sur_le_ratio']*100:+.1f} %)")
            print(f"    espérance BRUTE {p['esperance_brute_pct']*100:+.3f} pb NAV · "
                  f"coût {p['cout_pct']*100:.3f} pb NAV · "
                  f"NETTE {p['esperance_nette_pct']*100:+.3f} pb NAV")
            print(f"    seuil de rentabilité : {p['seuil_rentabilite_pb_notionnel']:.1f} pb "
                  f"du notionnel (coût retenu : {COUT_ALLER_RETOUR_PB:.0f} pb)")
            # ── CORRECTION F-2 : le biais de maille, MESURÉ ─────────────
            if conv.get("applicable"):
                ps, es = conv["p_stop"], conv["esperance_brute_pb"]
                print(f"    DISCRÉTISATION (m = {conv['m_grossier']} → "
                      f"{conv['m_retenu']} → ∞ par Richardson en 1/√m, "
                      f"{conv['n_trajectoires']:,} traj.)".replace(",", " "))
                print(f"      P(stop) {ps['m_grossier']:.4f} → {ps['m_retenu']:.4f} → "
                      f"{ps['extrapole_infini']:.4f}  ·  le pas journalier la "
                      f"sous-estimait de {abs(ps['sous_estimation_au_pas_journalier_pct']):.1f} %")
                print(f"      espérance brute {es['m_grossier']:+.2f} → {es['m_retenu']:+.2f} → "
                      f"{es['extrapole_infini']:+.2f} pb  ·  surévaluée de "
                      f"{es['surevaluation_au_pas_journalier_pct']:+.1f} % au pas journalier")
                print(f"      résidu à la maille retenue : "
                      f"{conv['residu_a_la_maille_retenue_pb']:.3f} pb NAV")
            # ── CORRECTION F-4 : l'incertitude qui compte est celle de κ ─
            if ic_k.get("applicable"):
                pb_, ph_ = (ic_k["points"]["demi_vie_basse_kappa_haut"],
                            ic_k["points"]["demi_vie_haute_kappa_bas"])
                print(f"    ESPÉRANCE SUR L'IC95 DE LA DEMI-VIE "
                      f"[{ic_k['ic95_demi_vie'][0]:.2f} ; {ic_k['ic95_demi_vie'][1]:.2f}] "
                      f"séances (κ ∈ [{ic_k['ic_kappa'][0]:.4f} ; {ic_k['ic_kappa'][1]:.4f}]) :")
                print(f"      nette {pb_['esperance_nette_pb']:+.2f} pb (demi-vie basse) … "
                      f"{ph_['esperance_nette_pb']:+.2f} pb (demi-vie haute) — "
                      f"{'signe STABLE' if ic_k['signe_stable_sur_ic'] else 'SIGNE INSTABLE'}")
                print(f"      [l'erreur type de Monte-Carlo, "
                      f"{sim['esperance_erreur_type_mc']*100:.3f} pb, mesure le "
                      f"générateur — elle ne tranche rien : RETIRÉE du critère 7]")
            else:
                print(f"    ESPÉRANCE SUR L'IC DE κ : non calculable — "
                      f"{ic_k.get('motif')}")
            if hors.get("n_trades"):
                print(f"    HORS ÉCHANTILLON ({hors['n_obs_test']} obs, "
                      f"{hors['n_trades']} signaux) : P&L moyen "
                      f"{hors['pnl_moyen_pb_nav']:+.2f} pb NAV · "
                      f"cible {hors['part_cible']:.0%} / stop {hors['part_stop']:.0%} / "
                      f"marché {hors['part_marche']:.0%} · gagnants {hors['part_gagnants']:.0%}")
            else:
                print(f"    HORS ÉCHANTILLON : {hors.get('note', 'indisponible')}")
            if confront.get("applicable"):
                o_, a_ = confront["observe"], confront["attendu_modele"]
                print(f"      CONFRONTATION AU MODÈLE — observé cible {o_['cible']} / "
                      f"stop {o_['stop']} / marché {o_['marche']}  ·  attendu "
                      f"{a_['cible']:.1f} / {a_['stop']:.1f} / {a_['marche']:.1f}")
                print(f"      TESTS DÉCLARÉS — multinomial EXACT p = "
                      f"{confront['p_multinomial_exact']:.2e} · Student P&L "
                      f"t = {confront['t_pnl']:+.2f} p = {confront['p_student_pnl']:.2e}")
                print(f"      pour mémoire (ne tranchent pas) : χ² {confront['chi2']:.1f} "
                      f"p = {confront['p_chi2']:.2e} "
                      f"[approximation {'valide' if confront['chi2_valide'] else 'INVALIDE, effectif attendu < 5'}] · "
                      f"binomial exact stops p = {confront['p_binomial_exact_stops']:.2e}")
                print(f"      min(p) = {confront['p_valeur']:.2e} "
                      f"({confront['test_le_plus_defavorable']}) vs seuil de Bonferroni "
                      f"{confront['seuil_bonferroni']:.4f} → "
                      f"{'MODÈLE RÉFUTÉ' if confront['modele_refute'] else 'non réfuté'}")
                print(f"      réserve : {confront['reserve']}")
            else:
                print(f"      CONFRONTATION AU MODÈLE : non applicable — "
                      f"{confront.get('motif')}")
            # ── CORRECTION F-7 : TABLE DE FRANCHISSEMENT DU CRITÈRE 1 ───
            if franch.get("applicable"):
                print(f"    TABLE DE FRANCHISSEMENT DU CRITÈRE 1 — constantes de "
                      f"doctrine INCHANGÉES (cible z {CIBLE_Z:+.2f}, stop "
                      f"z ±{STOP_Z_ABSOLU:.2f}) ;")
                print(f"    seul le z OBSERVÉ varie. {franch['formule_approchee']}.")
                print(f"      {'z₀':>8}{'ratio':>9}{'P(cible)':>10}"
                      f"{'E nette pb':>12}{'crit. 1':>10}")
                for l in franch["lignes"]:
                    print(f"      {l['z']:>8.3f}{l['ratio']:>9.3f}{l['p_cible']:>10.3f}"
                          f"{l['esperance_nette_pb']:>12.2f}"
                          f"{('PASSE' if l['ratio'] >= RATIO_MINIMUM else 'ÉCHEC'):>10}")
                print(f"      franchissement du seuil {RATIO_MINIMUM:.0f}:1 à "
                      f"|z₀| = {franch['z_franchissement_simule']:.3f} (simulé) / "
                      f"{franch['z_franchissement_analytique']:.3f} (analytique, "
                      f"2×{STOP_Z_ABSOLU:.1f}/3)")
                print(f"      espérance nette à ce point : "
                      f"{franch['esperance_nette_au_franchissement_pb']:+.2f} pb NAV "
                      f"(au z observé : "
                      f"{franch['esperance_nette_au_z_observe_pb']:+.2f} pb, soit "
                      f"{franch['gain_d_esperance_au_franchissement_pct']:+.0f} %)")
                print(f"      espérance nette MAXIMALE sur la grille : "
                      f"{franch['esperance_nette_maximale_pb']:+.2f} pb à "
                      f"z = {franch['z_esperance_maximale']:+.3f} → critères 1 et 7 "
                      f"{'ANTAGONISTES' if franch['criteres_1_et_7_antagonistes'] else 'NON antagonistes'}")
            if tab_stop:
                print(f"    SENSIBILITÉ AU STOP (recalculée, jamais recopiée — "
                      f"STOP_Z_ABSOLU reste une constante de doctrine) :")
                print(f"      {'stop z':>8}{'ratio':>9}{'P(cible)':>10}{'E nette pb':>12}")
                for l in tab_stop:
                    print(f"      {l['stop_z']:>8.2f}{l['ratio']:>9.3f}"
                          f"{l['p_cible']:>10.3f}{l['esperance_nette_pb']:>12.2f}")
            print(f"    {'critère':<34}{'valeur':>18}{'':>3}{'verdict':>9}")
            for k, v in p["criteres"].items():
                val = v["valeur"]
                if isinstance(val, float):
                    # Une p-valeur de 2e−21 affichée « 0.0000 » se lit comme
                    # une absence de mesure. Notation scientifique sous 1e−4.
                    aff = (f"{val:.4f}" if (val == 0.0 or abs(val) >= 1e-4)
                           else f"{val:.2e}")
                elif val is None:
                    aff = "ABSENT"
                else:
                    aff = str(val)[:16] + "…" if len(str(val)) > 17 else str(val)
                print(f"    {k:<34}{aff:>18}{'':>3}{'PASSE' if v['passe'] else 'ÉCHOUE':>9}")
            print(f"    VERDICT : {p['verdict']}"
                  + (f"  — échecs : {', '.join(e.split('_', 1)[1] for e in p['echecs'])}"
                     if p["echecs"] else "")
                  + f"  · statut_risque : {p['statut_risque']}")

            idees.append({
                "id": identifiant(lab, date_donnees),
                "paire": lab,
                "verdict": p["verdict"],
                "sens": sim["sens"],
                "taille_pct_nav": TAILLE_PCT_NAV,
                "esperance_brute_pct": p["esperance_brute_pct"],
                "esperance_nette_pct": p["esperance_nette_pct"],
                "perte_au_stop_pct": sim["perte_au_stop_pct"],
                "p_cible": sim["p_cible"], "p_stop": sim["p_stop"],
                "p_aucune": sim["p_aucune"],
                "z_entree": c["z_courant"], "demi_vie": c["demi_vie_seances"],
                "demi_vie_ic95": c["demi_vie_ic95"],
                "demi_vie_identifiee": c["demi_vie_identifiee"],
                "demi_vie_libelle": c["demi_vie_libelle"],
                "adf_t": c["adf_t"], "adf_retards": c["adf_retards"],
                "n_obs": c["n_obs"], "profondeur_annees": c["profondeur_annees"],
                "echantillon_contient_stress": c["echantillon_contient_stress"],
                "criteres": {k: {"passe": v["passe"], "valeur": v["valeur"]}
                             for k, v in p["criteres"].items()},
                # CORRECTION F-8 — statut RÉEL, plus une constante apposée
                # même sur les idées refusées.
                "statut_risque": p["statut_risque"],
                # — annexes, hors contrat minimal —
                "cible_z": sim["cible_z"], "stop_z": sim["stop_z"],
                "cout_pct": p["cout_pct"],
                "convention_cout": f"{COUT_ALLER_RETOUR_PB:.0f} pb — {BASE_COUT}",
                "seuil_rentabilite_pb_notionnel": p["seuil_rentabilite_pb_notionnel"],
                # CORRECTION F-4 — dépassement BILATÉRAL
                "depassement_du_stop": sim["depassement_du_stop"],
                "depassement_de_la_cible": sim["depassement_de_la_cible"],
                "ratio_aux_niveaux_nominaux": sim["ratio_aux_niveaux_nominaux"],
                "biais_de_discretisation_sur_le_ratio":
                    sim["biais_de_discretisation_sur_le_ratio"],
                "sous_pas_par_seance": sim["sous_pas_par_seance"],
                "z_causal_glissant": float(comm["causal"].iloc[-1]),
                "z_causal_expansif": float(comm["expansif"].iloc[-1]),
                "biais_anticipation_ecart_type": float(ecart_exp.std()),
                "ecart_type_z_glissant_vs_plein": float(ecart.std()),
                "test_hors_echantillon": hors,
                "confrontation_hors_echantillon": confront,      # F-6
                "adf_glissant": c["adf_glissant"],               # F-6
                "convergence_discretisation": conv,              # F-2
                "esperance_sur_ic_kappa": ic_k,                  # F-4
                "table_franchissement_critere1": franch,         # F-7
                "table_sensibilite_stop": tab_stop,              # F-7
                "alertes_echantillon": c["alertes"],
                "echecs": p["echecs"]})
            resultats_detail.append({"nom": lab, "simulation": sim, "portier": p,
                                     "qualification": {
                                         "catalyseur": (str(qualif["catalyseur"]["date"].date())
                                                        if qualif["catalyseur"] else None),
                                         "motif_absence_catalyseur": qualif["motif_absence_catalyseur"],
                                         "invalidation": qualif["invalidation"],
                                         "pourquoi_existe": qualif["pourquoi_existe"]}})
          except ControleInterneRompu as e:
            print(f"\n  ▸ {lab} : CONTRÔLE INTERNE ROMPU — {e}")
            print(f"    La paire est écartée. Le processus continue et le JSON "
                  f"sera écrit : une paire ne fait pas taire les autres.")
            erreurs_paires.append({"paire": lab, "type": "CONTROLE_INTERNE_ROMPU",
                                   "motif": str(e)})
          except Exception as e:                                  # noqa: BLE001
            print(f"\n  ▸ {lab} : ERREUR NON PRÉVUE — "
                  f"{type(e).__name__} : {e}")
            print(f"    La paire est écartée et l'incident est publié dans le "
                  f"JSON. Aucune idée n'est produite pour elle.")
            erreurs_paires.append({"paire": lab, "type": type(e).__name__,
                                   "motif": str(e)})

    # ── CONCLUSION ───────────────────────────────────────────────────────
    print("\n" + "=" * 78); print("CONCLUSION"); print("=" * 78)
    transmises = [i for i in idees if i["verdict"] == "TRANSMISE"]
    refusees = [i for i in idees if i["verdict"] != "TRANSMISE"]
    if transmises:
        print(f"  {len(transmises)} idée(s) transmise(s) à la Section Risque POUR VETO.")
        print("  Aucune n'est exécutable : statut_risque = EN_ATTENTE_VETO.")
    else:
        print("  AUCUNE idée transmise. Le portier refuse par défaut ; l'absence")
        print("  d'idée est un résultat, pas une panne.")
    if refusees:
        # CORRECTION F-8 — une idée refusée n'est pas soumise au veto.
        print(f"  {len(refusees)} idée(s) REFUSÉE(S) en amont : statut_risque = "
              f"NON_SOUMISE_REFUSEE_EN_AMONT.")
        print("  Elles ne sont PAS soumises au veto : une idée que cette section")
        print("  a écartée ne peut pas ressortir de l'aval avec un enregistrement")
        print("  favorable (`veto: false, motifs: []`). C'était le cas avant F-8.")
    if erreurs_paires:
        print(f"  {len(erreurs_paires)} paire(s) écartée(s) sur incident :")
        for e in erreurs_paires:
            print(f"    · {e['paire']} — {e['type']}")
    print("\n  REDÉCOUVERTE, PAS DÉCOUVERTE (P16) — l'espérance nulle sous tout")
    print("  couple (cible, stop) sans dérive est le théorème d'arrêt optionnel")
    print("  de Doob (1953). Le résultat est juste, l'attribution ne l'était pas.")
    # ── CORRECTION F-7 : la conversion log → prix est CALCULÉE ───────────
    # Les chiffres « +29,56 % / −22,82 %, ratio 1,296 » étaient saisis à la
    # main, tirés d'un seul cas, et ne se reproduisaient à partir d'aucune
    # sortie du module. Ils sont recalculés à partir du σ effectivement
    # mesuré sur chaque paire cointégrée.
    print("  Le « ratio 1,00 exactement » d'une position linéaire ne tient qu'en")
    print("  unités LOGARITHMIQUES. Conversion en unités de PRIX, recalculée")
    print("  sur le σ mesuré de chaque paire retenue (d = 2·σ_j·√T) :")
    for lab in retenus:
        c = coints[lab]
        d = 2.0 * c["sigma_increment"] * math.sqrt(HORIZON_SEANCES)
        haut, bas = math.exp(d) - 1.0, math.exp(-d) - 1.0
        print(f"    {lab} : ±2σ_H = ±{d:.6f} en log → {100*haut:+.2f} % / "
              f"{100*bas:+.2f} % en prix, ratio {abs(haut/bas):.3f}")
    print("  La convention log est déclarée ; aucune conclusion d'exclusion")
    print("  structurelle n'est bâtie sur elle sans que la conversion soit dite.")

    # ── CORRECTION P15 : BLOC DOCTRINE, SEULE SOURCE DES CHIFFRES ───────
    print("\n" + "=" * 78)
    print("BLOC DOCTRINE — COPIER TEL QUEL, NE RIEN RESSAISIR À LA MAIN (P15)")
    print("=" * 78)
    print(f"| paire | ADF t | retards | coint. 5 % | demi-vie (IC95) | z | n obs | ans | stress | ADF gliss. récent |")
    print(f"|---|---:|---:|:---:|---|---:|---:|---:|:---:|---:|")
    for lab, c in coints.items():
        dv, ic = c["demi_vie_seances"], c["demi_vie_ic95"]
        # CORRECTION F-5 — pas de borne supérieure là où il n'y en a pas.
        if not np.isfinite(dv):
            sdv = "—"
        elif c["demi_vie_identifiee"]:
            sdv = f"{dv:.1f} [{ic[0]:.1f} ; {ic[1]:.1f}]"
        else:
            sdv = (f"demi-vie non identifiée (borne supérieure infinie) "
                   f"— estimation ponctuelle {dv:.1f}, borne inférieure {ic[0]:.1f}")
        ag = c["adf_glissant"]
        sag = (f"{100*ag['fraction_franchissements_recents']:.0f} % "
               f"({ag['n_franchissements_recents']}/{ag['n_fenetres_recentes']})"
               if ag.get("disponible") else "—")
        print(f"| {lab} | {c['adf_t']:.2f} | {c['adf_retards']} | "
              f"{'OUI' if c['cointegre_5pct'] else 'non'} | {sdv} | "
              f"{c['z_courant']:+.2f} | {c['n_obs']} | {c['profondeur_annees']:.2f} | "
              f"{'oui' if c['echantillon_contient_stress'] else 'NON'} | {sag} |")
    print()
    for i in idees:
        print(f"| {i['paire']} | {i['verdict']} | espérance brute "
              f"{i['esperance_brute_pct']*100:+.2f} pb NAV | nette "
              f"{i['esperance_nette_pct']*100:+.2f} pb NAV | "
              f"P(cible) {i['p_cible']:.3f} · P(stop) {i['p_stop']:.3f} · "
              f"P(aucune) {i['p_aucune']:.3f} | seuil rentab. "
              f"{i['seuil_rentabilite_pb_notionnel']:.0f} pb notionnel | "
              f"statut {i['statut_risque']} |")
    # ── CORRECTION F-7 : la table de franchissement entre dans la doctrine
    print()
    print("| paire | z observé | ratio | |z| de franchissement du critère 1 "
          "(simulé / analytique) | E nette à ce point | E nette max (z) |")
    print("|---|---:|---:|---:|---:|---:|")
    for i in idees:
        f_ = i.get("table_franchissement_critere1") or {}
        if not f_.get("applicable"):
            continue
        print(f"| {i['paire']} | {i['z_entree']:+.3f} | "
              f"{i['criteres']['1_ratio_asymetrie']['valeur']:.3f} | "
              f"{f_['z_franchissement_simule']:.3f} / "
              f"{f_['z_franchissement_analytique']:.3f} | "
              f"{f_['esperance_nette_au_franchissement_pb']:+.2f} pb | "
              f"{f_['esperance_nette_maximale_pb']:+.2f} pb "
              f"(z {f_['z_esperance_maximale']:+.2f}) |")

    # ── CORRECTION F-9 : MARQUEUR DE FRAÎCHEUR ──────────────────────────
    # La Section Risque relisait ce fichier sans aucun moyen de savoir s'il
    # datait du jour. Un processus tué avant l'écriture laissait en place le
    # fichier de la veille, lu comme frais. Le fichier porte désormais son
    # heure de production, sa fenêtre de validité et l'heure de péremption
    # que l'aval doit contrôler avant toute lecture.
    peremption = horodatage_execution + timedelta(hours=VALIDITE_SORTIE_HEURES)
    fraicheur = {
        "genere_le_utc": horodatage_execution.isoformat(timespec="seconds") + "Z",
        "date_donnees": str(date_donnees.date()),
        "validite_heures": VALIDITE_SORTIE_HEURES,
        "perime_apres_utc": peremption.isoformat(timespec="seconds") + "Z",
        "execution_complete": True,
        "n_paires_examinees": len(coints),
        "n_paires_ecartees_sur_incident": len(erreurs_paires),
        "controle_attendu_de_l_aval": (
            "REFUSER ce fichier si l'heure UTC courante dépasse "
            "`perime_apres_utc`, ou si `date_donnees` ne correspond pas à la "
            "date d'arrêté examinée, ou si `execution_complete` est absent ou "
            "faux. Un fichier périmé lu comme frais est une position prise sur "
            "des chiffres morts."),
    }

    charge = {
        "fraicheur": fraicheur,                                   # F-9
        "idees": idees,
        "date_donnees": str(date_donnees.date()),
        "graine_simulation": GRAINE_SIMULATION,
        "n_trajectoires": N_TRAJECTOIRES,
        "n_trajectoires_exploration": N_TRAJECTOIRES_EXPLORATION,
        "sous_pas_par_seance": SOUS_PAS_PAR_SEANCE,               # F-2
        "taille_pct_nav": TAILLE_PCT_NAV,                          # F-9
        "convention_cout": {"valeur_pb": COUT_ALLER_RETOUR_PB, "base": BASE_COUT},
        "horizon_seances": HORIZON_SEANCES,
        "valeur_critique_engle_granger_5pct": -3.34,
        "adf_glissant_parametres": {                              # F-6
            "fenetre": ADF_GLISSANT_FENETRE, "pas": ADF_GLISSANT_PAS,
            "seuil_t": ADF_GLISSANT_SEUIL_T,
            "n_fenetres_recentes": ADF_GLISSANT_N_FENETRES_RECENTES,
            "fraction_max": ADF_GLISSANT_FRACTION_MAX},
        "hors_echantillon_parametres": {                          # F-6
            "seuil_p": HORS_ECHANTILLON_SEUIL_P,
            "min_signaux": HORS_ECHANTILLON_MIN_SIGNAUX},
        "doctrine_echantillon": {                                 # F-3
            "profondeur_min_annees": PROFONDEUR_MIN_ANNEES,
            "profondeur_min_obs": PROFONDEUR_MIN_OBS,
            "exiger_stress_dans_echantillon": EXIGER_STRESS_DANS_ECHANTILLON,
            "opposable": True},
        "paires_cointegrees_5pct": retenus,
        "cointegrations": {k: {kk: vv for kk, vv in v.items()
                               if kk not in ("serie_spread", "log_a", "log_b")}
                           for k, v in coints.items()},
        "detail_passages": resultats_detail,
        "paires_ecartees_sur_incident": erreurs_paires,           # F-9
        "n_transmises": len(transmises),
        "n_refusees": len(refusees),
        "statuts_risque_possibles": ["EN_ATTENTE_VETO",
                                     "NON_SOUMISE_REFUSEE_EN_AMONT"],
        "avertissement": ("Ce moteur ne peut pas déclarer une idée exécutable. "
                          "Une idée TRANSMISE sort en EN_ATTENTE_VETO et n'est "
                          "qu'une DEMANDE de veto ; une idée REFUSÉE sort en "
                          "NON_SOUMISE_REFUSEE_EN_AMONT et n'est pas soumise. "
                          "Seule la Section Risque peut statuer."),
    }
    sortie_json.write_text(json.dumps(charge, indent=2, ensure_ascii=False, default=str),
                           encoding="utf-8")
    print(f"\n→ {sortie_json}")
    print(f"  fraîcheur : généré le {fraicheur['genere_le_utc']} · "
          f"périmé après {fraicheur['perime_apres_utc']} "
          f"({VALIDITE_SORTIE_HEURES:.0f} h) — contrôle attendu de l'aval (F-9)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
