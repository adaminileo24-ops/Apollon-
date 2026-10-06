# BRIEF MACRO n° 005 — arrêté au 2026-10-05

*Produit par `apollon_macro.py` le 2026-10-06T23:16:25+00:00. Aucune valeur de ce document n'est saisie à la main : chacune porte sa série, sa date et sa profondeur. Bloc à copier tel quel.*

**Grille de scénarios (R-029, §11), déclarée avant toute lecture de données et empreintée :** `[-2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0]` · empreinte SHA-256 `6aaeb3863c875923…` · symétrique : True · horizon 60 séances (3 mois pour les séries mensuelles).

---

## 1. CONCLUSION, ÉNONCÉE D'ABORD

**40 candidats déclarés d'avance (10 instruments × 2 directions × 2 règles de confirmation). 40 évalués. 0 thèse(s) survivent aux quinze critères.**

**Abstention. Aucune thèse ne survit.** Ce n'est pas un silence : c'est un résultat, produit par le même portier que celui qui aurait admis une thèse. Le détail des échecs, critère par critère, figure au §6. La Section Macro ne transmet rien à la Section Risque ce cycle.

**Position détenue (contrôle 9, E-020) — 100 % cash, testée sur la même grille.** Espérance excédentaire du cash : +0.000 % de NAV. Référence 60/40 : +1.377 % (hors dérive : -0.173 %). **Écart du cash contre la référence : -1.377 % de NAV** sur 60 séances.

---

## 2. CE QUI A CHANGÉ — MÉCANISME, PAS CONTENU

Fait, étiqueté : les briefs 001 à 004 étaient rédigés par un agent. Celui-ci est produit par un moteur. Le paramètre libre de la Section Macro — la grille de scénarios — n'est plus accessible à l'agent : il est déclaré en tête de fichier, symétrique par construction, et son empreinte SHA-256 est vérifiée avant chaque usage. Sur le brief 004, ce paramètre avait porté le ratio annoncé de 1,29:1 à 3,0:1.

---

## 3. M1 · M2 · M3 · M4 — ÉTAT DES SÉRIES (FAIT)

Toutes les valeurs sont des FAITS lus dans le dépôt. Le retard est compté en séances ouvrées depuis la date d'arrêté unique. Les couples obligatoires sont vérifiés par le rendu : ce bloc ne peut pas être émis si un membre d'un couple manque.

| série | rôle déclaré | valeur | date | retard | n obs | profondeur | pct 1 an | pct 5 ans | pct complet |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| BAMLC0A0CM | risque_credit_ig | 0.84 | 2026-10-05 | 0 | 783 | 2.99 ans | 88.1 | REFUSÉ (insuffisante, -38 %) | 50.2 |
| BAMLH0A0HYM2 | risque_credit_hy | 3.12 | 2026-10-05 | 0 | 784 | 2.99 ans | 88.5 | REFUSÉ (insuffisante, -38 %) | 59.1 |
| CPIAUCSL | inflation_globale | 334.1 | 2026-08-01 | 65 | 118 | 9.83 ans | 100.0 | 100.0 | 100.0 |
| CPILFESL | inflation_sous_jacente | 337.8 | 2026-08-01 | 65 | 118 | 9.83 ans | 100.0 | 100.0 | 100.0 |
| DCOILBRENTEU | prix_energie | 114 | 2026-09-29 | 4 | 2529 | 9.97 ans | 86.1 | 93.2 | 96.6 |
| DCOILWTICO | prix_energie_wti | 96.16 | 2026-09-29 | 4 | 2493 | 9.97 ans | 79.4 | 87.4 | 93.6 |
| DEXJPUS | devise_usdjpy | 157.8 | 2026-10-02 | 1 | 2492 | 9.97 ans | 51.6 | 88.5 | 94.2 |
| DEXUSEU | devise_eurusd | 1.126 | 2026-10-02 | 1 | 2492 | 9.97 ans | 0.8 | 63.3 | 50.4 |
| DFF | politique_monetaire | 3.88 | 2026-10-05 | 0 | 3650 | 9.99 ans | 100.0 | 26.0 | 70.9 |
| DFII10 | taux_reel_10a | 2.95 | 2026-10-05 | 0 | 2496 | 9.98 ans | 100.0 | 100.0 | 100.0 |
| DGS10 | taux_nominal_10a | 5.31 | 2026-10-05 | 0 | 2496 | 9.98 ans | 100.0 | 100.0 | 100.0 |
| DGS2 | taux_nominal_2a | 4.84 | 2026-10-05 | 0 | 2496 | 9.98 ans | 98.0 | 90.1 | 95.0 |
| DGS30 | taux_nominal_30a | 5.66 | 2026-10-05 | 0 | 2496 | 9.98 ans | 100.0 | 100.0 | 100.0 |
| DTWEXBGS | dollar_large | 121.4 | 2026-10-02 | 1 | 2490 | 9.97 ans | 94.8 | 62.8 | 79.1 |
| INDPRO | activite_industrielle | 103.1 | 2026-08-01 | 65 | 119 | 9.83 ans | 100.0 | 100.0 | 92.4 |
| NASDAQ100 | prix_actions_tech | 3.108e+04 | 2026-10-05 | 0 | 2511 | 9.98 ans | 100.0 | 100.0 | 100.0 |
| OVXCLS | volatilite_implicite_petrole | 48.65 | 2026-10-05 | 0 | 2512 | 9.98 ans | 43.3 | 75.7 | 81.8 |
| PAYEMS | emploi | 1.59e+05 | 2026-09-01 | 34 | 120 | 9.92 ans | 100.0 | 100.0 | 100.0 |
| SP500 | prix_actions | 7774 | 2026-10-05 | 0 | 2510 | 9.98 ans | 99.2 | 99.8 | 99.9 |
| T10Y2Y | pente_courbe | 0.47 | 2026-10-05 | 0 | 2496 | 9.98 ans | 34.9 | 70.6 | 56.2 |
| T10YIE | point_mort_10a | 2.36 | 2026-10-05 | 0 | 2496 | 9.98 ans | 81.7 | 64.6 | 80.1 |
| T5YIFR | point_mort_5a5a | 2.36 | 2026-10-05 | 0 | 2496 | 9.98 ans | 100.0 | 85.3 | 92.5 |
| UNRATE | chomage | 4.2 | 2026-09-01 | 34 | 119 | 9.92 ans | 33.3 | 78.3 | 63.9 |
| VIXCLS | volatilite_implicite | 15.52 | 2026-10-05 | 0 | 2543 | 9.98 ans | 18.7 | 27.6 | 37.4 |
| VXDCLS | volatilite_implicite_dow | 15.82 | 2026-10-05 | 0 | 2513 | 9.98 ans | 50.0 | 46.4 | 49.2 |
| VXVCLS | volatilite_implicite_3m | 18 | 2026-10-05 | 0 | 2510 | 9.98 ans | 6.7 | 24.5 | 39.4 |

**Couples obligatoires contrôlés :** CPIAUCSL/CPILFESL, DGS10/DFII10, DGS10/T10YIE, BAMLH0A0HYM2/BAMLC0A0CM, UNRATE/PAYEMS, VIXCLS/SP500 — 0 manquement(s).

**Inflation en trois chiffres (contrôle 2, E-005).** Global +3.71 % sur un an (CPIAUCSL, 2026-08-01) · sous-jacent +2.76 % (CPILFESL) · **écart hors sous-jacent +95 pb**. Contribution énergie NON publiée : `CPIENGSL` est absente du dépôt. Lacune nommée avec le code FRED qui la comble (R-028) ; elle n'est pas présentée comme une limite de méthode. L'écart ci-dessus est l'écart global/sous-jacent, pas la contribution énergie.

---

## 4. IDENTITÉS COMPTABLES ET REDONDANCES (vérifiées numériquement)

| identité | vérifiable | n dates | résidu absolu max | tolérance | vérifiée |
|---|:---:|---:|---:|---:|:---:|
| T10YIE = DGS10 - DFII10 | oui | 2496 | 0.0000 | 0.02 | OUI |
| T10Y2Y = DGS10 - DGS2 | oui | 2496 | 0.0000 | 0.02 | OUI |

**Redondances détectées (11) — deux séries liées ne comptent jamais pour deux confirmations indépendantes :**

- identité comptable : T10YIE = DGS10 - DFII10 — T10YIE, DGS10, DFII10 (résidu max 0.0000)
- identité comptable : T10Y2Y = DGS10 - DGS2 — T10Y2Y, DGS10, DGS2 (résidu max 0.0000)
- corrélation des variations à 60 séances : BAMLC0A0CM / BAMLH0A0HYM2 = +0.940 sur 723 points (seuil 0.9)
- corrélation des variations à 60 séances : DGS10 / DGS30 = +0.966 sur 2436 points (seuil 0.9)
- corrélation des variations à 60 séances : INDPRO / PAYEMS = +0.913 sur 116 points (seuil 0.9)
- corrélation des variations à 60 séances : INDPRO / UNRATE = -0.918 sur 115 points (seuil 0.9)
- corrélation des variations à 60 séances : NASDAQ100 / SP500 = +0.903 sur 2450 points (seuil 0.9)
- corrélation des variations à 60 séances : PAYEMS / UNRATE = -0.983 sur 116 points (seuil 0.9)
- corrélation des variations à 60 séances : VIXCLS / VXDCLS = +0.930 sur 2450 points (seuil 0.9)
- corrélation des variations à 60 séances : VIXCLS / VXVCLS = +0.958 sur 2450 points (seuil 0.9)
- corrélation des variations à 60 séances : VXDCLS / VXVCLS = +0.934 sur 2450 points (seuil 0.9)

---

## 5. GRILLE, σ MESURÉ, ET DOUBLE CONFRONTATION DES PROBABILITÉS

σ est **mesuré** sur chaque série, jamais choisi. Les probabilités sont les **fréquences historiques** dans chaque bande, jamais un jugement. L'effectif de chaque bande est publié ; sous 20 observations la bande est déclarée NON ESTIMABLE. La colonne « emp./gauss. » est la double confrontation exigée par §11.5 : tout écart supérieur à un facteur 2 est déclaré (⚠).

**BAMLH0A0HYM2** (niveau) — σ à 60 pas = **0.45179** · estimateurs croisés : racine-h 0.53970, blocs disjoints 0.37618 (écart relatif 43.5 %) · dérive d'échantillon -0.09891 (-0.22 σ) · 724 variations chevauchantes, 12 blocs indépendants · 2023-10-09 → 2026-10-05

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.6777 | 52 | 1 | 0.0718 | 0.0668 | 1.08 | oui |
| -1.0 | -0.6777 | -0.3388 | 121 | 2 | 0.1671 | 0.1598 | 1.05 | oui |
| -0.5 | -0.3388 | -0.1129 | 189 | 3 | 0.2610 | 0.1747 | 1.49 | oui |
| +0.0 | -0.1129 | +0.1129 | 195 | 3 | 0.2693 | 0.1974 | 1.36 | oui |
| +0.5 | +0.1129 | +0.3388 | 79 | 1 | 0.1091 | 0.1747 | 0.62 | oui |
| +1.0 | +0.3388 | +0.6777 | 59 | 1 | 0.0815 | 0.1598 | 0.51 | oui |
| +2.0 | +0.6777 | +∞ | 29 | 0 | 0.0401 | 0.0668 | 0.60 | oui |

**DCOILBRENTEU** (log) — σ à 60 pas = **0.24741** · estimateurs croisés : racine-h 0.24810, blocs disjoints 0.35205 (écart relatif 42.3 %) · dérive d'échantillon +0.01652 (+0.07 σ) · 2469 variations chevauchantes, 41 blocs indépendants · 2016-10-10 → 2026-09-29

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.3711 | 84 | 1 | 0.0340 | 0.0668 | 0.51 | oui |
| -1.0 | -0.3711 | -0.1856 | 155 | 3 | 0.0628 | 0.1598 | 0.39 ⚠ | oui |
| -0.5 | -0.1856 | -0.0619 | 500 | 8 | 0.2025 | 0.1747 | 1.16 | oui |
| +0.0 | -0.0619 | +0.0619 | 768 | 13 | 0.3111 | 0.1974 | 1.58 | oui |
| +0.5 | +0.0619 | +0.1856 | 608 | 10 | 0.2463 | 0.1747 | 1.41 | oui |
| +1.0 | +0.1856 | +0.3711 | 219 | 4 | 0.0887 | 0.1598 | 0.55 | oui |
| +2.0 | +0.3711 | +∞ | 135 | 2 | 0.0547 | 0.0668 | 0.82 | oui |

**DCOILWTICO** — non scénarisable : convention log inapplicable : 1 observation(s) non strictement positive(s), minimum -36.98 le 2020-04-20. Le prix a été négatif : aucun log-rendement n'existe. La série est déclarée NON SCÉNARISABLE plutôt que corrigée en silence.

**DEXJPUS** (log) — σ à 60 pas = **0.04200** · estimateurs croisés : racine-h 0.04386, blocs disjoints 0.05386 (écart relatif 28.2 %) · dérive d'échantillon +0.00897 (+0.21 σ) · 2432 variations chevauchantes, 41 blocs indépendants · 2016-10-11 → 2026-10-02

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0630 | 104 | 2 | 0.0428 | 0.0668 | 0.64 | oui |
| -1.0 | -0.0630 | -0.0315 | 241 | 4 | 0.0991 | 0.1598 | 0.62 | oui |
| -0.5 | -0.0315 | -0.0105 | 384 | 6 | 0.1579 | 0.1747 | 0.90 | oui |
| +0.0 | -0.0105 | +0.0105 | 494 | 8 | 0.2031 | 0.1974 | 1.03 | oui |
| +0.5 | +0.0105 | +0.0315 | 537 | 9 | 0.2208 | 0.1747 | 1.26 | oui |
| +1.0 | +0.0315 | +0.0630 | 481 | 8 | 0.1978 | 0.1598 | 1.24 | oui |
| +2.0 | +0.0630 | +∞ | 191 | 3 | 0.0785 | 0.0668 | 1.18 | oui |

**DEXUSEU** (log) — σ à 60 pas = **0.03429** · estimateurs croisés : racine-h 0.03467, blocs disjoints 0.03601 (écart relatif 5.0 %) · dérive d'échantillon +0.00173 (+0.05 σ) · 2432 variations chevauchantes, 41 blocs indépendants · 2016-10-11 → 2026-10-02

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0514 | 130 | 2 | 0.0535 | 0.0668 | 0.80 | oui |
| -1.0 | -0.0514 | -0.0257 | 325 | 5 | 0.1336 | 0.1598 | 0.84 | oui |
| -0.5 | -0.0257 | -0.0086 | 505 | 8 | 0.2076 | 0.1747 | 1.19 | oui |
| +0.0 | -0.0086 | +0.0086 | 618 | 10 | 0.2541 | 0.1974 | 1.29 | oui |
| +0.5 | +0.0086 | +0.0257 | 320 | 5 | 0.1316 | 0.1747 | 0.75 | oui |
| +1.0 | +0.0257 | +0.0514 | 308 | 5 | 0.1266 | 0.1598 | 0.79 | oui |
| +2.0 | +0.0514 | +∞ | 226 | 4 | 0.0929 | 0.0668 | 1.39 | oui |

**DGS10** (niveau) — σ à 60 pas = **0.42305** · estimateurs croisés : racine-h 0.41452, blocs disjoints 0.43426 (écart relatif 4.8 %) · dérive d'échantillon +0.06439 (+0.15 σ) · 2436 variations chevauchantes, 41 blocs indépendants · 2016-10-11 → 2026-10-05

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.6346 | 123 | 2 | 0.0505 | 0.0668 | 0.76 | oui |
| -1.0 | -0.6346 | -0.3173 | 284 | 5 | 0.1166 | 0.1598 | 0.73 | oui |
| -0.5 | -0.3173 | -0.1058 | 371 | 6 | 0.1523 | 0.1747 | 0.87 | oui |
| +0.0 | -0.1058 | +0.1058 | 528 | 9 | 0.2167 | 0.1974 | 1.10 | oui |
| +0.5 | +0.1058 | +0.3173 | 555 | 9 | 0.2278 | 0.1747 | 1.30 | oui |
| +1.0 | +0.3173 | +0.6346 | 368 | 6 | 0.1511 | 0.1598 | 0.95 | oui |
| +2.0 | +0.6346 | +∞ | 207 | 3 | 0.0850 | 0.0668 | 1.27 | oui |

**DGS2** (niveau) — σ à 60 pas = **0.49601** · estimateurs croisés : racine-h 0.42180, blocs disjoints 0.51858 (écart relatif 22.9 %) · dérive d'échantillon +0.08296 (+0.17 σ) · 2436 variations chevauchantes, 41 blocs indépendants · 2016-10-11 → 2026-10-05

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.7440 | 115 | 2 | 0.0472 | 0.0668 | 0.71 | oui |
| -1.0 | -0.7440 | -0.3720 | 228 | 4 | 0.0936 | 0.1598 | 0.59 | oui |
| -0.5 | -0.3720 | -0.1240 | 323 | 5 | 0.1326 | 0.1747 | 0.76 | oui |
| +0.0 | -0.1240 | +0.1240 | 739 | 12 | 0.3034 | 0.1974 | 1.54 | oui |
| +0.5 | +0.1240 | +0.3720 | 482 | 8 | 0.1979 | 0.1747 | 1.13 | oui |
| +1.0 | +0.3720 | +0.7440 | 348 | 6 | 0.1429 | 0.1598 | 0.89 | oui |
| +2.0 | +0.7440 | +∞ | 201 | 3 | 0.0825 | 0.0668 | 1.24 | oui |

**DGS30** (niveau) — σ à 60 pas = **0.36492** · estimateurs croisés : racine-h 0.39248, blocs disjoints 0.36874 (écart relatif 7.6 %) · dérive d'échantillon +0.05900 (+0.16 σ) · 2436 variations chevauchantes, 41 blocs indépendants · 2016-10-11 → 2026-10-05

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.5474 | 128 | 2 | 0.0525 | 0.0668 | 0.79 | oui |
| -1.0 | -0.5474 | -0.2737 | 276 | 5 | 0.1133 | 0.1598 | 0.71 | oui |
| -0.5 | -0.2737 | -0.0912 | 338 | 6 | 0.1388 | 0.1747 | 0.79 | oui |
| +0.0 | -0.0912 | +0.0912 | 629 | 10 | 0.2582 | 0.1974 | 1.31 | oui |
| +0.5 | +0.0912 | +0.2737 | 461 | 8 | 0.1892 | 0.1747 | 1.08 | oui |
| +1.0 | +0.2737 | +0.5474 | 394 | 7 | 0.1617 | 0.1598 | 1.01 | oui |
| +2.0 | +0.5474 | +∞ | 210 | 4 | 0.0862 | 0.0668 | 1.29 | oui |

**DTWEXBGS** (log) — σ à 60 pas = **0.02584** · estimateurs croisés : racine-h 0.02408, blocs disjoints 0.02862 (écart relatif 18.9 %) · dérive d'échantillon +0.00068 (+0.03 σ) · 2430 variations chevauchantes, 40 blocs indépendants · 2016-10-11 → 2026-10-02

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0388 | 167 | 3 | 0.0687 | 0.0668 | 1.03 | oui |
| -1.0 | -0.0388 | -0.0194 | 382 | 6 | 0.1572 | 0.1598 | 0.98 | oui |
| -0.5 | -0.0194 | -0.0065 | 358 | 6 | 0.1473 | 0.1747 | 0.84 | oui |
| +0.0 | -0.0065 | +0.0065 | 547 | 9 | 0.2251 | 0.1974 | 1.14 | oui |
| +0.5 | +0.0065 | +0.0194 | 463 | 8 | 0.1905 | 0.1747 | 1.09 | oui |
| +1.0 | +0.0194 | +0.0388 | 305 | 5 | 0.1255 | 0.1598 | 0.79 | oui |
| +2.0 | +0.0388 | +∞ | 208 | 3 | 0.0856 | 0.0668 | 1.28 | oui |

**NASDAQ100** (log) — σ à 60 pas = **0.08869** · estimateurs croisés : racine-h 0.11135, blocs disjoints 0.07608 (écart relatif 46.4 %) · dérive d'échantillon +0.04417 (+0.50 σ) · 2451 variations chevauchantes, 41 blocs indépendants · 2016-10-10 → 2026-10-05

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.1330 | 109 | 2 | 0.0445 | 0.0668 | 0.67 | oui |
| -1.0 | -0.1330 | -0.0665 | 166 | 3 | 0.0677 | 0.1598 | 0.42 ⚠ | oui |
| -0.5 | -0.0665 | -0.0222 | 186 | 3 | 0.0759 | 0.1747 | 0.43 ⚠ | oui |
| +0.0 | -0.0222 | +0.0222 | 354 | 6 | 0.1444 | 0.1974 | 0.73 | oui |
| +0.5 | +0.0222 | +0.0665 | 589 | 10 | 0.2403 | 0.1747 | 1.38 | oui |
| +1.0 | +0.0665 | +0.1330 | 731 | 12 | 0.2982 | 0.1598 | 1.87 | oui |
| +2.0 | +0.1330 | +∞ | 316 | 5 | 0.1289 | 0.0668 | 1.93 | oui |

**SP500** (log) — σ à 60 pas = **0.06915** · estimateurs croisés : racine-h 0.08846, blocs disjoints 0.06194 (écart relatif 42.8 %) · dérive d'échantillon +0.03059 (+0.44 σ) · 2450 variations chevauchantes, 41 blocs indépendants · 2016-10-10 → 2026-10-05

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.1037 | 115 | 2 | 0.0469 | 0.0668 | 0.70 | oui |
| -1.0 | -0.1037 | -0.0519 | 158 | 3 | 0.0645 | 0.1598 | 0.40 ⚠ | oui |
| -0.5 | -0.0519 | -0.0173 | 176 | 3 | 0.0718 | 0.1747 | 0.41 ⚠ | oui |
| +0.0 | -0.0173 | +0.0173 | 293 | 5 | 0.1196 | 0.1974 | 0.61 | oui |
| +0.5 | +0.0173 | +0.0519 | 746 | 12 | 0.3045 | 0.1747 | 1.74 | oui |
| +1.0 | +0.0519 | +0.1037 | 752 | 13 | 0.3069 | 0.1598 | 1.92 | oui |
| +2.0 | +0.1037 | +∞ | 210 | 4 | 0.0857 | 0.0668 | 1.28 | oui |

**VIXCLS** (log) — σ à 60 pas = **0.34678** · estimateurs croisés : racine-h 0.61237, blocs disjoints 0.32332 (écart relatif 89.4 %) · dérive d'échantillon +0.00333 (+0.01 σ) · 2483 variations chevauchantes, 41 blocs indépendants · 2016-10-10 → 2026-10-05

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.5202 | 77 | 1 | 0.0310 | 0.0668 | 0.46 ⚠ | oui |
| -1.0 | -0.5202 | -0.2601 | 388 | 6 | 0.1563 | 0.1598 | 0.98 | oui |
| -0.5 | -0.2601 | -0.0867 | 604 | 10 | 0.2433 | 0.1747 | 1.39 | oui |
| +0.0 | -0.0867 | +0.0867 | 615 | 10 | 0.2477 | 0.1974 | 1.25 | oui |
| +0.5 | +0.0867 | +0.2601 | 373 | 6 | 0.1502 | 0.1747 | 0.86 | oui |
| +1.0 | +0.2601 | +0.5202 | 248 | 4 | 0.0999 | 0.1598 | 0.62 | oui |
| +2.0 | +0.5202 | +∞ | 178 | 3 | 0.0717 | 0.0668 | 1.07 | oui |

---

## 6. TEST D'ASYMÉTRIE — DÉFINITION UNIQUE (R-030), L'ESPÉRANCE DÉCIDE

> Test d'admission : **espérance calculée sur la grille symétrique complète, les deux queues incluses**. Le rapport gain maximal / perte maximale est publié **pour information** et ne peut fonder aucune admission seul (T-001, faute E-018). Le rapport gain maximal / perte du scénario central est **interdit**. Une seule formulation, appliquée à tous les candidats, position détenue comprise.

| candidat | verdict | espérance % NAV | sans dérive | 1re moitié | 2e moitié | gain max | perte max | ratio (info) | critères échoués |
|---|:---:|---:|---:|---:|---:|---:|---:|---:|---|
| M005-DCOILBRENTEU-HAUSSE-ALIGNE | REFUSEE | +0.260 | +0.126 | +0.253 | +0.146 | +5.05 | -3.20 | 1.58:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DCOILBRENTEU-HAUSSE-CONTRARIEN | REFUSEE | +0.260 | +0.126 | +0.253 | +0.146 | +5.05 | -3.20 | 1.58:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DCOILBRENTEU-BAISSE-ALIGNE | REFUSEE | -0.260 | -0.126 | -0.253 | -0.146 | +3.20 | -5.05 | 0.63:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILBRENTEU-BAISSE-CONTRARIEN | REFUSEE | -0.260 | -0.126 | -0.253 | -0.146 | +3.20 | -5.05 | 0.63:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-HAUSSE-ALIGNE | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-HAUSSE-CONTRARIEN | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-BAISSE-ALIGNE | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-BAISSE-CONTRARIEN | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-HAUSSE-ALIGNE | REFUSEE | +0.000 | -0.067 | -0.075 | +0.041 | +0.63 | -0.72 | 0.87:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-HAUSSE-CONTRARIEN | REFUSEE | +0.000 | -0.067 | -0.075 | +0.041 | +0.63 | -0.72 | 0.87:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-BAISSE-ALIGNE | REFUSEE | -0.000 | +0.067 | +0.075 | -0.041 | +0.72 | -0.63 | 1.15:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-BAISSE-CONTRARIEN | REFUSEE | -0.000 | +0.067 | +0.075 | -0.041 | +0.72 | -0.63 | 1.15:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-HAUSSE-ALIGNE | REFUSEE | -0.060 | -0.074 | -0.031 | -0.071 | +0.49 | -0.60 | 0.82:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-HAUSSE-CONTRARIEN | REFUSEE | -0.060 | -0.074 | -0.031 | -0.071 | +0.49 | -0.60 | 0.82:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-BAISSE-ALIGNE | REFUSEE | +0.060 | +0.074 | +0.031 | +0.071 | +0.60 | -0.49 | 1.22:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DEXUSEU-BAISSE-CONTRARIEN | REFUSEE | +0.060 | +0.074 | +0.031 | +0.071 | +0.60 | -0.49 | 1.22:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DGS10-HAUSSE-ALIGNE | REFUSEE | +0.005 | -0.030 | -0.053 | +0.054 | +0.47 | -0.57 | 0.83:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-HAUSSE-CONTRARIEN | REFUSEE | +0.005 | -0.030 | -0.053 | +0.054 | +0.47 | -0.57 | 0.83:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-BAISSE-ALIGNE | REFUSEE | -0.005 | +0.030 | +0.053 | -0.054 | +0.57 | -0.47 | 1.20:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-BAISSE-CONTRARIEN | REFUSEE | -0.005 | +0.030 | +0.053 | -0.054 | +0.57 | -0.47 | 1.20:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-HAUSSE-ALIGNE | REFUSEE | -0.007 | -0.018 | -0.024 | +0.004 | +0.13 | -0.17 | 0.76:1 | 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-HAUSSE-CONTRARIEN | REFUSEE | -0.007 | -0.018 | -0.024 | +0.004 | +0.13 | -0.17 | 0.76:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-BAISSE-ALIGNE | REFUSEE | +0.007 | +0.018 | +0.024 | -0.004 | +0.17 | -0.13 | 1.31:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-BAISSE-CONTRARIEN | REFUSEE | +0.007 | +0.018 | +0.024 | -0.004 | +0.17 | -0.13 | 1.31:1 | 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-HAUSSE-ALIGNE | REFUSEE | +0.010 | -0.046 | -0.099 | +0.119 | +0.74 | -0.94 | 0.79:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-HAUSSE-CONTRARIEN | REFUSEE | +0.010 | -0.046 | -0.099 | +0.119 | +0.74 | -0.94 | 0.79:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-BAISSE-ALIGNE | REFUSEE | -0.010 | +0.046 | +0.099 | -0.119 | +0.94 | -0.74 | 1.27:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-BAISSE-CONTRARIEN | REFUSEE | -0.010 | +0.046 | +0.099 | -0.119 | +0.94 | -0.74 | 1.27:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-HAUSSE-ALIGNE | REFUSEE | -0.066 | -0.071 | -0.083 | -0.053 | +0.35 | -0.48 | 0.73:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-HAUSSE-CONTRARIEN | REFUSEE | -0.066 | -0.071 | -0.083 | -0.053 | +0.35 | -0.48 | 0.73:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-BAISSE-ALIGNE | REFUSEE | +0.066 | +0.071 | +0.083 | +0.053 | +0.48 | -0.35 | 1.36:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DTWEXBGS-BAISSE-CONTRARIEN | REFUSEE | +0.066 | +0.071 | +0.083 | +0.053 | +0.48 | -0.35 | 1.36:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-HAUSSE-ALIGNE | REFUSEE | +0.305 | -0.034 | +0.453 | +0.183 | +1.48 | -1.37 | 1.08:1 | 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-HAUSSE-CONTRARIEN | REFUSEE | +0.305 | -0.034 | +0.453 | +0.183 | +1.48 | -1.37 | 1.08:1 | 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-BAISSE-ALIGNE | REFUSEE | -0.305 | +0.034 | -0.453 | -0.183 | +1.37 | -1.48 | 0.93:1 | 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-NASDAQ100-BAISSE-CONTRARIEN | REFUSEE | -0.305 | +0.034 | -0.453 | -0.183 | +1.37 | -1.48 | 0.93:1 | 12_esperance_positive, 13_esperance_non_portee_par_derive, 14_esperance_stable_dans_le_temps |
| M005-SP500-HAUSSE-ALIGNE | REFUSEE | +0.187 | -0.043 | +0.217 | +0.154 | +1.11 | -1.11 | 1.00:1 | 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-SP500-HAUSSE-CONTRARIEN | REFUSEE | +0.187 | -0.043 | +0.217 | +0.154 | +1.11 | -1.11 | 1.00:1 | 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-SP500-BAISSE-ALIGNE | REFUSEE | -0.187 | +0.043 | -0.217 | -0.154 | +1.11 | -1.11 | 1.00:1 | 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-SP500-BAISSE-CONTRARIEN | REFUSEE | -0.187 | +0.043 | -0.217 | -0.154 | +1.11 | -1.11 | 1.00:1 | 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |

**Décompte des échecs par critère** (un candidat peut échouer sur plusieurs) :

| critère | candidats en échec |
|---|---:|
| 1_series_presentes | 0 |
| 2_domaine_ouvert | 0 |
| 3_instrument_calculable | 0 |
| 4_profondeur_suffisante | 0 |
| 5_bandes_estimables | 4 |
| 6_couples_complets | 0 |
| 7_lecture_conforme_table | 0 |
| 8_confirmations_independantes | 20 |
| 9_test_execute_et_vrai | 20 |
| 10_invalidation_fait_date | 12 |
| 11_invalidation_non_deja_survenue | 26 |
| 12_esperance_positive | 22 |
| 13_esperance_non_portee_par_derive | 24 |
| 14_esperance_stable_dans_le_temps | 30 |
| 16_arete_conditionnelle_mesuree | 39 |
| 15_enonce_sans_affirmation_politique_non_etayee | 0 |

**Critères MORTS par construction** — un critère qu'aucune donnée ne peut franchir n'est pas un critère exigeant, c'est un critère éteint. « Aucune thèse ne passe parce qu'aucune n'est bonne » et « aucune thèse ne passe parce qu'un critère est mort » ne se pilotent pas pareil.

| critère | candidats concernés | motif |
|---|---:|---|
| 10_invalidation_fait_date | 12 | aucune série à publication mensuelle datée dans le dossier déclaré de l'instrument : le critère ne peut pas être franchi, quelle que soit la donnée |
| 5_bandes_estimables | 4 | série non scénarisable : voir le motif de distribution |

**Séries NON SCÉNARISABLES** (aucune grille ne peut leur être appliquée) :

- `DCOILWTICO` : convention log inapplicable : 1 observation(s) non strictement positive(s), minimum -36.98 le 2020-04-20. Le prix a été négatif : aucun log-rendement n'existe. La série est déclarée NON SCÉNARISABLE plutôt que corrigée en silence.

---

## 7. DÉCLENCHEURS

Aucun déclencheur pré-engagé n'est émis. Un déclencheur est une position différée : il exige les trois contrôles du §5 de la doctrine, dont la **fréquence historique de franchissement**. Le moteur publie cette fréquence pour tout seuil qu'il émet (§8 ci-dessous) et n'en engage aucun tant qu'aucune thèse n'est transmise.

---

## 8. PROBABILITÉS ASSIGNÉES — CALCULÉES (R-031), JAMAIS ESTIMÉES À VUE

Aucune prédiction émise ce cycle : aucune thèse n'a été transmise. Une prédiction émise sans thèse serait une inscription décorative au registre (interdit n° 3 du §7 de la doctrine).

**État du registre de calibration** — 0 lignes · 0 résolues mécaniquement · 0 ouvertes · 0 non résolubles mécaniquement (—).

**Score de Brier : non calculable.** aucune prédiction résolue mécaniquement à ce jour : le score de Brier n'est pas calculable et n'est pas remplacé par une approximation. Une section qui prédit sans jamais mesurer ses prédictions n'apprend rien — et ce moteur publie l'écart plutôt que de le combler.

---

## 9. CE QUI INVALIDERAIT CE BRIEF — ÉCRIT AVANT LES FAITS

1. **La grille.** Toute exécution ultérieure dont l'empreinte de grille diffère de `6aaeb3863c875923…` invalide toute comparaison avec ce brief.
2. **Les identités comptables.** Si un résidu dépasse la tolérance 0.02, la structure de redondance publiée au §4 est fausse et le décompte des confirmations indépendantes avec elle.
3. **Les bandes.** Toute bande retombant sous 20 observations rend l'espérance correspondante non estimable.
4. **Les invalidations de thèse** figurent dans chaque fiche du §6 : publication mensuelle datée, testée par le code.
5. **La stabilité temporelle.** Une thèse dont l'espérance cesse d'être positive sur l'une des deux moitiés de l'échantillon est retirée à l'exécution suivante, sans décision d'agent.

---

## 10. SOURCES, RÉSERVES DE QUALITÉ, ET CE QUE CE MOTEUR NE FAIT PAS

**Source unique : dépôt Apollon `data/history/*.csv`, 26 séries FRED.** Aucune valeur n'a d'autre origine. Portée temporelle complète publiée série par série au §3 (E-004).

- `BAMLC0A0CM` : percentile REFUSÉ sur 5 ans — profondeur réelle 783 obs / 2.99 ans (début 2023-10-09). R-011 : un percentile calculé sur une série tronquée est sans valeur.
- `BAMLH0A0HYM2` : percentile REFUSÉ sur 5 ans — profondeur réelle 784 obs / 2.99 ans (début 2023-10-09). R-011 : un percentile calculé sur une série tronquée est sans valeur.
- `BAMLH0A0HYM2` : instrument NON ADMISSIBLE — P&L non calculable depuis le dépôt : l'OAS est un spread, et le dépôt ne contient pas le rendement de l'indice, donc pas la duration de spread. Aucune valeur ne peut être produite sans un chiffre extérieur aux données (E-002).
- `BAMLC0A0CM` : instrument NON ADMISSIBLE — P&L non calculable depuis le dépôt : l'OAS est un spread, et le dépôt ne contient pas le rendement de l'indice, donc pas la duration de spread. Aucune valeur ne peut être produite sans un chiffre extérieur aux données (E-002).
- Retards sur la date d'arrêté unique (E-014) : DCOILBRENTEU 4 séance(s), DCOILWTICO 4 séance(s), DEXJPUS 1 séance(s), DEXUSEU 1 séance(s), DTWEXBGS 1 séance(s)

**Vérification tierce (R-032) : NON SATISFAITE pour ce brief.** Le moteur ne dispose d'aucune source extérieure au dépôt. Trois estimateurs **internes** de σ sont publiés côte à côte au §5 ; ce sont des contrôles de cohérence interne, **pas** une vérification tierce, et ils ne sont pas présentés comme telle.

**Ce que ce moteur ne peut pas faire.** Il ne prouve aucune capacité prédictive : la règle de confirmation est une règle de percentile, déclarée et symétrique, pas un modèle validé hors échantillon. Il ne corrige pas la multiplicité : 40 candidats sont évalués et aucune pénalité de sélection n'est appliquée à l'espérance — c'est une limite déclarée, pas un oubli. Il ne voit ni les événements politiques, ni les décisions de banques centrales : le dépôt ne contient que des séries FRED, et toute affirmation de politique monétaire non adossée à `DFF` est refusée (critère 15, faute E-006).

---

*Fin du brief 005. Produit mécaniquement. Ne constitue pas un conseil en investissement.*