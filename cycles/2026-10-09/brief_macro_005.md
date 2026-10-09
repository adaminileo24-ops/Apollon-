# BRIEF MACRO n° 005 — arrêté au 2026-10-08

*Produit par `apollon_macro.py` le 2026-10-09T23:30:46+00:00. Aucune valeur de ce document n'est saisie à la main : chacune porte sa série, sa date et sa profondeur. Bloc à copier tel quel.*

**Grille de scénarios (R-029, §11), déclarée avant toute lecture de données et empreintée :** `[-2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0]` · empreinte SHA-256 `6aaeb3863c875923…` · symétrique : True · horizon 60 séances (3 mois pour les séries mensuelles).

---

## 1. CONCLUSION, ÉNONCÉE D'ABORD

**40 candidats déclarés d'avance (10 instruments × 2 directions × 2 règles de confirmation). 40 évalués. 0 thèse(s) survivent aux quinze critères.**

**Abstention. Aucune thèse ne survit.** Ce n'est pas un silence : c'est un résultat, produit par le même portier que celui qui aurait admis une thèse. Le détail des échecs, critère par critère, figure au §6. La Section Macro ne transmet rien à la Section Risque ce cycle.

**Position détenue (contrôle 9, E-020) — 100 % cash, testée sur la même grille.** Espérance excédentaire du cash : +0.000 % de NAV. Référence 60/40 : +1.366 % (hors dérive : -0.176 %). **Écart du cash contre la référence : -1.366 % de NAV** sur 60 séances.

---

## 2. CE QUI A CHANGÉ — MÉCANISME, PAS CONTENU

Fait, étiqueté : les briefs 001 à 004 étaient rédigés par un agent. Celui-ci est produit par un moteur. Le paramètre libre de la Section Macro — la grille de scénarios — n'est plus accessible à l'agent : il est déclaré en tête de fichier, symétrique par construction, et son empreinte SHA-256 est vérifiée avant chaque usage. Sur le brief 004, ce paramètre avait porté le ratio annoncé de 1,29:1 à 3,0:1.

---

## 3. M1 · M2 · M3 · M4 — ÉTAT DES SÉRIES (FAIT)

Toutes les valeurs sont des FAITS lus dans le dépôt. Le retard est compté en séances ouvrées depuis la date d'arrêté unique. Les couples obligatoires sont vérifiés par le rendu : ce bloc ne peut pas être émis si un membre d'un couple manque.

| série | rôle déclaré | valeur | date | retard | n obs | profondeur | pct 1 an | pct 5 ans | pct complet |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| BAMLC0A0CM | risque_credit_ig | 0.82 | 2026-10-08 | 0 | 785 | 3.00 ans | 80.6 | REFUSÉ (insuffisante, -38 %) | 43.4 |
| BAMLH0A0HYM2 | risque_credit_hy | 3.15 | 2026-10-08 | 0 | 786 | 3.00 ans | 91.3 | REFUSÉ (insuffisante, -38 %) | 63.7 |
| CPIAUCSL | inflation_globale | 334.1 | 2026-08-01 | 68 | 118 | 9.83 ans | 100.0 | 100.0 | 100.0 |
| CPILFESL | inflation_sous_jacente | 337.8 | 2026-08-01 | 68 | 118 | 9.83 ans | 100.0 | 100.0 | 100.0 |
| DCOILBRENTEU | prix_energie | 125.4 | 2026-10-06 | 2 | 2533 | 9.98 ans | 97.2 | 98.5 | 99.2 |
| DCOILWTICO | prix_energie_wti | 96.24 | 2026-10-06 | 2 | 2497 | 9.98 ans | 79.0 | 87.3 | 93.6 |
| DEXJPUS | devise_usdjpy | 157.8 | 2026-10-02 | 4 | 2492 | 9.97 ans | 51.6 | 88.5 | 94.2 |
| DEXUSEU | devise_eurusd | 1.126 | 2026-10-02 | 4 | 2492 | 9.97 ans | 0.8 | 63.3 | 50.4 |
| DFF | politique_monetaire | 3.88 | 2026-10-08 | 0 | 3650 | 9.99 ans | 100.0 | 26.3 | 70.9 |
| DFII10 | taux_reel_10a | 2.87 | 2026-10-08 | 0 | 2499 | 9.99 ans | 96.8 | 99.4 | 99.7 |
| DGS10 | taux_nominal_10a | 5.22 | 2026-10-08 | 0 | 2499 | 9.99 ans | 96.8 | 99.4 | 99.7 |
| DGS2 | taux_nominal_2a | 4.75 | 2026-10-08 | 0 | 2499 | 9.99 ans | 94.8 | 87.0 | 93.4 |
| DGS30 | taux_nominal_30a | 5.6 | 2026-10-08 | 0 | 2499 | 9.99 ans | 97.6 | 99.5 | 99.8 |
| DTWEXBGS | dollar_large | 121.4 | 2026-10-02 | 4 | 2490 | 9.97 ans | 94.8 | 62.8 | 79.1 |
| INDPRO | activite_industrielle | 103.1 | 2026-08-01 | 68 | 119 | 9.83 ans | 100.0 | 100.0 | 92.4 |
| NASDAQ100 | prix_actions_tech | 3.073e+04 | 2026-10-08 | 0 | 2513 | 9.99 ans | 98.0 | 99.6 | 99.8 |
| OVXCLS | volatilite_implicite_petrole | 48.4 | 2026-10-08 | 0 | 2514 | 9.99 ans | 41.7 | 74.8 | 81.2 |
| PAYEMS | emploi | 1.59e+05 | 2026-09-01 | 37 | 120 | 9.92 ans | 100.0 | 100.0 | 100.0 |
| SP500 | prix_actions | 7765 | 2026-10-08 | 0 | 2512 | 9.99 ans | 98.0 | 99.6 | 99.8 |
| T10Y2Y | pente_courbe | 0.47 | 2026-10-08 | 0 | 2499 | 9.99 ans | 35.3 | 70.6 | 56.1 |
| T10YIE | point_mort_10a | 2.35 | 2026-10-08 | 0 | 2499 | 9.99 ans | 74.2 | 61.0 | 78.0 |
| T5YIFR | point_mort_5a5a | 2.33 | 2026-10-08 | 0 | 2499 | 9.99 ans | 91.7 | 77.0 | 88.1 |
| UNRATE | chomage | 4.2 | 2026-09-01 | 37 | 119 | 9.92 ans | 33.3 | 78.3 | 63.9 |
| VIXCLS | volatilite_implicite | 15.41 | 2026-10-08 | 0 | 2545 | 9.99 ans | 17.9 | 27.0 | 36.5 |
| VXDCLS | volatilite_implicite_dow | 15.45 | 2026-10-08 | 0 | 2515 | 9.99 ans | 44.0 | 41.8 | 45.3 |
| VXVCLS | volatilite_implicite_3m | 18.08 | 2026-10-08 | 0 | 2512 | 9.99 ans | 9.1 | 25.7 | 40.1 |

**Couples obligatoires contrôlés :** CPIAUCSL/CPILFESL, DGS10/DFII10, DGS10/T10YIE, BAMLH0A0HYM2/BAMLC0A0CM, UNRATE/PAYEMS, VIXCLS/SP500 — 0 manquement(s).

**Inflation en trois chiffres (contrôle 2, E-005).** Global +3.71 % sur un an (CPIAUCSL, 2026-08-01) · sous-jacent +2.76 % (CPILFESL) · **écart hors sous-jacent +95 pb**. Contribution énergie NON publiée : `CPIENGSL` est absente du dépôt. Lacune nommée avec le code FRED qui la comble (R-028) ; elle n'est pas présentée comme une limite de méthode. L'écart ci-dessus est l'écart global/sous-jacent, pas la contribution énergie.

---

## 4. IDENTITÉS COMPTABLES ET REDONDANCES (vérifiées numériquement)

| identité | vérifiable | n dates | résidu absolu max | tolérance | vérifiée |
|---|:---:|---:|---:|---:|:---:|
| T10YIE = DGS10 - DFII10 | oui | 2499 | 0.0000 | 0.02 | OUI |
| T10Y2Y = DGS10 - DGS2 | oui | 2499 | 0.0000 | 0.02 | OUI |

**Redondances détectées (11) — deux séries liées ne comptent jamais pour deux confirmations indépendantes :**

- identité comptable : T10YIE = DGS10 - DFII10 — T10YIE, DGS10, DFII10 (résidu max 0.0000)
- identité comptable : T10Y2Y = DGS10 - DGS2 — T10Y2Y, DGS10, DGS2 (résidu max 0.0000)
- corrélation des variations à 60 séances : BAMLC0A0CM / BAMLH0A0HYM2 = +0.939 sur 725 points (seuil 0.9)
- corrélation des variations à 60 séances : DGS10 / DGS30 = +0.967 sur 2439 points (seuil 0.9)
- corrélation des variations à 60 séances : INDPRO / PAYEMS = +0.913 sur 116 points (seuil 0.9)
- corrélation des variations à 60 séances : INDPRO / UNRATE = -0.918 sur 115 points (seuil 0.9)
- corrélation des variations à 60 séances : NASDAQ100 / SP500 = +0.903 sur 2452 points (seuil 0.9)
- corrélation des variations à 60 séances : PAYEMS / UNRATE = -0.983 sur 116 points (seuil 0.9)
- corrélation des variations à 60 séances : VIXCLS / VXDCLS = +0.930 sur 2452 points (seuil 0.9)
- corrélation des variations à 60 séances : VIXCLS / VXVCLS = +0.958 sur 2452 points (seuil 0.9)
- corrélation des variations à 60 séances : VXDCLS / VXVCLS = +0.934 sur 2452 points (seuil 0.9)

---

## 5. GRILLE, σ MESURÉ, ET DOUBLE CONFRONTATION DES PROBABILITÉS

σ est **mesuré** sur chaque série, jamais choisi. Les probabilités sont les **fréquences historiques** dans chaque bande, jamais un jugement. L'effectif de chaque bande est publié ; sous 20 observations la bande est déclarée NON ESTIMABLE. La colonne « emp./gauss. » est la double confrontation exigée par §11.5 : tout écart supérieur à un facteur 2 est déclaré (⚠).

**BAMLH0A0HYM2** (niveau) — σ à 60 pas = **0.45145** · estimateurs croisés : racine-h 0.53967, blocs disjoints 0.37276 (écart relatif 44.8 %) · dérive d'échantillon -0.09598 (-0.21 σ) · 726 variations chevauchantes, 12 blocs indépendants · 2023-10-10 → 2026-10-08

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.6772 | 51 | 1 | 0.0702 | 0.0668 | 1.05 | oui |
| -1.0 | -0.6772 | -0.3386 | 121 | 2 | 0.1667 | 0.1598 | 1.04 | oui |
| -0.5 | -0.3386 | -0.1129 | 189 | 3 | 0.2603 | 0.1747 | 1.49 | oui |
| +0.0 | -0.1129 | +0.1129 | 195 | 3 | 0.2686 | 0.1974 | 1.36 | oui |
| +0.5 | +0.1129 | +0.3386 | 80 | 1 | 0.1102 | 0.1747 | 0.63 | oui |
| +1.0 | +0.3386 | +0.6772 | 61 | 1 | 0.0840 | 0.1598 | 0.53 | oui |
| +2.0 | +0.6772 | +∞ | 29 | 0 | 0.0399 | 0.0668 | 0.60 | oui |

**DCOILBRENTEU** (log) — σ à 60 pas = **0.24814** · estimateurs croisés : racine-h 0.24948, blocs disjoints 0.33864 (écart relatif 36.5 %) · dérive d'échantillon +0.01745 (+0.07 σ) · 2473 variations chevauchantes, 41 blocs indépendants · 2016-10-11 → 2026-10-06

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.3722 | 84 | 1 | 0.0340 | 0.0668 | 0.51 | oui |
| -1.0 | -0.3722 | -0.1861 | 154 | 3 | 0.0623 | 0.1598 | 0.39 ⚠ | oui |
| -0.5 | -0.1861 | -0.0620 | 500 | 8 | 0.2022 | 0.1747 | 1.16 | oui |
| +0.0 | -0.0620 | +0.0620 | 770 | 13 | 0.3114 | 0.1974 | 1.58 | oui |
| +0.5 | +0.0620 | +0.1861 | 607 | 10 | 0.2455 | 0.1747 | 1.41 | oui |
| +1.0 | +0.1861 | +0.3722 | 218 | 4 | 0.0882 | 0.1598 | 0.55 | oui |
| +2.0 | +0.3722 | +∞ | 140 | 2 | 0.0566 | 0.0668 | 0.85 | oui |

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

**DGS10** (niveau) — σ à 60 pas = **0.42333** · estimateurs croisés : racine-h 0.41444, blocs disjoints 0.43426 (écart relatif 4.8 %) · dérive d'échantillon +0.06514 (+0.15 σ) · 2439 variations chevauchantes, 41 blocs indépendants · 2016-10-11 → 2026-10-08

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.6350 | 123 | 2 | 0.0504 | 0.0668 | 0.75 | oui |
| -1.0 | -0.6350 | -0.3175 | 284 | 5 | 0.1164 | 0.1598 | 0.73 | oui |
| -0.5 | -0.3175 | -0.1058 | 371 | 6 | 0.1521 | 0.1747 | 0.87 | oui |
| +0.0 | -0.1058 | +0.1058 | 528 | 9 | 0.2165 | 0.1974 | 1.10 | oui |
| +0.5 | +0.1058 | +0.3175 | 555 | 9 | 0.2276 | 0.1747 | 1.30 | oui |
| +1.0 | +0.3175 | +0.6350 | 368 | 6 | 0.1509 | 0.1598 | 0.94 | oui |
| +2.0 | +0.6350 | +∞ | 210 | 4 | 0.0861 | 0.0668 | 1.29 | oui |

**DGS2** (niveau) — σ à 60 pas = **0.49602** · estimateurs croisés : racine-h 0.42164, blocs disjoints 0.51858 (écart relatif 23.0 %) · dérive d'échantillon +0.08357 (+0.17 σ) · 2439 variations chevauchantes, 41 blocs indépendants · 2016-10-11 → 2026-10-08

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.7440 | 115 | 2 | 0.0472 | 0.0668 | 0.71 | oui |
| -1.0 | -0.7440 | -0.3720 | 228 | 4 | 0.0935 | 0.1598 | 0.58 | oui |
| -0.5 | -0.3720 | -0.1240 | 323 | 5 | 0.1324 | 0.1747 | 0.76 | oui |
| +0.0 | -0.1240 | +0.1240 | 739 | 12 | 0.3030 | 0.1974 | 1.53 | oui |
| +0.5 | +0.1240 | +0.3720 | 482 | 8 | 0.1976 | 0.1747 | 1.13 | oui |
| +1.0 | +0.3720 | +0.7440 | 351 | 6 | 0.1439 | 0.1598 | 0.90 | oui |
| +2.0 | +0.7440 | +∞ | 201 | 3 | 0.0824 | 0.0668 | 1.23 | oui |

**DGS30** (niveau) — σ à 60 pas = **0.36510** · estimateurs croisés : racine-h 0.39244, blocs disjoints 0.36874 (écart relatif 7.5 %) · dérive d'échantillon +0.05961 (+0.16 σ) · 2439 variations chevauchantes, 41 blocs indépendants · 2016-10-11 → 2026-10-08

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.5476 | 128 | 2 | 0.0525 | 0.0668 | 0.79 | oui |
| -1.0 | -0.5476 | -0.2738 | 276 | 5 | 0.1132 | 0.1598 | 0.71 | oui |
| -0.5 | -0.2738 | -0.0913 | 338 | 6 | 0.1386 | 0.1747 | 0.79 | oui |
| +0.0 | -0.0913 | +0.0913 | 629 | 10 | 0.2579 | 0.1974 | 1.31 | oui |
| +0.5 | +0.0913 | +0.2738 | 461 | 8 | 0.1890 | 0.1747 | 1.08 | oui |
| +1.0 | +0.2738 | +0.5476 | 396 | 7 | 0.1624 | 0.1598 | 1.02 | oui |
| +2.0 | +0.5476 | +∞ | 211 | 4 | 0.0865 | 0.0668 | 1.29 | oui |

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

**NASDAQ100** (log) — σ à 60 pas = **0.08865** · estimateurs croisés : racine-h 0.11130, blocs disjoints 0.07849 (écart relatif 41.8 %) · dérive d'échantillon +0.04419 (+0.50 σ) · 2453 variations chevauchantes, 41 blocs indépendants · 2016-10-11 → 2026-10-08

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.1330 | 109 | 2 | 0.0444 | 0.0668 | 0.67 | oui |
| -1.0 | -0.1330 | -0.0665 | 166 | 3 | 0.0677 | 0.1598 | 0.42 ⚠ | oui |
| -0.5 | -0.0665 | -0.0222 | 186 | 3 | 0.0758 | 0.1747 | 0.43 ⚠ | oui |
| +0.0 | -0.0222 | +0.0222 | 353 | 6 | 0.1439 | 0.1974 | 0.73 | oui |
| +0.5 | +0.0222 | +0.0665 | 592 | 10 | 0.2413 | 0.1747 | 1.38 | oui |
| +1.0 | +0.0665 | +0.1330 | 731 | 12 | 0.2980 | 0.1598 | 1.86 | oui |
| +2.0 | +0.1330 | +∞ | 316 | 5 | 0.1288 | 0.0668 | 1.93 | oui |

**SP500** (log) — σ à 60 pas = **0.06913** · estimateurs croisés : racine-h 0.08841, blocs disjoints 0.05969 (écart relatif 48.1 %) · dérive d'échantillon +0.03059 (+0.44 σ) · 2452 variations chevauchantes, 41 blocs indépendants · 2016-10-11 → 2026-10-08

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.1037 | 115 | 2 | 0.0469 | 0.0668 | 0.70 | oui |
| -1.0 | -0.1037 | -0.0518 | 158 | 3 | 0.0644 | 0.1598 | 0.40 ⚠ | oui |
| -0.5 | -0.0518 | -0.0173 | 176 | 3 | 0.0718 | 0.1747 | 0.41 ⚠ | oui |
| +0.0 | -0.0173 | +0.0173 | 293 | 5 | 0.1195 | 0.1974 | 0.61 | oui |
| +0.5 | +0.0173 | +0.0518 | 746 | 12 | 0.3042 | 0.1747 | 1.74 | oui |
| +1.0 | +0.0518 | +0.1037 | 754 | 13 | 0.3075 | 0.1598 | 1.92 | oui |
| +2.0 | +0.1037 | +∞ | 210 | 4 | 0.0856 | 0.0668 | 1.28 | oui |

**VIXCLS** (log) — σ à 60 pas = **0.34664** · estimateurs croisés : racine-h 0.61180, blocs disjoints 0.31894 (écart relatif 91.8 %) · dérive d'échantillon +0.00330 (+0.01 σ) · 2485 variations chevauchantes, 41 blocs indépendants · 2016-10-11 → 2026-10-08

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.5200 | 77 | 1 | 0.0310 | 0.0668 | 0.46 ⚠ | oui |
| -1.0 | -0.5200 | -0.2600 | 388 | 6 | 0.1561 | 0.1598 | 0.98 | oui |
| -0.5 | -0.2600 | -0.0867 | 604 | 10 | 0.2431 | 0.1747 | 1.39 | oui |
| +0.0 | -0.0867 | +0.0867 | 617 | 10 | 0.2483 | 0.1974 | 1.26 | oui |
| +0.5 | +0.0867 | +0.2600 | 373 | 6 | 0.1501 | 0.1747 | 0.86 | oui |
| +1.0 | +0.2600 | +0.5200 | 248 | 4 | 0.0998 | 0.1598 | 0.62 | oui |
| +2.0 | +0.5200 | +∞ | 178 | 3 | 0.0716 | 0.0668 | 1.07 | oui |

---

## 6. TEST D'ASYMÉTRIE — DÉFINITION UNIQUE (R-030), L'ESPÉRANCE DÉCIDE

> Test d'admission : **espérance calculée sur la grille symétrique complète, les deux queues incluses**. Le rapport gain maximal / perte maximale est publié **pour information** et ne peut fonder aucune admission seul (T-001, faute E-018). Le rapport gain maximal / perte du scénario central est **interdit**. Une seule formulation, appliquée à tous les candidats, position détenue comprise.

| candidat | verdict | espérance % NAV | sans dérive | 1re moitié | 2e moitié | gain max | perte max | ratio (info) | critères échoués |
|---|:---:|---:|---:|---:|---:|---:|---:|---:|---|
| M005-DCOILBRENTEU-HAUSSE-ALIGNE | REFUSEE | +0.271 | +0.127 | +0.253 | +0.170 | +5.07 | -3.20 | 1.58:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DCOILBRENTEU-HAUSSE-CONTRARIEN | REFUSEE | +0.271 | +0.127 | +0.253 | +0.170 | +5.07 | -3.20 | 1.58:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DCOILBRENTEU-BAISSE-ALIGNE | REFUSEE | -0.271 | -0.127 | -0.253 | -0.170 | +3.20 | -5.07 | 0.63:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILBRENTEU-BAISSE-CONTRARIEN | REFUSEE | -0.271 | -0.127 | -0.253 | -0.170 | +3.20 | -5.07 | 0.63:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
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
| M005-DGS10-HAUSSE-ALIGNE | REFUSEE | +0.007 | -0.030 | -0.051 | +0.057 | +0.48 | -0.57 | 0.84:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-HAUSSE-CONTRARIEN | REFUSEE | +0.007 | -0.030 | -0.051 | +0.057 | +0.48 | -0.57 | 0.84:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-BAISSE-ALIGNE | REFUSEE | -0.007 | +0.030 | +0.051 | -0.057 | +0.57 | -0.48 | 1.19:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-BAISSE-CONTRARIEN | REFUSEE | -0.007 | +0.030 | +0.051 | -0.057 | +0.57 | -0.48 | 1.19:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-HAUSSE-ALIGNE | REFUSEE | -0.005 | -0.016 | -0.022 | +0.006 | +0.13 | -0.17 | 0.78:1 | 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-HAUSSE-CONTRARIEN | REFUSEE | -0.005 | -0.016 | -0.022 | +0.006 | +0.13 | -0.17 | 0.78:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-BAISSE-ALIGNE | REFUSEE | +0.005 | +0.016 | +0.022 | -0.006 | +0.17 | -0.13 | 1.28:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-BAISSE-CONTRARIEN | REFUSEE | +0.005 | +0.016 | +0.022 | -0.006 | +0.17 | -0.13 | 1.28:1 | 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-HAUSSE-ALIGNE | REFUSEE | +0.012 | -0.044 | -0.099 | +0.122 | +0.75 | -0.95 | 0.79:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-HAUSSE-CONTRARIEN | REFUSEE | +0.012 | -0.044 | -0.099 | +0.122 | +0.75 | -0.95 | 0.79:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-BAISSE-ALIGNE | REFUSEE | -0.012 | +0.044 | +0.099 | -0.122 | +0.95 | -0.75 | 1.27:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-BAISSE-CONTRARIEN | REFUSEE | -0.012 | +0.044 | +0.099 | -0.122 | +0.95 | -0.75 | 1.27:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-HAUSSE-ALIGNE | REFUSEE | -0.066 | -0.071 | -0.083 | -0.053 | +0.35 | -0.48 | 0.73:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-HAUSSE-CONTRARIEN | REFUSEE | -0.066 | -0.071 | -0.083 | -0.053 | +0.35 | -0.48 | 0.73:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-BAISSE-ALIGNE | REFUSEE | +0.066 | +0.071 | +0.083 | +0.053 | +0.48 | -0.35 | 1.36:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DTWEXBGS-BAISSE-CONTRARIEN | REFUSEE | +0.066 | +0.071 | +0.083 | +0.053 | +0.48 | -0.35 | 1.36:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-HAUSSE-ALIGNE | REFUSEE | +0.305 | -0.035 | +0.452 | +0.184 | +1.48 | -1.37 | 1.08:1 | 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-HAUSSE-CONTRARIEN | REFUSEE | +0.305 | -0.035 | +0.452 | +0.184 | +1.48 | -1.37 | 1.08:1 | 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-BAISSE-ALIGNE | REFUSEE | -0.305 | +0.035 | -0.452 | -0.184 | +1.37 | -1.48 | 0.93:1 | 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-NASDAQ100-BAISSE-CONTRARIEN | REFUSEE | -0.305 | +0.035 | -0.452 | -0.184 | +1.37 | -1.48 | 0.93:1 | 12_esperance_positive, 13_esperance_non_portee_par_derive, 14_esperance_stable_dans_le_temps |
| M005-SP500-HAUSSE-ALIGNE | REFUSEE | +0.187 | -0.043 | +0.216 | +0.153 | +1.11 | -1.11 | 1.00:1 | 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-SP500-HAUSSE-CONTRARIEN | REFUSEE | +0.187 | -0.043 | +0.216 | +0.153 | +1.11 | -1.11 | 1.00:1 | 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-SP500-BAISSE-ALIGNE | REFUSEE | -0.187 | +0.043 | -0.216 | -0.153 | +1.11 | -1.11 | 1.00:1 | 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-SP500-BAISSE-CONTRARIEN | REFUSEE | -0.187 | +0.043 | -0.216 | -0.153 | +1.11 | -1.11 | 1.00:1 | 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |

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

- `BAMLC0A0CM` : percentile REFUSÉ sur 5 ans — profondeur réelle 785 obs / 3.00 ans (début 2023-10-10). R-011 : un percentile calculé sur une série tronquée est sans valeur.
- `BAMLH0A0HYM2` : percentile REFUSÉ sur 5 ans — profondeur réelle 786 obs / 3.00 ans (début 2023-10-10). R-011 : un percentile calculé sur une série tronquée est sans valeur.
- `BAMLH0A0HYM2` : instrument NON ADMISSIBLE — P&L non calculable depuis le dépôt : l'OAS est un spread, et le dépôt ne contient pas le rendement de l'indice, donc pas la duration de spread. Aucune valeur ne peut être produite sans un chiffre extérieur aux données (E-002).
- `BAMLC0A0CM` : instrument NON ADMISSIBLE — P&L non calculable depuis le dépôt : l'OAS est un spread, et le dépôt ne contient pas le rendement de l'indice, donc pas la duration de spread. Aucune valeur ne peut être produite sans un chiffre extérieur aux données (E-002).
- Retards sur la date d'arrêté unique (E-014) : DCOILBRENTEU 2 séance(s), DCOILWTICO 2 séance(s), DEXJPUS 4 séance(s), DEXUSEU 4 séance(s), DTWEXBGS 4 séance(s)

**Vérification tierce (R-032) : NON SATISFAITE pour ce brief.** Le moteur ne dispose d'aucune source extérieure au dépôt. Trois estimateurs **internes** de σ sont publiés côte à côte au §5 ; ce sont des contrôles de cohérence interne, **pas** une vérification tierce, et ils ne sont pas présentés comme telle.

**Ce que ce moteur ne peut pas faire.** Il ne prouve aucune capacité prédictive : la règle de confirmation est une règle de percentile, déclarée et symétrique, pas un modèle validé hors échantillon. Il ne corrige pas la multiplicité : 40 candidats sont évalués et aucune pénalité de sélection n'est appliquée à l'espérance — c'est une limite déclarée, pas un oubli. Il ne voit ni les événements politiques, ni les décisions de banques centrales : le dépôt ne contient que des séries FRED, et toute affirmation de politique monétaire non adossée à `DFF` est refusée (critère 15, faute E-006).

---

*Fin du brief 005. Produit mécaniquement. Ne constitue pas un conseil en investissement.*