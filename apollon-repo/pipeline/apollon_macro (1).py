#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
APOLLON — MOTEUR MACRO
======================
Produit un brief macro *mécaniquement*, depuis les séries du dépôt, de sorte
qu'aucune affirmation du brief ne puisse être choisie par l'agent qui le rend.

Origine
-------
Quatre briefs Macro, zéro validé sans réserve. La Macro était la seule section
dont le livrable était rédigé en prose au lieu d'être produit par du code. Le
diagnostic est écrit en toutes lettres dans la doctrine §11 (R-029) :

    « Quand l'agent construit lui-même la distribution qui juge sa position,
      il la construit à son avantage — et d'autant plus efficacement qu'il est
      devenu rigoureux partout ailleurs. »

Mesure du dommage : brief 004, queue gauche ×5, queue droite supprimée, ratio
annoncé 3,0:1, ratio réel 1,29:1.

Ce que ce moteur ferme
----------------------
E-001  la conclusion précédait le raisonnement  -> le test s'exécute avant que
       l'énoncé soit rendu ; l'énoncé est un gabarit rempli par le calcul.
E-002  Brent d'un titre de presse                -> tout nombre sort d'une série,
       avec sa date et sa profondeur ; aucune saisie manuelle.
E-004  source tronquée                           -> portée temporelle complète
       publiée pour chaque série citée.
E-005  inflation sans le sous-jacent             -> couples obligatoires, refus
       de rendu si un membre est publié seul.
E-006  prémisse de politique monétaire non vérifiée -> tout énoncé contenant du
       vocabulaire de politique monétaire exige DFF dans les séries utilisées.
E-007  même indicateur, deux sens                -> table des sens, refus nommé.
E-018  espérance négative sous ratio flatteur    -> l'espérance décide.
E-028  grille amputée                            -> grille symétrique déclarée
       avant toute lecture, empreinte SHA-256 vérifiée à chaque usage.
R-011  percentile sur série tronquée             -> profondeur réelle publiée,
       percentile refusé si la profondeur est insuffisante.
R-038  critère franchissable par une chaîne      -> objets typés, vocabulaire
       fermé, une seule fonction de qualification appelée une seule fois.
R-043  test nommé mais non exécuté               -> chaque test est un Callable
       exécuté, son résultat publié.
R-044  instrument branché sur rien               -> toute mesure produite est
       opposable, ou déclarée non opposable dans la sortie.

Usage
-----
    python3 apollon_macro.py

Sorties
-------
    macro_resultats.json      contrat avec la Section Risque (horodaté)
    brief_macro_005.md        brief produit par le code, aucune ressaisie
    registre_calibration.csv  registre alimenté et relu

Code de sortie
--------------
    0  brief produit
    2  production bloquée (série obligatoire manquante ou données périmées)
    3  rendu refusé (couple incomplet, conflit de sens, grille altérée)
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
import re
import sys
from dataclasses import dataclass, field
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Callable

import numpy as np
import pandas as pd

# =====================================================================
# §0  CONSTANTES DÉCLARÉES AVANT TOUTE LECTURE DE DONNÉES
#     Rien dans ce bloc ne dépend d'un chiffre observé. Il est écrit,
#     figé, empreinté, et vérifié à chaque usage.
# =====================================================================

# ---- LA GRILLE (R-029, §11) -----------------------------------------
# Symétrique par construction. Les scénarios sont les mêmes pour toute
# thèse, quelle qu'elle soit. σ est mesuré sur la série, jamais choisi.
GRILLE_SIGMA: tuple[float, ...] = (-2.0, -1.0, -0.5, 0.0, +0.5, +1.0, +2.0)
HORIZON_SEANCES: int = 60
HORIZON_MOIS: int = 3          # 60 séances / 21 séances par mois, arrondi

# Empreinte de la grille : toute fonction qui ajouterait, retirerait ou
# repondérerait un point de grille est détectée avant usage.
_EMPREINTE_GRILLE_ATTENDUE = hashlib.sha256(
    repr(tuple(float(x) for x in GRILLE_SIGMA)).encode("utf-8")
).hexdigest()

MIN_OBS_BANDE: int = 20        # sous ce seuil, la bande est NON ESTIMABLE
SEUIL_ECART_LOI: float = 2.0   # facteur d'écart empirique/gaussien à déclarer

# ---- Fenêtres et seuils ---------------------------------------------
FENETRES_PERCENTILE = {"1 an": 252, "5 ans": 1260, "echantillon complet": None}
FENETRES_PERCENTILE_MENSUEL = {"1 an": 12, "5 ans": 60, "echantillon complet": None}
SEUIL_PROFONDEUR_MARGINALE: float = 0.70   # < 70 % du requis => insuffisante
SEUIL_CONFIRMATION_PCT: float = 30.0       # extrême de percentile exigé
SEUIL_REDONDANCE_CORR: float = 0.90        # fusion des classes de confirmation
MIN_CLASSES_CONFIRMATION: int = 2
# E-050 / R-051 — l'écart entre rendement conditionnel et rendement hors
# déclenchement doit dépasser ce nombre d'erreurs types, calculées sur les
# BLOCS INDÉPENDANTS. Origine : posée à la main, non dérivée.
T_MINIMUM_ARETE: float = 2.0
RETARD_MAX_SEANCES: int = 5                # retard toléré sur la date d'arrêté
TAILLE_PCT_NAV: float = 8.0                # plafond alpha de la charte
TOLERANCE_IDENTITE: float = 0.02           # arrondi FRED à 2 décimales
VALIDITE_SORTIE_HEURES: float = 24.0

# ---- Séries obligatoires (R-028) ------------------------------------
# La doctrine en liste quatorze. VXVCLS n'est pas au dépôt : le domaine
# qui en dépend est FERMÉ, pas contourné.
SERIES_OBLIGATOIRES_DOCTRINE = {
    "DGS2", "DGS10", "DGS30", "T10Y2Y", "DFII10", "T10YIE",
    "CPIAUCSL", "CPILFESL", "UNRATE", "PAYEMS",
    "VIXCLS", "VXVCLS", "SP500", "DFF",
}
SERIES_NOYAU = {                    # absence => PRODUCTION BLOQUÉE
    "DGS2", "DGS10", "DGS30", "T10Y2Y", "DFII10", "T10YIE",
    "CPIAUCSL", "CPILFESL", "UNRATE", "PAYEMS", "VIXCLS", "SP500", "DFF",
}
DOMAINES = {                        # absence => DOMAINE FERMÉ, thèses interdites
    "M1_taux":        ["DGS2", "DGS10", "DGS30", "T10Y2Y", "DFII10", "T10YIE", "T5YIFR", "DFF"],
    "M2_cycle":       ["CPIAUCSL", "CPILFESL", "UNRATE", "PAYEMS", "INDPRO"],
    "M3_energie":     ["DCOILBRENTEU", "DCOILWTICO"],
    "M4_devises":     ["DEXUSEU", "DEXJPUS", "DTWEXBGS"],
    "RISQUE_actions": ["VIXCLS", "SP500", "NASDAQ100"],
    "RISQUE_credit":  ["BAMLH0A0HYM2", "BAMLC0A0CM"],
    "VOL_TENOR":      ["VIXCLS", "VXVCLS"],   # fermé : VXVCLS absente du dépôt
}

# ---- Couples obligatoires (E-005) -----------------------------------
COUPLES_OBLIGATOIRES = [
    ("CPIAUCSL", "CPILFESL"),
    ("DGS10", "DFII10"),
    ("DGS10", "T10YIE"),
    ("BAMLH0A0HYM2", "BAMLC0A0CM"),
    ("UNRATE", "PAYEMS"),
    ("VIXCLS", "SP500"),
]

# ---- Table des sens (E-007) -----------------------------------------
# Chaque série reçoit UN sens, déclaré ici. `signe_risque` = +1 si une
# hausse de la série signifie davantage de risque macro / de resserrement,
# -1 si une hausse signifie détente. Une thèse qui lit une série à
# l'envers de cette table est refusée ; deux thèses qui la lisent en sens
# opposés font refuser le brief entier.
SENS_SERIE: dict[str, dict] = {
    "DFF":          {"role": "politique_monetaire",     "signe_risque": +1},
    "DGS2":         {"role": "taux_nominal_2a",         "signe_risque": +1},
    "DGS10":        {"role": "taux_nominal_10a",        "signe_risque": +1},
    "DGS30":        {"role": "taux_nominal_30a",        "signe_risque": +1},
    "T10Y2Y":       {"role": "pente_courbe",            "signe_risque": -1},
    "DFII10":       {"role": "taux_reel_10a",           "signe_risque": +1},
    "T10YIE":       {"role": "point_mort_10a",          "signe_risque": +1},
    "T5IFR_ALIAS":  {"role": "point_mort_5a5a",         "signe_risque": +1},
    "T5YIFR":       {"role": "point_mort_5a5a",         "signe_risque": +1},
    "CPIAUCSL":     {"role": "inflation_globale",       "signe_risque": +1},
    "CPILFESL":     {"role": "inflation_sous_jacente",  "signe_risque": +1},
    "UNRATE":       {"role": "chomage",                 "signe_risque": +1},
    "PAYEMS":       {"role": "emploi",                  "signe_risque": -1},
    "INDPRO":       {"role": "activite_industrielle",   "signe_risque": -1},
    "VIXCLS":       {"role": "volatilite_implicite",    "signe_risque": +1},
    "SP500":        {"role": "prix_actions",            "signe_risque": -1},
    "NASDAQ100":    {"role": "prix_actions_tech",       "signe_risque": -1},
    "DCOILBRENTEU": {"role": "prix_energie",            "signe_risque": +1},
    "DCOILWTICO":   {"role": "prix_energie_wti",        "signe_risque": +1},
    "DEXUSEU":      {"role": "devise_eurusd",           "signe_risque": -1},
    "DEXJPUS":      {"role": "devise_usdjpy",           "signe_risque": +1},
    "DTWEXBGS":     {"role": "dollar_large",            "signe_risque": +1},
    "BAMLH0A0HYM2": {"role": "risque_credit_hy",        "signe_risque": +1},
    "BAMLC0A0CM":   {"role": "risque_credit_ig",        "signe_risque": +1},
}

# ---- Identités comptables (redondance cachée) -----------------------
# Vérifiées numériquement sur les données. Deux séries liées par une
# identité ne comptent jamais pour deux confirmations indépendantes.
IDENTITES = [
    ("T10YIE", ("DGS10", "DFII10"), (+1, -1), "T10YIE = DGS10 - DFII10"),
    ("T10Y2Y", ("DGS10", "DGS2"),   (+1, -1), "T10Y2Y = DGS10 - DGS2"),
]

# ---- Conventions de variation ---------------------------------------
# 'log'    : la variation est un log-rendement (prix, indices, VIX)
# 'niveau' : la variation est une différence en points de pourcentage
CONVENTION = {
    "DFF": "niveau", "DGS2": "niveau", "DGS10": "niveau", "DGS30": "niveau",
    "T10Y2Y": "niveau", "DFII10": "niveau", "T10YIE": "niveau", "T5YIFR": "niveau",
    "UNRATE": "niveau", "BAMLH0A0HYM2": "niveau", "BAMLC0A0CM": "niveau",
    "CPIAUCSL": "log", "CPILFESL": "log", "PAYEMS": "log", "INDPRO": "log",
    "VIXCLS": "log", "SP500": "log", "NASDAQ100": "log",
    "DCOILBRENTEU": "log", "DCOILWTICO": "log",
    "DEXUSEU": "log", "DEXJPUS": "log", "DTWEXBGS": "log",
}

# ---- Instruments admissibles et maturité implicite -------------------
# Un instrument n'est admissible que si son P&L est calculable depuis le
# dépôt SEUL. Les OAS de crédit ne le sont pas : le dépôt ne contient pas
# le rendement de l'indice, donc pas la duration de spread. Toute thèse
# dont l'instrument est un spread est REFUSÉE, et le motif est publié.
MATURITE_OBLIGATION = {"DGS2": 2.0, "DGS10": 10.0, "DGS30": 30.0}
INSTRUMENTS_PRIX = ["SP500", "NASDAQ100", "DCOILBRENTEU", "DCOILWTICO",
                    "DEXUSEU", "DEXJPUS", "DTWEXBGS"]
INSTRUMENTS_TAUX = ["DGS2", "DGS10", "DGS30"]
INSTRUMENTS_NON_CALCULABLES = ["BAMLH0A0HYM2", "BAMLC0A0CM"]

# ---- Dossier de confirmation par instrument -------------------------
# Table déclarée AVANT les données et IDENTIQUE pour les deux directions
# de pari : l'agent ne peut pas construire l'instrument qui juge sa
# position. `series` inclut de quoi satisfaire les couples obligatoires.
DOSSIER_INSTRUMENT: dict[str, list[str]] = {
    "SP500":        ["SP500", "VIXCLS", "BAMLH0A0HYM2", "BAMLC0A0CM", "T10Y2Y", "UNRATE", "PAYEMS"],
    "NASDAQ100":    ["NASDAQ100", "SP500", "VIXCLS", "BAMLH0A0HYM2", "BAMLC0A0CM", "T10Y2Y", "UNRATE", "PAYEMS"],
    "DGS2":         ["DGS2", "DGS10", "DFII10", "T10YIE", "CPIAUCSL", "CPILFESL", "UNRATE", "PAYEMS"],
    "DGS10":        ["DGS10", "DFII10", "T10YIE", "CPIAUCSL", "CPILFESL", "UNRATE", "PAYEMS"],
    "DGS30":        ["DGS30", "DGS10", "DFII10", "T10YIE", "CPIAUCSL", "CPILFESL", "UNRATE", "PAYEMS"],
    "DCOILBRENTEU": ["DCOILBRENTEU", "DTWEXBGS", "DGS10", "DFII10", "T10YIE", "INDPRO"],
    "DCOILWTICO":   ["DCOILWTICO", "DTWEXBGS", "DGS10", "DFII10", "T10YIE", "INDPRO"],
    "DEXUSEU":      ["DEXUSEU", "DGS2", "DGS10", "DFII10", "T10YIE", "VIXCLS", "SP500"],
    "DEXJPUS":      ["DEXJPUS", "DGS2", "DGS10", "DFII10", "T10YIE", "VIXCLS", "SP500"],
    "DTWEXBGS":     ["DTWEXBGS", "DGS2", "DGS10", "DFII10", "T10YIE", "VIXCLS", "SP500"],
}
DOMAINE_INSTRUMENT = {
    "SP500": "RISQUE_actions", "NASDAQ100": "RISQUE_actions",
    "DGS2": "M1_taux", "DGS10": "M1_taux", "DGS30": "M1_taux",
    "DCOILBRENTEU": "M3_energie", "DCOILWTICO": "M3_energie",
    "DEXUSEU": "M4_devises", "DEXJPUS": "M4_devises", "DTWEXBGS": "M4_devises",
}

# ---- Grille de candidats (multiplicité déclarée d'avance) ------------
DIRECTIONS = (+1, -1)                       # +1 : la série monte ; -1 : elle baisse
REGLES_CONFIRMATION = ("aligne", "contrarien")
N_CANDIDATS_DECLARES = len(DOSSIER_INSTRUMENT) * len(DIRECTIONS) * len(REGLES_CONFIRMATION)

# ---- Invalidation : vocabulaire fermé (R-038, E-043) ----------------
# L'invalidation doit être un FAIT observable et daté. Elle s'adosse à une
# publication mensuelle dont la cadence est mesurée sur les données. Un
# niveau de prix est refusé.
SERIES_PUBLICATION_DATEE = ["CPIAUCSL", "CPILFESL", "UNRATE", "PAYEMS", "INDPRO"]
MOTIFS_NIVEAU_DE_PRIX = re.compile(
    r"(au-dessus de|au dessus de|sous\s+\d|en dessous de|franchit|touche|"
    r"stop|seuil de\s*[\d,.]+\s*(\$|%|pb)|[\d,.]+\s*(\$|USD|pb)\b|σ\s*touch)",
    re.IGNORECASE)
VOCABULAIRE_POLITIQUE = re.compile(
    r"\b(fed|fomc|bce|ecb|boj|boe|banque centrale|taux directeur|"
    r"hausse de taux|baisse de taux|quantitative|qt\b|qe\b)", re.IGNORECASE)

# ---- Résolution mécanique des prédictions héritées (R-031) ----------
# Chaque règle encode LITTÉRALEMENT le texte de la prédiction héritée.
# Une prédiction sans règle est déclarée NON RÉSOLUBLE MÉCANIQUEMENT ;
# elle n'entre pas au score de Brier et son absence est publiée.
REGLES_RESOLUTION_HERITEES = {
    "C-004": {"type": "barriere", "serie": "DCOILBRENTEU", "sens": "sup",
              "seuil": 100.0, "texte": "Brent au-dessus de 100 USD avant le 30/09/2026"},
    "C-005": {"type": "barriere", "serie": "VIXCLS", "sens": "sup",
              "seuil": 20.0, "texte": "VIX cloture au-dessus de 20 avant le 30/09/2026"},
    "C-008": {"type": "barriere", "serie": "DCOILBRENTEU", "sens": "inf",
              "seuil": 78.0, "texte": "Brent sous 78 USD avant le 31/12/2026"},
}

# ---- Chemins ---------------------------------------------------------
BASE = Path(__file__).resolve().parent
HIST = BASE / "data" / "history"
SORTIE_JSON = BASE / "macro_resultats.json"
SORTIE_BRIEF = BASE / "brief_macro_005.md"
REGISTRE = BASE / "registre_calibration.csv"
REGISTRE_SOURCE = Path("/home/claude/notes/registre_calibration.csv")
NUMERO_BRIEF = "005"

ENTETE_REGISTRE = ["ref", "date_emission", "section", "affirmation", "probabilite",
                   "horizon_jours", "echeance", "resultat", "brier", "statut",
                   "regle_resolution", "note"]


# =====================================================================
# §1  GARDE DE GRILLE — la grille ne peut pas être touchée
# =====================================================================

class GrilleAlteree(RuntimeError):
    """Levée dès qu'un point de grille a été ajouté, retiré ou déplacé."""


class RenduRefuse(RuntimeError):
    """Levée quand le moteur refuse de rendre : couple, sens, ou grille."""


def _empreinte(grille) -> str:
    return hashlib.sha256(repr(tuple(float(x) for x in grille)).encode("utf-8")).hexdigest()


def verifier_grille(grille=GRILLE_SIGMA) -> dict:
    """Contrôle de symétrie et d'intégrité. Appelé à chaque usage de la grille.

    AUCUN `assert` ici — c'est délibéré, et c'est une faute corrigée.

    La version antérieure doublait la vérification d'un `assert`. Il se
    déclenchait EN PREMIER et levait une `AssertionError` nue, masquant le
    motif de `GrilleAlteree` — donc le nom de la queue manquante, qui est
    la seule information utile à qui lit l'erreur. Et sous `python -O` il
    disparaissait : le contrôle ne se comportait pas de la même façon selon
    la façon dont l'interpréteur était lancé.

    C'est la faute F-9 relevée par Astra sur la Section Trading, reproduite
    ici dans le garde-fou du paramètre libre de la Section Macro.

    R-046 — Un contrôle de sûreté ne s'écrit jamais avec `assert`.
    """
    g = list(grille)
    if sorted(g) != sorted(-x for x in g):
        raise GrilleAlteree(
            f"GRILLE ASYMÉTRIQUE : {g} — la queue manquante est "
            f"{sorted(set(-x for x in g) - set(g))}. Faute E-028 (brief 004 : "
            f"ratio annoncé 3,0:1, ratio réel 1,29:1).")
    if len(set(g)) != len(g):
        raise GrilleAlteree(f"GRILLE À POINTS DUPLIQUÉS : {g} — repondération déguisée.")
    if len(g) != len(GRILLE_SIGMA):
        raise GrilleAlteree(
            f"GRILLE DE TAILLE {len(g)} ALORS QUE {len(GRILLE_SIGMA)} EST DÉCLARÉE.")
    emp = _empreinte(g)
    if emp != _EMPREINTE_GRILLE_ATTENDUE:
        raise GrilleAlteree(
            f"EMPREINTE DE GRILLE ROMPUE\n  attendue : {_EMPREINTE_GRILLE_ATTENDUE}"
            f"\n  obtenue  : {emp}\n  La grille a été modifiée après déclaration.")
    return {"grille": g, "empreinte_sha256": emp, "symetrique": True,
            "n_points": len(g), "horizon_seances": HORIZON_SEANCES}


def bornes_bandes(grille=GRILLE_SIGMA) -> list[tuple[float, float]]:
    """Bandes autour de chaque point de grille : frontières aux milieux.

    Symétriques par construction puisque la grille l'est. Les deux bandes
    extrêmes sont ouvertes : aucune queue ne peut être supprimée.
    """
    verifier_grille(grille)
    g = sorted(grille)
    milieux = [(g[i] + g[i + 1]) / 2.0 for i in range(len(g) - 1)]
    bornes = []
    for i in range(len(g)):
        bas = -math.inf if i == 0 else milieux[i - 1]
        haut = math.inf if i == len(g) - 1 else milieux[i]
        bornes.append((bas, haut))
    return bornes


# Vérification à l'import : le module ne se charge pas sur une grille fausse.
_ETAT_GRILLE = verifier_grille()


# =====================================================================
# §2  CHARGEMENT, PROFONDEUR, FRAÎCHEUR
#     Aucune valeur n'entre dans le brief sans sa série, sa date et sa
#     profondeur réelle (E-002, R-011, E-014).
# =====================================================================

def charger_series(repertoire: Path | None = None) -> dict[str, pd.Series]:
    """Charge chaque CSV `date,value` en série indexée par date, triée.

    Le répertoire est résolu à l'APPEL, jamais à la définition : le banc de
    test doit pouvoir substituer un dépôt amputé sans réécrire le moteur.
    """
    repertoire = HIST if repertoire is None else repertoire
    series: dict[str, pd.Series] = {}
    if not repertoire.exists():
        return series
    for f in sorted(repertoire.glob("*.csv")):
        sid = f.stem
        try:
            df = pd.read_csv(f)
        except Exception:
            continue
        if not {"date", "value"}.issubset(df.columns):
            continue
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df["value"] = pd.to_numeric(df["value"], errors="coerce")
        df = df.dropna().sort_values("date")
        if df.empty:
            continue
        series[sid] = pd.Series(df["value"].to_numpy(float),
                                index=pd.DatetimeIndex(df["date"]), name=sid)
    return series


def periodicite(s: pd.Series) -> str:
    """'ouvree' (quotidienne ouvrée) ou 'mensuelle', mesurée, jamais supposée."""
    if len(s) < 3:
        return "indeterminee"
    ecart = float(np.median(np.diff(s.index.values).astype("timedelta64[D]").astype(float)))
    if ecart <= 7.0:
        return "ouvree"
    if 25.0 <= ecart <= 35.0:
        return "mensuelle"
    return "indeterminee"


def date_arrete_unique(series: dict[str, pd.Series], noyau: set[str]) -> pd.Timestamp:
    """Une seule date d'arrêté pour tout le document (contrôle 1, E-014).

    C'est la date la plus récente à laquelle TOUTES les séries quotidiennes
    du noyau disposent d'une observation. Elle n'est pas choisie : elle est
    le minimum des dernières dates. Aucun poste ne peut être retardé au
    profit d'une thèse.
    """
    dernieres = [s.index[-1] for sid, s in series.items()
                 if sid in noyau and periodicite(s) == "ouvree"]
    if not dernieres:
        raise RenduRefuse("aucune série quotidienne du noyau : date d'arrêté impossible")
    return min(dernieres)


def diagnostic_series(sid: str, s: pd.Series, arrete: pd.Timestamp) -> dict:
    """Profondeur réelle, retard sur l'arrêté, percentiles gradués."""
    per = periodicite(s)
    fenetres = FENETRES_PERCENTILE if per != "mensuelle" else FENETRES_PERCENTILE_MENSUEL
    s_arr = s[s.index <= arrete]
    if s_arr.empty:
        s_arr = s
    n = int(len(s_arr))
    debut, fin = s_arr.index[0], s_arr.index[-1]
    annees = float((fin - debut).days) / 365.25
    if per == "ouvree":
        retard = int(np.busday_count(fin.date(), arrete.date()))
    else:
        retard = int((arrete - fin).days)
    courant = float(s_arr.iloc[-1])

    percentiles = {}
    for nom, requis in fenetres.items():
        if requis is None:
            fen = s_arr
            drapeau, ecart_pct = "suffisante", 0.0
            libelle = f"echantillon complet ({n} obs, {annees:.2f} ans)"
        else:
            dispo = n
            ratio = dispo / requis
            if dispo >= requis:
                drapeau = "suffisante"
            elif ratio >= SEUIL_PROFONDEUR_MARGINALE:
                drapeau = "marginale"
            else:
                drapeau = "insuffisante"
            ecart_pct = 100.0 * (dispo - requis) / requis
            fen = s_arr.iloc[-requis:]
            libelle = (f"{nom} — requis {requis} obs, disponible {min(dispo, requis)} obs "
                       f"({ecart_pct:+.1f} %)")
        if drapeau == "insuffisante":
            valeur = None            # R-011 : un percentile tronqué est un mensonge
        else:
            valeur = float(100.0 * (fen.to_numpy() <= courant).mean())
        percentiles[nom] = {"percentile": valeur, "drapeau": drapeau,
                            "ecart_pct_vs_requis": round(ecart_pct, 1),
                            "n_utilise": int(len(fen)), "libelle": libelle,
                            "debut_fenetre": str(fen.index[0].date()),
                            "fin_fenetre": str(fen.index[-1].date())}

    hist = s_arr.to_numpy()
    return {
        "serie": sid, "role": SENS_SERIE.get(sid, {}).get("role", "NON_DECLARE"),
        "signe_risque": SENS_SERIE.get(sid, {}).get("signe_risque"),
        "periodicite": per, "convention": CONVENTION.get(sid, "NON_DECLAREE"),
        "valeur": courant, "date_valeur": str(fin.date()),
        "retard_vs_arrete": retard,
        "n_obs": n, "debut": str(debut.date()), "fin": str(fin.date()),
        "profondeur_annees": round(annees, 2),
        "maximum": float(hist.max()), "minimum": float(hist.min()),
        "date_maximum": str(s_arr.idxmax().date()), "date_minimum": str(s_arr.idxmin().date()),
        "ecart_au_maximum_pct": (float(100.0 * (courant / hist.max() - 1.0))
                                 if hist.max() != 0 else None),
        "percentiles": percentiles,
    }


def controle_production(series: dict[str, pd.Series], diags: dict[str, dict]) -> dict:
    """Mécanisme d'`apollon_data.py` : production_autorisee = not manquantes.

    Un manque sur le noyau BLOQUE. Un manque sur un domaine FERME le
    domaine : aucune thèse ne peut en sortir. Une lacune n'est jamais une
    réserve de méthode (R-028).
    """
    presentes = set(series)
    manquantes_noyau = sorted(SERIES_NOYAU - presentes)
    manquantes_doctrine = sorted(SERIES_OBLIGATOIRES_DOCTRINE - presentes)
    domaines_fermes = {d: sorted(set(l) - presentes)
                       for d, l in DOMAINES.items() if set(l) - presentes}
    perimees = sorted(sid for sid in SERIES_NOYAU & presentes
                      if diags[sid]["periodicite"] == "ouvree"
                      and diags[sid]["retard_vs_arrete"] > RETARD_MAX_SEANCES)
    non_declarees = sorted(presentes - set(SENS_SERIE))
    return {
        "series_presentes": sorted(presentes),
        "manquantes_noyau": manquantes_noyau,
        "manquantes_liste_doctrine": manquantes_doctrine,
        "series_perimees_vs_arrete": perimees,
        "series_sans_sens_declare": non_declarees,
        "domaines_fermes": domaines_fermes,
        "retard_max_tolere_seances": RETARD_MAX_SEANCES,
        "production_autorisee": (not manquantes_noyau) and (not perimees)
                                and (not non_declarees),
    }


# =====================================================================
# §3  IDENTITÉS COMPTABLES ET REDONDANCE
#     Quatre séries de taux partagent DGS10. Deux séries liées par une
#     identité ne comptent jamais pour deux confirmations.
# =====================================================================

def verifier_identites(series: dict[str, pd.Series], arrete: pd.Timestamp) -> list[dict]:
    resultats = []
    for cible, membres, signes, texte in IDENTITES:
        if cible not in series or any(m not in series for m in membres):
            resultats.append({"identite": texte, "verifiable": False,
                              "motif": "série absente du dépôt"})
            continue
        df = pd.concat([series[cible]] + [series[m] for m in membres], axis=1,
                       join="inner").dropna()
        df = df[df.index <= arrete]
        if df.empty:
            resultats.append({"identite": texte, "verifiable": False,
                              "motif": "aucune date commune"})
            continue
        recompose = sum(sg * df.iloc[:, 1 + i].to_numpy()
                        for i, sg in enumerate(signes))
        residu = df.iloc[:, 0].to_numpy() - recompose
        resultats.append({
            "identite": texte, "verifiable": True,
            "n_dates_communes": int(len(df)),
            "debut": str(df.index[0].date()), "fin": str(df.index[-1].date()),
            "residu_moyen": float(np.mean(residu)),
            "residu_absolu_max": float(np.max(np.abs(residu))),
            "tolerance": TOLERANCE_IDENTITE,
            "identite_verifiee": bool(np.max(np.abs(residu)) <= TOLERANCE_IDENTITE),
            "fraction_hors_tolerance": float(np.mean(np.abs(residu) > TOLERANCE_IDENTITE)),
            "membres": [cible, *membres],
        })
    return resultats


class Classes:
    """Union-find : regroupe les séries qui ne sont pas des confirmations
    indépendantes (identité comptable exacte, ou corrélation des variations
    à l'horizon au-dessus du seuil déclaré)."""

    def __init__(self):
        self.parent: dict[str, str] = {}

    def _r(self, x: str) -> str:
        self.parent.setdefault(x, x)
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def unir(self, a: str, b: str) -> None:
        ra, rb = self._r(a), self._r(b)
        if ra != rb:
            self.parent[rb] = ra

    def classe(self, x: str) -> str:
        return self._r(x)

    def n_classes(self, membres) -> int:
        return len({self._r(m) for m in membres})


def construire_redondances(series: dict[str, pd.Series], arrete: pd.Timestamp,
                           identites: list[dict]) -> tuple[Classes, list[dict]]:
    cl = Classes()
    for sid in series:
        cl.classe(sid)
    journal = []
    for r in identites:
        if r.get("verifiable") and r.get("identite_verifiee"):
            membres = r["membres"]
            for m in membres[1:]:
                cl.unir(membres[0], m)
            journal.append({"type": "identite_comptable", "motif": r["identite"],
                            "membres": membres,
                            "residu_absolu_max": r["residu_absolu_max"]})
    # Redondance empirique : corrélation des variations à l'horizon
    ids = sorted(series)
    chg: dict[str, pd.Series] = {}
    for sid in ids:
        s = series[sid]
        s = s[s.index <= arrete]
        h = HORIZON_SEANCES if periodicite(s) != "mensuelle" else HORIZON_MOIS
        if len(s) <= h + 5:
            continue
        v = s.to_numpy(float)
        if CONVENTION.get(sid) == "log":
            if np.any(v <= 0):
                continue
            d = np.log(v[h:]) - np.log(v[:-h])
        else:
            d = v[h:] - v[:-h]
        chg[sid] = pd.Series(d, index=s.index[h:])
    for i, a in enumerate(sorted(chg)):
        for b in sorted(chg)[i + 1:]:
            df = pd.concat([chg[a], chg[b]], axis=1, join="inner").dropna()
            if len(df) < 100:
                continue
            c = float(np.corrcoef(df.iloc[:, 0], df.iloc[:, 1])[0, 1])
            if abs(c) >= SEUIL_REDONDANCE_CORR:
                cl.unir(a, b)
                journal.append({"type": "correlation_variations", "membres": [a, b],
                                "correlation": round(c, 4), "n": int(len(df)),
                                "seuil": SEUIL_REDONDANCE_CORR})
    return cl, journal


# =====================================================================
# §4  DISTRIBUTION EMPIRIQUE À L'HORIZON
#     σ est MESURÉ. Les probabilités des scénarios sont des FRÉQUENCES
#     HISTORIQUES dans chaque bande, jamais un jugement. L'effectif de
#     chaque bande est publié ; sous 20 observations, la bande est
#     déclarée NON ESTIMABLE.
# =====================================================================

def variations_horizon(s: pd.Series, sid: str, arrete: pd.Timestamp,
                       motif: list | None = None) -> tuple[np.ndarray, int]:
    s = s[s.index <= arrete].dropna()
    h = HORIZON_SEANCES if periodicite(s) != "mensuelle" else HORIZON_MOIS
    v = s.to_numpy(float)
    if len(v) <= h + 1:
        if motif is not None:
            motif.append(f"historique insuffisant : {len(v)} obs pour un horizon de {h}")
        return np.array([]), h
    if CONVENTION.get(sid) == "log":
        if np.any(v <= 0):
            if motif is not None:
                n_neg = int(np.count_nonzero(v <= 0))
                i = int(np.argmin(v))
                motif.append(
                    f"convention log inapplicable : {n_neg} observation(s) "
                    f"non strictement positive(s), minimum {v[i]:.4g} le "
                    f"{s.index[i].date()}. Le prix a été négatif : aucun "
                    f"log-rendement n'existe. La série est déclarée NON "
                    f"SCÉNARISABLE plutôt que corrigée en silence.")
            return np.array([]), h
        d = np.log(v[h:]) - np.log(v[:-h])
    else:
        d = v[h:] - v[:-h]
    return d.astype(float), h


def _phi(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def distribution_scenarios(sid: str, s: pd.Series, arrete: pd.Timestamp) -> dict:
    """Grille symétrique + fréquences empiriques + double confrontation.

    Deux jeux de probabilités sont produits :
      - `centre_zero`   : bandes centrées sur 0, la dérive historique de
                          l'échantillon apparaît dans les fréquences ;
      - `sans_derive`   : bandes centrées sur la moyenne d'échantillon,
                          la dérive est retirée.
    Une thèse dont l'espérance change de signe entre les deux est réputée
    portée par la dérive en échantillon, et refusée.
    """
    etat = verifier_grille()
    motif: list[str] = []
    d, h = variations_horizon(s, sid, arrete, motif)
    if d.size == 0:
        return {"serie": sid, "estimable": False,
                "motif": motif[0] if motif else "série non scénarisable",
                "horizon": h}

    sigma_direct = float(np.std(d, ddof=1))
    mu = float(np.mean(d))
    # Trois estimateurs indépendants de σ à l'horizon (vérification croisée
    # INTERNE — voir §14 de la sortie : la vérification tierce EXTERNE n'est
    # pas effectuée et est déclarée non satisfaite).
    v = s[s.index <= arrete].to_numpy(float)
    if CONVENTION.get(sid) == "log":
        pas = np.diff(np.log(v))
    else:
        pas = np.diff(v)
    sigma_racine_h = float(np.std(pas, ddof=1) * math.sqrt(h))
    blocs = d[::h]
    sigma_blocs = float(np.std(blocs, ddof=1)) if len(blocs) > 2 else float("nan")
    ests = [x for x in (sigma_direct, sigma_racine_h, sigma_blocs) if np.isfinite(x) and x > 0]
    ecart_estimateurs = (max(ests) / min(ests) - 1.0) if len(ests) > 1 else float("nan")

    bornes = bornes_bandes()
    n = int(d.size)
    n_effectif = int(max(1, round(n / h)))   # blocs indépendants (chevauchement)

    def bandes_pour(centre: float) -> list[dict]:
        out = []
        for k, (bas, haut) in zip(GRILLE_SIGMA, bornes):
            lo = centre + bas * sigma_direct if math.isfinite(bas) else -math.inf
            hi = centre + haut * sigma_direct if math.isfinite(haut) else math.inf
            masque = (d > lo) & (d <= hi) if math.isfinite(lo) else (d <= hi)
            cnt = int(np.count_nonzero(masque))
            p_emp = cnt / n
            p_gauss = _phi((hi - centre) / sigma_direct if math.isfinite(hi) else 40.0) - \
                      _phi((lo - centre) / sigma_direct if math.isfinite(lo) else -40.0)
            ratio = (p_emp / p_gauss) if p_gauss > 0 and p_emp > 0 else (
                float("inf") if p_emp > 0 else 0.0)
            out.append({
                "k_sigma": float(k),
                "borne_basse_sigma": bas, "borne_haute_sigma": haut,
                "borne_basse_valeur": None if not math.isfinite(lo) else float(lo),
                "borne_haute_valeur": None if not math.isfinite(hi) else float(hi),
                "n_observations": cnt,
                "n_effectif_independant": int(max(0, round(cnt / h))),
                "probabilite_empirique": float(p_emp),
                "probabilite_gaussienne": float(p_gauss),
                "ratio_empirique_sur_gaussienne": None if not np.isfinite(ratio) else float(ratio),
                "ecart_declare_facteur_2": bool(
                    (np.isfinite(ratio) and (ratio >= SEUIL_ECART_LOI or
                                             (ratio > 0 and ratio <= 1 / SEUIL_ECART_LOI)))
                    or not np.isfinite(ratio)),
                "estimable": cnt >= MIN_OBS_BANDE,
            })
        return out

    b0 = bandes_pour(0.0)
    b1 = bandes_pour(mu)
    somme = sum(x["probabilite_empirique"] for x in b0)
    if abs(somme - 1.0) > 1e-9:
        raise RenduRefuse(
            f"{sid} : les probabilités de bandes somment à {somme:.6f} au lieu de 1. "
            f"Les bandes ne couvrent pas la droite réelle — une queue a été perdue.")

    return {
        "serie": sid, "estimable": True, "horizon": h,
        "convention": CONVENTION.get(sid),
        "n_variations": n, "n_effectif_independant": n_effectif,
        "chevauchement": h,
        "debut_echantillon": str(s.index[0].date()),
        "fin_echantillon": str(min(s.index[-1], arrete).date()),
        "sigma_horizon": sigma_direct,
        "sigma_horizon_racine_h": sigma_racine_h,
        "sigma_horizon_blocs_disjoints": sigma_blocs,
        "ecart_relatif_estimateurs": None if not np.isfinite(ecart_estimateurs) else float(ecart_estimateurs),
        "derive_moyenne_horizon": mu,
        "derive_en_sigma": float(mu / sigma_direct) if sigma_direct > 0 else None,
        "bandes_centre_zero": b0,
        "bandes_sans_derive": b1,
        "bandes_non_estimables": [x["k_sigma"] for x in b0 if not x["estimable"]],
        "empreinte_grille": etat["empreinte_sha256"],
    }


def p_barriere(a_sigma: float, sigma_h: float, d: np.ndarray, h: int) -> dict:
    """Probabilité de FRANCHISSEMENT (R-031) : calculée, jamais estimée à vue.

    Deux méthodes publiées côte à côte :
      - réflexion (marche sans dérive) : P(max ≥ a) = 2·(1 − Φ(a/σ_H)) ;
      - base historique : fréquence des fenêtres de h séances dont l'extrême
        a franchi a.
    """
    a = abs(a_sigma) * sigma_h
    p_refl = 2.0 * (1.0 - _phi(a / sigma_h)) if sigma_h > 0 else float("nan")
    return {"seuil_sigma": abs(a_sigma), "seuil_valeur": float(a),
            "p_reflexion": float(min(1.0, max(0.0, p_refl))),
            "methode": "réflexion sans dérive : P(max ≥ a) = 2·(1 − Φ(a/σ_H))",
            "p_base_historique_terminale": float(np.mean(np.abs(d) >= a)) if d.size else None,
            "n_base": int(d.size)}


# =====================================================================
# §5  P&L PAR INSTRUMENT — calculé, jamais posé
#     Convention unique pour tous les candidats : rendement EXCÉDENTAIRE
#     sur le taux sans risque (DFF), à l'horizon de la grille.
#     Un instrument dont le P&L n'est pas calculable depuis le dépôt seul
#     est déclaré NON ADMISSIBLE, et le motif est publié.
# =====================================================================

def prix_obligation_pair(y: float, maturite: float, y_actualisation: float) -> float:
    """Prix d'une obligation au pair de coupon `y`, actualisée à `y_actualisation`.
    Semestriel. Aucun paramètre libre : coupon et actualisation viennent
    tous deux de la série de rendement."""
    n = int(round(maturite * 2))
    c = y / 2.0
    r = y_actualisation / 2.0
    if abs(r) < 1e-12:
        return c * n + 1.0
    a = (1.0 - (1.0 + r) ** (-n)) / r
    return c * a + (1.0 + r) ** (-n)


def rendement_directionnel(sid: str, k: float, dist: dict, niveau: float,
                           taux_cash: float) -> float:
    """Rendement excédentaire d'une position unitaire qui GAGNE quand la
    série MONTE, pour le point de grille k. Le sens de la position est
    appliqué ensuite (`direction × ce rendement`)."""
    sigma_h = dist["sigma_horizon"]
    portage_cash = taux_cash * HORIZON_SEANCES / 252.0
    if sid in MATURITE_OBLIGATION:
        # position sur le RENDEMENT : gagne quand le taux monte => vendeuse
        # de l'obligation. Repricing exact, convexité incluse.
        y0 = niveau / 100.0
        dy = (k * sigma_h) / 100.0
        T = MATURITE_OBLIGATION[sid]
        p0 = prix_obligation_pair(y0, T, y0)
        p1 = prix_obligation_pair(y0, T, y0 + dy)
        rendement_prix = p1 / p0 - 1.0
        portage_obl = y0 * HORIZON_SEANCES / 252.0
        excedent_obligation = rendement_prix + portage_obl - portage_cash
        return -excedent_obligation
    if CONVENTION.get(sid) == "log":
        return math.exp(k * sigma_h) - 1.0 - portage_cash
    raise RenduRefuse(f"{sid} : aucune convention de P&L déclarée")


def instrument_admissible(sid: str) -> tuple[bool, str]:
    if sid in INSTRUMENTS_NON_CALCULABLES:
        return False, ("P&L non calculable depuis le dépôt : l'OAS est un spread, "
                       "et le dépôt ne contient pas le rendement de l'indice, donc "
                       "pas la duration de spread. Aucune valeur ne peut être "
                       "produite sans un chiffre extérieur aux données (E-002).")
    if sid in MATURITE_OBLIGATION or CONVENTION.get(sid) == "log":
        return True, ""
    return False, "instrument sans convention de P&L déclarée"


# =====================================================================
# §6  COUPLES ET SENS — refus de rendu
# =====================================================================

def controler_couples(series_publiees) -> list[dict]:
    """E-005. Publier un membre d'un couple sans l'autre est impossible."""
    ens = set(series_publiees)
    manquements = []
    for a, b in COUPLES_OBLIGATOIRES:
        if a in ens and b not in ens:
            manquements.append({"publie": a, "manquant": b, "couple": [a, b]})
        if b in ens and a not in ens:
            manquements.append({"publie": b, "manquant": a, "couple": [a, b]})
    return manquements


def rendre_bloc_series(series_publiees, diags: dict[str, dict]) -> str:
    """Rendu de la table des séries. REFUSE si un couple est incomplet."""
    manquements = controler_couples(series_publiees)
    if manquements:
        detail = " ; ".join(f"{m['publie']} publié sans {m['manquant']}"
                            for m in manquements)
        raise RenduRefuse(
            "RENDU REFUSÉ — COUPLE OBLIGATOIRE INCOMPLET : " + detail +
            ". Faute E-005 : le brief 001 a publié une inflation globale de "
            "3,4 % sans le sous-jacent à 2,5 % ; les 90 pb d'écart étaient "
            "intégralement énergétiques et inversaient la lecture de la Fed.")
    lignes = ["| série | rôle déclaré | valeur | date | retard | n obs | profondeur | "
              "pct 1 an | pct 5 ans | pct complet |",
              "|---|---|---:|---|---:|---:|---:|---:|---:|---:|"]
    for sid in sorted(series_publiees):
        d = diags[sid]
        p = d["percentiles"]

        def _p(nom):
            x = p[nom]
            if x["percentile"] is None:
                return f"REFUSÉ ({x['drapeau']}, {x['ecart_pct_vs_requis']:+.0f} %)"
            marque = "" if x["drapeau"] == "suffisante" else f" ({x['drapeau']})"
            return f"{x['percentile']:.1f}{marque}"

        lignes.append(
            f"| {sid} | {d['role']} | {d['valeur']:.4g} | {d['date_valeur']} | "
            f"{d['retard_vs_arrete']} | {d['n_obs']} | {d['profondeur_annees']:.2f} ans | "
            f"{_p('1 an')} | {_p('5 ans')} | {_p('echantillon complet')} |")
    return "\n".join(lignes)


def controler_sens(theses) -> list[dict]:
    """E-007. Deux lectures opposées de la même série font refuser le brief."""
    lectures: dict[str, list[tuple[str, int]]] = {}
    conflits = []
    for t in theses:
        for sid, signe in t.lectures.items():
            declare = SENS_SERIE.get(sid, {}).get("signe_risque")
            if declare is None:
                conflits.append({"type": "serie_sans_sens_declare", "serie": sid,
                                 "these": t.identifiant})
            elif signe != declare:
                conflits.append({"type": "lecture_inverse_table", "serie": sid,
                                 "these": t.identifiant, "lecture": signe,
                                 "sens_declare": declare,
                                 "role": SENS_SERIE[sid]["role"]})
            lectures.setdefault(sid, []).append((t.identifiant, signe))
    for sid, lst in lectures.items():
        signes = {sg for _, sg in lst}
        if len(signes) > 1:
            conflits.append({
                "type": "double_sens_entre_theses", "serie": sid,
                "role": SENS_SERIE.get(sid, {}).get("role"),
                "theses": [{"these": i, "lecture": sg} for i, sg in lst],
                "motif": (f"{sid} lue dans deux sens opposés dans le même brief. "
                          f"Faute E-007 : le spread haut rendement servait de "
                          f"signal de vente du crédit et d'indicateur avancé "
                          f"haussier des actions ; ensemble, les deux "
                          f"impliquaient la conclusion inverse.")})
    return conflits


# =====================================================================
# §7  LA THÈSE — objet typé, falsifiable, ou inexistante
# =====================================================================

@dataclass
class These:
    identifiant: str
    enonce: str                       # gabarit rempli APRÈS exécution du test
    series_utilisees: list            # doivent exister dans les données
    sens: str                         # cohérent avec la table des sens
    test: Callable                    # renvoie un booléen calculé sur les données
    invalidation: str                 # un FAIT observable et daté
    horizon_jours: int
    esperance_pct: float = 0.0        # calculée, jamais écrite
    # --- champs typés supplémentaires (R-038 : rien de franchissable
    #     par une chaîne non vide)
    instrument: str = ""
    direction: int = 0
    regle_confirmation: str = ""
    lectures: dict = field(default_factory=dict)
    invalidation_serie: str = ""
    invalidation_date: str = ""
    invalidation_test: Callable | None = None
    scenarios: list = field(default_factory=list)
    diagnostics: dict = field(default_factory=dict)
    echecs: list = field(default_factory=list)
    verdict: str = "REFUSEE"


def invalidation_est_un_fait(texte: str, serie: str, date_obs: str,
                             instrument: str) -> tuple[bool, str]:
    """Une invalidation qui est un niveau de prix est REJETÉE, pas signalée."""
    if MOTIFS_NIVEAU_DE_PRIX.search(texte or ""):
        return False, ("invalidation exprimée comme un niveau de prix ou un stop "
                       "— la doctrine exige un FAIT observable et daté (R-038 : "
                       "« ou stop à −1σ touché » était exactement un niveau de prix)")
    if serie not in SERIES_PUBLICATION_DATEE:
        return False, (f"invalidation adossée à « {serie} » : hors du calendrier "
                       f"de publication daté {SERIES_PUBLICATION_DATEE}")
    if serie == instrument:
        return False, "invalidation adossée à l'instrument lui-même (circulaire)"
    try:
        datetime.strptime(date_obs, "%Y-%m-%d")
    except Exception:
        return False, f"date d'observation invalide : « {date_obs} »"
    return True, ""



# ---------------------------------------------------------------------
# CALENDRIER OFFICIEL — le catalyseur cesse d'être déduit
#
# `prochaine_publication` extrapolait la cadence OBSERVÉE de la série :
# médiane des écarts, puis addition. C'est une ESTIMATION, pas un fait
# daté — et le critère 10 exige un fait. Le calendrier ALFRED, collecté
# par apollon_data.py, porte les dates réelles annoncées par l'émetteur.
#
# R-044 — un instrument collecté et lu par personne est du code mort.
# Ce bloc est la contrepartie de la collecte : sans lui, le calendrier
# serait la neuvième occurrence du mode de défaillance dominant.
# ---------------------------------------------------------------------
CALENDRIER = BASE / "data" / "calendrier_publications.csv"

# Quelle publication officielle date quelle série.
RELEASE_DE_SERIE = {
    "CPIAUCSL": 10, "CPILFESL": 10,       # Consumer Price Index
    "UNRATE": 50,  "PAYEMS": 50,          # Employment Situation
    "INDPRO": 13,                          # Production industrielle (G.17)
}


def charger_calendrier(chemin: Path | None = None) -> dict:
    """Dates officielles à venir, par release. {} si le fichier est absent."""
    chemin = CALENDRIER if chemin is None else chemin
    if not chemin.exists():
        return {}
    try:
        d = pd.read_csv(chemin)
    except Exception:                                       # noqa: BLE001
        return {}
    if not {"release_id", "date"}.issubset(d.columns):
        return {}
    par_release: dict[int, list[str]] = {}
    for rid, grp in d.groupby("release_id"):
        try:
            par_release[int(rid)] = sorted(str(x) for x in grp["date"])
        except Exception:                                   # noqa: BLE001
            continue
    return par_release


def publication_officielle(serie: str, arrete: pd.Timestamp,
                           calendrier: dict) -> tuple[str, str]:
    """(date, origine). Origine vaut 'officielle' ou 'deduite'.

    L'origine est publiée avec la date : une date extrapolée et une date
    annoncée ne se valent pas, et le brief doit dire laquelle il utilise.
    """
    rid = RELEASE_DE_SERIE.get(serie)
    if rid and calendrier.get(rid):
        borne = str(arrete.date())
        futures = [j for j in calendrier[rid] if j > borne]
        if futures:
            return futures[0], "officielle"
    return "", "deduite"


def prochaine_publication(s: pd.Series, arrete: pd.Timestamp,
                          serie: str = "", calendrier: dict | None = None) -> str:
    """Date officielle si le calendrier la porte ; sinon cadence observée.

    Aucune date n'est jamais saisie à la main : elle vient du calendrier
    collecté, ou d'une extrapolation déclarée comme telle.
    """
    if serie and calendrier:
        officielle, origine = publication_officielle(serie, arrete, calendrier)
        if origine == "officielle":
            return officielle
    idx = s[s.index <= arrete].index
    if len(idx) < 3:
        return ""
    cadence = float(np.median(np.diff(idx.values).astype("timedelta64[D]").astype(float)))
    prochaine = idx[-1] + pd.Timedelta(days=cadence)
    while prochaine <= arrete:
        prochaine = prochaine + pd.Timedelta(days=cadence)
    return str(prochaine.date())


# --- LE PORTIER : une seule fonction, appelée une seule fois par candidat
#     (R-038 — la structure d'une position ne peut pas créer un critère)
CRITERES = [
    "1_series_presentes", "2_domaine_ouvert", "3_instrument_calculable",
    "4_profondeur_suffisante", "5_bandes_estimables", "6_couples_complets",
    "7_lecture_conforme_table", "8_confirmations_independantes",
    "9_test_execute_et_vrai", "10_invalidation_fait_date",
    "11_invalidation_non_deja_survenue", "12_esperance_positive",
    "13_esperance_non_portee_par_derive", "14_esperance_stable_dans_le_temps",
    "16_arete_conditionnelle_mesuree",
    "15_enonce_sans_affirmation_politique_non_etayee",
]


def esperance_sur_grille(bandes: list[dict], pnl: dict[float, float]) -> float:
    verifier_grille()
    if len(bandes) != len(GRILLE_SIGMA):
        raise GrilleAlteree(f"{len(bandes)} bandes pour {len(GRILLE_SIGMA)} points de grille")
    return float(sum(b["probabilite_empirique"] * pnl[b["k_sigma"]] for b in bandes))


def percentile_utilisable(diag: dict) -> tuple[float | None, str, str]:
    """Fenêtre la plus longue dont la profondeur n'est pas insuffisante.
    Règle déclarée, appliquée identiquement à toutes les séries et aux deux
    directions de pari : ce n'est pas un paramètre libre."""
    for nom in ("5 ans", "1 an"):
        p = diag["percentiles"].get(nom)
        if p and p["percentile"] is not None:
            return p["percentile"], nom, p["drapeau"]
    return None, "", "insuffisante"



# =====================================================================
# §9 bis  L'ARÊTE CONDITIONNELLE — E-050 / R-051
#
# DÉFAUT CORRIGÉ. Jusqu'au 17/08, la règle de confirmation n'était
# évaluée QU'À LA DATE DU JOUR. L'espérance publiée était donc calculée
# sur la distribution INCONDITIONNELLE des variations : elle mesurait la
# dérive de la série, pas la capacité prédictive de la règle.
#
# Contrôle positif qui l'a établi : une arête plantée à t = 20,2
# (+10,96 points d'écart entre quartile haut et bas du VIX) laissait les
# compteurs d'échec IDENTIQUES au candidat près, et FAISAIT BAISSER
# l'espérance publiée de +0,1911 % à +0,0487 %.
#
# Ce bloc évalue la règle À CHAQUE DATE de l'historique, avec la seule
# information disponible à cette date, et compare le rendement futur
# quand la règle est vérifiée à celui quand elle ne l'est pas.
# =====================================================================

def percentile_glissant(s: pd.Series, fenetre: int | None) -> pd.Series:
    """Percentile de chaque observation dans sa propre fenêtre passée.

    Aucun regard vers l'avenir : le rang à la date t n'utilise que les
    observations jusqu'à t incluse.
    """
    if fenetre is None:
        return s.expanding(min_periods=60).rank(pct=True) * 100.0
    return s.rolling(fenetre, min_periods=max(20, fenetre // 4)).rank(pct=True) * 100.0


def masque_confirmation_historique(instr, dossier, direction, regle, series,
                                   arrete, h, profondeur, classes) -> dict:
    """Vrai à chaque date où la règle de confirmation AURAIT été vérifiée.

    Le masque est aligné sur les rendements futurs : l'élément i correspond
    au rendement de la date i à la date i+h, et n'utilise que l'information
    disponible EN i.
    """
    si = series[instr]
    si = si[si.index <= arrete].dropna()
    if len(si) <= h + 1:
        return {"disponible": False, "motif": "historique insuffisant"}
    dates = si.index[:-h]                       # dates de DÉCISION
    sens_pari = direction * SENS_SERIE.get(instr, {}).get("signe_risque", 0)
    per_instr = periodicite(si)

    satisfaites: dict[str, np.ndarray] = {}
    for sid in dossier:
        if sid == instr or sid not in series or sid not in SENS_SERIE:
            continue
        info = profondeur.get(sid) or {}
        nom_fen = info.get("fenetre_utilisee")
        if not nom_fen:
            continue
        table = (FENETRES_PERCENTILE if periodicite(series[sid]) != "mensuelle"
                 else FENETRES_PERCENTILE_MENSUEL)
        fen = table.get(nom_fen)
        ss = series[sid]
        ss = ss[ss.index <= arrete].dropna()
        if ss.empty:
            continue
        pct = percentile_glissant(ss, fen).reindex(dates, method="ffill")
        sg = SENS_SERIE[sid]["signe_risque"]
        niveau = pct if sg > 0 else (100.0 - pct)
        if regle == "aligne":
            sat = (niveau >= 100.0 - SEUIL_CONFIRMATION_PCT) if sens_pari > 0 \
                else (niveau <= SEUIL_CONFIRMATION_PCT)
        else:
            sat = (niveau <= SEUIL_CONFIRMATION_PCT) if sens_pari > 0 \
                else (niveau >= 100.0 - SEUIL_CONFIRMATION_PCT)
        satisfaites[sid] = sat.fillna(False).to_numpy(bool)

    if not satisfaites:
        return {"disponible": False, "motif": "aucune série de confirmation exploitable"}

    n = len(dates)
    masque = np.zeros(n, dtype=bool)
    n_classes_par_date = np.zeros(n, dtype=int)
    for i in range(n):
        retenues = [sid for sid, arr in satisfaites.items() if arr[i]]
        k = classes.n_classes(retenues) if retenues else 0
        n_classes_par_date[i] = k
        masque[i] = k >= MIN_CLASSES_CONFIRMATION
    return {"disponible": True, "masque": masque, "n_dates": n,
            "n_declenchements": int(masque.sum()),
            "n_series_testees": len(satisfaites),
            "classes_medianes": float(np.median(n_classes_par_date))}


def arete_conditionnelle(instr, series, arrete, h, masque, pnl, dist) -> dict:
    """Compare le rendement futur QUAND la règle se déclenche à celui du reste.

    Retourne l'espérance conditionnelle, l'inconditionnelle, l'écart, et
    l'erreur type de l'écart calculée sur le nombre de blocs INDÉPENDANTS
    (les rendements à h jours se chevauchent : n/h, pas n).
    """
    d, h2 = variations_horizon(series[instr], instr, arrete)
    if d.size == 0 or masque is None or len(masque) != d.size:
        return {"mesurable": False,
                "motif": f"alignement impossible ({d.size} rendements, "
                         f"{0 if masque is None else len(masque)} dates)"}
    taille = TAILLE_PCT_NAV / 100.0
    niveau = float(series[instr][series[instr].index <= arrete].dropna().iloc[-1])

    def pnl_de(variations: np.ndarray) -> np.ndarray:
        sig = dist["sigma_horizon"]
        ks = variations / sig if sig else variations * 0.0
        # P&L interpolé sur la grille déclarée — mêmes points, même convention
        gk = np.array(sorted(pnl), dtype=float)
        gv = np.array([pnl[k] for k in sorted(pnl)], dtype=float)
        return np.interp(np.clip(ks, gk[0], gk[-1]), gk, gv)

    dedans, dehors = d[masque], d[~masque]
    if dedans.size < MIN_OBS_BANDE or dehors.size < MIN_OBS_BANDE:
        return {"mesurable": False,
                "motif": f"effectifs insuffisants : {dedans.size} déclenchements, "
                         f"{dehors.size} hors déclenchement (minimum {MIN_OBS_BANDE})"}
    p_in, p_out, p_all = pnl_de(dedans), pnl_de(dehors), pnl_de(d)
    e_in = 100.0 * float(np.mean(p_in)) * taille
    e_out = 100.0 * float(np.mean(p_out)) * taille
    e_all = 100.0 * float(np.mean(p_all)) * taille
    n_in = max(1, dedans.size // h2)          # blocs indépendants
    n_out = max(1, dehors.size // h2)
    se = 100.0 * taille * math.sqrt(float(np.var(p_in, ddof=1)) / n_in
                                    + float(np.var(p_out, ddof=1)) / n_out)
    ecart = e_in - e_out
    return {"mesurable": True,
            "esperance_conditionnelle_pct_nav": e_in,
            "esperance_hors_declenchement_pct_nav": e_out,
            "esperance_inconditionnelle_pct_nav": e_all,
            "ecart_pct_nav": ecart,
            "erreur_type_ecart": se,
            "t_ecart": (ecart / se) if se > 0 else float("nan"),
            "n_declenchements": int(dedans.size),
            "n_blocs_independants_declenchement": int(n_in),
            "n_hors": int(dehors.size),
            "note": ("l'écart mesure la CAPACITÉ PRÉDICTIVE de la règle. "
                     "L'espérance inconditionnelle mesure la dérive de la "
                     "série et ne peut fonder aucune admission (E-050).")}


def engendrer_candidats(series, diags, dists, arrete, classes, ctrl):
    """Énumère la grille complète de candidats déclarée en tête de fichier.
    Aucun candidat n'est ajouté ni retiré : instruments × directions ×
    règles de confirmation, soit N_CANDIDATS_DECLARES."""
    verifier_grille()
    taux_cash = float(diags["DFF"]["valeur"]) / 100.0 if "DFF" in diags else 0.0
    candidats = []
    for instr in sorted(DOSSIER_INSTRUMENT):
        for direction in DIRECTIONS:
            for regle in REGLES_CONFIRMATION:
                candidats.append(evaluer_candidat(
                    instr, direction, regle, series, diags, dists, arrete,
                    classes, ctrl, taux_cash))
    return candidats


def evaluer_candidat(instr, direction, regle, series, diags, dists, arrete,
                     classes, ctrl, taux_cash) -> These:
    ident = f"M{NUMERO_BRIEF}-{instr}-{'HAUSSE' if direction > 0 else 'BAISSE'}-{regle.upper()}"
    dossier = list(DOSSIER_INSTRUMENT[instr])
    echecs: list[str] = []
    diag_crit: dict = {}

    # --- 1. séries présentes
    absentes = [s for s in dossier if s not in series]
    diag_crit["1_series_presentes"] = {"absentes": absentes, "ok": not absentes}
    if absentes:
        echecs.append("1_series_presentes")

    # --- 2. domaine ouvert
    dom = DOMAINE_INSTRUMENT.get(instr, "")
    ferme = dom in ctrl["domaines_fermes"]
    diag_crit["2_domaine_ouvert"] = {"domaine": dom, "ferme": ferme,
                                     "series_manquantes": ctrl["domaines_fermes"].get(dom, []),
                                     "ok": not ferme}
    if ferme:
        echecs.append("2_domaine_ouvert")

    # --- 3. instrument calculable
    ok_instr, motif_instr = instrument_admissible(instr)
    diag_crit["3_instrument_calculable"] = {"ok": ok_instr, "motif": motif_instr}
    if not ok_instr:
        echecs.append("3_instrument_calculable")

    # --- 4. profondeur
    profondeur = {}
    for s in dossier:
        if s not in diags:
            continue
        pct, fen, drap = percentile_utilisable(diags[s])
        profondeur[s] = {"percentile": pct, "fenetre_utilisee": fen, "drapeau": drap,
                         "n_obs": diags[s]["n_obs"],
                         "profondeur_annees": diags[s]["profondeur_annees"],
                         "fenetre_reduite": fen == "1 an"}
    sans_percentile = [s for s, v in profondeur.items() if v["percentile"] is None]
    diag_crit["4_profondeur_suffisante"] = {"detail": profondeur,
                                            "series_sans_percentile": sans_percentile,
                                            "ok": not sans_percentile}
    if sans_percentile:
        echecs.append("4_profondeur_suffisante")

    # --- 5. bandes estimables sur l'instrument
    dist = dists.get(instr, {})
    non_est = dist.get("bandes_non_estimables", None)
    ok_bandes = bool(dist.get("estimable")) and not non_est
    diag_crit["5_bandes_estimables"] = {
        "ok": ok_bandes, "bandes_non_estimables": non_est,
        "min_obs_bande": MIN_OBS_BANDE,
        "effectifs": [{"k": b["k_sigma"], "n": b["n_observations"],
                       "n_effectif": b["n_effectif_independant"]}
                      for b in dist.get("bandes_centre_zero", [])]}
    if not ok_bandes:
        echecs.append("5_bandes_estimables")

    # --- 6. couples obligatoires sur les séries utilisées
    manquements = controler_couples(dossier)
    diag_crit["6_couples_complets"] = {"ok": not manquements, "manquements": manquements}
    if manquements:
        echecs.append("6_couples_complets")

    # --- 7. lectures conformes à la table des sens
    lectures = {s: SENS_SERIE[s]["signe_risque"] for s in dossier if s in SENS_SERIE}
    non_declarees = [s for s in dossier if s not in SENS_SERIE]
    diag_crit["7_lecture_conforme_table"] = {"ok": not non_declarees,
                                             "series_sans_sens": non_declarees,
                                             "lectures": lectures}
    if non_declarees:
        echecs.append("7_lecture_conforme_table")

    # --- 8/9. confirmations indépendantes ET test exécuté
    sens_pari = direction * SENS_SERIE.get(instr, {}).get("signe_risque", 0)
    confirmations = []
    for s in dossier:
        if s == instr or s not in profondeur or profondeur[s]["percentile"] is None:
            continue
        sg = SENS_SERIE[s]["signe_risque"]
        pct = profondeur[s]["percentile"]
        niveau_risque = pct if sg > 0 else 100.0 - pct
        if regle == "aligne":
            satisfait = (niveau_risque >= 100.0 - SEUIL_CONFIRMATION_PCT) if sens_pari > 0 \
                else (niveau_risque <= SEUIL_CONFIRMATION_PCT)
        else:
            satisfait = (niveau_risque <= SEUIL_CONFIRMATION_PCT) if sens_pari > 0 \
                else (niveau_risque >= 100.0 - SEUIL_CONFIRMATION_PCT)
        confirmations.append({"serie": s, "role": SENS_SERIE[s]["role"],
                              "percentile": round(pct, 1),
                              "fenetre": profondeur[s]["fenetre_utilisee"],
                              "niveau_risque_percentile": round(niveau_risque, 1),
                              "satisfait": bool(satisfait),
                              "classe_independance": classes.classe(s)})
    retenues = [c["serie"] for c in confirmations if c["satisfait"]]
    n_classes = classes.n_classes(retenues) if retenues else 0
    diag_crit["8_confirmations_independantes"] = {
        "ok": n_classes >= MIN_CLASSES_CONFIRMATION,
        "n_classes_independantes": n_classes, "minimum": MIN_CLASSES_CONFIRMATION,
        "series_retenues": retenues, "detail": confirmations,
        "note": ("les séries liées par une identité comptable ou corrélées "
                 f"au-delà de {SEUIL_REDONDANCE_CORR} sur les variations à "
                 "l'horizon comptent pour UNE seule confirmation")}
    if n_classes < MIN_CLASSES_CONFIRMATION:
        echecs.append("8_confirmations_independantes")

    def test_confirmation() -> bool:
        """Test exécutable, recalculé sur les données (R-043)."""
        rets = [c["serie"] for c in confirmations if c["satisfait"]]
        return classes.n_classes(rets) >= MIN_CLASSES_CONFIRMATION if rets else False

    try:
        resultat_test = bool(test_confirmation())
        test_erreur = ""
    except Exception as exc:                                    # pragma: no cover
        resultat_test, test_erreur = False, f"{type(exc).__name__}: {exc}"
    diag_crit["9_test_execute_et_vrai"] = {"ok": resultat_test and not test_erreur,
                                           "resultat": resultat_test,
                                           "erreur": test_erreur}
    if not (resultat_test and not test_erreur):
        echecs.append("9_test_execute_et_vrai")

    # --- 10/11. invalidation : un FAIT observable et daté
    serie_inval = next((s for s in dossier if s in SERIES_PUBLICATION_DATEE), "")
    if serie_inval and serie_inval in series:
        _cal = charger_calendrier()
        date_inval = prochaine_publication(series[serie_inval], arrete,
                                           serie_inval, _cal)
        _, _origine_date = publication_officielle(serie_inval, arrete, _cal)
        sg_i = SENS_SERIE[serie_inval]["signe_risque"]
        cible = "s'écarte de la lecture retenue" if sens_pari > 0 else "confirme la détente"
        texte_inval = (
            f"publication de {serie_inval} ({SENS_SERIE[serie_inval]['role']}) "
            f"attendue le {date_inval} : si la variation publiée sur un mois est "
            f"de signe {'négatif' if sens_pari * sg_i > 0 else 'positif'}, "
            f"le dossier de confirmation de cette thèse cesse d'être vérifié "
            f"et la thèse est retirée. Fait observable, daté, indépendant du "
            f"prix de l'instrument.")

        def test_invalidation(_s=serie_inval, _sg=sg_i, _sp=sens_pari) -> bool:
            v = series[_s]
            v = v[v.index <= arrete].to_numpy(float)
            if len(v) < 2:
                return True
            variation = v[-1] - v[-2]
            return bool(_sp * _sg * variation < 0)
    else:
        date_inval, texte_inval, test_invalidation = "", "", None
        _origine_date = "aucune"

    ok_inval, motif_inval = (invalidation_est_un_fait(texte_inval, serie_inval,
                                                      date_inval, instr)
                             if texte_inval else (False, "aucune série de publication datée"))
    diag_crit["10_invalidation_fait_date"] = {
        "ok": ok_inval, "motif": motif_inval, "serie": serie_inval,
        "date": date_inval,
        "origine_date": (_origine_date if serie_inval and serie_inval in series
                         else "aucune"),
        "note": ("« officielle » = date annoncée par l'émetteur, lue dans "
                 "data/calendrier_publications.csv. « deduite » = extrapolée "
                 "de la cadence observée : c'est une estimation, pas un fait "
                 "daté, et le critère l'indique plutôt que de les confondre.")}
    if not ok_inval:
        echecs.append("10_invalidation_fait_date")

    if test_invalidation is not None:
        try:
            deja = bool(test_invalidation())
            err_i = ""
        except Exception as exc:                                # pragma: no cover
            deja, err_i = True, f"{type(exc).__name__}: {exc}"
    else:
        deja, err_i = True, "aucun test d'invalidation exécutable"
    diag_crit["11_invalidation_non_deja_survenue"] = {"ok": not deja,
                                                      "deja_survenue": deja, "erreur": err_i}
    if deja:
        echecs.append("11_invalidation_non_deja_survenue")

    # --- 12/13/14. l'espérance décide (E-018, T-001)
    scenarios, esp, esp_sd, ratio, gmax, pmax = [], float("nan"), float("nan"), None, None, None
    esp_h1 = esp_h2 = float("nan")
    if ok_instr and dist.get("estimable"):
        niveau = diags[instr]["valeur"]
        pnl = {}
        for k in GRILLE_SIGMA:
            r = rendement_directionnel(instr, k, dist, niveau, taux_cash)
            pnl[k] = direction * r
        taille = TAILLE_PCT_NAV / 100.0
        for b in dist["bandes_centre_zero"]:
            k = b["k_sigma"]
            scenarios.append({
                "k_sigma": k,
                "variation_serie": float(k * dist["sigma_horizon"]),
                "probabilite_empirique": b["probabilite_empirique"],
                "probabilite_gaussienne": b["probabilite_gaussienne"],
                "ecart_facteur_2_declare": b["ecart_declare_facteur_2"],
                "n_observations": b["n_observations"],
                "pnl_position_pct": 100.0 * pnl[k],
                "pnl_nav_pct": 100.0 * pnl[k] * taille})
        esp = 100.0 * esperance_sur_grille(dist["bandes_centre_zero"], pnl) * taille
        esp_sd = 100.0 * esperance_sur_grille(dist["bandes_sans_derive"], pnl) * taille
        vals = [s["pnl_nav_pct"] for s in scenarios]
        gmax, pmax = max(vals), min(vals)
        ratio = abs(gmax / pmax) if pmax != 0 else None
        # stabilité temporelle : deux moitiés disjointes de l'échantillon
        s_full = series[instr]
        s_full = s_full[s_full.index <= arrete]
        mid = len(s_full) // 2
        try:
            d1 = distribution_scenarios(instr, s_full.iloc[:mid], arrete)
            d2 = distribution_scenarios(instr, s_full.iloc[mid:], arrete)
            if d1.get("estimable"):
                esp_h1 = 100.0 * esperance_sur_grille(d1["bandes_centre_zero"], pnl) * taille
            if d2.get("estimable"):
                esp_h2 = 100.0 * esperance_sur_grille(d2["bandes_centre_zero"], pnl) * taille
        except Exception:                                       # pragma: no cover
            pass

    ok_esp = np.isfinite(esp) and esp > 0.0
    diag_crit["12_esperance_positive"] = {
        "ok": bool(ok_esp), "esperance_pct_nav": None if not np.isfinite(esp) else esp,
        "gain_maximal_pct_nav": gmax, "perte_maximale_pct_nav": pmax,
        "ratio_gain_max_sur_perte_max": ratio,
        "note": ("le ratio est publié pour information et ne peut jamais fonder "
                 "une admission seul (T-001, faute E-018). L'espérance décide.")}
    if not ok_esp:
        echecs.append("12_esperance_positive")

    # Le critère 13 ne teste QUE la conservation du signe : la positivité est
    # le critère 12. Deux critères ne peuvent pas mesurer la même chose, sinon
    # le décompte des échecs devient illisible (R-034 : réconcilier deux
    # mesures du même document avant publication).
    ok_derive = bool(np.isfinite(esp) and np.isfinite(esp_sd)
                     and esp != 0.0 and np.sign(esp) == np.sign(esp_sd))
    diag_crit["13_esperance_non_portee_par_derive"] = {
        "ok": ok_derive, "esperance_avec_derive": None if not np.isfinite(esp) else esp,
        "esperance_sans_derive": None if not np.isfinite(esp_sd) else esp_sd,
        "derive_en_sigma": dist.get("derive_en_sigma"),
        "note": ("bandes recentrées sur la moyenne d'échantillon : si le signe "
                 "de l'espérance change, elle était portée par la dérive en "
                 "échantillon, pas par la forme de la distribution")}
    if not ok_derive:
        echecs.append("13_esperance_non_portee_par_derive")

    # --- 16. L'ARÊTE CONDITIONNELLE (E-050 / R-051)
    # L'espérance des critères 12 à 14 est INCONDITIONNELLE : elle mesure la
    # dérive de la série. Ce critère mesure ce que la règle de confirmation
    # apporte RÉELLEMENT, en comparant le rendement futur quand elle se
    # déclenche à celui du reste de l'échantillon.
    arete = {"mesurable": False, "motif": "non calculé"}
    if ok_instr and dist.get("estimable") and pnl:
        try:
            mh = masque_confirmation_historique(instr, dossier, direction, regle,
                                                series, arrete, dist.get("horizon", HORIZON_SEANCES),
                                                profondeur, classes)
            if mh.get("disponible"):
                arete = arete_conditionnelle(instr, series, arrete,
                                             dist.get("horizon", HORIZON_SEANCES),
                                             mh["masque"], pnl, dist)
                arete["declenchements"] = mh
            else:
                arete = {"mesurable": False, "motif": mh.get("motif", "masque indisponible")}
        except Exception as exc:                                # pragma: no cover
            arete = {"mesurable": False, "motif": f"{type(exc).__name__}: {exc}"}

    t_arete = arete.get("t_ecart", float("nan")) if arete.get("mesurable") else float("nan")
    ok_arete = bool(np.isfinite(t_arete) and t_arete >= T_MINIMUM_ARETE)
    # PUISSANCE — R-051. Publier ce que le portier PEUT voir, à côté de ce
    # qu'il voit. Sans cette ligne, « 0 thèse » se lit comme une information
    # sur le marché alors que c'est une propriété de l'échantillon.
    se_a = arete.get("erreur_type_ecart", float("nan")) if arete.get("mesurable") else float("nan")
    arete_min = T_MINIMUM_ARETE * se_a if np.isfinite(se_a) else float("nan")
    arete["ecart_minimal_detectable_pct_nav"] = None if not np.isfinite(arete_min) else arete_min
    arete["ecart_minimal_detectable_annualise_pct"] = (
        None if not np.isfinite(arete_min)
        else arete_min * (252.0 / max(1, dist.get("horizon", HORIZON_SEANCES))))
    arete["note_puissance"] = (
        "écart minimal détectable au seuil déclaré. Un écart réel INFÉRIEUR à "
        "ce nombre est invisible pour ce portier, quelle que soit sa réalité : "
        "le refus ne porte alors aucune information sur le marché.")

    diag_crit["16_arete_conditionnelle_mesuree"] = {
        "ok": ok_arete, "t_minimum_exige": T_MINIMUM_ARETE, **arete,
        "note": ("un portier qui n'a jamais mesuré sa capacite a dire OUI ne "
                 "mesure rien quand il dit NON (R-051). Ce critere est le seul "
                 "qui teste une capacite PREDICTIVE ; les criteres 12 a 14 "
                 "testent la forme de la distribution inconditionnelle.")}
    if not ok_arete:
        echecs.append("16_arete_conditionnelle_mesuree")

    ok_stab = bool(np.isfinite(esp_h1) and np.isfinite(esp_h2)
                   and esp_h1 > 0 and esp_h2 > 0)
    diag_crit["14_esperance_stable_dans_le_temps"] = {
        "ok": ok_stab,
        "esperance_premiere_moitie": None if not np.isfinite(esp_h1) else esp_h1,
        "esperance_seconde_moitie": None if not np.isfinite(esp_h2) else esp_h2,
        "note": "espérance exigée positive sur les deux moitiés disjointes de l'échantillon"}
    if not ok_stab:
        echecs.append("14_esperance_stable_dans_le_temps")

    # --- 15. aucune affirmation de politique monétaire non étayée (E-006)
    #     L'énoncé n'est composé qu'APRÈS l'exécution des tests (E-001).
    d_instr = diags.get(instr, {})
    sens_txt = "hausse" if direction > 0 else "baisse"
    enonce = (
        f"À {HORIZON_SEANCES} séances, position dont le P&L est croissant avec la "
        f"{sens_txt} de {instr} ({d_instr.get('role', '?')}), "
        f"niveau {d_instr.get('valeur', float('nan')):.4g} au {d_instr.get('date_valeur', '?')}, "
        f"percentile {percentile_utilisable(d_instr)[0] if d_instr else float('nan')} "
        f"sur {percentile_utilisable(d_instr)[1] if d_instr else '?'} "
        f"(profondeur réelle {d_instr.get('profondeur_annees', 0):.2f} ans, "
        f"{d_instr.get('n_obs', 0)} obs). "
        f"Dossier de confirmation « {regle} » : "
        f"{len(retenues)} séries retenues, {n_classes} classes indépendantes. "
        f"σ à l'horizon mesuré {dist.get('sigma_horizon', float('nan')):.4f} "
        f"({dist.get('convention', '?')}). "
        f"Espérance {esp:+.3f} % de NAV, ratio "
        f"{('%.2f' % ratio) if ratio else 'n/d'}:1 (information)."
        if d_instr else "énoncé non composé : instrument absent des données")
    politique = bool(VOCABULAIRE_POLITIQUE.search(enonce + " " + texte_inval))
    etaye = "DFF" in dossier
    ok_pol = (not politique) or etaye
    diag_crit["15_enonce_sans_affirmation_politique_non_etayee"] = {
        "ok": ok_pol, "vocabulaire_politique_detecte": politique,
        "serie_de_politique_presente": etaye,
        "note": ("E-006 : « hausse BoJ non anticipée » alors qu'elle avait déjà eu "
                 "lieu. Aucune affirmation sur une politique sans donnée à l'appui.")}
    if not ok_pol:
        echecs.append("15_enonce_sans_affirmation_politique_non_etayee")

    t = These(
        identifiant=ident, enonce=enonce, series_utilisees=dossier,
        sens=f"{SENS_SERIE.get(instr, {}).get('role', '?')}::{sens_txt}",
        test=test_confirmation, invalidation=texte_inval,
        horizon_jours=HORIZON_SEANCES,
        esperance_pct=(esp if np.isfinite(esp) else float("nan")),
        instrument=instr, direction=direction, regle_confirmation=regle,
        lectures=lectures, invalidation_serie=serie_inval,
        invalidation_date=date_inval, invalidation_test=test_invalidation,
        scenarios=scenarios, diagnostics=diag_crit, echecs=echecs,
        verdict=("TRANSMISE" if not echecs else "REFUSEE"))
    return t


# =====================================================================
# §8  LA POSITION DÉTENUE ET LA RÉFÉRENCE 60/40 (contrôle 9)
#     Ce qu'on garde est chiffré comme ce qu'on refuse. Le cash est une
#     position : short bêta actions, short duration, long dollar.
# =====================================================================

def tester_position_detenue(diags, dists, taux_cash) -> dict:
    """Espérance du 100 % cash et de la référence 60/40, sur la MÊME grille.

    L'espérance est linéaire : E[60/40] = 0,6·E[actions] + 0,4·E[obligation]
    sans hypothèse de dépendance. Le ratio gain/perte de la composition
    exigerait la loi jointe : il n'est PAS publié (R-044 — une mesure non
    calculable n'est pas remplacée par une approximation muette).
    """
    verifier_grille()
    out = {"convention": "rendement excédentaire sur DFF, horizon "
                         f"{HORIZON_SEANCES} séances",
           "taux_cash_annualise_pct": 100.0 * taux_cash}
    out["cash"] = {"esperance_excedentaire_pct_nav": 0.0,
                   "note": ("le 100 % cash a une espérance excédentaire nulle par "
                            "construction de la convention ; son écart à la "
                            "référence est l'opposé de l'espérance de la référence")}
    jambes = {}
    for sid, poids in (("SP500", 0.60), ("DGS10", 0.40)):
        d = dists.get(sid, {})
        if not d.get("estimable") or sid not in diags:
            jambes[sid] = {"poids": poids, "calculable": False}
            continue
        niveau = diags[sid]["valeur"]
        # la jambe obligataire est LONGUE l'obligation : direction -1 sur le taux
        direction = +1 if sid == "SP500" else -1
        pnl = {k: direction * rendement_directionnel(sid, k, d, niveau, taux_cash)
               for k in GRILLE_SIGMA}
        e = esperance_sur_grille(d["bandes_centre_zero"], pnl)
        e_sd = esperance_sur_grille(d["bandes_sans_derive"], pnl)
        jambes[sid] = {"poids": poids, "calculable": True,
                       "esperance_excedentaire_pct": 100.0 * e,
                       "esperance_sans_derive_pct": 100.0 * e_sd,
                       "sigma_horizon": d["sigma_horizon"],
                       "gain_max_pct": 100.0 * max(pnl.values()),
                       "perte_max_pct": 100.0 * min(pnl.values())}
    out["jambes_reference"] = jambes
    if all(j.get("calculable") for j in jambes.values()):
        e6040 = sum(j["poids"] * j["esperance_excedentaire_pct"] for j in jambes.values())
        e6040_sd = sum(j["poids"] * j["esperance_sans_derive_pct"] for j in jambes.values())
        out["reference_60_40"] = {
            "esperance_excedentaire_pct_nav": e6040,
            "esperance_sans_derive_pct_nav": e6040_sd,
            "ratio_gain_perte": None,
            "motif_ratio_absent": ("exige la loi jointe des deux jambes ; le dépôt "
                                   "permet les marges, pas la copule. Non publié "
                                   "plutôt qu'approximé.")}
        out["ecart_cash_vs_60_40_pct_nav"] = -e6040
    else:
        out["reference_60_40"] = {"calculable": False}
        out["ecart_cash_vs_60_40_pct_nav"] = None
    return out


# =====================================================================
# §9  REGISTRE DE CALIBRATION — alimenté, RELU, résolu, scoré
#     Une section qui prédit sans jamais mesurer ses prédictions
#     n'apprend rien.
# =====================================================================

def _lire_registre() -> list[dict]:
    if REGISTRE.exists():
        with REGISTRE.open(encoding="utf-8") as fh:
            return [dict(r) for r in csv.DictReader(fh)]
    lignes = []
    if REGISTRE_SOURCE.exists():
        with REGISTRE_SOURCE.open(encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                lignes.append({
                    "ref": r.get("ref", ""), "date_emission": r.get("date_emission", ""),
                    "section": r.get("section", ""), "affirmation": r.get("affirmation", ""),
                    "probabilite": r.get("probabilite", ""),
                    "horizon_jours": "", "echeance": r.get("echeance", ""),
                    "resultat": r.get("resultat", ""), "brier": r.get("brier", ""),
                    "statut": r.get("statut", "OUVERT"),
                    "regle_resolution": json.dumps(REGLES_RESOLUTION_HERITEES[r["ref"]],
                                                   ensure_ascii=False)
                    if r.get("ref") in REGLES_RESOLUTION_HERITEES else "",
                    "note": r.get("note", "")})
    return lignes


def _ecrire_registre(lignes: list[dict]) -> None:
    with REGISTRE.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=ENTETE_REGISTRE)
        w.writeheader()
        for l in lignes:
            w.writerow({k: l.get(k, "") for k in ENTETE_REGISTRE})


def resoudre_registre(lignes: list[dict], series, arrete) -> dict:
    """Résout sur les données ce qui est résoluble. Publie ce qui ne l'est pas.
    Le score de Brier ne porte QUE sur les prédictions résolues mécaniquement."""
    resolus, non_resolubles, ouverts = [], [], []
    for l in lignes:
        if l.get("statut") in ("RESOLU_VRAI", "RESOLU_FAUX"):
            resolus.append(l)
            continue
        regle_txt = (l.get("regle_resolution") or "").strip()
        if not regle_txt:
            l["statut"] = l.get("statut") or "NON_RESOLUBLE_MECANIQUEMENT"
            if l["statut"] not in ("REFORMULE",):
                l["statut"] = "NON_RESOLUBLE_MECANIQUEMENT"
            l["note"] = (l.get("note", "") +
                         " | aucune règle de résolution mécanique attachée : "
                         "exclue du score de Brier").strip(" |")
            non_resolubles.append(l)
            continue
        try:
            regle = json.loads(regle_txt)
        except Exception:
            non_resolubles.append(l)
            continue
        sid = regle.get("serie")
        if sid not in series:
            non_resolubles.append(l)
            continue
        s = series[sid]
        debut = pd.Timestamp(l.get("date_emission") or s.index[0])
        fin_prevue = pd.Timestamp(l.get("echeance") or arrete)
        fenetre = s[(s.index > debut) & (s.index <= min(arrete, fin_prevue))]
        franchi = False
        if len(fenetre):
            if regle.get("type") == "barriere":
                franchi = bool(fenetre.max() >= regle["seuil"]) if regle["sens"] == "sup" \
                    else bool(fenetre.min() <= regle["seuil"])
            elif regle.get("type") == "terminal":
                dernier = float(fenetre.iloc[-1])
                franchi = (dernier >= regle["seuil"]) if regle["sens"] == "sup" \
                    else (dernier <= regle["seuil"])
        p = float(l.get("probabilite") or 0.0)
        if franchi:
            l["statut"], l["resultat"] = "RESOLU_VRAI", "1"
            l["brier"] = f"{(p - 1.0) ** 2:.4f}"
            resolus.append(l)
        elif arrete >= fin_prevue:
            l["statut"], l["resultat"] = "RESOLU_FAUX", "0"
            l["brier"] = f"{(p - 0.0) ** 2:.4f}"
            resolus.append(l)
        else:
            l["statut"] = "OUVERT"
            l["note"] = (f"barrière non franchie au {arrete.date()} ; "
                         f"{len(fenetre)} obs examinées depuis {debut.date()}")
            ouverts.append(l)
    briers = [float(l["brier"]) for l in resolus if l.get("brier")]
    seaux = {}
    for l in resolus:
        p = float(l.get("probabilite") or 0)
        b = int(min(9, max(0, math.floor(p * 10))))
        seaux.setdefault(b, {"n": 0, "somme_p": 0.0, "n_vrais": 0})
        seaux[b]["n"] += 1
        seaux[b]["somme_p"] += p
        seaux[b]["n_vrais"] += int(l.get("resultat") == "1")
    courbe = [{"seau": f"{k/10:.1f}–{(k+1)/10:.1f}", "n": v["n"],
               "probabilite_moyenne_annoncee": v["somme_p"] / v["n"],
               "frequence_realisee": v["n_vrais"] / v["n"]}
              for k, v in sorted(seaux.items())]
    return {
        "n_lignes": len(lignes), "n_resolues_mecaniquement": len(resolus),
        "n_ouvertes": len(ouverts), "n_non_resolubles": len(non_resolubles),
        "refs_non_resolubles": [l["ref"] for l in non_resolubles],
        "score_de_brier": (sum(briers) / len(briers)) if briers else None,
        "motif_brier_absent": None if briers else
            ("aucune prédiction résolue mécaniquement à ce jour : le score de "
             "Brier n'est pas calculable et n'est pas remplacé par une "
             "approximation. Une section qui prédit sans jamais mesurer ses "
             "prédictions n'apprend rien — et ce moteur publie l'écart plutôt "
             "que de le combler."),
        "courbe_de_calibration": courbe,
        "detail_ouvertes": [{"ref": l["ref"], "affirmation": l["affirmation"],
                             "probabilite": l["probabilite"], "echeance": l["echeance"],
                             "note": l.get("note", "")} for l in ouverts],
    }


def emettre_predictions(theses, dists, diags, arrete) -> list[dict]:
    """Chaque thèse publiée émet ses prédictions, calculées, avec règle de
    résolution machine. Aucune probabilité n'est estimée à vue (R-031)."""
    nouvelles = []
    for t in theses:
        dist = dists[t.instrument]
        # probabilité TERMINALE : somme des bandes du côté favorable
        p_term = sum(b["probabilite_empirique"] for b in dist["bandes_centre_zero"]
                     if t.direction * b["k_sigma"] > 0)
        p_term += 0.5 * sum(b["probabilite_empirique"] for b in dist["bandes_centre_zero"]
                            if b["k_sigma"] == 0.0)
        echeance = str(np.busday_offset(arrete.date(), HORIZON_SEANCES, roll="forward"))
        niveau = diags[t.instrument]["valeur"]
        seuil = niveau  # franchissement du niveau courant, dans le sens de la thèse
        nouvelles.append({
            "ref": f"{t.identifiant}-T", "date_emission": str(arrete.date()),
            "section": "Macro",
            "affirmation": (f"{t.instrument} au {echeance} "
                            f"{'au-dessus' if t.direction > 0 else 'au-dessous'} de "
                            f"{seuil:.4g} (niveau du {diags[t.instrument]['date_valeur']})"),
            "probabilite": f"{p_term:.4f}",
            "horizon_jours": HORIZON_SEANCES, "echeance": echeance,
            "resultat": "", "brier": "", "statut": "OUVERT",
            "regle_resolution": json.dumps(
                {"type": "terminal", "serie": t.instrument,
                 "sens": "sup" if t.direction > 0 else "inf", "seuil": float(seuil),
                 "texte": "résolution terminale à l'échéance sur la série FRED"},
                ensure_ascii=False),
            "note": ("probabilité = somme des fréquences empiriques des bandes "
                     "favorables de la grille symétrique ; bande centrale "
                     "partagée à parts égales")})
        # probabilité de BARRIÈRE, calculée (R-031), jamais estimée
        dvar, _ = variations_horizon(SERIES_GLOBALES[t.instrument], t.instrument, arrete)
        pb = p_barriere(1.0, dist["sigma_horizon"], dvar, dist["horizon"])
        nouvelles.append({
            "ref": f"{t.identifiant}-B", "date_emission": str(arrete.date()),
            "section": "Macro",
            "affirmation": (f"{t.instrument} touche {niveau:.4g} "
                            f"{'+' if t.direction > 0 else '-'} 1σ "
                            f"({pb['seuil_valeur']:.4f} en {dist['convention']}) "
                            f"à un moment avant le {echeance}"),
            "probabilite": f"{pb['p_reflexion'] / 2.0:.4f}",
            "horizon_jours": HORIZON_SEANCES, "echeance": echeance,
            "resultat": "", "brier": "", "statut": "OUVERT",
            "regle_resolution": json.dumps(
                {"type": "barriere", "serie": t.instrument,
                 "sens": "sup" if t.direction > 0 else "inf",
                 "seuil": float(niveau * math.exp(t.direction * dist["sigma_horizon"])
                                if dist["convention"] == "log"
                                else niveau + t.direction * dist["sigma_horizon"]),
                 "texte": "franchissement unilatéral à 1σ"}, ensure_ascii=False),
            "note": (f"méthode : {pb['methode']} ; unilatérale = moitié de la "
                     f"bilatérale {pb['p_reflexion']:.4f} ; base historique "
                     f"bilatérale {pb['p_base_historique_terminale']}")})
    return nouvelles


SERIES_GLOBALES: dict[str, pd.Series] = {}


# =====================================================================
# §10  RENDU DU BRIEF — bloc à copier tel quel, rien de ressaisi
# =====================================================================

def _pct(x, n=3):
    return "n/d" if x is None or (isinstance(x, float) and not np.isfinite(x)) else f"{x:+.{n}f}"


def rendre_brief(ctx: dict) -> str:
    """Compose le brief. Toute valeur provient de `ctx`, produit par le calcul.
    Aucune chaîne de ce rendu ne contient un chiffre saisi à la main."""
    verifier_grille()
    arrete = ctx["date_arrete"]
    diags, dists = ctx["diagnostics"], ctx["distributions"]
    theses, candidats = ctx["theses_transmises"], ctx["candidats"]
    L = []
    A = L.append
    A(f"# BRIEF MACRO n° {NUMERO_BRIEF} — arrêté au {arrete}")
    A("")
    A(f"*Produit par `apollon_macro.py` le {ctx['genere_le_utc']}. "
      f"Aucune valeur de ce document n'est saisie à la main : chacune porte sa "
      f"série, sa date et sa profondeur. Bloc à copier tel quel.*")
    A("")
    A(f"**Grille de scénarios (R-029, §11), déclarée avant toute lecture de "
      f"données et empreintée :** `{list(GRILLE_SIGMA)}` · "
      f"empreinte SHA-256 `{ctx['empreinte_grille'][:16]}…` · "
      f"symétrique : {ctx['grille_symetrique']} · horizon {HORIZON_SEANCES} séances "
      f"({HORIZON_MOIS} mois pour les séries mensuelles).")
    A("")
    A("---")
    A("")
    A("## 1. CONCLUSION, ÉNONCÉE D'ABORD")
    A("")
    if not ctx["production_autorisee"]:
        A(f"**PRODUCTION BLOQUÉE.** {ctx['motif_blocage']}")
        return "\n".join(L)
    n_t = len(theses)
    A(f"**{N_CANDIDATS_DECLARES} candidats déclarés d'avance "
      f"({len(DOSSIER_INSTRUMENT)} instruments × {len(DIRECTIONS)} directions × "
      f"{len(REGLES_CONFIRMATION)} règles de confirmation). "
      f"{ctx['n_evalues']} évalués. {n_t} thèse(s) survivent aux quinze critères.**")
    A("")
    if n_t == 0:
        A("**Abstention. Aucune thèse ne survit.** Ce n'est pas un silence : c'est "
          "un résultat, produit par le même portier que celui qui aurait admis une "
          "thèse. Le détail des échecs, critère par critère, figure au §6. La "
          "Section Macro ne transmet rien à la Section Risque ce cycle.")
    else:
        for t in theses:
            A(f"- **{t.identifiant}** — espérance **{_pct(t.esperance_pct)} % de NAV** "
              f"à {t.horizon_jours} séances, taille {TAILLE_PCT_NAV:.0f} % de NAV.")
    A("")
    pd_ = ctx["position_detenue"]
    A(f"**Position détenue (contrôle 9, E-020) — 100 % cash, testée sur la même "
      f"grille.** Espérance excédentaire du cash : "
      f"{pd_['cash']['esperance_excedentaire_pct_nav']:+.3f} % de NAV. "
      f"Référence 60/40 : "
      f"{_pct(pd_['reference_60_40'].get('esperance_excedentaire_pct_nav'))} % "
      f"(hors dérive : "
      f"{_pct(pd_['reference_60_40'].get('esperance_sans_derive_pct_nav'))} %). "
      f"**Écart du cash contre la référence : "
      f"{_pct(pd_.get('ecart_cash_vs_60_40_pct_nav'))} % de NAV** sur "
      f"{HORIZON_SEANCES} séances.")
    A("")
    A("---")
    A("")
    A("## 2. CE QUI A CHANGÉ — MÉCANISME, PAS CONTENU")
    A("")
    A("Fait, étiqueté : les briefs 001 à 004 étaient rédigés par un agent. "
      "Celui-ci est produit par un moteur. Le paramètre libre de la Section "
      "Macro — la grille de scénarios — n'est plus accessible à l'agent : "
      "il est déclaré en tête de fichier, symétrique par construction, et son "
      "empreinte SHA-256 est vérifiée avant chaque usage. Sur le brief 004, "
      "ce paramètre avait porté le ratio annoncé de 1,29:1 à 3,0:1.")
    A("")
    A("---")
    A("")
    A("## 3. M1 · M2 · M3 · M4 — ÉTAT DES SÉRIES (FAIT)")
    A("")
    A("Toutes les valeurs sont des FAITS lus dans le dépôt. Le retard est compté "
      "en séances ouvrées depuis la date d'arrêté unique. Les couples "
      "obligatoires sont vérifiés par le rendu : ce bloc ne peut pas être émis "
      "si un membre d'un couple manque.")
    A("")
    A(ctx["table_series"])
    A("")
    A(f"**Couples obligatoires contrôlés :** "
      f"{', '.join('/'.join(c) for c in COUPLES_OBLIGATOIRES)} — "
      f"{ctx['n_manquements_couples']} manquement(s).")
    A("")
    infl = ctx["inflation_trois_chiffres"]
    A(f"**Inflation en trois chiffres (contrôle 2, E-005).** "
      f"Global {infl['global_ga_pct']:+.2f} % sur un an ({infl['serie_globale']}, "
      f"{infl['date']}) · sous-jacent {infl['coeur_ga_pct']:+.2f} % "
      f"({infl['serie_coeur']}) · **écart hors sous-jacent "
      f"{infl['ecart_pb']:+.0f} pb**. "
      f"{infl['reserve']}")
    A("")
    A("---")
    A("")
    A("## 4. IDENTITÉS COMPTABLES ET REDONDANCES (vérifiées numériquement)")
    A("")
    A("| identité | vérifiable | n dates | résidu absolu max | tolérance | vérifiée |")
    A("|---|:---:|---:|---:|---:|:---:|")
    for r in ctx["identites"]:
        if not r.get("verifiable"):
            A(f"| {r['identite']} | non | — | — | — | {r.get('motif','')} |")
        else:
            A(f"| {r['identite']} | oui | {r['n_dates_communes']} | "
              f"{r['residu_absolu_max']:.4f} | {r['tolerance']:.2f} | "
              f"{'OUI' if r['identite_verifiee'] else 'NON'} |")
    A("")
    A(f"**Redondances détectées ({len(ctx['redondances'])}) — deux séries liées "
      f"ne comptent jamais pour deux confirmations indépendantes :**")
    A("")
    for j in ctx["redondances"]:
        if j["type"] == "identite_comptable":
            A(f"- identité comptable : {j['motif']} — {', '.join(j['membres'])} "
              f"(résidu max {j['residu_absolu_max']:.4f})")
        else:
            A(f"- corrélation des variations à {HORIZON_SEANCES} séances : "
              f"{j['membres'][0]} / {j['membres'][1]} = {j['correlation']:+.3f} "
              f"sur {j['n']} points (seuil {j['seuil']})")
    A("")
    A("---")
    A("")
    A("## 5. GRILLE, σ MESURÉ, ET DOUBLE CONFRONTATION DES PROBABILITÉS")
    A("")
    A("σ est **mesuré** sur chaque série, jamais choisi. Les probabilités sont "
      "les **fréquences historiques** dans chaque bande, jamais un jugement. "
      "L'effectif de chaque bande est publié ; sous "
      f"{MIN_OBS_BANDE} observations la bande est déclarée NON ESTIMABLE. "
      "La colonne « emp./gauss. » est la double confrontation exigée par §11.5 : "
      f"tout écart supérieur à un facteur {SEUIL_ECART_LOI:.0f} est déclaré (⚠).")
    A("")
    for sid in ctx["series_scenarisees"]:
        d = dists[sid]
        if not d.get("estimable"):
            A(f"**{sid}** — non scénarisable : {d.get('motif')}")
            A("")
            continue
        A(f"**{sid}** ({d['convention']}) — σ à {d['horizon']} pas = "
          f"**{d['sigma_horizon']:.5f}** · estimateurs croisés : "
          f"racine-h {d['sigma_horizon_racine_h']:.5f}, blocs disjoints "
          f"{d['sigma_horizon_blocs_disjoints']:.5f} "
          f"(écart relatif {100*d['ecart_relatif_estimateurs']:.1f} %) · "
          f"dérive d'échantillon {d['derive_moyenne_horizon']:+.5f} "
          f"({d['derive_en_sigma']:+.2f} σ) · {d['n_variations']} variations "
          f"chevauchantes, {d['n_effectif_independant']} blocs indépendants · "
          f"{d['debut_echantillon']} → {d['fin_echantillon']}")
        A("")
        A("| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |")
        A("|---:|---:|---:|---:|---:|---:|---:|---:|:---:|")
        for b in d["bandes_centre_zero"]:
            bb = "−∞" if b["borne_basse_valeur"] is None else f"{b['borne_basse_valeur']:+.4f}"
            bh = "+∞" if b["borne_haute_valeur"] is None else f"{b['borne_haute_valeur']:+.4f}"
            rr = b["ratio_empirique_sur_gaussienne"]
            rs = "n/d" if rr is None else f"{rr:.2f}"
            if b["ecart_declare_facteur_2"]:
                rs += " ⚠"
            A(f"| {b['k_sigma']:+.1f} | {bb} | {bh} | {b['n_observations']} | "
              f"{b['n_effectif_independant']} | {b['probabilite_empirique']:.4f} | "
              f"{b['probabilite_gaussienne']:.4f} | {rs} | "
              f"{'oui' if b['estimable'] else '**NON**'} |")
        A("")
    A("---")
    A("")
    A("## 6. TEST D'ASYMÉTRIE — DÉFINITION UNIQUE (R-030), L'ESPÉRANCE DÉCIDE")
    A("")
    A("> Test d'admission : **espérance calculée sur la grille symétrique "
      "complète, les deux queues incluses**. Le rapport gain maximal / perte "
      "maximale est publié **pour information** et ne peut fonder aucune "
      "admission seul (T-001, faute E-018). Le rapport gain maximal / perte du "
      "scénario central est **interdit**. Une seule formulation, appliquée à "
      "tous les candidats, position détenue comprise.")
    A("")
    A("| candidat | verdict | espérance % NAV | sans dérive | 1re moitié | 2e moitié | "
      "gain max | perte max | ratio (info) | critères échoués |")
    A("|---|:---:|---:|---:|---:|---:|---:|---:|---:|---|")
    for c in candidats:
        d12 = c.diagnostics.get("12_esperance_positive", {})
        d13 = c.diagnostics.get("13_esperance_non_portee_par_derive", {})
        d14 = c.diagnostics.get("14_esperance_stable_dans_le_temps", {})
        r = d12.get("ratio_gain_max_sur_perte_max")
        A(f"| {c.identifiant} | {c.verdict} | {_pct(d12.get('esperance_pct_nav'))} | "
          f"{_pct(d13.get('esperance_sans_derive'))} | "
          f"{_pct(d14.get('esperance_premiere_moitie'))} | "
          f"{_pct(d14.get('esperance_seconde_moitie'))} | "
          f"{_pct(d12.get('gain_maximal_pct_nav'), 2)} | "
          f"{_pct(d12.get('perte_maximale_pct_nav'), 2)} | "
          f"{'n/d' if r is None else f'{r:.2f}:1'} | "
          f"{', '.join(c.echecs) if c.echecs else '—'} |")
    A("")
    A("**Décompte des échecs par critère** (un candidat peut échouer sur "
      "plusieurs) :")
    A("")
    A("| critère | candidats en échec |")
    A("|---|---:|")
    for k in CRITERES:
        A(f"| {k} | {ctx['echecs_par_critere'].get(k, 0)} |")
    A("")
    A("**Critères MORTS par construction** — un critère qu'aucune donnée ne peut "
      "franchir n'est pas un critère exigeant, c'est un critère éteint. "
      "« Aucune thèse ne passe parce qu'aucune n'est bonne » et « aucune thèse ne "
      "passe parce qu'un critère est mort » ne se pilotent pas pareil.")
    A("")
    if ctx["criteres_morts_par_construction"]:
        A("| critère | candidats concernés | motif |")
        A("|---|---:|---|")
        for k, v in ctx["criteres_morts_par_construction"].items():
            A(f"| {k} | {v['n_candidats_concernes']} | {v['motif']} |")
    else:
        A("Aucun. Les quinze critères sont franchissables sur les données du jour.")
    A("")
    if ctx["distributions_non_scenarisables"]:
        A("**Séries NON SCÉNARISABLES** (aucune grille ne peut leur être appliquée) :")
        A("")
        for sid, m in ctx["distributions_non_scenarisables"].items():
            A(f"- `{sid}` : {m}")
        A("")
    for t in theses:
        A(f"### Thèse retenue — {t.identifiant}")
        A("")
        A(f"**Énoncé (composé APRÈS exécution du test, E-001).** {t.enonce}")
        A("")
        A(f"**Sens déclaré :** `{t.sens}`. **Séries utilisées :** "
          f"{', '.join(t.series_utilisees)}.")
        A("")
        A(f"**Invalidation (FAIT observable et daté, jamais un niveau de prix).** "
          f"{t.invalidation}")
        A("")
        A("| kσ | variation série | p empirique | n | P&L position % | P&L NAV % |")
        A("|---:|---:|---:|---:|---:|---:|")
        for s in t.scenarios:
            A(f"| {s['k_sigma']:+.1f} | {s['variation_serie']:+.5f} | "
              f"{s['probabilite_empirique']:.4f} | {s['n_observations']} | "
              f"{s['pnl_position_pct']:+.3f} | {s['pnl_nav_pct']:+.3f} |")
        A("")
    A("---")
    A("")
    A("## 7. DÉCLENCHEURS")
    A("")
    A("Aucun déclencheur pré-engagé n'est émis. Un déclencheur est une position "
      "différée : il exige les trois contrôles du §5 de la doctrine, dont la "
      "**fréquence historique de franchissement**. Le moteur publie cette "
      "fréquence pour tout seuil qu'il émet (§8 ci-dessous) et n'en engage "
      "aucun tant qu'aucune thèse n'est transmise." if not theses else
      "Les seuils de franchissement à 1σ des thèses retenues figurent au §8, "
      "avec leur probabilité calculée par réflexion et leur base historique.")
    A("")
    A("---")
    A("")
    A("## 8. PROBABILITÉS ASSIGNÉES — CALCULÉES (R-031), JAMAIS ESTIMÉES À VUE")
    A("")
    cal = ctx["calibration"]
    if ctx["predictions_emises"]:
        A("| ref | affirmation | probabilité | échéance | méthode |")
        A("|---|---|---:|---|---|")
        for p in ctx["predictions_emises"]:
            A(f"| {p['ref']} | {p['affirmation']} | {float(p['probabilite']):.3f} | "
              f"{p['echeance']} | {p['note'][:120]} |")
    else:
        A("Aucune prédiction émise ce cycle : aucune thèse n'a été transmise. "
          "Une prédiction émise sans thèse serait une inscription décorative au "
          "registre (interdit n° 3 du §7 de la doctrine).")
    A("")
    A(f"**État du registre de calibration** — {cal['n_lignes']} lignes · "
      f"{cal['n_resolues_mecaniquement']} résolues mécaniquement · "
      f"{cal['n_ouvertes']} ouvertes · "
      f"{cal['n_non_resolubles']} non résolubles mécaniquement "
      f"({', '.join(cal['refs_non_resolubles']) or '—'}).")
    A("")
    if cal["score_de_brier"] is None:
        A(f"**Score de Brier : non calculable.** {cal['motif_brier_absent']}")
    else:
        A(f"**Score de Brier : {cal['score_de_brier']:.4f}** sur "
          f"{cal['n_resolues_mecaniquement']} prédictions résolues.")
        A("")
        A("| seau de probabilité | n | p moyenne annoncée | fréquence réalisée |")
        A("|---|---:|---:|---:|")
        for c in cal["courbe_de_calibration"]:
            A(f"| {c['seau']} | {c['n']} | {c['probabilite_moyenne_annoncee']:.3f} | "
              f"{c['frequence_realisee']:.3f} |")
    A("")
    A("---")
    A("")
    A("## 9. CE QUI INVALIDERAIT CE BRIEF — ÉCRIT AVANT LES FAITS")
    A("")
    A("1. **La grille.** Toute exécution ultérieure dont l'empreinte de grille "
      f"diffère de `{ctx['empreinte_grille'][:16]}…` invalide toute comparaison "
      "avec ce brief.")
    A("2. **Les identités comptables.** Si un résidu dépasse la tolérance "
      f"{TOLERANCE_IDENTITE:.2f}, la structure de redondance publiée au §4 est "
      "fausse et le décompte des confirmations indépendantes avec elle.")
    A("3. **Les bandes.** Toute bande retombant sous "
      f"{MIN_OBS_BANDE} observations rend l'espérance correspondante non estimable.")
    A("4. **Les invalidations de thèse** figurent dans chaque fiche du §6 : "
      "publication mensuelle datée, testée par le code.")
    A("5. **La stabilité temporelle.** Une thèse dont l'espérance cesse d'être "
      "positive sur l'une des deux moitiés de l'échantillon est retirée à "
      "l'exécution suivante, sans décision d'agent.")
    A("")
    A("---")
    A("")
    A("## 10. SOURCES, RÉSERVES DE QUALITÉ, ET CE QUE CE MOTEUR NE FAIT PAS")
    A("")
    A(f"**Source unique : dépôt Apollon `data/history/*.csv`, "
      f"{ctx['n_series']} séries FRED.** Aucune valeur n'a d'autre origine. "
      f"Portée temporelle complète publiée série par série au §3 (E-004).")
    A("")
    for r in ctx["reserves"]:
        A(f"- {r}")
    A("")
    A("**Vérification tierce (R-032) : NON SATISFAITE pour ce brief.** Le moteur "
      "ne dispose d'aucune source extérieure au dépôt. Trois estimateurs "
      "**internes** de σ sont publiés côte à côte au §5 ; ce sont des contrôles "
      "de cohérence interne, **pas** une vérification tierce, et ils ne sont pas "
      "présentés comme telle.")
    A("")
    A("**Ce que ce moteur ne peut pas faire.** Il ne prouve aucune capacité "
      "prédictive : la règle de confirmation est une règle de percentile, "
      "déclarée et symétrique, pas un modèle validé hors échantillon. Il ne "
      "corrige pas la multiplicité : "
      f"{N_CANDIDATS_DECLARES} candidats sont évalués et aucune pénalité de "
      "sélection n'est appliquée à l'espérance — c'est une limite déclarée, pas "
      "un oubli. Il ne voit ni les événements politiques, ni les décisions de "
      "banques centrales : le dépôt ne contient que des séries FRED, et toute "
      "affirmation de politique monétaire non adossée à `DFF` est refusée "
      "(critère 15, faute E-006).")
    A("")
    A("---")
    A("")
    A(f"*Fin du brief {NUMERO_BRIEF}. Produit mécaniquement. "
      f"Ne constitue pas un conseil en investissement.*")
    return "\n".join(L)


# =====================================================================
# §11  MAIN — contrat avec la Section Risque, code de sortie
# =====================================================================

def inflation_trois_chiffres(series, arrete) -> dict:
    """Contrôle 2 (E-005). Global, sous-jacent, et écart. Jamais le global seul.
    La contribution énergie exigerait `CPIENGSL`, absente du dépôt : la lacune
    est nommée avec le code FRED qui la comble (R-028)."""
    out = {"serie_globale": "CPIAUCSL", "serie_coeur": "CPILFESL"}
    g = series["CPIAUCSL"]; c = series["CPILFESL"]
    g = g[g.index <= arrete]; c = c[c.index <= arrete]
    ga = 100.0 * (float(g.iloc[-1]) / float(g.iloc[-13]) - 1.0)
    ca = 100.0 * (float(c.iloc[-1]) / float(c.iloc[-13]) - 1.0)
    out.update({"global_ga_pct": ga, "coeur_ga_pct": ca,
                "ecart_pb": 100.0 * (ga - ca),
                "date": str(g.index[-1].date()),
                "reserve": ("Contribution énergie NON publiée : `CPIENGSL` est "
                            "absente du dépôt. Lacune nommée avec le code FRED qui "
                            "la comble (R-028) ; elle n'est pas présentée comme une "
                            "limite de méthode. L'écart ci-dessus est l'écart "
                            "global/sous-jacent, pas la contribution énergie.")})
    return out


def main() -> int:
    horodatage = datetime.now(timezone.utc)
    print("=" * 78)
    print("APOLLON — MOTEUR MACRO")
    print("=" * 78)
    etat = verifier_grille()
    print(f"grille déclarée   : {list(GRILLE_SIGMA)}")
    print(f"symétrie          : vérifiée par contrôle explicite (sans assert, -O compris) — R-046")
    print(f"empreinte SHA-256 : {etat['empreinte_sha256']}")
    print(f"horizon           : {HORIZON_SEANCES} séances / {HORIZON_MOIS} mois")
    print(f"candidats déclarés: {N_CANDIDATS_DECLARES}")
    print()

    series = charger_series()
    SERIES_GLOBALES.clear(); SERIES_GLOBALES.update(series)
    print(f"séries chargées   : {len(series)}")
    if not series:
        print("AUCUNE SÉRIE — PRODUCTION BLOQUÉE", file=sys.stderr)
        return 2

    try:
        arrete = date_arrete_unique(series, SERIES_NOYAU)
    except RenduRefuse as exc:
        print(f"PRODUCTION BLOQUÉE : {exc}", file=sys.stderr)
        return 2
    print(f"date d'arrêté     : {arrete.date()}  (minimum des dernières dates du noyau)")

    diags = {sid: diagnostic_series(sid, s, arrete) for sid, s in series.items()}
    ctrl = controle_production(series, diags)
    print(f"production autorisée : {ctrl['production_autorisee']}")
    if ctrl["manquantes_noyau"]:
        print(f"  séries de noyau manquantes : {ctrl['manquantes_noyau']}")
    if ctrl["series_perimees_vs_arrete"]:
        print(f"  séries périmées : {ctrl['series_perimees_vs_arrete']}")
    if ctrl["series_sans_sens_declare"]:
        print(f"  séries sans sens déclaré : {ctrl['series_sans_sens_declare']}")
    for d, m in ctrl["domaines_fermes"].items():
        print(f"  DOMAINE FERMÉ : {d} — manque {m}")

    identites = verifier_identites(series, arrete)
    classes, redondances = construire_redondances(series, arrete, identites)
    print(f"identités vérifiées : "
          f"{sum(1 for r in identites if r.get('identite_verifiee'))}/{len(identites)}")
    print(f"redondances détectées : {len(redondances)}")

    dists = {sid: distribution_scenarios(sid, s, arrete) for sid, s in series.items()}

    if not ctrl["production_autorisee"]:
        motif = ("séries de noyau manquantes : " + ", ".join(ctrl["manquantes_noyau"])
                 if ctrl["manquantes_noyau"] else
                 "séries périmées au-delà du retard toléré : "
                 + ", ".join(ctrl["series_perimees_vs_arrete"] +
                             ctrl["series_sans_sens_declare"]))
        charge = {"fraicheur": {"genere_le_utc": horodatage.isoformat(timespec="seconds"),
                                "date_donnees": str(arrete.date()),
                                "execution_complete": False},
                  "production_autorisee": False, "motif_blocage": motif,
                  "controle_series": ctrl, "theses": []}
        SORTIE_JSON.write_text(json.dumps(charge, indent=2, ensure_ascii=False,
                                          default=str), encoding="utf-8")
        SORTIE_BRIEF.write_text(
            f"# BRIEF MACRO n° {NUMERO_BRIEF} — NON PRODUIT\n\n"
            f"**PRODUCTION BLOQUÉE au {arrete.date()}.** {motif}\n\n"
            f"Le brief n'est pas produit. Il n'est pas produit avec une réserve "
            f"(R-028).\n", encoding="utf-8")
        print("\n### PRODUCTION BLOQUÉE — brief NON produit ###", file=sys.stderr)
        return 2

    taux_cash = float(diags["DFF"]["valeur"]) / 100.0
    candidats = engendrer_candidats(series, diags, dists, arrete, classes, ctrl)
    transmises = [c for c in candidats if c.verdict == "TRANSMISE"]
    print(f"candidats évalués : {len(candidats)} · transmises : {len(transmises)}")

    conflits = controler_sens(transmises)
    if conflits:
        print("\nRENDU REFUSÉ — CONFLIT DE SENS :", file=sys.stderr)
        for c in conflits:
            print(f"  {c}", file=sys.stderr)
        return 3

    echecs_par_critere = {k: 0 for k in CRITERES}
    for c in candidats:
        for e in c.echecs:
            echecs_par_critere[e] = echecs_par_critere.get(e, 0) + 1

    # --- CRITÈRES MORTS PAR CONSTRUCTION -------------------------------
    # « Aucune thèse ne passe parce qu'aucune n'est bonne » et « aucune thèse
    # ne passe parce qu'un critère est mort » ne se pilotent pas pareil, et
    # cela doit être discernable en aval (registre, 16/08/2026).
    morts = {}
    for c in candidats:
        dossier = DOSSIER_INSTRUMENT[c.instrument]
        if not any(x in SERIES_PUBLICATION_DATEE for x in dossier):
            morts.setdefault("10_invalidation_fait_date", []).append(c.identifiant)
        if c.instrument in INSTRUMENTS_NON_CALCULABLES:
            morts.setdefault("3_instrument_calculable", []).append(c.identifiant)
        if DOMAINE_INSTRUMENT.get(c.instrument) in ctrl["domaines_fermes"]:
            morts.setdefault("2_domaine_ouvert", []).append(c.identifiant)
        if not dists.get(c.instrument, {}).get("estimable"):
            morts.setdefault("5_bandes_estimables", []).append(c.identifiant)
    criteres_morts = {
        k: {"n_candidats_concernes": len(v), "candidats": v,
            "motif": ({"10_invalidation_fait_date":
                       "aucune série à publication mensuelle datée dans le dossier "
                       "déclaré de l'instrument : le critère ne peut pas être "
                       "franchi, quelle que soit la donnée",
                       "3_instrument_calculable":
                       "P&L non calculable depuis le dépôt seul",
                       "2_domaine_ouvert": "domaine fermé par série obligatoire manquante",
                       "5_bandes_estimables":
                       "série non scénarisable : voir le motif de distribution"}
                      .get(k, ""))}
        for k, v in sorted(morts.items())}

    position = tester_position_detenue(diags, dists, taux_cash)

    # --- registre de calibration : relu, résolu, puis alimenté
    lignes = _lire_registre()
    cal = resoudre_registre(lignes, series, arrete)
    nouvelles = emettre_predictions(transmises, dists, diags, arrete)
    refs = {l["ref"] for l in lignes}
    lignes.extend([n for n in nouvelles if n["ref"] not in refs])
    _ecrire_registre(lignes)
    brier_txt = ("n/d" if cal["score_de_brier"] is None
                 else f"{cal['score_de_brier']:.4f}")
    print(f"registre : {cal['n_lignes']} lignes relues · "
          f"{cal['n_resolues_mecaniquement']} résolues · "
          f"{len(nouvelles)} émises · Brier : {brier_txt}")

    # --- rendu (refus possible sur couple incomplet)
    series_publiees = sorted(series)
    try:
        table = rendre_bloc_series(series_publiees, diags)
    except RenduRefuse as exc:
        print(f"\n{exc}", file=sys.stderr)
        return 3

    reserves = []
    for sid in sorted(series):
        d = diags[sid]
        insuf = [n for n, p in d["percentiles"].items() if p["percentile"] is None]
        if insuf:
            reserves.append(
                f"`{sid}` : percentile REFUSÉ sur {', '.join(insuf)} — profondeur "
                f"réelle {d['n_obs']} obs / {d['profondeur_annees']:.2f} ans "
                f"(début {d['debut']}). R-011 : un percentile calculé sur une série "
                f"tronquée est sans valeur.")
    for d, m in ctrl["domaines_fermes"].items():
        reserves.append(f"**Domaine `{d}` FERMÉ** — série(s) obligatoire(s) "
                        f"manquante(s) : {', '.join(m)}. Aucune thèse ne peut en "
                        f"sortir ; ce n'est pas une réserve, c'est une interdiction.")
    for sid in INSTRUMENTS_NON_CALCULABLES:
        if sid in series:
            reserves.append(f"`{sid}` : instrument NON ADMISSIBLE — "
                            f"{instrument_admissible(sid)[1]}")
    lents = [(sid, diags[sid]["retard_vs_arrete"]) for sid in sorted(series)
             if diags[sid]["periodicite"] == "ouvree" and diags[sid]["retard_vs_arrete"] > 0]
    if lents:
        reserves.append("Retards sur la date d'arrêté unique (E-014) : " +
                        ", ".join(f"{s} {r} séance(s)" for s, r in lents))

    ctx = {
        "date_arrete": str(arrete.date()),
        "genere_le_utc": horodatage.isoformat(timespec="seconds"),
        "empreinte_grille": etat["empreinte_sha256"],
        "grille_symetrique": etat["symetrique"],
        "production_autorisee": True, "motif_blocage": "",
        "n_series": len(series), "n_evalues": len(candidats),
        "diagnostics": diags, "distributions": dists,
        "candidats": candidats, "theses_transmises": transmises,
        "table_series": table, "n_manquements_couples": len(controler_couples(series_publiees)),
        "identites": identites, "redondances": redondances,
        "series_scenarisees": sorted(set(list(DOSSIER_INSTRUMENT) + ["VIXCLS", "BAMLH0A0HYM2"])),
        "echecs_par_critere": echecs_par_critere,
        "criteres_morts_par_construction": criteres_morts,
        "distributions_non_scenarisables": {
            sid: d.get("motif") for sid, d in dists.items() if not d.get("estimable")},
        "position_detenue": position,
        "calibration": cal, "predictions_emises": nouvelles,
        "inflation_trois_chiffres": inflation_trois_chiffres(series, arrete),
        "reserves": reserves,
    }
    brief = rendre_brief(ctx)
    SORTIE_BRIEF.write_text(brief, encoding="utf-8")

    peremption = horodatage + pd.Timedelta(hours=VALIDITE_SORTIE_HEURES)
    charge = {
        "fraicheur": {
            "genere_le_utc": horodatage.isoformat(timespec="seconds"),
            "date_donnees": str(arrete.date()),
            "validite_heures": VALIDITE_SORTIE_HEURES,
            "perime_apres_utc": peremption.isoformat(timespec="seconds"),
            "execution_complete": True,
            "controle_attendu_de_l_aval": (
                "REFUSER ce fichier si l'heure UTC courante dépasse "
                "`perime_apres_utc`, si `date_donnees` ne correspond pas à la date "
                "d'arrêté examinée, ou si `execution_complete` est absent ou faux.")},
        "grille": {"points_sigma": list(GRILLE_SIGMA),
                   "empreinte_sha256": etat["empreinte_sha256"],
                   "symetrique": True, "horizon_seances": HORIZON_SEANCES,
                   "modifiable": False,
                   "note": "déclarée avant toute lecture de données ; vérifiée à chaque usage"},
        "production_autorisee": True,
        "controle_series": ctrl,
        "identites_comptables": identites,
        "redondances": redondances,
        "table_des_sens": SENS_SERIE,
        "couples_obligatoires": [list(c) for c in COUPLES_OBLIGATOIRES],
        "n_candidats_declares": N_CANDIDATS_DECLARES,
        "n_candidats_evalues": len(candidats),
        "echecs_par_critere": echecs_par_critere,
        "criteres_morts_par_construction": criteres_morts,
        "distributions_non_scenarisables": {
            sid: d.get("motif") for sid, d in dists.items() if not d.get("estimable")},
        "position_detenue_et_reference": position,
        "calibration": cal,
        "predictions_emises": nouvelles,
        "theses": [{
            "identifiant": t.identifiant, "enonce": t.enonce,
            "instrument": t.instrument, "direction": t.direction,
            "regle_confirmation": t.regle_confirmation,
            "sens": t.sens, "series_utilisees": t.series_utilisees,
            "lectures": t.lectures,
            "invalidation": t.invalidation,
            "invalidation_serie": t.invalidation_serie,
            "invalidation_date": t.invalidation_date,
            "horizon_jours": t.horizon_jours,
            "esperance_pct_nav": (None if not np.isfinite(t.esperance_pct)
                                  else t.esperance_pct),
            "scenarios": t.scenarios,
            "criteres": t.diagnostics,
            "criteres_echoues": t.echecs,
            "statut": t.verdict,
            "statut_risque": ("EN_ATTENTE_VETO" if t.verdict == "TRANSMISE"
                              else "NON_SOUMISE_REFUSEE_EN_AMONT"),
        } for t in candidats],
        "n_transmises": len(transmises),
        "n_refusees": len(candidats) - len(transmises),
        "statuts_risque_possibles": ["EN_ATTENTE_VETO", "NON_SOUMISE_REFUSEE_EN_AMONT"],
        "avertissement": (
            "Ce moteur ne peut pas déclarer une thèse exécutable. Une thèse "
            "TRANSMISE sort en EN_ATTENTE_VETO et n'est qu'une DEMANDE de veto ; "
            "une thèse REFUSÉE sort en NON_SOUMISE_REFUSEE_EN_AMONT et n'est pas "
            "soumise. Seule la Section Risque peut statuer."),
        "mesures_non_opposables": [
            {"mesure": "ratio gain max / perte max",
             "opposable": False,
             "motif": "publié pour information ; l'espérance décide (T-001, E-018)"},
            {"mesure": "estimateurs croisés de σ",
             "opposable": False,
             "motif": "cohérence interne ; ne vaut pas vérification tierce (R-032)"},
            {"mesure": "probabilité gaussienne des bandes",
             "opposable": False,
             "motif": "référence de confrontation (§11.5) ; les fréquences "
                      "empiriques décident"},
        ],
    }
    SORTIE_JSON.write_text(json.dumps(charge, indent=2, ensure_ascii=False, default=str),
                           encoding="utf-8")

    print()
    print("=" * 78)
    print(f"THÈSES TRANSMISES : {len(transmises)} / {len(candidats)} candidats évalués")
    print("=" * 78)
    for t in transmises:
        print(f"  {t.identifiant} — espérance {t.esperance_pct:+.3f} % NAV")
    if not transmises:
        print("  aucune. Le brief le dit : c'est un résultat, pas un silence.")
    print(f"\n→ {SORTIE_BRIEF}")
    print(f"→ {SORTIE_JSON}")
    print(f"→ {REGISTRE}")
    print(f"  fraîcheur : généré le {horodatage.isoformat(timespec='seconds')} · "
          f"périmé après {peremption.isoformat(timespec='seconds')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
