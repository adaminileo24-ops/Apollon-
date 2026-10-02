# BRIEF MACRO n° 005 — arrêté au 2026-09-30

*Produit par `apollon_macro.py` le 2026-10-02T11:06:49+00:00. Aucune valeur de ce document n'est saisie à la main : chacune porte sa série, sa date et sa profondeur. Bloc à copier tel quel.*

**Grille de scénarios (R-029, §11), déclarée avant toute lecture de données et empreintée :** `[-2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0]` · empreinte SHA-256 `6aaeb3863c875923…` · symétrique : True · horizon 60 séances (3 mois pour les séries mensuelles).

---

## 1. CONCLUSION, ÉNONCÉE D'ABORD

**40 candidats déclarés d'avance (10 instruments × 2 directions × 2 règles de confirmation). 40 évalués. 0 thèse(s) survivent aux quinze critères.**

**Abstention. Aucune thèse ne survit.** Ce n'est pas un silence : c'est un résultat, produit par le même portier que celui qui aurait admis une thèse. Le détail des échecs, critère par critère, figure au §6. La Section Macro ne transmet rien à la Section Risque ce cycle.

**Position détenue (contrôle 9, E-020) — 100 % cash, testée sur la même grille.** Espérance excédentaire du cash : +0.000 % de NAV. Référence 60/40 : +1.376 % (hors dérive : -0.176 %). **Écart du cash contre la référence : -1.376 % de NAV** sur 60 séances.

---

## 2. CE QUI A CHANGÉ — MÉCANISME, PAS CONTENU

Fait, étiqueté : les briefs 001 à 004 étaient rédigés par un agent. Celui-ci est produit par un moteur. Le paramètre libre de la Section Macro — la grille de scénarios — n'est plus accessible à l'agent : il est déclaré en tête de fichier, symétrique par construction, et son empreinte SHA-256 est vérifiée avant chaque usage. Sur le brief 004, ce paramètre avait porté le ratio annoncé de 1,29:1 à 3,0:1.

---

## 3. M1 · M2 · M3 · M4 — ÉTAT DES SÉRIES (FAIT)

Toutes les valeurs sont des FAITS lus dans le dépôt. Le retard est compté en séances ouvrées depuis la date d'arrêté unique. Les couples obligatoires sont vérifiés par le rendu : ce bloc ne peut pas être émis si un membre d'un couple manque.

| série | rôle déclaré | valeur | date | retard | n obs | profondeur | pct 1 an | pct 5 ans | pct complet |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| BAMLC0A0CM | risque_credit_ig | 0.84 | 2026-09-30 | 0 | 785 | 3.00 ans | 88.9 | REFUSÉ (insuffisante, -38 %) | 49.9 |
| BAMLH0A0HYM2 | risque_credit_hy | 3.12 | 2026-09-30 | 0 | 786 | 3.00 ans | 88.9 | REFUSÉ (insuffisante, -38 %) | 58.7 |
| CPIAUCSL | inflation_globale | 334.1 | 2026-08-01 | 60 | 118 | 9.83 ans | 100.0 | 100.0 | 100.0 |
| CPILFESL | inflation_sous_jacente | 337.8 | 2026-08-01 | 60 | 118 | 9.83 ans | 100.0 | 100.0 | 100.0 |
| DCOILBRENTEU | prix_energie | 114 | 2026-09-29 | 1 | 2533 | 9.98 ans | 86.1 | 93.2 | 96.6 |
| DCOILWTICO | prix_energie_wti | 96.16 | 2026-09-29 | 1 | 2497 | 9.98 ans | 79.4 | 87.4 | 93.6 |
| DEXJPUS | devise_usdjpy | 157.2 | 2026-09-25 | 3 | 2491 | 9.97 ans | 45.2 | 85.6 | 92.7 |
| DEXUSEU | devise_eurusd | 1.14 | 2026-09-25 | 3 | 2491 | 9.97 ans | 4.8 | 70.4 | 59.4 |
| DFF | politique_monetaire | 3.88 | 2026-09-30 | 0 | 3649 | 9.99 ans | 100.0 | 25.6 | 70.9 |
| DFII10 | taux_reel_10a | 2.93 | 2026-09-30 | 0 | 2497 | 9.99 ans | 100.0 | 100.0 | 100.0 |
| DGS10 | taux_nominal_10a | 5.29 | 2026-09-30 | 0 | 2497 | 9.99 ans | 100.0 | 100.0 | 100.0 |
| DGS2 | taux_nominal_2a | 4.88 | 2026-09-30 | 0 | 2497 | 9.99 ans | 99.2 | 92.1 | 96.0 |
| DGS30 | taux_nominal_30a | 5.64 | 2026-09-30 | 0 | 2497 | 9.99 ans | 100.0 | 100.0 | 100.0 |
| DTWEXBGS | dollar_large | 120.3 | 2026-09-25 | 3 | 2489 | 9.97 ans | 67.1 | 43.5 | 69.0 |
| INDPRO | activite_industrielle | 103.1 | 2026-08-01 | 60 | 119 | 9.83 ans | 100.0 | 100.0 | 92.4 |
| NASDAQ100 | prix_actions_tech | 3.041e+04 | 2026-09-30 | 0 | 2512 | 9.99 ans | 96.4 | 99.3 | 99.6 |
| OVXCLS | volatilite_implicite_petrole | 52.24 | 2026-09-30 | 0 | 2513 | 9.99 ans | 52.0 | 83.1 | 86.8 |
| PAYEMS | emploi | 1.591e+05 | 2026-08-01 | 60 | 119 | 9.83 ans | 100.0 | 100.0 | 100.0 |
| SP500 | prix_actions | 7652 | 2026-09-30 | 0 | 2511 | 9.99 ans | 87.7 | 97.5 | 98.8 |
| T10Y2Y | pente_courbe | 0.41 | 2026-09-30 | 0 | 2497 | 9.99 ans | 23.0 | 66.3 | 51.4 |
| T10YIE | point_mort_10a | 2.36 | 2026-09-30 | 0 | 2497 | 9.99 ans | 81.7 | 64.6 | 80.1 |
| T5YIFR | point_mort_5a5a | 2.36 | 2026-09-30 | 0 | 2497 | 9.99 ans | 100.0 | 85.3 | 92.5 |
| UNRATE | chomage | 4.1 | 2026-08-01 | 60 | 118 | 9.83 ans | 16.7 | 65.0 | 55.9 |
| VIXCLS | volatilite_implicite | 16.34 | 2026-09-30 | 0 | 2544 | 9.99 ans | 32.5 | 35.6 | 44.9 |
| VXDCLS | volatilite_implicite_dow | 16.06 | 2026-09-30 | 0 | 2514 | 9.99 ans | 56.0 | 49.2 | 51.5 |
| VXVCLS | volatilite_implicite_3m | 18.37 | 2026-09-30 | 0 | 2511 | 9.99 ans | 11.9 | 28.7 | 42.3 |

**Couples obligatoires contrôlés :** CPIAUCSL/CPILFESL, DGS10/DFII10, DGS10/T10YIE, BAMLH0A0HYM2/BAMLC0A0CM, UNRATE/PAYEMS, VIXCLS/SP500 — 0 manquement(s).

**Inflation en trois chiffres (contrôle 2, E-005).** Global +3.71 % sur un an (CPIAUCSL, 2026-08-01) · sous-jacent +2.76 % (CPILFESL) · **écart hors sous-jacent +95 pb**. Contribution énergie NON publiée : `CPIENGSL` est absente du dépôt. Lacune nommée avec le code FRED qui la comble (R-028) ; elle n'est pas présentée comme une limite de méthode. L'écart ci-dessus est l'écart global/sous-jacent, pas la contribution énergie.

---

## 4. IDENTITÉS COMPTABLES ET REDONDANCES (vérifiées numériquement)

| identité | vérifiable | n dates | résidu absolu max | tolérance | vérifiée |
|---|:---:|---:|---:|---:|:---:|
| T10YIE = DGS10 - DFII10 | oui | 2497 | 0.0000 | 0.02 | OUI |
| T10Y2Y = DGS10 - DGS2 | oui | 2497 | 0.0000 | 0.02 | OUI |

**Redondances détectées (11) — deux séries liées ne comptent jamais pour deux confirmations indépendantes :**

- identité comptable : T10YIE = DGS10 - DFII10 — T10YIE, DGS10, DFII10 (résidu max 0.0000)
- identité comptable : T10Y2Y = DGS10 - DGS2 — T10Y2Y, DGS10, DGS2 (résidu max 0.0000)
- corrélation des variations à 60 séances : BAMLC0A0CM / BAMLH0A0HYM2 = +0.941 sur 725 points (seuil 0.9)
- corrélation des variations à 60 séances : DGS10 / DGS30 = +0.967 sur 2437 points (seuil 0.9)
- corrélation des variations à 60 séances : INDPRO / PAYEMS = +0.913 sur 116 points (seuil 0.9)
- corrélation des variations à 60 séances : INDPRO / UNRATE = -0.918 sur 115 points (seuil 0.9)
- corrélation des variations à 60 séances : NASDAQ100 / SP500 = +0.903 sur 2451 points (seuil 0.9)
- corrélation des variations à 60 séances : PAYEMS / UNRATE = -0.983 sur 115 points (seuil 0.9)
- corrélation des variations à 60 séances : VIXCLS / VXDCLS = +0.930 sur 2451 points (seuil 0.9)
- corrélation des variations à 60 séances : VIXCLS / VXVCLS = +0.958 sur 2451 points (seuil 0.9)
- corrélation des variations à 60 séances : VXDCLS / VXVCLS = +0.934 sur 2451 points (seuil 0.9)

---

## 5. GRILLE, σ MESURÉ, ET DOUBLE CONFRONTATION DES PROBABILITÉS

σ est **mesuré** sur chaque série, jamais choisi. Les probabilités sont les **fréquences historiques** dans chaque bande, jamais un jugement. L'effectif de chaque bande est publié ; sous 20 observations la bande est déclarée NON ESTIMABLE. La colonne « emp./gauss. » est la double confrontation exigée par §11.5 : tout écart supérieur à un facteur 2 est déclaré (⚠).

**BAMLH0A0HYM2** (niveau) — σ à 60 pas = **0.45511** · estimateurs croisés : racine-h 0.53926, blocs disjoints 0.31394 (écart relatif 71.8 %) · dérive d'échantillon -0.10700 (-0.24 σ) · 726 variations chevauchantes, 12 blocs indépendants · 2023-10-02 → 2026-09-30

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.6827 | 55 | 1 | 0.0758 | 0.0668 | 1.13 | oui |
| -1.0 | -0.6827 | -0.3413 | 118 | 2 | 0.1625 | 0.1598 | 1.02 | oui |
| -0.5 | -0.3413 | -0.1138 | 194 | 3 | 0.2672 | 0.1747 | 1.53 | oui |
| +0.0 | -0.1138 | +0.1138 | 195 | 3 | 0.2686 | 0.1974 | 1.36 | oui |
| +0.5 | +0.1138 | +0.3413 | 82 | 1 | 0.1129 | 0.1747 | 0.65 | oui |
| +1.0 | +0.3413 | +0.6827 | 53 | 1 | 0.0730 | 0.1598 | 0.46 ⚠ | oui |
| +2.0 | +0.6827 | +∞ | 29 | 0 | 0.0399 | 0.0668 | 0.60 | oui |

**DCOILBRENTEU** (log) — σ à 60 pas = **0.24724** · estimateurs croisés : racine-h 0.24794, blocs disjoints 0.29941 (écart relatif 21.1 %) · dérive d'échantillon +0.01665 (+0.07 σ) · 2473 variations chevauchantes, 41 blocs indépendants · 2016-10-04 → 2026-09-29

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.3709 | 84 | 1 | 0.0340 | 0.0668 | 0.51 | oui |
| -1.0 | -0.3709 | -0.1854 | 155 | 3 | 0.0627 | 0.1598 | 0.39 ⚠ | oui |
| -0.5 | -0.1854 | -0.0618 | 500 | 8 | 0.2022 | 0.1747 | 1.16 | oui |
| +0.0 | -0.0618 | +0.0618 | 768 | 13 | 0.3106 | 0.1974 | 1.57 | oui |
| +0.5 | +0.0618 | +0.1854 | 612 | 10 | 0.2475 | 0.1747 | 1.42 | oui |
| +1.0 | +0.1854 | +0.3709 | 219 | 4 | 0.0886 | 0.1598 | 0.55 | oui |
| +2.0 | +0.3709 | +∞ | 135 | 2 | 0.0546 | 0.0668 | 0.82 | oui |

**DCOILWTICO** — non scénarisable : convention log inapplicable : 1 observation(s) non strictement positive(s), minimum -36.98 le 2020-04-20. Le prix a été négatif : aucun log-rendement n'existe. La série est déclarée NON SCÉNARISABLE plutôt que corrigée en silence.

**DEXJPUS** (log) — σ à 60 pas = **0.04223** · estimateurs croisés : racine-h 0.04390, blocs disjoints 0.05085 (écart relatif 20.4 %) · dérive d'échantillon +0.00923 (+0.22 σ) · 2431 variations chevauchantes, 41 blocs indépendants · 2016-10-04 → 2026-09-25

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0633 | 103 | 2 | 0.0424 | 0.0668 | 0.63 | oui |
| -1.0 | -0.0633 | -0.0317 | 240 | 4 | 0.0987 | 0.1598 | 0.62 | oui |
| -0.5 | -0.0317 | -0.0106 | 381 | 6 | 0.1567 | 0.1747 | 0.90 | oui |
| +0.0 | -0.0106 | +0.0106 | 496 | 8 | 0.2040 | 0.1974 | 1.03 | oui |
| +0.5 | +0.0106 | +0.0317 | 540 | 9 | 0.2221 | 0.1747 | 1.27 | oui |
| +1.0 | +0.0317 | +0.0633 | 479 | 8 | 0.1970 | 0.1598 | 1.23 | oui |
| +2.0 | +0.0633 | +∞ | 192 | 3 | 0.0790 | 0.0668 | 1.18 | oui |

**DEXUSEU** (log) — σ à 60 pas = **0.03439** · estimateurs croisés : racine-h 0.03466, blocs disjoints 0.03708 (écart relatif 7.8 %) · dérive d'échantillon +0.00165 (+0.05 σ) · 2431 variations chevauchantes, 41 blocs indépendants · 2016-10-04 → 2026-09-25

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0516 | 133 | 2 | 0.0547 | 0.0668 | 0.82 | oui |
| -1.0 | -0.0516 | -0.0258 | 324 | 5 | 0.1333 | 0.1598 | 0.83 | oui |
| -0.5 | -0.0258 | -0.0086 | 505 | 8 | 0.2077 | 0.1747 | 1.19 | oui |
| +0.0 | -0.0086 | +0.0086 | 615 | 10 | 0.2530 | 0.1974 | 1.28 | oui |
| +0.5 | +0.0086 | +0.0258 | 324 | 5 | 0.1333 | 0.1747 | 0.76 | oui |
| +1.0 | +0.0258 | +0.0516 | 304 | 5 | 0.1251 | 0.1598 | 0.78 | oui |
| +2.0 | +0.0516 | +∞ | 226 | 4 | 0.0930 | 0.0668 | 1.39 | oui |

**DGS10** (niveau) — σ à 60 pas = **0.42313** · estimateurs croisés : racine-h 0.41440, blocs disjoints 0.39939 (écart relatif 5.9 %) · dérive d'échantillon +0.06463 (+0.15 σ) · 2437 variations chevauchantes, 41 blocs indépendants · 2016-10-04 → 2026-09-30

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.6347 | 123 | 2 | 0.0505 | 0.0668 | 0.76 | oui |
| -1.0 | -0.6347 | -0.3173 | 284 | 5 | 0.1165 | 0.1598 | 0.73 | oui |
| -0.5 | -0.3173 | -0.1058 | 371 | 6 | 0.1522 | 0.1747 | 0.87 | oui |
| +0.0 | -0.1058 | +0.1058 | 528 | 9 | 0.2167 | 0.1974 | 1.10 | oui |
| +0.5 | +0.1058 | +0.3173 | 555 | 9 | 0.2277 | 0.1747 | 1.30 | oui |
| +1.0 | +0.3173 | +0.6347 | 369 | 6 | 0.1514 | 0.1598 | 0.95 | oui |
| +2.0 | +0.6347 | +∞ | 207 | 3 | 0.0849 | 0.0668 | 1.27 | oui |

**DGS2** (niveau) — σ à 60 pas = **0.49569** · estimateurs croisés : racine-h 0.42144, blocs disjoints 0.48739 (écart relatif 17.6 %) · dérive d'échantillon +0.08277 (+0.17 σ) · 2437 variations chevauchantes, 41 blocs indépendants · 2016-10-04 → 2026-09-30

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.7435 | 115 | 2 | 0.0472 | 0.0668 | 0.71 | oui |
| -1.0 | -0.7435 | -0.3718 | 228 | 4 | 0.0936 | 0.1598 | 0.59 | oui |
| -0.5 | -0.3718 | -0.1239 | 323 | 5 | 0.1325 | 0.1747 | 0.76 | oui |
| +0.0 | -0.1239 | +0.1239 | 739 | 12 | 0.3032 | 0.1974 | 1.54 | oui |
| +0.5 | +0.1239 | +0.3718 | 483 | 8 | 0.1982 | 0.1747 | 1.13 | oui |
| +1.0 | +0.3718 | +0.7435 | 348 | 6 | 0.1428 | 0.1598 | 0.89 | oui |
| +2.0 | +0.7435 | +∞ | 201 | 3 | 0.0825 | 0.0668 | 1.23 | oui |

**DGS30** (niveau) — σ à 60 pas = **0.36499** · estimateurs croisés : racine-h 0.39244, blocs disjoints 0.34384 (écart relatif 14.1 %) · dérive d'échantillon +0.05921 (+0.16 σ) · 2437 variations chevauchantes, 41 blocs indépendants · 2016-10-04 → 2026-09-30

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.5475 | 128 | 2 | 0.0525 | 0.0668 | 0.79 | oui |
| -1.0 | -0.5475 | -0.2737 | 276 | 5 | 0.1133 | 0.1598 | 0.71 | oui |
| -0.5 | -0.2737 | -0.0912 | 338 | 6 | 0.1387 | 0.1747 | 0.79 | oui |
| +0.0 | -0.0912 | +0.0912 | 629 | 10 | 0.2581 | 0.1974 | 1.31 | oui |
| +0.5 | +0.0912 | +0.2737 | 461 | 8 | 0.1892 | 0.1747 | 1.08 | oui |
| +1.0 | +0.2737 | +0.5475 | 396 | 7 | 0.1625 | 0.1598 | 1.02 | oui |
| +2.0 | +0.5475 | +∞ | 209 | 3 | 0.0858 | 0.0668 | 1.28 | oui |

**DTWEXBGS** (log) — σ à 60 pas = **0.02592** · estimateurs croisés : racine-h 0.02405, blocs disjoints 0.02779 (écart relatif 15.5 %) · dérive d'échantillon +0.00075 (+0.03 σ) · 2429 variations chevauchantes, 40 blocs indépendants · 2016-10-04 → 2026-09-25

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0389 | 159 | 3 | 0.0655 | 0.0668 | 0.98 | oui |
| -1.0 | -0.0389 | -0.0194 | 388 | 6 | 0.1597 | 0.1598 | 1.00 | oui |
| -0.5 | -0.0194 | -0.0065 | 360 | 6 | 0.1482 | 0.1747 | 0.85 | oui |
| +0.0 | -0.0065 | +0.0065 | 543 | 9 | 0.2235 | 0.1974 | 1.13 | oui |
| +0.5 | +0.0065 | +0.0194 | 462 | 8 | 0.1902 | 0.1747 | 1.09 | oui |
| +1.0 | +0.0194 | +0.0389 | 307 | 5 | 0.1264 | 0.1598 | 0.79 | oui |
| +2.0 | +0.0389 | +∞ | 210 | 4 | 0.0865 | 0.0668 | 1.29 | oui |

**NASDAQ100** (log) — σ à 60 pas = **0.08868** · estimateurs croisés : racine-h 0.11132, blocs disjoints 0.08347 (écart relatif 33.4 %) · dérive d'échantillon +0.04411 (+0.50 σ) · 2452 variations chevauchantes, 41 blocs indépendants · 2016-10-04 → 2026-09-30

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.1330 | 109 | 2 | 0.0445 | 0.0668 | 0.67 | oui |
| -1.0 | -0.1330 | -0.0665 | 166 | 3 | 0.0677 | 0.1598 | 0.42 ⚠ | oui |
| -0.5 | -0.0665 | -0.0222 | 186 | 3 | 0.0759 | 0.1747 | 0.43 ⚠ | oui |
| +0.0 | -0.0222 | +0.0222 | 358 | 6 | 0.1460 | 0.1974 | 0.74 | oui |
| +0.5 | +0.0222 | +0.0665 | 586 | 10 | 0.2390 | 0.1747 | 1.37 | oui |
| +1.0 | +0.0665 | +0.1330 | 731 | 12 | 0.2981 | 0.1598 | 1.87 | oui |
| +2.0 | +0.1330 | +∞ | 316 | 5 | 0.1289 | 0.0668 | 1.93 | oui |

**SP500** (log) — σ à 60 pas = **0.06914** · estimateurs croisés : racine-h 0.08843, blocs disjoints 0.06441 (écart relatif 37.3 %) · dérive d'échantillon +0.03062 (+0.44 σ) · 2451 variations chevauchantes, 41 blocs indépendants · 2016-10-04 → 2026-09-30

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.1037 | 115 | 2 | 0.0469 | 0.0668 | 0.70 | oui |
| -1.0 | -0.1037 | -0.0519 | 158 | 3 | 0.0645 | 0.1598 | 0.40 ⚠ | oui |
| -0.5 | -0.0519 | -0.0173 | 176 | 3 | 0.0718 | 0.1747 | 0.41 ⚠ | oui |
| +0.0 | -0.0173 | +0.0173 | 293 | 5 | 0.1195 | 0.1974 | 0.61 | oui |
| +0.5 | +0.0173 | +0.0519 | 745 | 12 | 0.3040 | 0.1747 | 1.74 | oui |
| +1.0 | +0.0519 | +0.1037 | 754 | 13 | 0.3076 | 0.1598 | 1.92 | oui |
| +2.0 | +0.1037 | +∞ | 210 | 4 | 0.0857 | 0.0668 | 1.28 | oui |

**VIXCLS** (log) — σ à 60 pas = **0.34672** · estimateurs croisés : racine-h 0.61225, blocs disjoints 0.34610 (écart relatif 76.9 %) · dérive d'échantillon +0.00332 (+0.01 σ) · 2484 variations chevauchantes, 41 blocs indépendants · 2016-10-04 → 2026-09-30

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.5201 | 77 | 1 | 0.0310 | 0.0668 | 0.46 ⚠ | oui |
| -1.0 | -0.5201 | -0.2600 | 388 | 6 | 0.1562 | 0.1598 | 0.98 | oui |
| -0.5 | -0.2600 | -0.0867 | 604 | 10 | 0.2432 | 0.1747 | 1.39 | oui |
| +0.0 | -0.0867 | +0.0867 | 616 | 10 | 0.2480 | 0.1974 | 1.26 | oui |
| +0.5 | +0.0867 | +0.2600 | 373 | 6 | 0.1502 | 0.1747 | 0.86 | oui |
| +1.0 | +0.2600 | +0.5201 | 248 | 4 | 0.0998 | 0.1598 | 0.62 | oui |
| +2.0 | +0.5201 | +∞ | 178 | 3 | 0.0717 | 0.0668 | 1.07 | oui |

---

## 6. TEST D'ASYMÉTRIE — DÉFINITION UNIQUE (R-030), L'ESPÉRANCE DÉCIDE

> Test d'admission : **espérance calculée sur la grille symétrique complète, les deux queues incluses**. Le rapport gain maximal / perte maximale est publié **pour information** et ne peut fonder aucune admission seul (T-001, faute E-018). Le rapport gain maximal / perte du scénario central est **interdit**. Une seule formulation, appliquée à tous les candidats, position détenue comprise.

| candidat | verdict | espérance % NAV | sans dérive | 1re moitié | 2e moitié | gain max | perte max | ratio (info) | critères échoués |
|---|:---:|---:|---:|---:|---:|---:|---:|---:|---|
| M005-DCOILBRENTEU-HAUSSE-ALIGNE | REFUSEE | +0.261 | +0.127 | +0.255 | +0.144 | +5.04 | -3.19 | 1.58:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DCOILBRENTEU-HAUSSE-CONTRARIEN | REFUSEE | +0.261 | +0.127 | +0.255 | +0.144 | +5.04 | -3.19 | 1.58:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DCOILBRENTEU-BAISSE-ALIGNE | REFUSEE | -0.261 | -0.127 | -0.255 | -0.144 | +3.19 | -5.04 | 0.63:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILBRENTEU-BAISSE-CONTRARIEN | REFUSEE | -0.261 | -0.127 | -0.255 | -0.144 | +3.19 | -5.04 | 0.63:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-HAUSSE-ALIGNE | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-HAUSSE-CONTRARIEN | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-BAISSE-ALIGNE | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-BAISSE-CONTRARIEN | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-HAUSSE-ALIGNE | REFUSEE | +0.001 | -0.067 | -0.073 | +0.044 | +0.63 | -0.72 | 0.87:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-HAUSSE-CONTRARIEN | REFUSEE | +0.001 | -0.067 | -0.073 | +0.044 | +0.63 | -0.72 | 0.87:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-BAISSE-ALIGNE | REFUSEE | -0.001 | +0.067 | +0.073 | -0.044 | +0.72 | -0.63 | 1.14:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-BAISSE-CONTRARIEN | REFUSEE | -0.001 | +0.067 | +0.073 | -0.044 | +0.72 | -0.63 | 1.14:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-HAUSSE-ALIGNE | REFUSEE | -0.061 | -0.075 | -0.033 | -0.072 | +0.50 | -0.61 | 0.82:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-HAUSSE-CONTRARIEN | REFUSEE | -0.061 | -0.075 | -0.033 | -0.072 | +0.50 | -0.61 | 0.82:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-BAISSE-ALIGNE | REFUSEE | +0.061 | +0.075 | +0.033 | +0.072 | +0.61 | -0.50 | 1.22:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DEXUSEU-BAISSE-CONTRARIEN | REFUSEE | +0.061 | +0.075 | +0.033 | +0.072 | +0.61 | -0.50 | 1.22:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DGS10-HAUSSE-ALIGNE | REFUSEE | +0.005 | -0.030 | -0.051 | +0.053 | +0.47 | -0.57 | 0.83:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-HAUSSE-CONTRARIEN | REFUSEE | +0.005 | -0.030 | -0.051 | +0.053 | +0.47 | -0.57 | 0.83:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-BAISSE-ALIGNE | REFUSEE | -0.005 | +0.030 | +0.051 | -0.053 | +0.57 | -0.47 | 1.20:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-BAISSE-CONTRARIEN | REFUSEE | -0.005 | +0.030 | +0.051 | -0.053 | +0.57 | -0.47 | 1.20:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-HAUSSE-ALIGNE | REFUSEE | -0.008 | -0.019 | -0.024 | +0.003 | +0.13 | -0.17 | 0.76:1 | 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-HAUSSE-CONTRARIEN | REFUSEE | -0.008 | -0.019 | -0.024 | +0.003 | +0.13 | -0.17 | 0.76:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-BAISSE-ALIGNE | REFUSEE | +0.008 | +0.019 | +0.024 | -0.003 | +0.17 | -0.13 | 1.32:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-BAISSE-CONTRARIEN | REFUSEE | +0.008 | +0.019 | +0.024 | -0.003 | +0.17 | -0.13 | 1.32:1 | 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-HAUSSE-ALIGNE | REFUSEE | +0.011 | -0.045 | -0.097 | +0.117 | +0.74 | -0.95 | 0.79:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-HAUSSE-CONTRARIEN | REFUSEE | +0.011 | -0.045 | -0.097 | +0.117 | +0.74 | -0.95 | 0.79:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-BAISSE-ALIGNE | REFUSEE | -0.011 | +0.045 | +0.097 | -0.117 | +0.95 | -0.74 | 1.27:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-BAISSE-CONTRARIEN | REFUSEE | -0.011 | +0.045 | +0.097 | -0.117 | +0.95 | -0.74 | 1.27:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-HAUSSE-ALIGNE | REFUSEE | -0.065 | -0.072 | -0.082 | -0.053 | +0.35 | -0.48 | 0.74:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-HAUSSE-CONTRARIEN | REFUSEE | -0.065 | -0.072 | -0.082 | -0.053 | +0.35 | -0.48 | 0.74:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-BAISSE-ALIGNE | REFUSEE | +0.065 | +0.072 | +0.082 | +0.053 | +0.48 | -0.35 | 1.36:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DTWEXBGS-BAISSE-CONTRARIEN | REFUSEE | +0.065 | +0.072 | +0.082 | +0.053 | +0.48 | -0.35 | 1.36:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-HAUSSE-ALIGNE | REFUSEE | +0.304 | -0.035 | +0.453 | +0.183 | +1.48 | -1.37 | 1.08:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-HAUSSE-CONTRARIEN | REFUSEE | +0.304 | -0.035 | +0.453 | +0.183 | +1.48 | -1.37 | 1.08:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-BAISSE-ALIGNE | REFUSEE | -0.304 | +0.035 | -0.453 | -0.183 | +1.37 | -1.48 | 0.93:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-NASDAQ100-BAISSE-CONTRARIEN | REFUSEE | -0.304 | +0.035 | -0.453 | -0.183 | +1.37 | -1.48 | 0.93:1 | 12_esperance_positive, 13_esperance_non_portee_par_derive, 14_esperance_stable_dans_le_temps |
| M005-SP500-HAUSSE-ALIGNE | REFUSEE | +0.187 | -0.043 | +0.218 | +0.155 | +1.11 | -1.11 | 1.00:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-SP500-HAUSSE-CONTRARIEN | REFUSEE | +0.187 | -0.043 | +0.218 | +0.155 | +1.11 | -1.11 | 1.00:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-SP500-BAISSE-ALIGNE | REFUSEE | -0.187 | +0.043 | -0.218 | -0.155 | +1.11 | -1.11 | 1.00:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-SP500-BAISSE-CONTRARIEN | REFUSEE | -0.187 | +0.043 | -0.218 | -0.155 | +1.11 | -1.11 | 1.00:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |

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
| 8_confirmations_independantes | 32 |
| 9_test_execute_et_vrai | 32 |
| 10_invalidation_fait_date | 12 |
| 11_invalidation_non_deja_survenue | 22 |
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

- `BAMLC0A0CM` : percentile REFUSÉ sur 5 ans — profondeur réelle 785 obs / 3.00 ans (début 2023-10-02). R-011 : un percentile calculé sur une série tronquée est sans valeur.
- `BAMLH0A0HYM2` : percentile REFUSÉ sur 5 ans — profondeur réelle 786 obs / 3.00 ans (début 2023-10-02). R-011 : un percentile calculé sur une série tronquée est sans valeur.
- `BAMLH0A0HYM2` : instrument NON ADMISSIBLE — P&L non calculable depuis le dépôt : l'OAS est un spread, et le dépôt ne contient pas le rendement de l'indice, donc pas la duration de spread. Aucune valeur ne peut être produite sans un chiffre extérieur aux données (E-002).
- `BAMLC0A0CM` : instrument NON ADMISSIBLE — P&L non calculable depuis le dépôt : l'OAS est un spread, et le dépôt ne contient pas le rendement de l'indice, donc pas la duration de spread. Aucune valeur ne peut être produite sans un chiffre extérieur aux données (E-002).
- Retards sur la date d'arrêté unique (E-014) : DCOILBRENTEU 1 séance(s), DCOILWTICO 1 séance(s), DEXJPUS 3 séance(s), DEXUSEU 3 séance(s), DTWEXBGS 3 séance(s)

**Vérification tierce (R-032) : NON SATISFAITE pour ce brief.** Le moteur ne dispose d'aucune source extérieure au dépôt. Trois estimateurs **internes** de σ sont publiés côte à côte au §5 ; ce sont des contrôles de cohérence interne, **pas** une vérification tierce, et ils ne sont pas présentés comme telle.

**Ce que ce moteur ne peut pas faire.** Il ne prouve aucune capacité prédictive : la règle de confirmation est une règle de percentile, déclarée et symétrique, pas un modèle validé hors échantillon. Il ne corrige pas la multiplicité : 40 candidats sont évalués et aucune pénalité de sélection n'est appliquée à l'espérance — c'est une limite déclarée, pas un oubli. Il ne voit ni les événements politiques, ni les décisions de banques centrales : le dépôt ne contient que des séries FRED, et toute affirmation de politique monétaire non adossée à `DFF` est refusée (critère 15, faute E-006).

---

*Fin du brief 005. Produit mécaniquement. Ne constitue pas un conseil en investissement.*