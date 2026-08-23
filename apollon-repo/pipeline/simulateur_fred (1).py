#!/usr/bin/env python3
"""SIMULATEUR FRED / ALFRED — pour tester la collecte SANS accès réseau.

POURQUOI CE FICHIER EXISTE
==========================
Quatre cycles consécutifs ont échoué sur la couche de collecte (E-052,
E-054, E-056, E-057). Les quatre fautes avaient la même cause racine :
l'environnement de développement n'a aucun accès à api.stlouisfed.org,
donc `apollon_data.py` était écrit et livré SANS AVOIR JAMAIS ÉTÉ EXÉCUTÉ.
Chaque défaut n'apparaissait qu'en production, chez l'utilisateur.

Ce module reproduit les comportements DOCUMENTÉS de l'API — y compris ses
modes dégradés — pour que la collecte soit testable hors ligne.

Il ne remplace pas une vérification contre le vrai serveur. Il rend
simplement impossible de livrer un collecteur qui n'a jamais tourné.

MODES DÉGRADÉS REPRODUITS — un par faute déjà commise
=====================================================
  E-052  output_type=2 : structure à une colonne par millésime, sans
         champ `value`. L'analyseur ne trouve rien et rend une liste vide.
  E-056  output_type=4 sur série mensuelle : ZÉRO observation renvoyée.
  E-054  output_type=4 sur série longue : historique tronqué.
         calendrier sans include_release_dates_with_no_data : passé seul.
  —      clé absente, HTTP 400/429/500, JSON malformé, timeout.
"""
from __future__ import annotations

import json
from datetime import date, timedelta

__all__ = ["SimulateurFred", "ReponseSimulee"]

# Séries mensuelles : ALFRED n'archive pas leurs millésimes aussi loin que
# l'observation_start habituellement demandé. C'est la faute E-056.
MENSUELLES = {"CPIAUCSL", "CPILFESL", "PAYEMS", "UNRATE", "INDPRO"}

# Séries jamais révisées : demander un millésime n'a aucun sens (E-054).
JAMAIS_REVISEES = {
    "DGS2", "DGS10", "DGS30", "T10Y2Y", "DFII10", "T10YIE", "T5YIFR", "DFF",
    "VIXCLS", "VXVCLS", "VXDCLS", "OVXCLS", "SP500", "NASDAQ100",
    "DCOILBRENTEU", "DCOILWTICO", "DEXUSEU", "DEXJPUS", "DTWEXBGS",
    "BAMLH0A0HYM2", "BAMLC0A0CM",
}

RELEASES_CONNUES = {10: "CPI", 50: "Employment Situation", 53: "GDP",
                    13: "G.17", 18: "H.15", 175: "FOMC", 99: "non suivie"}


class ErreurHttp(Exception):
    """Équivalent de requests.HTTPError."""


class ReponseSimulee:
    def __init__(self, charge, code: int = 200, brut: str | None = None):
        self._charge, self.status_code, self._brut = charge, code, brut

    def raise_for_status(self):
        if self.status_code >= 400:
            raise ErreurHttp(f"{self.status_code} pour l'URL simulée")

    def json(self):
        if self._brut is not None:
            return json.loads(self._brut)      # lève si malformé, comme requests
        return self._charge


class SimulateurFred:
    """Remplace `requests` dans apollon_data.py.

    `mode` choisit le comportement :
      "nominal"          — l'API se comporte comme documenté
      "millesime_vide"   — output_type=4 rend 0 observation  (E-056)
      "millesime_tronque"— output_type=4 rend 12 % de l'historique (E-054)
      "forme_millesime"  — output_type=4 rend la structure du type 2 (E-052)
      "http_500"         — le serveur tombe
      "json_malforme"    — réponse non parsable
      "calendrier_passe" — le calendrier ne rend que des dates passées
      "millesime_http400"— output_type=4 fait répondre le serveur en ERREUR
                           (comportement RÉEL observé en production, E-062)
    """

    def __init__(self, mode: str = "nominal", n_obs_quotidien: int = 2500,
                 n_obs_mensuel: int = 120):
        self.mode = mode
        self.n_q, self.n_m = n_obs_quotidien, n_obs_mensuel
        self.appels: list[dict] = []          # journal, pour les assertions

    # ------------------------------------------------------------------
    def get(self, url, params=None, timeout=None):
        params = params or {}
        self.appels.append({"url": url, **params})
        if self.mode == "http_500":
            return ReponseSimulee(None, 500)
        if self.mode == "json_malforme":
            return ReponseSimulee(None, 200, brut='{"observations": [')
        if "releases/dates" in url:
            return self._calendrier(params)
        return self._observations(params)

    # ------------------------------------------------------------------
    def _observations(self, params):
        sid = params.get("series_id", "?")
        ot = params.get("output_type")
        n = self.n_m if sid in MENSUELLES else self.n_q
        mensuelle = sid in MENSUELLES

        if ot == 4:                                    # millésime demandé
            if self.mode == "millesime_http400":
                # Comportement RÉEL du serveur, mesuré sur 5 cycles.
                return ReponseSimulee(None, 400)
            if self.mode == "forme_millesime":
                # Structure du type 2 : une colonne par millésime, pas de `value`
                return ReponseSimulee({"observations": [
                    {"date": self._jour(i, mensuelle), f"{sid}_20260101": "1.0"}
                    for i in range(3)]})
            if self.mode == "millesime_vide" or (self.mode == "nominal" and mensuelle):
                # Comportement RÉEL observé en production : rien.
                return ReponseSimulee({"observations": []})
            if self.mode == "millesime_tronque":
                n = max(1, int(n * 0.12))

        return ReponseSimulee({"observations": [
            {"date": self._jour(i, mensuelle),
             "value": "." if i % 97 == 0 else f"{100 + i * 0.01:.4f}"}
            for i in range(n)]})

    def _jour(self, i: int, mensuelle: bool) -> str:
        depart = date(2016, 8, 15)
        return str(depart + timedelta(days=31 * i if mensuelle else i))

    # ------------------------------------------------------------------
    def _calendrier(self, params):
        futur = params.get("include_release_dates_with_no_data") in ("true", True)
        if self.mode == "calendrier_passe":
            futur = False
        aujourd = date.today()
        dates = []
        for rid in RELEASES_CONNUES:
            for k in range(1, 4):
                dates.append({"release_id": rid,
                              "date": str(aujourd - timedelta(days=30 * k))})
            if futur:
                for k in range(1, 4):
                    dates.append({"release_id": rid,
                                  "date": str(aujourd + timedelta(days=30 * k))})
        return ReponseSimulee({"release_dates": dates})
