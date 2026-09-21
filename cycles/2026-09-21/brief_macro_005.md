# BRIEF MACRO n° 005 — arrêté au 2026-09-18

*Produit par `apollon_macro.py` le 2026-09-21T22:50:17+00:00. Aucune valeur de ce document n'est saisie à la main : chacune porte sa série, sa date et sa profondeur. Bloc à copier tel quel.*

**Grille de scénarios (R-029, §11), déclarée avant toute lecture de données et empreintée :** `[-2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0]` · empreinte SHA-256 `6aaeb3863c875923…` · symétrique : True · horizon 60 séances (3 mois pour les séries mensuelles).

---

## 1. CONCLUSION, ÉNONCÉE D'ABORD

**40 candidats déclarés d'avance (10 instruments × 2 directions × 2 règles de confirmation). 40 évalués. 0 thèse(s) survivent aux quinze critères.**

**Abstention. Aucune thèse ne survit.** Ce n'est pas un silence : c'est un résultat, produit par le même portier que celui qui aurait admis une thèse. Le détail des échecs, critère par critère, figure au §6. La Section Macro ne transmet rien à la Section Risque ce cycle.

**Position détenue (contrôle 9, E-020) — 100 % cash, testée sur la même grille.** Espérance excédentaire du cash : +0.000 % de NAV. Référence 60/40 : +1.345 % (hors dérive : -0.202 %). **Écart du cash contre la référence : -1.345 % de NAV** sur 60 séances.

---

## 2. CE QUI A CHANGÉ — MÉCANISME, PAS CONTENU

Fait, étiqueté : les briefs 001 à 004 étaient rédigés par un agent. Celui-ci est produit par un moteur. Le paramètre libre de la Section Macro — la grille de scénarios — n'est plus accessible à l'agent : il est déclaré en tête de fichier, symétrique par construction, et son empreinte SHA-256 est vérifiée avant chaque usage. Sur le brief 004, ce paramètre avait porté le ratio annoncé de 1,29:1 à 3,0:1.

---

## 3. M1 · M2 · M3 · M4 — ÉTAT DES SÉRIES (FAIT)

Toutes les valeurs sont des FAITS lus dans le dépôt. Le retard est compté en séances ouvrées depuis la date d'arrêté unique. Les couples obligatoires sont vérifiés par le rendu : ce bloc ne peut pas être émis si un membre d'un couple manque.

| série | rôle déclaré | valeur | date | retard | n obs | profondeur | pct 1 an | pct 5 ans | pct complet |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| BAMLC0A0CM | risque_credit_ig | 0.77 | 2026-09-18 | 0 | 784 | 2.99 ans | 31.0 | REFUSÉ (insuffisante, -38 %) | 13.4 |
| BAMLH0A0HYM2 | risque_credit_hy | 2.68 | 2026-09-18 | 0 | 785 | 2.99 ans | 9.5 | REFUSÉ (insuffisante, -38 %) | 8.4 |
| CPIAUCSL | inflation_globale | 334.1 | 2026-08-01 | 48 | 119 | 9.91 ans | 100.0 | 100.0 | 100.0 |
| CPILFESL | inflation_sous_jacente | 337.8 | 2026-08-01 | 48 | 119 | 9.91 ans | 100.0 | 100.0 | 100.0 |
| DCOILBRENTEU | prix_energie | 130.8 | 2026-09-15 | 3 | 2530 | 9.98 ans | 99.6 | 99.8 | 99.9 |
| DCOILWTICO | prix_energie_wti | 107 | 2026-09-15 | 3 | 2494 | 9.98 ans | 96.4 | 95.3 | 97.6 |
| DEXJPUS | devise_usdjpy | 156.9 | 2026-09-18 | 0 | 2493 | 9.98 ans | 43.7 | 84.8 | 92.3 |
| DEXUSEU | devise_eurusd | 1.146 | 2026-09-18 | 0 | 2493 | 9.98 ans | 11.9 | 73.2 | 62.5 |
| DFF | politique_monetaire | 3.88 | 2026-09-18 | 0 | 3648 | 9.98 ans | 100.0 | 24.7 | 70.9 |
| DFII10 | taux_reel_10a | 2.68 | 2026-09-18 | 0 | 2496 | 9.98 ans | 100.0 | 100.0 | 100.0 |
| DGS10 | taux_nominal_10a | 5.01 | 2026-09-18 | 0 | 2496 | 9.98 ans | 100.0 | 100.0 | 100.0 |
| DGS2 | taux_nominal_2a | 4.76 | 2026-09-18 | 0 | 2496 | 9.98 ans | 100.0 | 88.1 | 94.0 |
| DGS30 | taux_nominal_30a | 5.34 | 2026-09-18 | 0 | 2496 | 9.98 ans | 98.4 | 99.7 | 99.8 |
| DTWEXBGS | dollar_large | 119.5 | 2026-09-18 | 0 | 2491 | 9.98 ans | 45.6 | 31.0 | 62.1 |
| INDPRO | activite_industrielle | 103.1 | 2026-08-01 | 48 | 120 | 9.91 ans | 100.0 | 100.0 | 92.5 |
| NASDAQ100 | prix_actions_tech | 2.964e+04 | 2026-09-18 | 0 | 2511 | 9.98 ans | 90.1 | 98.0 | 99.0 |
| OVXCLS | volatilite_implicite_petrole | 50.39 | 2026-09-18 | 0 | 2512 | 9.98 ans | 51.2 | 80.3 | 84.8 |
| PAYEMS | emploi | 1.591e+05 | 2026-08-01 | 48 | 120 | 9.91 ans | 100.0 | 100.0 | 100.0 |
| SP500 | prix_actions | 7650 | 2026-09-18 | 0 | 2510 | 9.98 ans | 90.5 | 98.1 | 99.0 |
| T10Y2Y | pente_courbe | 0.25 | 2026-09-18 | 0 | 2496 | 9.98 ans | 0.4 | 54.5 | 40.2 |
| T10YIE | point_mort_10a | 2.33 | 2026-09-18 | 0 | 2496 | 9.98 ans | 61.9 | 52.2 | 73.1 |
| T5YIFR | point_mort_5a5a | 2.35 | 2026-09-18 | 0 | 2496 | 9.98 ans | 100.0 | 83.8 | 91.6 |
| UNRATE | chomage | 4.1 | 2026-08-01 | 48 | 119 | 9.91 ans | 16.7 | 65.0 | 55.5 |
| VIXCLS | volatilite_implicite | 14.81 | 2026-09-18 | 0 | 2543 | 9.98 ans | 6.7 | 20.6 | 32.2 |
| VXDCLS | volatilite_implicite_dow | 14.03 | 2026-09-18 | 0 | 2513 | 9.98 ans | 17.1 | 25.6 | 31.6 |
| VXVCLS | volatilite_implicite_3m | 18.24 | 2026-09-18 | 0 | 2510 | 9.98 ans | 7.9 | 26.7 | 41.6 |

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
- corrélation des variations à 60 séances : BAMLC0A0CM / BAMLH0A0HYM2 = +0.941 sur 724 points (seuil 0.9)
- corrélation des variations à 60 séances : DGS10 / DGS30 = +0.967 sur 2436 points (seuil 0.9)
- corrélation des variations à 60 séances : INDPRO / PAYEMS = +0.913 sur 117 points (seuil 0.9)
- corrélation des variations à 60 séances : INDPRO / UNRATE = -0.917 sur 116 points (seuil 0.9)
- corrélation des variations à 60 séances : NASDAQ100 / SP500 = +0.902 sur 2450 points (seuil 0.9)
- corrélation des variations à 60 séances : PAYEMS / UNRATE = -0.983 sur 116 points (seuil 0.9)
- corrélation des variations à 60 séances : VIXCLS / VXDCLS = +0.930 sur 2450 points (seuil 0.9)
- corrélation des variations à 60 séances : VIXCLS / VXVCLS = +0.958 sur 2450 points (seuil 0.9)
- corrélation des variations à 60 séances : VXDCLS / VXVCLS = +0.934 sur 2450 points (seuil 0.9)

---

## 5. GRILLE, σ MESURÉ, ET DOUBLE CONFRONTATION DES PROBABILITÉS

σ est **mesuré** sur chaque série, jamais choisi. Les probabilités sont les **fréquences historiques** dans chaque bande, jamais un jugement. L'effectif de chaque bande est publié ; sous 20 observations la bande est déclarée NON ESTIMABLE. La colonne « emp./gauss. » est la double confrontation exigée par §11.5 : tout écart supérieur à un facteur 2 est déclaré (⚠).

**BAMLH0A0HYM2** (niveau) — σ à 60 pas = **0.45636** · estimateurs croisés : racine-h 0.53826, blocs disjoints 0.47312 (écart relatif 17.9 %) · dérive d'échantillon -0.11417 (-0.25 σ) · 725 variations chevauchantes, 12 blocs indépendants · 2023-09-22 → 2026-09-18

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.6845 | 55 | 1 | 0.0759 | 0.0668 | 1.14 | oui |
| -1.0 | -0.6845 | -0.3423 | 125 | 2 | 0.1724 | 0.1598 | 1.08 | oui |
| -0.5 | -0.3423 | -0.1141 | 193 | 3 | 0.2662 | 0.1747 | 1.52 | oui |
| +0.0 | -0.1141 | +0.1141 | 192 | 3 | 0.2648 | 0.1974 | 1.34 | oui |
| +0.5 | +0.1141 | +0.3423 | 80 | 1 | 0.1103 | 0.1747 | 0.63 | oui |
| +1.0 | +0.3423 | +0.6845 | 51 | 1 | 0.0703 | 0.1598 | 0.44 ⚠ | oui |
| +2.0 | +0.6845 | +∞ | 29 | 0 | 0.0400 | 0.0668 | 0.60 | oui |

**DCOILBRENTEU** (log) — σ à 60 pas = **0.24542** · estimateurs croisés : racine-h 0.24780, blocs disjoints 0.22521 (écart relatif 10.0 %) · dérive d'échantillon +0.01498 (+0.06 σ) · 2470 variations chevauchantes, 41 blocs indépendants · 2016-09-23 → 2026-09-15

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.3681 | 84 | 1 | 0.0340 | 0.0668 | 0.51 | oui |
| -1.0 | -0.3681 | -0.1841 | 156 | 3 | 0.0632 | 0.1598 | 0.40 ⚠ | oui |
| -0.5 | -0.1841 | -0.0614 | 502 | 8 | 0.2032 | 0.1747 | 1.16 | oui |
| +0.0 | -0.0614 | +0.0614 | 761 | 13 | 0.3081 | 0.1974 | 1.56 | oui |
| +0.5 | +0.0614 | +0.1841 | 617 | 10 | 0.2498 | 0.1747 | 1.43 | oui |
| +1.0 | +0.1841 | +0.3681 | 225 | 4 | 0.0911 | 0.1598 | 0.57 | oui |
| +2.0 | +0.3681 | +∞ | 125 | 2 | 0.0506 | 0.0668 | 0.76 | oui |

**DCOILWTICO** — non scénarisable : convention log inapplicable : 1 observation(s) non strictement positive(s), minimum -36.98 le 2020-04-20. Le prix a été négatif : aucun log-rendement n'existe. La série est déclarée NON SCÉNARISABLE plutôt que corrigée en silence.

**DEXJPUS** (log) — σ à 60 pas = **0.04285** · estimateurs croisés : racine-h 0.04391, blocs disjoints 0.04505 (écart relatif 5.1 %) · dérive d'échantillon +0.00971 (+0.23 σ) · 2433 variations chevauchantes, 41 blocs indépendants · 2016-09-23 → 2026-09-18

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0643 | 102 | 2 | 0.0419 | 0.0668 | 0.63 | oui |
| -1.0 | -0.0643 | -0.0321 | 236 | 4 | 0.0970 | 0.1598 | 0.61 | oui |
| -0.5 | -0.0321 | -0.0107 | 378 | 6 | 0.1554 | 0.1747 | 0.89 | oui |
| +0.0 | -0.0107 | +0.0107 | 508 | 8 | 0.2088 | 0.1974 | 1.06 | oui |
| +0.5 | +0.0107 | +0.0321 | 549 | 9 | 0.2256 | 0.1747 | 1.29 | oui |
| +1.0 | +0.0321 | +0.0643 | 469 | 8 | 0.1928 | 0.1598 | 1.21 | oui |
| +2.0 | +0.0643 | +∞ | 191 | 3 | 0.0785 | 0.0668 | 1.18 | oui |

**DEXUSEU** (log) — σ à 60 pas = **0.03460** · estimateurs croisés : racine-h 0.03466, blocs disjoints 0.03724 (écart relatif 7.6 %) · dérive d'échantillon +0.00144 (+0.04 σ) · 2433 variations chevauchantes, 41 blocs indépendants · 2016-09-23 → 2026-09-18

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0519 | 138 | 2 | 0.0567 | 0.0668 | 0.85 | oui |
| -1.0 | -0.0519 | -0.0259 | 319 | 5 | 0.1311 | 0.1598 | 0.82 | oui |
| -0.5 | -0.0259 | -0.0086 | 509 | 8 | 0.2092 | 0.1747 | 1.20 | oui |
| +0.0 | -0.0086 | +0.0086 | 613 | 10 | 0.2520 | 0.1974 | 1.28 | oui |
| +0.5 | +0.0086 | +0.0259 | 327 | 5 | 0.1344 | 0.1747 | 0.77 | oui |
| +1.0 | +0.0259 | +0.0519 | 306 | 5 | 0.1258 | 0.1598 | 0.79 | oui |
| +2.0 | +0.0519 | +∞ | 221 | 4 | 0.0908 | 0.0668 | 1.36 | oui |

**DGS10** (niveau) — σ à 60 pas = **0.42422** · estimateurs croisés : racine-h 0.41368, blocs disjoints 0.40017 (écart relatif 6.0 %) · dérive d'échantillon +0.06505 (+0.15 σ) · 2436 variations chevauchantes, 41 blocs indépendants · 2016-09-23 → 2026-09-18

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.6363 | 123 | 2 | 0.0505 | 0.0668 | 0.76 | oui |
| -1.0 | -0.6363 | -0.3182 | 284 | 5 | 0.1166 | 0.1598 | 0.73 | oui |
| -0.5 | -0.3182 | -0.1061 | 371 | 6 | 0.1523 | 0.1747 | 0.87 | oui |
| +0.0 | -0.1061 | +0.1061 | 528 | 9 | 0.2167 | 0.1974 | 1.10 | oui |
| +0.5 | +0.1061 | +0.3182 | 555 | 9 | 0.2278 | 0.1747 | 1.30 | oui |
| +1.0 | +0.3182 | +0.6363 | 367 | 6 | 0.1507 | 0.1598 | 0.94 | oui |
| +2.0 | +0.6363 | +∞ | 208 | 3 | 0.0854 | 0.0668 | 1.28 | oui |

**DGS2** (niveau) — σ à 60 pas = **0.49492** · estimateurs croisés : racine-h 0.42051, blocs disjoints 0.48658 (écart relatif 17.7 %) · dérive d'échantillon +0.08183 (+0.17 σ) · 2436 variations chevauchantes, 41 blocs indépendants · 2016-09-23 → 2026-09-18

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.7424 | 115 | 2 | 0.0472 | 0.0668 | 0.71 | oui |
| -1.0 | -0.7424 | -0.3712 | 228 | 4 | 0.0936 | 0.1598 | 0.59 | oui |
| -0.5 | -0.3712 | -0.1237 | 323 | 5 | 0.1326 | 0.1747 | 0.76 | oui |
| +0.0 | -0.1237 | +0.1237 | 739 | 12 | 0.3034 | 0.1974 | 1.54 | oui |
| +0.5 | +0.1237 | +0.3712 | 483 | 8 | 0.1983 | 0.1747 | 1.14 | oui |
| +1.0 | +0.3712 | +0.7424 | 350 | 6 | 0.1437 | 0.1598 | 0.90 | oui |
| +2.0 | +0.7424 | +∞ | 198 | 3 | 0.0813 | 0.0668 | 1.22 | oui |

**DGS30** (niveau) — σ à 60 pas = **0.36618** · estimateurs croisés : racine-h 0.39191, blocs disjoints 0.34637 (écart relatif 13.1 %) · dérive d'échantillon +0.05977 (+0.16 σ) · 2436 variations chevauchantes, 41 blocs indépendants · 2016-09-23 → 2026-09-18

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.5493 | 128 | 2 | 0.0525 | 0.0668 | 0.79 | oui |
| -1.0 | -0.5493 | -0.2746 | 276 | 5 | 0.1133 | 0.1598 | 0.71 | oui |
| -0.5 | -0.2746 | -0.0915 | 338 | 6 | 0.1388 | 0.1747 | 0.79 | oui |
| +0.0 | -0.0915 | +0.0915 | 629 | 10 | 0.2582 | 0.1974 | 1.31 | oui |
| +0.5 | +0.0915 | +0.2746 | 461 | 8 | 0.1892 | 0.1747 | 1.08 | oui |
| +1.0 | +0.2746 | +0.5493 | 392 | 7 | 0.1609 | 0.1598 | 1.01 | oui |
| +2.0 | +0.5493 | +∞ | 212 | 4 | 0.0870 | 0.0668 | 1.30 | oui |

**DTWEXBGS** (log) — σ à 60 pas = **0.02606** · estimateurs croisés : racine-h 0.02403, blocs disjoints 0.02739 (écart relatif 14.0 %) · dérive d'échantillon +0.00092 (+0.04 σ) · 2431 variations chevauchantes, 41 blocs indépendants · 2016-09-23 → 2026-09-18

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0391 | 159 | 3 | 0.0654 | 0.0668 | 0.98 | oui |
| -1.0 | -0.0391 | -0.0195 | 386 | 6 | 0.1588 | 0.1598 | 0.99 | oui |
| -0.5 | -0.0195 | -0.0065 | 358 | 6 | 0.1473 | 0.1747 | 0.84 | oui |
| +0.0 | -0.0065 | +0.0065 | 542 | 9 | 0.2230 | 0.1974 | 1.13 | oui |
| +0.5 | +0.0065 | +0.0195 | 465 | 8 | 0.1913 | 0.1747 | 1.10 | oui |
| +1.0 | +0.0195 | +0.0391 | 307 | 5 | 0.1263 | 0.1598 | 0.79 | oui |
| +2.0 | +0.0391 | +∞ | 214 | 4 | 0.0880 | 0.0668 | 1.32 | oui |

**NASDAQ100** (log) — σ à 60 pas = **0.08870** · estimateurs croisés : racine-h 0.11126, blocs disjoints 0.08092 (écart relatif 37.5 %) · dérive d'échantillon +0.04408 (+0.50 σ) · 2451 variations chevauchantes, 41 blocs indépendants · 2016-09-23 → 2026-09-18

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.1331 | 108 | 2 | 0.0441 | 0.0668 | 0.66 | oui |
| -1.0 | -0.1331 | -0.0665 | 167 | 3 | 0.0681 | 0.1598 | 0.43 ⚠ | oui |
| -0.5 | -0.0665 | -0.0222 | 186 | 3 | 0.0759 | 0.1747 | 0.43 ⚠ | oui |
| +0.0 | -0.0222 | +0.0222 | 362 | 6 | 0.1477 | 0.1974 | 0.75 | oui |
| +0.5 | +0.0222 | +0.0665 | 581 | 10 | 0.2370 | 0.1747 | 1.36 | oui |
| +1.0 | +0.0665 | +0.1331 | 731 | 12 | 0.2982 | 0.1598 | 1.87 | oui |
| +2.0 | +0.1331 | +∞ | 316 | 5 | 0.1289 | 0.0668 | 1.93 | oui |

**SP500** (log) — σ à 60 pas = **0.06916** · estimateurs croisés : racine-h 0.08845, blocs disjoints 0.06396 (écart relatif 38.3 %) · dérive d'échantillon +0.03066 (+0.44 σ) · 2450 variations chevauchantes, 41 blocs indépendants · 2016-09-23 → 2026-09-18

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.1037 | 115 | 2 | 0.0469 | 0.0668 | 0.70 | oui |
| -1.0 | -0.1037 | -0.0519 | 158 | 3 | 0.0645 | 0.1598 | 0.40 ⚠ | oui |
| -0.5 | -0.0519 | -0.0173 | 176 | 3 | 0.0718 | 0.1747 | 0.41 ⚠ | oui |
| +0.0 | -0.0173 | +0.0173 | 293 | 5 | 0.1196 | 0.1974 | 0.61 | oui |
| +0.5 | +0.0173 | +0.0519 | 746 | 12 | 0.3045 | 0.1747 | 1.74 | oui |
| +1.0 | +0.0519 | +0.1037 | 752 | 13 | 0.3069 | 0.1598 | 1.92 | oui |
| +2.0 | +0.1037 | +∞ | 210 | 4 | 0.0857 | 0.0668 | 1.28 | oui |

**VIXCLS** (log) — σ à 60 pas = **0.34684** · estimateurs croisés : racine-h 0.61320, blocs disjoints 0.30886 (écart relatif 98.5 %) · dérive d'échantillon +0.00318 (+0.01 σ) · 2483 variations chevauchantes, 41 blocs indépendants · 2016-09-23 → 2026-09-18

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.5203 | 77 | 1 | 0.0310 | 0.0668 | 0.46 ⚠ | oui |
| -1.0 | -0.5203 | -0.2601 | 388 | 6 | 0.1563 | 0.1598 | 0.98 | oui |
| -0.5 | -0.2601 | -0.0867 | 605 | 10 | 0.2437 | 0.1747 | 1.39 | oui |
| +0.0 | -0.0867 | +0.0867 | 614 | 10 | 0.2473 | 0.1974 | 1.25 | oui |
| +0.5 | +0.0867 | +0.2601 | 373 | 6 | 0.1502 | 0.1747 | 0.86 | oui |
| +1.0 | +0.2601 | +0.5203 | 249 | 4 | 0.1003 | 0.1598 | 0.63 | oui |
| +2.0 | +0.5203 | +∞ | 177 | 3 | 0.0713 | 0.0668 | 1.07 | oui |

---

## 6. TEST D'ASYMÉTRIE — DÉFINITION UNIQUE (R-030), L'ESPÉRANCE DÉCIDE

> Test d'admission : **espérance calculée sur la grille symétrique complète, les deux queues incluses**. Le rapport gain maximal / perte maximale est publié **pour information** et ne peut fonder aucune admission seul (T-001, faute E-018). Le rapport gain maximal / perte du scénario central est **interdit**. Une seule formulation, appliquée à tous les candidats, position détenue comprise.

| candidat | verdict | espérance % NAV | sans dérive | 1re moitié | 2e moitié | gain max | perte max | ratio (info) | critères échoués |
|---|:---:|---:|---:|---:|---:|---:|---:|---:|---|
| M005-DCOILBRENTEU-HAUSSE-ALIGNE | REFUSEE | +0.243 | +0.122 | +0.259 | +0.093 | +5.00 | -3.18 | 1.57:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DCOILBRENTEU-HAUSSE-CONTRARIEN | REFUSEE | +0.243 | +0.122 | +0.259 | +0.093 | +5.00 | -3.18 | 1.57:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DCOILBRENTEU-BAISSE-ALIGNE | REFUSEE | -0.243 | -0.122 | -0.259 | -0.093 | +3.18 | -5.00 | 0.64:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILBRENTEU-BAISSE-CONTRARIEN | REFUSEE | -0.243 | -0.122 | -0.259 | -0.093 | +3.18 | -5.00 | 0.64:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-HAUSSE-ALIGNE | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-HAUSSE-CONTRARIEN | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-BAISSE-ALIGNE | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-BAISSE-CONTRARIEN | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-HAUSSE-ALIGNE | REFUSEE | +0.002 | -0.067 | -0.066 | +0.047 | +0.64 | -0.73 | 0.88:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-HAUSSE-CONTRARIEN | REFUSEE | +0.002 | -0.067 | -0.066 | +0.047 | +0.64 | -0.73 | 0.88:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-BAISSE-ALIGNE | REFUSEE | -0.002 | +0.067 | +0.066 | -0.047 | +0.73 | -0.64 | 1.14:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-BAISSE-CONTRARIEN | REFUSEE | -0.002 | +0.067 | +0.066 | -0.047 | +0.73 | -0.64 | 1.14:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-HAUSSE-ALIGNE | REFUSEE | -0.062 | -0.074 | -0.035 | -0.073 | +0.50 | -0.61 | 0.82:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-HAUSSE-CONTRARIEN | REFUSEE | -0.062 | -0.074 | -0.035 | -0.073 | +0.50 | -0.61 | 0.82:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-BAISSE-ALIGNE | REFUSEE | +0.062 | +0.074 | +0.035 | +0.073 | +0.61 | -0.50 | 1.22:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DEXUSEU-BAISSE-CONTRARIEN | REFUSEE | +0.062 | +0.074 | +0.035 | +0.073 | +0.61 | -0.50 | 1.22:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DGS10-HAUSSE-ALIGNE | REFUSEE | +0.011 | -0.025 | -0.043 | +0.057 | +0.49 | -0.57 | 0.85:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-HAUSSE-CONTRARIEN | REFUSEE | +0.011 | -0.025 | -0.043 | +0.057 | +0.49 | -0.57 | 0.85:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-BAISSE-ALIGNE | REFUSEE | -0.011 | +0.025 | +0.043 | -0.057 | +0.57 | -0.49 | 1.18:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-BAISSE-CONTRARIEN | REFUSEE | -0.011 | +0.025 | +0.043 | -0.057 | +0.57 | -0.49 | 1.18:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-HAUSSE-ALIGNE | REFUSEE | -0.006 | -0.016 | -0.021 | +0.006 | +0.13 | -0.17 | 0.78:1 | 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-HAUSSE-CONTRARIEN | REFUSEE | -0.006 | -0.016 | -0.021 | +0.006 | +0.13 | -0.17 | 0.78:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-BAISSE-ALIGNE | REFUSEE | +0.006 | +0.016 | +0.021 | -0.006 | +0.17 | -0.13 | 1.28:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-BAISSE-CONTRARIEN | REFUSEE | +0.006 | +0.016 | +0.021 | -0.006 | +0.17 | -0.13 | 1.28:1 | 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-HAUSSE-ALIGNE | REFUSEE | +0.018 | -0.039 | -0.089 | +0.124 | +0.78 | -0.98 | 0.80:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-HAUSSE-CONTRARIEN | REFUSEE | +0.018 | -0.039 | -0.089 | +0.124 | +0.78 | -0.98 | 0.80:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-BAISSE-ALIGNE | REFUSEE | -0.018 | +0.039 | +0.089 | -0.124 | +0.98 | -0.78 | 1.26:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-BAISSE-CONTRARIEN | REFUSEE | -0.018 | +0.039 | +0.089 | -0.124 | +0.98 | -0.78 | 1.26:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-HAUSSE-ALIGNE | REFUSEE | -0.064 | -0.072 | -0.078 | -0.052 | +0.35 | -0.48 | 0.74:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-HAUSSE-CONTRARIEN | REFUSEE | -0.064 | -0.072 | -0.078 | -0.052 | +0.35 | -0.48 | 0.74:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-BAISSE-ALIGNE | REFUSEE | +0.064 | +0.072 | +0.078 | +0.052 | +0.48 | -0.35 | 1.36:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DTWEXBGS-BAISSE-CONTRARIEN | REFUSEE | +0.064 | +0.072 | +0.078 | +0.052 | +0.48 | -0.35 | 1.36:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-HAUSSE-ALIGNE | REFUSEE | +0.304 | -0.035 | +0.452 | +0.185 | +1.48 | -1.37 | 1.08:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-HAUSSE-CONTRARIEN | REFUSEE | +0.304 | -0.035 | +0.452 | +0.185 | +1.48 | -1.37 | 1.08:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-BAISSE-ALIGNE | REFUSEE | -0.304 | +0.035 | -0.452 | -0.185 | +1.37 | -1.48 | 0.93:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-NASDAQ100-BAISSE-CONTRARIEN | REFUSEE | -0.304 | +0.035 | -0.452 | -0.185 | +1.37 | -1.48 | 0.93:1 | 12_esperance_positive, 13_esperance_non_portee_par_derive, 14_esperance_stable_dans_le_temps |
| M005-SP500-HAUSSE-ALIGNE | REFUSEE | +0.187 | -0.044 | +0.218 | +0.155 | +1.11 | -1.11 | 1.00:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-SP500-HAUSSE-CONTRARIEN | REFUSEE | +0.187 | -0.044 | +0.218 | +0.155 | +1.11 | -1.11 | 1.00:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-SP500-BAISSE-ALIGNE | REFUSEE | -0.187 | +0.044 | -0.218 | -0.155 | +1.11 | -1.11 | 1.00:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-SP500-BAISSE-CONTRARIEN | REFUSEE | -0.187 | +0.044 | -0.218 | -0.155 | +1.11 | -1.11 | 1.00:1 | 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |

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

- `BAMLC0A0CM` : percentile REFUSÉ sur 5 ans — profondeur réelle 784 obs / 2.99 ans (début 2023-09-22). R-011 : un percentile calculé sur une série tronquée est sans valeur.
- `BAMLH0A0HYM2` : percentile REFUSÉ sur 5 ans — profondeur réelle 785 obs / 2.99 ans (début 2023-09-22). R-011 : un percentile calculé sur une série tronquée est sans valeur.
- `BAMLH0A0HYM2` : instrument NON ADMISSIBLE — P&L non calculable depuis le dépôt : l'OAS est un spread, et le dépôt ne contient pas le rendement de l'indice, donc pas la duration de spread. Aucune valeur ne peut être produite sans un chiffre extérieur aux données (E-002).
- `BAMLC0A0CM` : instrument NON ADMISSIBLE — P&L non calculable depuis le dépôt : l'OAS est un spread, et le dépôt ne contient pas le rendement de l'indice, donc pas la duration de spread. Aucune valeur ne peut être produite sans un chiffre extérieur aux données (E-002).
- Retards sur la date d'arrêté unique (E-014) : DCOILBRENTEU 3 séance(s), DCOILWTICO 3 séance(s)

**Vérification tierce (R-032) : NON SATISFAITE pour ce brief.** Le moteur ne dispose d'aucune source extérieure au dépôt. Trois estimateurs **internes** de σ sont publiés côte à côte au §5 ; ce sont des contrôles de cohérence interne, **pas** une vérification tierce, et ils ne sont pas présentés comme telle.

**Ce que ce moteur ne peut pas faire.** Il ne prouve aucune capacité prédictive : la règle de confirmation est une règle de percentile, déclarée et symétrique, pas un modèle validé hors échantillon. Il ne corrige pas la multiplicité : 40 candidats sont évalués et aucune pénalité de sélection n'est appliquée à l'espérance — c'est une limite déclarée, pas un oubli. Il ne voit ni les événements politiques, ni les décisions de banques centrales : le dépôt ne contient que des séries FRED, et toute affirmation de politique monétaire non adossée à `DFF` est refusée (critère 15, faute E-006).

---

*Fin du brief 005. Produit mécaniquement. Ne constitue pas un conseil en investissement.*