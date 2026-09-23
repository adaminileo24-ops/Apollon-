# BRIEF MACRO n° 005 — arrêté au 2026-09-22

*Produit par `apollon_macro.py` le 2026-09-23T22:27:53+00:00. Aucune valeur de ce document n'est saisie à la main : chacune porte sa série, sa date et sa profondeur. Bloc à copier tel quel.*

**Grille de scénarios (R-029, §11), déclarée avant toute lecture de données et empreintée :** `[-2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0]` · empreinte SHA-256 `6aaeb3863c875923…` · symétrique : True · horizon 60 séances (3 mois pour les séries mensuelles).

---

## 1. CONCLUSION, ÉNONCÉE D'ABORD

**40 candidats déclarés d'avance (10 instruments × 2 directions × 2 règles de confirmation). 40 évalués. 0 thèse(s) survivent aux quinze critères.**

**Abstention. Aucune thèse ne survit.** Ce n'est pas un silence : c'est un résultat, produit par le même portier que celui qui aurait admis une thèse. Le détail des échecs, critère par critère, figure au §6. La Section Macro ne transmet rien à la Section Risque ce cycle.

**Position détenue (contrôle 9, E-020) — 100 % cash, testée sur la même grille.** Espérance excédentaire du cash : +0.000 % de NAV. Référence 60/40 : +1.343 % (hors dérive : -0.205 %). **Écart du cash contre la référence : -1.343 % de NAV** sur 60 séances.

---

## 2. CE QUI A CHANGÉ — MÉCANISME, PAS CONTENU

Fait, étiqueté : les briefs 001 à 004 étaient rédigés par un agent. Celui-ci est produit par un moteur. Le paramètre libre de la Section Macro — la grille de scénarios — n'est plus accessible à l'agent : il est déclaré en tête de fichier, symétrique par construction, et son empreinte SHA-256 est vérifiée avant chaque usage. Sur le brief 004, ce paramètre avait porté le ratio annoncé de 1,29:1 à 3,0:1.

---

## 3. M1 · M2 · M3 · M4 — ÉTAT DES SÉRIES (FAIT)

Toutes les valeurs sont des FAITS lus dans le dépôt. Le retard est compté en séances ouvrées depuis la date d'arrêté unique. Les couples obligatoires sont vérifiés par le rendu : ce bloc ne peut pas être émis si un membre d'un couple manque.

| série | rôle déclaré | valeur | date | retard | n obs | profondeur | pct 1 an | pct 5 ans | pct complet |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| BAMLC0A0CM | risque_credit_ig | 0.77 | 2026-09-22 | 0 | 785 | 2.99 ans | 31.0 | REFUSÉ (insuffisante, -38 %) | 13.6 |
| BAMLH0A0HYM2 | risque_credit_hy | 2.68 | 2026-09-22 | 0 | 786 | 2.99 ans | 10.3 | REFUSÉ (insuffisante, -38 %) | 8.7 |
| CPIAUCSL | inflation_globale | 334.1 | 2026-08-01 | 52 | 119 | 9.91 ans | 100.0 | 100.0 | 100.0 |
| CPILFESL | inflation_sous_jacente | 337.8 | 2026-08-01 | 52 | 119 | 9.91 ans | 100.0 | 100.0 | 100.0 |
| DCOILBRENTEU | prix_energie | 114.9 | 2026-09-22 | 0 | 2534 | 9.99 ans | 88.9 | 94.2 | 97.1 |
| DCOILWTICO | prix_energie_wti | 96.41 | 2026-09-22 | 0 | 2498 | 9.99 ans | 81.0 | 87.8 | 93.8 |
| DEXJPUS | devise_usdjpy | 156.9 | 2026-09-18 | 2 | 2492 | 9.98 ans | 43.7 | 84.8 | 92.3 |
| DEXUSEU | devise_eurusd | 1.146 | 2026-09-18 | 2 | 2492 | 9.98 ans | 11.9 | 73.2 | 62.4 |
| DFF | politique_monetaire | 3.88 | 2026-09-22 | 0 | 3650 | 9.99 ans | 100.0 | 25.0 | 70.9 |
| DFII10 | taux_reel_10a | 2.63 | 2026-09-22 | 0 | 2497 | 9.99 ans | 99.2 | 99.8 | 99.9 |
| DGS10 | taux_nominal_10a | 4.96 | 2026-09-22 | 0 | 2497 | 9.99 ans | 98.4 | 99.6 | 99.8 |
| DGS2 | taux_nominal_2a | 4.71 | 2026-09-22 | 0 | 2497 | 9.99 ans | 98.8 | 86.0 | 92.9 |
| DGS30 | taux_nominal_30a | 5.29 | 2026-09-22 | 0 | 2497 | 9.99 ans | 97.2 | 99.4 | 99.7 |
| DTWEXBGS | dollar_large | 119.5 | 2026-09-18 | 2 | 2490 | 9.98 ans | 45.6 | 31.0 | 62.1 |
| INDPRO | activite_industrielle | 103.1 | 2026-08-01 | 52 | 120 | 9.91 ans | 100.0 | 100.0 | 92.5 |
| NASDAQ100 | prix_actions_tech | 3.073e+04 | 2026-09-22 | 0 | 2512 | 9.99 ans | 100.0 | 100.0 | 100.0 |
| OVXCLS | volatilite_implicite_petrole | 51.89 | 2026-09-22 | 0 | 2513 | 9.99 ans | 53.6 | 82.9 | 86.6 |
| PAYEMS | emploi | 1.591e+05 | 2026-08-01 | 52 | 120 | 9.91 ans | 100.0 | 100.0 | 100.0 |
| SP500 | prix_actions | 7765 | 2026-09-22 | 0 | 2511 | 9.99 ans | 98.8 | 99.8 | 99.9 |
| T10Y2Y | pente_courbe | 0.25 | 2026-09-22 | 0 | 2497 | 9.99 ans | 1.2 | 54.7 | 40.3 |
| T10YIE | point_mort_10a | 2.33 | 2026-09-22 | 0 | 2497 | 9.99 ans | 62.3 | 52.2 | 73.0 |
| T5YIFR | point_mort_5a5a | 2.34 | 2026-09-22 | 0 | 2497 | 9.99 ans | 98.0 | 81.5 | 90.4 |
| UNRATE | chomage | 4.1 | 2026-08-01 | 52 | 119 | 9.91 ans | 16.7 | 65.0 | 55.5 |
| VIXCLS | volatilite_implicite | 14.21 | 2026-09-22 | 0 | 2544 | 9.99 ans | 2.4 | 15.6 | 27.7 |
| VXDCLS | volatilite_implicite_dow | 14.56 | 2026-09-22 | 0 | 2514 | 9.99 ans | 26.2 | 31.9 | 36.9 |
| VXVCLS | volatilite_implicite_3m | 17.61 | 2026-09-22 | 0 | 2511 | 9.99 ans | 2.4 | 21.3 | 37.3 |

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
- corrélation des variations à 60 séances : INDPRO / PAYEMS = +0.913 sur 117 points (seuil 0.9)
- corrélation des variations à 60 séances : INDPRO / UNRATE = -0.917 sur 116 points (seuil 0.9)
- corrélation des variations à 60 séances : NASDAQ100 / SP500 = +0.902 sur 2451 points (seuil 0.9)
- corrélation des variations à 60 séances : PAYEMS / UNRATE = -0.983 sur 116 points (seuil 0.9)
- corrélation des variations à 60 séances : VIXCLS / VXDCLS = +0.930 sur 2451 points (seuil 0.9)
- corrélation des variations à 60 séances : VIXCLS / VXVCLS = +0.958 sur 2451 points (seuil 0.9)
- corrélation des variations à 60 séances : VXDCLS / VXVCLS = +0.934 sur 2451 points (seuil 0.9)

---

## 5. GRILLE, σ MESURÉ, ET DOUBLE CONFRONTATION DES PROBABILITÉS

σ est **mesuré** sur chaque série, jamais choisi. Les probabilités sont les **fréquences historiques** dans chaque bande, jamais un jugement. L'effectif de chaque bande est publié ; sous 20 observations la bande est déclarée NON ESTIMABLE. La colonne « emp./gauss. » est la double confrontation exigée par §11.5 : tout écart supérieur à un facteur 2 est déclaré (⚠).

**BAMLH0A0HYM2** (niveau) — σ à 60 pas = **0.45587** · estimateurs croisés : racine-h 0.53785, blocs disjoints 0.45432 (écart relatif 18.4 %) · dérive d'échantillon -0.11366 (-0.25 σ) · 726 variations chevauchantes, 12 blocs indépendants · 2023-09-25 → 2026-09-22

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.6838 | 55 | 1 | 0.0758 | 0.0668 | 1.13 | oui |
| -1.0 | -0.6838 | -0.3419 | 124 | 2 | 0.1708 | 0.1598 | 1.07 | oui |
| -0.5 | -0.3419 | -0.1140 | 194 | 3 | 0.2672 | 0.1747 | 1.53 | oui |
| +0.0 | -0.1140 | +0.1140 | 193 | 3 | 0.2658 | 0.1974 | 1.35 | oui |
| +0.5 | +0.1140 | +0.3419 | 80 | 1 | 0.1102 | 0.1747 | 0.63 | oui |
| +1.0 | +0.3419 | +0.6838 | 51 | 1 | 0.0702 | 0.1598 | 0.44 ⚠ | oui |
| +2.0 | +0.6838 | +∞ | 29 | 0 | 0.0399 | 0.0668 | 0.60 | oui |

**DCOILBRENTEU** (log) — σ à 60 pas = **0.24618** · estimateurs croisés : racine-h 0.24783, blocs disjoints 0.23947 (écart relatif 3.5 %) · dérive d'échantillon +0.01591 (+0.06 σ) · 2474 variations chevauchantes, 41 blocs indépendants · 2016-09-26 → 2026-09-22

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.3693 | 84 | 1 | 0.0340 | 0.0668 | 0.51 | oui |
| -1.0 | -0.3693 | -0.1846 | 155 | 3 | 0.0627 | 0.1598 | 0.39 ⚠ | oui |
| -0.5 | -0.1846 | -0.0615 | 503 | 8 | 0.2033 | 0.1747 | 1.16 | oui |
| +0.0 | -0.0615 | +0.0615 | 763 | 13 | 0.3084 | 0.1974 | 1.56 | oui |
| +0.5 | +0.0615 | +0.1846 | 618 | 10 | 0.2498 | 0.1747 | 1.43 | oui |
| +1.0 | +0.1846 | +0.3693 | 221 | 4 | 0.0893 | 0.1598 | 0.56 | oui |
| +2.0 | +0.3693 | +∞ | 130 | 2 | 0.0525 | 0.0668 | 0.79 | oui |

**DCOILWTICO** — non scénarisable : convention log inapplicable : 1 observation(s) non strictement positive(s), minimum -36.98 le 2020-04-20. Le prix a été négatif : aucun log-rendement n'existe. La série est déclarée NON SCÉNARISABLE plutôt que corrigée en silence.

**DEXJPUS** (log) — σ à 60 pas = **0.04276** · estimateurs croisés : racine-h 0.04390, blocs disjoints 0.04722 (écart relatif 10.4 %) · dérive d'échantillon +0.00965 (+0.23 σ) · 2432 variations chevauchantes, 41 blocs indépendants · 2016-09-26 → 2026-09-18

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0641 | 102 | 2 | 0.0419 | 0.0668 | 0.63 | oui |
| -1.0 | -0.0641 | -0.0321 | 238 | 4 | 0.0979 | 0.1598 | 0.61 | oui |
| -0.5 | -0.0321 | -0.0107 | 377 | 6 | 0.1550 | 0.1747 | 0.89 | oui |
| +0.0 | -0.0107 | +0.0107 | 507 | 8 | 0.2085 | 0.1974 | 1.06 | oui |
| +0.5 | +0.0107 | +0.0321 | 546 | 9 | 0.2245 | 0.1747 | 1.29 | oui |
| +1.0 | +0.0321 | +0.0641 | 471 | 8 | 0.1937 | 0.1598 | 1.21 | oui |
| +2.0 | +0.0641 | +∞ | 191 | 3 | 0.0785 | 0.0668 | 1.18 | oui |

**DEXUSEU** (log) — σ à 60 pas = **0.03457** · estimateurs croisés : racine-h 0.03466, blocs disjoints 0.03807 (écart relatif 10.1 %) · dérive d'échantillon +0.00148 (+0.04 σ) · 2432 variations chevauchantes, 41 blocs indépendants · 2016-09-26 → 2026-09-18

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0519 | 137 | 2 | 0.0563 | 0.0668 | 0.84 | oui |
| -1.0 | -0.0519 | -0.0259 | 319 | 5 | 0.1312 | 0.1598 | 0.82 | oui |
| -0.5 | -0.0259 | -0.0086 | 509 | 8 | 0.2093 | 0.1747 | 1.20 | oui |
| +0.0 | -0.0086 | +0.0086 | 613 | 10 | 0.2521 | 0.1974 | 1.28 | oui |
| +0.5 | +0.0086 | +0.0259 | 327 | 5 | 0.1345 | 0.1747 | 0.77 | oui |
| +1.0 | +0.0259 | +0.0519 | 305 | 5 | 0.1254 | 0.1598 | 0.78 | oui |
| +2.0 | +0.0519 | +∞ | 222 | 4 | 0.0913 | 0.0668 | 1.37 | oui |

**DGS10** (niveau) — σ à 60 pas = **0.42402** · estimateurs croisés : racine-h 0.41365, blocs disjoints 0.41632 (écart relatif 2.5 %) · dérive d'échantillon +0.06511 (+0.15 σ) · 2437 variations chevauchantes, 41 blocs indépendants · 2016-09-26 → 2026-09-22

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.6360 | 123 | 2 | 0.0505 | 0.0668 | 0.76 | oui |
| -1.0 | -0.6360 | -0.3180 | 284 | 5 | 0.1165 | 0.1598 | 0.73 | oui |
| -0.5 | -0.3180 | -0.1060 | 371 | 6 | 0.1522 | 0.1747 | 0.87 | oui |
| +0.0 | -0.1060 | +0.1060 | 528 | 9 | 0.2167 | 0.1974 | 1.10 | oui |
| +0.5 | +0.1060 | +0.3180 | 555 | 9 | 0.2277 | 0.1747 | 1.30 | oui |
| +1.0 | +0.3180 | +0.6360 | 369 | 6 | 0.1514 | 0.1598 | 0.95 | oui |
| +2.0 | +0.6360 | +∞ | 207 | 3 | 0.0849 | 0.0668 | 1.27 | oui |

**DGS2** (niveau) — σ à 60 pas = **0.49504** · estimateurs croisés : racine-h 0.42050, blocs disjoints 0.50571 (écart relatif 20.3 %) · dérive d'échantillon +0.08215 (+0.17 σ) · 2437 variations chevauchantes, 41 blocs indépendants · 2016-09-26 → 2026-09-22

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.7426 | 115 | 2 | 0.0472 | 0.0668 | 0.71 | oui |
| -1.0 | -0.7426 | -0.3713 | 228 | 4 | 0.0936 | 0.1598 | 0.59 | oui |
| -0.5 | -0.3713 | -0.1238 | 323 | 5 | 0.1325 | 0.1747 | 0.76 | oui |
| +0.0 | -0.1238 | +0.1238 | 739 | 12 | 0.3032 | 0.1974 | 1.54 | oui |
| +0.5 | +0.1238 | +0.3713 | 483 | 8 | 0.1982 | 0.1747 | 1.13 | oui |
| +1.0 | +0.3713 | +0.7426 | 351 | 6 | 0.1440 | 0.1598 | 0.90 | oui |
| +2.0 | +0.7426 | +∞ | 198 | 3 | 0.0812 | 0.0668 | 1.22 | oui |

**DGS30** (niveau) — σ à 60 pas = **0.36596** · estimateurs croisés : racine-h 0.39190, blocs disjoints 0.35585 (écart relatif 10.1 %) · dérive d'échantillon +0.05978 (+0.16 σ) · 2437 variations chevauchantes, 41 blocs indépendants · 2016-09-26 → 2026-09-22

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.5489 | 128 | 2 | 0.0525 | 0.0668 | 0.79 | oui |
| -1.0 | -0.5489 | -0.2745 | 276 | 5 | 0.1133 | 0.1598 | 0.71 | oui |
| -0.5 | -0.2745 | -0.0915 | 338 | 6 | 0.1387 | 0.1747 | 0.79 | oui |
| +0.0 | -0.0915 | +0.0915 | 629 | 10 | 0.2581 | 0.1974 | 1.31 | oui |
| +0.5 | +0.0915 | +0.2745 | 461 | 8 | 0.1892 | 0.1747 | 1.08 | oui |
| +1.0 | +0.2745 | +0.5489 | 394 | 7 | 0.1617 | 0.1598 | 1.01 | oui |
| +2.0 | +0.5489 | +∞ | 211 | 4 | 0.0866 | 0.0668 | 1.30 | oui |

**DTWEXBGS** (log) — σ à 60 pas = **0.02604** · estimateurs croisés : racine-h 0.02404, blocs disjoints 0.02672 (écart relatif 11.2 %) · dérive d'échantillon +0.00090 (+0.03 σ) · 2430 variations chevauchantes, 40 blocs indépendants · 2016-09-26 → 2026-09-18

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0391 | 159 | 3 | 0.0654 | 0.0668 | 0.98 | oui |
| -1.0 | -0.0391 | -0.0195 | 386 | 6 | 0.1588 | 0.1598 | 0.99 | oui |
| -0.5 | -0.0195 | -0.0065 | 358 | 6 | 0.1473 | 0.1747 | 0.84 | oui |
| +0.0 | -0.0065 | +0.0065 | 542 | 9 | 0.2230 | 0.1974 | 1.13 | oui |
| +0.5 | +0.0065 | +0.0195 | 465 | 8 | 0.1914 | 0.1747 | 1.10 | oui |
| +1.0 | +0.0195 | +0.0391 | 307 | 5 | 0.1263 | 0.1598 | 0.79 | oui |
| +2.0 | +0.0391 | +∞ | 213 | 4 | 0.0877 | 0.0668 | 1.31 | oui |

**NASDAQ100** (log) — σ à 60 pas = **0.08869** · estimateurs croisés : racine-h 0.11131, blocs disjoints 0.08263 (écart relatif 34.7 %) · dérive d'échantillon +0.04409 (+0.50 σ) · 2452 variations chevauchantes, 41 blocs indépendants · 2016-09-26 → 2026-09-22

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.1330 | 109 | 2 | 0.0445 | 0.0668 | 0.67 | oui |
| -1.0 | -0.1330 | -0.0665 | 166 | 3 | 0.0677 | 0.1598 | 0.42 ⚠ | oui |
| -0.5 | -0.0665 | -0.0222 | 186 | 3 | 0.0759 | 0.1747 | 0.43 ⚠ | oui |
| +0.0 | -0.0222 | +0.0222 | 361 | 6 | 0.1472 | 0.1974 | 0.75 | oui |
| +0.5 | +0.0222 | +0.0665 | 583 | 10 | 0.2378 | 0.1747 | 1.36 | oui |
| +1.0 | +0.0665 | +0.1330 | 731 | 12 | 0.2981 | 0.1598 | 1.87 | oui |
| +2.0 | +0.1330 | +∞ | 316 | 5 | 0.1289 | 0.0668 | 1.93 | oui |

**SP500** (log) — σ à 60 pas = **0.06915** · estimateurs croisés : racine-h 0.08844, blocs disjoints 0.06115 (écart relatif 44.6 %) · dérive d'échantillon +0.03067 (+0.44 σ) · 2451 variations chevauchantes, 41 blocs indépendants · 2016-09-26 → 2026-09-22

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.1037 | 115 | 2 | 0.0469 | 0.0668 | 0.70 | oui |
| -1.0 | -0.1037 | -0.0519 | 158 | 3 | 0.0645 | 0.1598 | 0.40 ⚠ | oui |
| -0.5 | -0.0519 | -0.0173 | 176 | 3 | 0.0718 | 0.1747 | 0.41 ⚠ | oui |
| +0.0 | -0.0173 | +0.0173 | 293 | 5 | 0.1195 | 0.1974 | 0.61 | oui |
| +0.5 | +0.0173 | +0.0519 | 744 | 12 | 0.3035 | 0.1747 | 1.74 | oui |
| +1.0 | +0.0519 | +0.1037 | 755 | 13 | 0.3080 | 0.1598 | 1.93 | oui |
| +2.0 | +0.1037 | +∞ | 210 | 4 | 0.0857 | 0.0668 | 1.28 | oui |

**VIXCLS** (log) — σ à 60 pas = **0.34680** · estimateurs croisés : racine-h 0.61259, blocs disjoints 0.27119 (écart relatif 125.9 %) · dérive d'échantillon +0.00307 (+0.01 σ) · 2484 variations chevauchantes, 41 blocs indépendants · 2016-09-26 → 2026-09-22

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.5202 | 77 | 1 | 0.0310 | 0.0668 | 0.46 ⚠ | oui |
| -1.0 | -0.5202 | -0.2601 | 388 | 6 | 0.1562 | 0.1598 | 0.98 | oui |
| -0.5 | -0.2601 | -0.0867 | 607 | 10 | 0.2444 | 0.1747 | 1.40 | oui |
| +0.0 | -0.0867 | +0.0867 | 613 | 10 | 0.2468 | 0.1974 | 1.25 | oui |
| +0.5 | +0.0867 | +0.2601 | 373 | 6 | 0.1502 | 0.1747 | 0.86 | oui |
| +1.0 | +0.2601 | +0.5202 | 248 | 4 | 0.0998 | 0.1598 | 0.62 | oui |
| +2.0 | +0.5202 | +∞ | 178 | 3 | 0.0717 | 0.0668 | 1.07 | oui |

---

## 6. TEST D'ASYMÉTRIE — DÉFINITION UNIQUE (R-030), L'ESPÉRANCE DÉCIDE

> Test d'admission : **espérance calculée sur la grille symétrique complète, les deux queues incluses**. Le rapport gain maximal / perte maximale est publié **pour information** et ne peut fonder aucune admission seul (T-001, faute E-018). Le rapport gain maximal / perte du scénario central est **interdit**. Une seule formulation, appliquée à tous les candidats, position détenue comprise.

| candidat | verdict | espérance % NAV | sans dérive | 1re moitié | 2e moitié | gain max | perte max | ratio (info) | critères échoués |
|---|:---:|---:|---:|---:|---:|---:|---:|---:|---|
| M005-DCOILBRENTEU-HAUSSE-ALIGNE | REFUSEE | +0.251 | +0.125 | +0.258 | +0.123 | +5.02 | -3.18 | 1.58:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DCOILBRENTEU-HAUSSE-CONTRARIEN | REFUSEE | +0.251 | +0.125 | +0.258 | +0.123 | +5.02 | -3.18 | 1.58:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DCOILBRENTEU-BAISSE-ALIGNE | REFUSEE | -0.251 | -0.125 | -0.258 | -0.123 | +3.18 | -5.02 | 0.63:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILBRENTEU-BAISSE-CONTRARIEN | REFUSEE | -0.251 | -0.125 | -0.258 | -0.123 | +3.18 | -5.02 | 0.63:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-HAUSSE-ALIGNE | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-HAUSSE-CONTRARIEN | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-BAISSE-ALIGNE | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-BAISSE-CONTRARIEN | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-HAUSSE-ALIGNE | REFUSEE | +0.002 | -0.067 | -0.067 | +0.047 | +0.64 | -0.73 | 0.88:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-HAUSSE-CONTRARIEN | REFUSEE | +0.002 | -0.067 | -0.067 | +0.047 | +0.64 | -0.73 | 0.88:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-BAISSE-ALIGNE | REFUSEE | -0.002 | +0.067 | +0.067 | -0.047 | +0.73 | -0.64 | 1.14:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-BAISSE-CONTRARIEN | REFUSEE | -0.002 | +0.067 | +0.067 | -0.047 | +0.73 | -0.64 | 1.14:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-HAUSSE-ALIGNE | REFUSEE | -0.062 | -0.075 | -0.036 | -0.073 | +0.50 | -0.61 | 0.82:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-HAUSSE-CONTRARIEN | REFUSEE | -0.062 | -0.075 | -0.036 | -0.073 | +0.50 | -0.61 | 0.82:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-BAISSE-ALIGNE | REFUSEE | +0.062 | +0.075 | +0.036 | +0.073 | +0.61 | -0.50 | 1.22:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DEXUSEU-BAISSE-CONTRARIEN | REFUSEE | +0.062 | +0.075 | +0.036 | +0.073 | +0.61 | -0.50 | 1.22:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DGS10-HAUSSE-ALIGNE | REFUSEE | +0.012 | -0.024 | -0.043 | +0.058 | +0.49 | -0.57 | 0.85:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-HAUSSE-CONTRARIEN | REFUSEE | +0.012 | -0.024 | -0.043 | +0.058 | +0.49 | -0.57 | 0.85:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-BAISSE-ALIGNE | REFUSEE | -0.012 | +0.024 | +0.043 | -0.058 | +0.57 | -0.49 | 1.17:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-BAISSE-CONTRARIEN | REFUSEE | -0.012 | +0.024 | +0.043 | -0.058 | +0.57 | -0.49 | 1.17:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-HAUSSE-ALIGNE | REFUSEE | -0.005 | -0.015 | -0.020 | +0.007 | +0.13 | -0.17 | 0.79:1 | 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-HAUSSE-CONTRARIEN | REFUSEE | -0.005 | -0.015 | -0.020 | +0.007 | +0.13 | -0.17 | 0.79:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-BAISSE-ALIGNE | REFUSEE | +0.005 | +0.015 | +0.020 | -0.007 | +0.17 | -0.13 | 1.27:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-BAISSE-CONTRARIEN | REFUSEE | +0.005 | +0.015 | +0.020 | -0.007 | +0.17 | -0.13 | 1.27:1 | 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-HAUSSE-ALIGNE | REFUSEE | +0.019 | -0.038 | -0.089 | +0.126 | +0.78 | -0.98 | 0.80:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-HAUSSE-CONTRARIEN | REFUSEE | +0.019 | -0.038 | -0.089 | +0.126 | +0.78 | -0.98 | 0.80:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-BAISSE-ALIGNE | REFUSEE | -0.019 | +0.038 | +0.089 | -0.126 | +0.98 | -0.78 | 1.25:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-BAISSE-CONTRARIEN | REFUSEE | -0.019 | +0.038 | +0.089 | -0.126 | +0.98 | -0.78 | 1.25:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-HAUSSE-ALIGNE | REFUSEE | -0.064 | -0.072 | -0.079 | -0.052 | +0.35 | -0.48 | 0.74:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-HAUSSE-CONTRARIEN | REFUSEE | -0.064 | -0.072 | -0.079 | -0.052 | +0.35 | -0.48 | 0.74:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-BAISSE-ALIGNE | REFUSEE | +0.064 | +0.072 | +0.079 | +0.052 | +0.48 | -0.35 | 1.36:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DTWEXBGS-BAISSE-CONTRARIEN | REFUSEE | +0.064 | +0.072 | +0.079 | +0.052 | +0.48 | -0.35 | 1.36:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-HAUSSE-ALIGNE | REFUSEE | +0.304 | -0.035 | +0.452 | +0.185 | +1.48 | -1.37 | 1.08:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-HAUSSE-CONTRARIEN | REFUSEE | +0.304 | -0.035 | +0.452 | +0.185 | +1.48 | -1.37 | 1.08:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-BAISSE-ALIGNE | REFUSEE | -0.304 | +0.035 | -0.452 | -0.185 | +1.37 | -1.48 | 0.93:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-NASDAQ100-BAISSE-CONTRARIEN | REFUSEE | -0.304 | +0.035 | -0.452 | -0.185 | +1.37 | -1.48 | 0.93:1 | 12_esperance_positive, 13_esperance_non_portee_par_derive, 14_esperance_stable_dans_le_temps |
| M005-SP500-HAUSSE-ALIGNE | REFUSEE | +0.187 | -0.043 | +0.218 | +0.156 | +1.11 | -1.11 | 1.00:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-SP500-HAUSSE-CONTRARIEN | REFUSEE | +0.187 | -0.043 | +0.218 | +0.156 | +1.11 | -1.11 | 1.00:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-SP500-BAISSE-ALIGNE | REFUSEE | -0.187 | +0.043 | -0.218 | -0.156 | +1.11 | -1.11 | 1.00:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-SP500-BAISSE-CONTRARIEN | REFUSEE | -0.187 | +0.043 | -0.218 | -0.156 | +1.11 | -1.11 | 1.00:1 | 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |

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
| 8_confirmations_independantes | 24 |
| 9_test_execute_et_vrai | 24 |
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

- `BAMLC0A0CM` : percentile REFUSÉ sur 5 ans — profondeur réelle 785 obs / 2.99 ans (début 2023-09-25). R-011 : un percentile calculé sur une série tronquée est sans valeur.
- `BAMLH0A0HYM2` : percentile REFUSÉ sur 5 ans — profondeur réelle 786 obs / 2.99 ans (début 2023-09-25). R-011 : un percentile calculé sur une série tronquée est sans valeur.
- `BAMLH0A0HYM2` : instrument NON ADMISSIBLE — P&L non calculable depuis le dépôt : l'OAS est un spread, et le dépôt ne contient pas le rendement de l'indice, donc pas la duration de spread. Aucune valeur ne peut être produite sans un chiffre extérieur aux données (E-002).
- `BAMLC0A0CM` : instrument NON ADMISSIBLE — P&L non calculable depuis le dépôt : l'OAS est un spread, et le dépôt ne contient pas le rendement de l'indice, donc pas la duration de spread. Aucune valeur ne peut être produite sans un chiffre extérieur aux données (E-002).
- Retards sur la date d'arrêté unique (E-014) : DEXJPUS 2 séance(s), DEXUSEU 2 séance(s), DTWEXBGS 2 séance(s)

**Vérification tierce (R-032) : NON SATISFAITE pour ce brief.** Le moteur ne dispose d'aucune source extérieure au dépôt. Trois estimateurs **internes** de σ sont publiés côte à côte au §5 ; ce sont des contrôles de cohérence interne, **pas** une vérification tierce, et ils ne sont pas présentés comme telle.

**Ce que ce moteur ne peut pas faire.** Il ne prouve aucune capacité prédictive : la règle de confirmation est une règle de percentile, déclarée et symétrique, pas un modèle validé hors échantillon. Il ne corrige pas la multiplicité : 40 candidats sont évalués et aucune pénalité de sélection n'est appliquée à l'espérance — c'est une limite déclarée, pas un oubli. Il ne voit ni les événements politiques, ni les décisions de banques centrales : le dépôt ne contient que des séries FRED, et toute affirmation de politique monétaire non adossée à `DFF` est refusée (critère 15, faute E-006).

---

*Fin du brief 005. Produit mécaniquement. Ne constitue pas un conseil en investissement.*