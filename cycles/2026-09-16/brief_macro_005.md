# BRIEF MACRO n° 005 — arrêté au 2026-09-15

*Produit par `apollon_macro.py` le 2026-09-16T22:21:33+00:00. Aucune valeur de ce document n'est saisie à la main : chacune porte sa série, sa date et sa profondeur. Bloc à copier tel quel.*

**Grille de scénarios (R-029, §11), déclarée avant toute lecture de données et empreintée :** `[-2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0]` · empreinte SHA-256 `6aaeb3863c875923…` · symétrique : True · horizon 60 séances (3 mois pour les séries mensuelles).

---

## 1. CONCLUSION, ÉNONCÉE D'ABORD

**40 candidats déclarés d'avance (10 instruments × 2 directions × 2 règles de confirmation). 40 évalués. 0 thèse(s) survivent aux quinze critères.**

**Abstention. Aucune thèse ne survit.** Ce n'est pas un silence : c'est un résultat, produit par le même portier que celui qui aurait admis une thèse. Le détail des échecs, critère par critère, figure au §6. La Section Macro ne transmet rien à la Section Risque ce cycle.

**Position détenue (contrôle 9, E-020) — 100 % cash, testée sur la même grille.** Espérance excédentaire du cash : +0.000 % de NAV. Référence 60/40 : +1.404 % (hors dérive : -0.143 %). **Écart du cash contre la référence : -1.404 % de NAV** sur 60 séances.

---

## 2. CE QUI A CHANGÉ — MÉCANISME, PAS CONTENU

Fait, étiqueté : les briefs 001 à 004 étaient rédigés par un agent. Celui-ci est produit par un moteur. Le paramètre libre de la Section Macro — la grille de scénarios — n'est plus accessible à l'agent : il est déclaré en tête de fichier, symétrique par construction, et son empreinte SHA-256 est vérifiée avant chaque usage. Sur le brief 004, ce paramètre avait porté le ratio annoncé de 1,29:1 à 3,0:1.

---

## 3. M1 · M2 · M3 · M4 — ÉTAT DES SÉRIES (FAIT)

Toutes les valeurs sont des FAITS lus dans le dépôt. Le retard est compté en séances ouvrées depuis la date d'arrêté unique. Les couples obligatoires sont vérifiés par le rendu : ce bloc ne peut pas être émis si un membre d'un couple manque.

| série | rôle déclaré | valeur | date | retard | n obs | profondeur | pct 1 an | pct 5 ans | pct complet |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| BAMLC0A0CM | risque_credit_ig | 0.8 | 2026-09-15 | 0 | 785 | 2.99 ans | 64.3 | REFUSÉ (insuffisante, -38 %) | 30.3 |
| BAMLH0A0HYM2 | risque_credit_hy | 2.76 | 2026-09-15 | 0 | 786 | 2.99 ans | 35.3 | REFUSÉ (insuffisante, -38 %) | 20.2 |
| CPIAUCSL | inflation_globale | 334.1 | 2026-08-01 | 45 | 119 | 9.91 ans | 100.0 | 100.0 | 100.0 |
| CPILFESL | inflation_sous_jacente | 337.8 | 2026-08-01 | 45 | 119 | 9.91 ans | 100.0 | 100.0 | 100.0 |
| DCOILBRENTEU | prix_energie | 130.8 | 2026-09-15 | 0 | 2534 | 9.99 ans | 99.6 | 99.8 | 99.9 |
| DCOILWTICO | prix_energie_wti | 107 | 2026-09-15 | 0 | 2498 | 9.99 ans | 96.4 | 95.3 | 97.6 |
| DEXJPUS | devise_usdjpy | 153.7 | 2026-09-11 | 2 | 2492 | 9.98 ans | 18.7 | 74.4 | 87.0 |
| DEXUSEU | devise_eurusd | 1.16 | 2026-09-11 | 2 | 2492 | 9.98 ans | 39.7 | 81.7 | 69.0 |
| DFF | politique_monetaire | 3.63 | 2026-09-15 | 0 | 3650 | 9.99 ans | 52.4 | 10.5 | 64.9 |
| DFII10 | taux_reel_10a | 2.62 | 2026-09-15 | 0 | 2497 | 9.99 ans | 100.0 | 100.0 | 100.0 |
| DGS10 | taux_nominal_10a | 5 | 2026-09-15 | 0 | 2497 | 9.99 ans | 100.0 | 100.0 | 100.0 |
| DGS2 | taux_nominal_2a | 4.67 | 2026-09-15 | 0 | 2497 | 9.99 ans | 100.0 | 84.3 | 92.1 |
| DGS30 | taux_nominal_30a | 5.36 | 2026-09-15 | 0 | 2497 | 9.99 ans | 99.6 | 99.9 | 100.0 |
| DTWEXBGS | dollar_large | 118.2 | 2026-09-11 | 2 | 2490 | 9.98 ans | 12.3 | 16.7 | 53.3 |
| INDPRO | activite_industrielle | 103 | 2026-07-01 | 76 | 119 | 9.83 ans | 100.0 | 100.0 | 92.4 |
| NASDAQ100 | prix_actions_tech | 2.894e+04 | 2026-09-15 | 0 | 2512 | 9.99 ans | 69.8 | 94.0 | 97.0 |
| OVXCLS | volatilite_implicite_petrole | 61.73 | 2026-09-15 | 0 | 2513 | 9.99 ans | 72.6 | 92.5 | 93.0 |
| PAYEMS | emploi | 1.591e+05 | 2026-08-01 | 45 | 120 | 9.91 ans | 100.0 | 100.0 | 100.0 |
| SP500 | prix_actions | 7586 | 2026-09-15 | 0 | 2511 | 9.99 ans | 87.3 | 97.5 | 98.7 |
| T10Y2Y | pente_courbe | 0.33 | 2026-09-15 | 0 | 2497 | 9.99 ans | 4.8 | 59.9 | 47.1 |
| T10YIE | point_mort_10a | 2.38 | 2026-09-15 | 0 | 2497 | 9.99 ans | 87.3 | 70.9 | 83.8 |
| T5YIFR | point_mort_5a5a | 2.35 | 2026-09-15 | 0 | 2497 | 9.99 ans | 100.0 | 83.8 | 91.6 |
| UNRATE | chomage | 4.1 | 2026-08-01 | 45 | 119 | 9.91 ans | 16.7 | 65.0 | 55.5 |
| VIXCLS | volatilite_implicite | 17.2 | 2026-09-15 | 0 | 2544 | 9.99 ans | 49.6 | 45.6 | 52.2 |
| VXDCLS | volatilite_implicite_dow | 15.95 | 2026-09-15 | 0 | 2514 | 9.99 ans | 54.0 | 47.5 | 50.8 |
| VXVCLS | volatilite_implicite_3m | 19.36 | 2026-09-15 | 0 | 2511 | 9.99 ans | 35.3 | 39.0 | 49.7 |

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
- corrélation des variations à 60 séances : BAMLC0A0CM / BAMLH0A0HYM2 = +0.940 sur 725 points (seuil 0.9)
- corrélation des variations à 60 séances : DGS10 / DGS30 = +0.967 sur 2437 points (seuil 0.9)
- corrélation des variations à 60 séances : INDPRO / PAYEMS = +0.914 sur 116 points (seuil 0.9)
- corrélation des variations à 60 séances : INDPRO / UNRATE = -0.918 sur 115 points (seuil 0.9)
- corrélation des variations à 60 séances : NASDAQ100 / SP500 = +0.902 sur 2451 points (seuil 0.9)
- corrélation des variations à 60 séances : PAYEMS / UNRATE = -0.983 sur 116 points (seuil 0.9)
- corrélation des variations à 60 séances : VIXCLS / VXDCLS = +0.930 sur 2451 points (seuil 0.9)
- corrélation des variations à 60 séances : VIXCLS / VXVCLS = +0.958 sur 2451 points (seuil 0.9)
- corrélation des variations à 60 séances : VXDCLS / VXVCLS = +0.934 sur 2451 points (seuil 0.9)

---

## 5. GRILLE, σ MESURÉ, ET DOUBLE CONFRONTATION DES PROBABILITÉS

σ est **mesuré** sur chaque série, jamais choisi. Les probabilités sont les **fréquences historiques** dans chaque bande, jamais un jugement. L'effectif de chaque bande est publié ; sous 20 observations la bande est déclarée NON ESTIMABLE. La colonne « emp./gauss. » est la double confrontation exigée par §11.5 : tout écart supérieur à un facteur 2 est déclaré (⚠).

**BAMLH0A0HYM2** (niveau) — σ à 60 pas = **0.45607** · estimateurs croisés : racine-h 0.53899, blocs disjoints 0.46493 (écart relatif 18.2 %) · dérive d'échantillon -0.11390 (-0.25 σ) · 726 variations chevauchantes, 12 blocs indépendants · 2023-09-18 → 2026-09-15

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.6841 | 55 | 1 | 0.0758 | 0.0668 | 1.13 | oui |
| -1.0 | -0.6841 | -0.3421 | 125 | 2 | 0.1722 | 0.1598 | 1.08 | oui |
| -0.5 | -0.3421 | -0.1140 | 192 | 3 | 0.2645 | 0.1747 | 1.51 | oui |
| +0.0 | -0.1140 | +0.1140 | 194 | 3 | 0.2672 | 0.1974 | 1.35 | oui |
| +0.5 | +0.1140 | +0.3421 | 80 | 1 | 0.1102 | 0.1747 | 0.63 | oui |
| +1.0 | +0.3421 | +0.6841 | 51 | 1 | 0.0702 | 0.1598 | 0.44 ⚠ | oui |
| +2.0 | +0.6841 | +∞ | 29 | 0 | 0.0399 | 0.0668 | 0.60 | oui |

**DCOILBRENTEU** (log) — σ à 60 pas = **0.24528** · estimateurs croisés : racine-h 0.24767, blocs disjoints 0.27340 (écart relatif 11.5 %) · dérive d'échantillon +0.01518 (+0.06 σ) · 2474 variations chevauchantes, 41 blocs indépendants · 2016-09-19 → 2026-09-15

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.3679 | 84 | 1 | 0.0340 | 0.0668 | 0.51 | oui |
| -1.0 | -0.3679 | -0.1840 | 156 | 3 | 0.0631 | 0.1598 | 0.39 ⚠ | oui |
| -0.5 | -0.1840 | -0.0613 | 502 | 8 | 0.2029 | 0.1747 | 1.16 | oui |
| +0.0 | -0.0613 | +0.0613 | 761 | 13 | 0.3076 | 0.1974 | 1.56 | oui |
| +0.5 | +0.0613 | +0.1840 | 621 | 10 | 0.2510 | 0.1747 | 1.44 | oui |
| +1.0 | +0.1840 | +0.3679 | 224 | 4 | 0.0905 | 0.1598 | 0.57 | oui |
| +2.0 | +0.3679 | +∞ | 126 | 2 | 0.0509 | 0.0668 | 0.76 | oui |

**DCOILWTICO** — non scénarisable : convention log inapplicable : 1 observation(s) non strictement positive(s), minimum -36.98 le 2020-04-20. Le prix a été négatif : aucun log-rendement n'existe. La série est déclarée NON SCÉNARISABLE plutôt que corrigée en silence.

**DEXJPUS** (log) — σ à 60 pas = **0.04318** · estimateurs croisés : racine-h 0.04392, blocs disjoints 0.04508 (écart relatif 4.4 %) · dérive d'échantillon +0.01004 (+0.23 σ) · 2432 variations chevauchantes, 41 blocs indépendants · 2016-09-19 → 2026-09-11

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0648 | 100 | 2 | 0.0411 | 0.0668 | 0.62 | oui |
| -1.0 | -0.0648 | -0.0324 | 226 | 4 | 0.0929 | 0.1598 | 0.58 | oui |
| -0.5 | -0.0324 | -0.0108 | 385 | 6 | 0.1583 | 0.1747 | 0.91 | oui |
| +0.0 | -0.0108 | +0.0108 | 508 | 8 | 0.2089 | 0.1974 | 1.06 | oui |
| +0.5 | +0.0108 | +0.0324 | 551 | 9 | 0.2266 | 0.1747 | 1.30 | oui |
| +1.0 | +0.0324 | +0.0648 | 473 | 8 | 0.1945 | 0.1598 | 1.22 | oui |
| +2.0 | +0.0648 | +∞ | 189 | 3 | 0.0777 | 0.0668 | 1.16 | oui |

**DEXUSEU** (log) — σ à 60 pas = **0.03473** · estimateurs croisés : racine-h 0.03466, blocs disjoints 0.03642 (écart relatif 5.1 %) · dérive d'échantillon +0.00132 (+0.04 σ) · 2432 variations chevauchantes, 41 blocs indépendants · 2016-09-19 → 2026-09-11

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0521 | 139 | 2 | 0.0572 | 0.0668 | 0.86 | oui |
| -1.0 | -0.0521 | -0.0260 | 320 | 5 | 0.1316 | 0.1598 | 0.82 | oui |
| -0.5 | -0.0260 | -0.0087 | 509 | 8 | 0.2093 | 0.1747 | 1.20 | oui |
| +0.0 | -0.0087 | +0.0087 | 612 | 10 | 0.2516 | 0.1974 | 1.27 | oui |
| +0.5 | +0.0087 | +0.0260 | 329 | 5 | 0.1353 | 0.1747 | 0.77 | oui |
| +1.0 | +0.0260 | +0.0521 | 303 | 5 | 0.1246 | 0.1598 | 0.78 | oui |
| +2.0 | +0.0521 | +∞ | 220 | 4 | 0.0905 | 0.0668 | 1.35 | oui |

**DGS10** (niveau) — σ à 60 pas = **0.42521** · estimateurs croisés : racine-h 0.41338, blocs disjoints 0.39285 (écart relatif 8.2 %) · dérive d'échantillon +0.06588 (+0.15 σ) · 2437 variations chevauchantes, 41 blocs indépendants · 2016-09-19 → 2026-09-15

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.6378 | 123 | 2 | 0.0505 | 0.0668 | 0.76 | oui |
| -1.0 | -0.6378 | -0.3189 | 284 | 5 | 0.1165 | 0.1598 | 0.73 | oui |
| -0.5 | -0.3189 | -0.1063 | 371 | 6 | 0.1522 | 0.1747 | 0.87 | oui |
| +0.0 | -0.1063 | +0.1063 | 528 | 9 | 0.2167 | 0.1974 | 1.10 | oui |
| +0.5 | +0.1063 | +0.3189 | 555 | 9 | 0.2277 | 0.1747 | 1.30 | oui |
| +1.0 | +0.3189 | +0.6378 | 364 | 6 | 0.1494 | 0.1598 | 0.93 | oui |
| +2.0 | +0.6378 | +∞ | 212 | 4 | 0.0870 | 0.0668 | 1.30 | oui |

**DGS2** (niveau) — σ à 60 pas = **0.49480** · estimateurs croisés : racine-h 0.41994, blocs disjoints 0.47140 (écart relatif 17.8 %) · dérive d'échantillon +0.08189 (+0.17 σ) · 2437 variations chevauchantes, 41 blocs indépendants · 2016-09-19 → 2026-09-15

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.7422 | 115 | 2 | 0.0472 | 0.0668 | 0.71 | oui |
| -1.0 | -0.7422 | -0.3711 | 228 | 4 | 0.0936 | 0.1598 | 0.59 | oui |
| -0.5 | -0.3711 | -0.1237 | 323 | 5 | 0.1325 | 0.1747 | 0.76 | oui |
| +0.0 | -0.1237 | +0.1237 | 739 | 12 | 0.3032 | 0.1974 | 1.54 | oui |
| +0.5 | +0.1237 | +0.3711 | 483 | 8 | 0.1982 | 0.1747 | 1.13 | oui |
| +1.0 | +0.3711 | +0.7422 | 351 | 6 | 0.1440 | 0.1598 | 0.90 | oui |
| +2.0 | +0.7422 | +∞ | 198 | 3 | 0.0812 | 0.0668 | 1.22 | oui |

**DGS30** (niveau) — σ à 60 pas = **0.36697** · estimateurs croisés : racine-h 0.39179, blocs disjoints 0.33573 (écart relatif 16.7 %) · dérive d'échantillon +0.06048 (+0.16 σ) · 2437 variations chevauchantes, 41 blocs indépendants · 2016-09-19 → 2026-09-15

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.5505 | 127 | 2 | 0.0521 | 0.0668 | 0.78 | oui |
| -1.0 | -0.5505 | -0.2752 | 277 | 5 | 0.1137 | 0.1598 | 0.71 | oui |
| -0.5 | -0.2752 | -0.0917 | 338 | 6 | 0.1387 | 0.1747 | 0.79 | oui |
| +0.0 | -0.0917 | +0.0917 | 629 | 10 | 0.2581 | 0.1974 | 1.31 | oui |
| +0.5 | +0.0917 | +0.2752 | 461 | 8 | 0.1892 | 0.1747 | 1.08 | oui |
| +1.0 | +0.2752 | +0.5505 | 394 | 7 | 0.1617 | 0.1598 | 1.01 | oui |
| +2.0 | +0.5505 | +∞ | 211 | 4 | 0.0866 | 0.0668 | 1.30 | oui |

**DTWEXBGS** (log) — σ à 60 pas = **0.02613** · estimateurs croisés : racine-h 0.02406, blocs disjoints 0.02685 (écart relatif 11.6 %) · dérive d'échantillon +0.00103 (+0.04 σ) · 2430 variations chevauchantes, 40 blocs indépendants · 2016-09-19 → 2026-09-11

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0392 | 157 | 3 | 0.0646 | 0.0668 | 0.97 | oui |
| -1.0 | -0.0392 | -0.0196 | 387 | 6 | 0.1593 | 0.1598 | 1.00 | oui |
| -0.5 | -0.0196 | -0.0065 | 355 | 6 | 0.1461 | 0.1747 | 0.84 | oui |
| +0.0 | -0.0065 | +0.0065 | 543 | 9 | 0.2235 | 0.1974 | 1.13 | oui |
| +0.5 | +0.0065 | +0.0196 | 463 | 8 | 0.1905 | 0.1747 | 1.09 | oui |
| +1.0 | +0.0196 | +0.0392 | 309 | 5 | 0.1272 | 0.1598 | 0.80 | oui |
| +2.0 | +0.0392 | +∞ | 216 | 4 | 0.0889 | 0.0668 | 1.33 | oui |

**NASDAQ100** (log) — σ à 60 pas = **0.08867** · estimateurs croisés : racine-h 0.11123, blocs disjoints 0.08621 (écart relatif 29.0 %) · dérive d'échantillon +0.04411 (+0.50 σ) · 2452 variations chevauchantes, 41 blocs indépendants · 2016-09-19 → 2026-09-15

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.1330 | 109 | 2 | 0.0445 | 0.0668 | 0.67 | oui |
| -1.0 | -0.1330 | -0.0665 | 166 | 3 | 0.0677 | 0.1598 | 0.42 ⚠ | oui |
| -0.5 | -0.0665 | -0.0222 | 185 | 3 | 0.0754 | 0.1747 | 0.43 ⚠ | oui |
| +0.0 | -0.0222 | +0.0222 | 362 | 6 | 0.1476 | 0.1974 | 0.75 | oui |
| +0.5 | +0.0222 | +0.0665 | 583 | 10 | 0.2378 | 0.1747 | 1.36 | oui |
| +1.0 | +0.0665 | +0.1330 | 731 | 12 | 0.2981 | 0.1598 | 1.87 | oui |
| +2.0 | +0.1330 | +∞ | 316 | 5 | 0.1289 | 0.0668 | 1.93 | oui |

**SP500** (log) — σ à 60 pas = **0.06915** · estimateurs croisés : racine-h 0.08843, blocs disjoints 0.06244 (écart relatif 41.6 %) · dérive d'échantillon +0.03069 (+0.44 σ) · 2451 variations chevauchantes, 41 blocs indépendants · 2016-09-19 → 2026-09-15

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.1037 | 115 | 2 | 0.0469 | 0.0668 | 0.70 | oui |
| -1.0 | -0.1037 | -0.0519 | 158 | 3 | 0.0645 | 0.1598 | 0.40 ⚠ | oui |
| -0.5 | -0.0519 | -0.0173 | 176 | 3 | 0.0718 | 0.1747 | 0.41 ⚠ | oui |
| +0.0 | -0.0173 | +0.0173 | 292 | 5 | 0.1191 | 0.1974 | 0.60 | oui |
| +0.5 | +0.0173 | +0.0519 | 746 | 12 | 0.3044 | 0.1747 | 1.74 | oui |
| +1.0 | +0.0519 | +0.1037 | 754 | 13 | 0.3076 | 0.1598 | 1.92 | oui |
| +2.0 | +0.1037 | +∞ | 210 | 4 | 0.0857 | 0.0668 | 1.28 | oui |

**VIXCLS** (log) — σ à 60 pas = **0.34676** · estimateurs croisés : racine-h 0.61351, blocs disjoints 0.29119 (écart relatif 110.7 %) · dérive d'échantillon +0.00320 (+0.01 σ) · 2484 variations chevauchantes, 41 blocs indépendants · 2016-09-19 → 2026-09-15

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.5201 | 77 | 1 | 0.0310 | 0.0668 | 0.46 ⚠ | oui |
| -1.0 | -0.5201 | -0.2601 | 388 | 6 | 0.1562 | 0.1598 | 0.98 | oui |
| -0.5 | -0.2601 | -0.0867 | 605 | 10 | 0.2436 | 0.1747 | 1.39 | oui |
| +0.0 | -0.0867 | +0.0867 | 615 | 10 | 0.2476 | 0.1974 | 1.25 | oui |
| +0.5 | +0.0867 | +0.2601 | 373 | 6 | 0.1502 | 0.1747 | 0.86 | oui |
| +1.0 | +0.2601 | +0.5201 | 248 | 4 | 0.0998 | 0.1598 | 0.62 | oui |
| +2.0 | +0.5201 | +∞ | 178 | 3 | 0.0717 | 0.0668 | 1.07 | oui |

---

## 6. TEST D'ASYMÉTRIE — DÉFINITION UNIQUE (R-030), L'ESPÉRANCE DÉCIDE

> Test d'admission : **espérance calculée sur la grille symétrique complète, les deux queues incluses**. Le rapport gain maximal / perte maximale est publié **pour information** et ne peut fonder aucune admission seul (T-001, faute E-018). Le rapport gain maximal / perte du scénario central est **interdit**. Une seule formulation, appliquée à tous les candidats, position détenue comprise.

| candidat | verdict | espérance % NAV | sans dérive | 1re moitié | 2e moitié | gain max | perte max | ratio (info) | critères échoués |
|---|:---:|---:|---:|---:|---:|---:|---:|---:|---|
| M005-DCOILBRENTEU-HAUSSE-ALIGNE | REFUSEE | +0.250 | +0.125 | +0.266 | +0.099 | +5.00 | -3.17 | 1.58:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DCOILBRENTEU-HAUSSE-CONTRARIEN | REFUSEE | +0.250 | +0.125 | +0.266 | +0.099 | +5.00 | -3.17 | 1.58:1 | 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DCOILBRENTEU-BAISSE-ALIGNE | REFUSEE | -0.250 | -0.125 | -0.266 | -0.099 | +3.17 | -5.00 | 0.63:1 | 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILBRENTEU-BAISSE-CONTRARIEN | REFUSEE | -0.250 | -0.125 | -0.266 | -0.099 | +3.17 | -5.00 | 0.63:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-HAUSSE-ALIGNE | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-HAUSSE-CONTRARIEN | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-BAISSE-ALIGNE | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-BAISSE-CONTRARIEN | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-HAUSSE-ALIGNE | REFUSEE | +0.009 | -0.062 | -0.060 | +0.055 | +0.65 | -0.73 | 0.89:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-HAUSSE-CONTRARIEN | REFUSEE | +0.009 | -0.062 | -0.060 | +0.055 | +0.65 | -0.73 | 0.89:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-BAISSE-ALIGNE | REFUSEE | -0.009 | +0.062 | +0.060 | -0.055 | +0.73 | -0.65 | 1.12:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-BAISSE-CONTRARIEN | REFUSEE | -0.009 | +0.062 | +0.060 | -0.055 | +0.73 | -0.65 | 1.12:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-HAUSSE-ALIGNE | REFUSEE | -0.058 | -0.070 | -0.032 | -0.069 | +0.51 | -0.61 | 0.84:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-HAUSSE-CONTRARIEN | REFUSEE | -0.058 | -0.070 | -0.032 | -0.069 | +0.51 | -0.61 | 0.84:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-BAISSE-ALIGNE | REFUSEE | +0.058 | +0.070 | +0.032 | +0.069 | +0.61 | -0.51 | 1.20:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DEXUSEU-BAISSE-CONTRARIEN | REFUSEE | +0.058 | +0.070 | +0.032 | +0.069 | +0.61 | -0.51 | 1.20:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DGS10-HAUSSE-ALIGNE | REFUSEE | +0.007 | -0.029 | -0.046 | +0.052 | +0.48 | -0.58 | 0.84:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-HAUSSE-CONTRARIEN | REFUSEE | +0.007 | -0.029 | -0.046 | +0.052 | +0.48 | -0.58 | 0.84:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-BAISSE-ALIGNE | REFUSEE | -0.007 | +0.029 | +0.046 | -0.052 | +0.58 | -0.48 | 1.20:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-BAISSE-CONTRARIEN | REFUSEE | -0.007 | +0.029 | +0.046 | -0.052 | +0.58 | -0.48 | 1.20:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-HAUSSE-ALIGNE | REFUSEE | -0.009 | -0.019 | -0.024 | +0.003 | +0.13 | -0.17 | 0.75:1 | 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-HAUSSE-CONTRARIEN | REFUSEE | -0.009 | -0.019 | -0.024 | +0.003 | +0.13 | -0.17 | 0.75:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-BAISSE-ALIGNE | REFUSEE | +0.009 | +0.019 | +0.024 | -0.003 | +0.17 | -0.13 | 1.34:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-BAISSE-CONTRARIEN | REFUSEE | +0.009 | +0.019 | +0.024 | -0.003 | +0.17 | -0.13 | 1.34:1 | 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-HAUSSE-ALIGNE | REFUSEE | +0.013 | -0.045 | -0.091 | +0.118 | +0.77 | -0.98 | 0.79:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-HAUSSE-CONTRARIEN | REFUSEE | +0.013 | -0.045 | -0.091 | +0.118 | +0.77 | -0.98 | 0.79:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-BAISSE-ALIGNE | REFUSEE | -0.013 | +0.045 | +0.091 | -0.118 | +0.98 | -0.77 | 1.27:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-BAISSE-CONTRARIEN | REFUSEE | -0.013 | +0.045 | +0.091 | -0.118 | +0.98 | -0.77 | 1.27:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-HAUSSE-ALIGNE | REFUSEE | -0.058 | -0.067 | -0.072 | -0.046 | +0.36 | -0.48 | 0.76:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-HAUSSE-CONTRARIEN | REFUSEE | -0.058 | -0.067 | -0.072 | -0.046 | +0.36 | -0.48 | 0.76:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-BAISSE-ALIGNE | REFUSEE | +0.058 | +0.067 | +0.072 | +0.046 | +0.48 | -0.36 | 1.32:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DTWEXBGS-BAISSE-CONTRARIEN | REFUSEE | +0.058 | +0.067 | +0.072 | +0.046 | +0.48 | -0.36 | 1.32:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-HAUSSE-ALIGNE | REFUSEE | +0.308 | -0.030 | +0.455 | +0.191 | +1.48 | -1.37 | 1.08:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-HAUSSE-CONTRARIEN | REFUSEE | +0.308 | -0.030 | +0.455 | +0.191 | +1.48 | -1.37 | 1.08:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-BAISSE-ALIGNE | REFUSEE | -0.308 | +0.030 | -0.455 | -0.191 | +1.37 | -1.48 | 0.92:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-NASDAQ100-BAISSE-CONTRARIEN | REFUSEE | -0.308 | +0.030 | -0.455 | -0.191 | +1.37 | -1.48 | 0.92:1 | 12_esperance_positive, 13_esperance_non_portee_par_derive, 14_esperance_stable_dans_le_temps |
| M005-SP500-HAUSSE-ALIGNE | REFUSEE | +0.192 | -0.038 | +0.223 | +0.161 | +1.12 | -1.10 | 1.01:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-SP500-HAUSSE-CONTRARIEN | REFUSEE | +0.192 | -0.038 | +0.223 | +0.161 | +1.12 | -1.10 | 1.01:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-SP500-BAISSE-ALIGNE | REFUSEE | -0.192 | +0.038 | -0.223 | -0.161 | +1.10 | -1.12 | 0.99:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-SP500-BAISSE-CONTRARIEN | REFUSEE | -0.192 | +0.038 | -0.223 | -0.161 | +1.10 | -1.12 | 0.99:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |

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
| 8_confirmations_independantes | 28 |
| 9_test_execute_et_vrai | 28 |
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

- `BAMLC0A0CM` : percentile REFUSÉ sur 5 ans — profondeur réelle 785 obs / 2.99 ans (début 2023-09-18). R-011 : un percentile calculé sur une série tronquée est sans valeur.
- `BAMLH0A0HYM2` : percentile REFUSÉ sur 5 ans — profondeur réelle 786 obs / 2.99 ans (début 2023-09-18). R-011 : un percentile calculé sur une série tronquée est sans valeur.
- `BAMLH0A0HYM2` : instrument NON ADMISSIBLE — P&L non calculable depuis le dépôt : l'OAS est un spread, et le dépôt ne contient pas le rendement de l'indice, donc pas la duration de spread. Aucune valeur ne peut être produite sans un chiffre extérieur aux données (E-002).
- `BAMLC0A0CM` : instrument NON ADMISSIBLE — P&L non calculable depuis le dépôt : l'OAS est un spread, et le dépôt ne contient pas le rendement de l'indice, donc pas la duration de spread. Aucune valeur ne peut être produite sans un chiffre extérieur aux données (E-002).
- Retards sur la date d'arrêté unique (E-014) : DEXJPUS 2 séance(s), DEXUSEU 2 séance(s), DTWEXBGS 2 séance(s)

**Vérification tierce (R-032) : NON SATISFAITE pour ce brief.** Le moteur ne dispose d'aucune source extérieure au dépôt. Trois estimateurs **internes** de σ sont publiés côte à côte au §5 ; ce sont des contrôles de cohérence interne, **pas** une vérification tierce, et ils ne sont pas présentés comme telle.

**Ce que ce moteur ne peut pas faire.** Il ne prouve aucune capacité prédictive : la règle de confirmation est une règle de percentile, déclarée et symétrique, pas un modèle validé hors échantillon. Il ne corrige pas la multiplicité : 40 candidats sont évalués et aucune pénalité de sélection n'est appliquée à l'espérance — c'est une limite déclarée, pas un oubli. Il ne voit ni les événements politiques, ni les décisions de banques centrales : le dépôt ne contient que des séries FRED, et toute affirmation de politique monétaire non adossée à `DFF` est refusée (critère 15, faute E-006).

---

*Fin du brief 005. Produit mécaniquement. Ne constitue pas un conseil en investissement.*