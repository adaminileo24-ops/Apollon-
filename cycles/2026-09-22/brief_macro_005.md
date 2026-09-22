# BRIEF MACRO n° 005 — arrêté au 2026-09-18

*Produit par `apollon_macro.py` le 2026-09-22T09:57:33+00:00. Aucune valeur de ce document n'est saisie à la main : chacune porte sa série, sa date et sa profondeur. Bloc à copier tel quel.*

**Grille de scénarios (R-029, §11), déclarée avant toute lecture de données et empreintée :** `[-2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0]` · empreinte SHA-256 `6aaeb3863c875923…` · symétrique : True · horizon 60 séances (3 mois pour les séries mensuelles).

---

## 1. CONCLUSION, ÉNONCÉE D'ABORD

**40 candidats déclarés d'avance (10 instruments × 2 directions × 2 règles de confirmation). 40 évalués. 0 thèse(s) survivent aux quinze critères.**

**Abstention. Aucune thèse ne survit.** Ce n'est pas un silence : c'est un résultat, produit par le même portier que celui qui aurait admis une thèse. Le détail des échecs, critère par critère, figure au §6. La Section Macro ne transmet rien à la Section Risque ce cycle.

**Position détenue (contrôle 9, E-020) — 100 % cash, testée sur la même grille.** Espérance excédentaire du cash : +0.000 % de NAV. Référence 60/40 : +1.347 % (hors dérive : -0.200 %). **Écart du cash contre la référence : -1.347 % de NAV** sur 60 séances.

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
| DCOILBRENTEU | prix_energie | 130.8 | 2026-09-15 | 3 | 2529 | 9.97 ans | 99.6 | 99.8 | 99.9 |
| DCOILWTICO | prix_energie_wti | 107 | 2026-09-15 | 3 | 2493 | 9.97 ans | 96.4 | 95.3 | 97.6 |
| DEXJPUS | devise_usdjpy | 156.9 | 2026-09-18 | 0 | 2492 | 9.98 ans | 43.7 | 84.8 | 92.3 |
| DEXUSEU | devise_eurusd | 1.146 | 2026-09-18 | 0 | 2492 | 9.98 ans | 11.9 | 73.2 | 62.4 |
| DFF | politique_monetaire | 3.88 | 2026-09-18 | 0 | 3647 | 9.98 ans | 100.0 | 24.7 | 70.9 |
| DFII10 | taux_reel_10a | 2.68 | 2026-09-18 | 0 | 2495 | 9.98 ans | 100.0 | 100.0 | 100.0 |
| DGS10 | taux_nominal_10a | 5.01 | 2026-09-18 | 0 | 2495 | 9.98 ans | 100.0 | 100.0 | 100.0 |
| DGS2 | taux_nominal_2a | 4.76 | 2026-09-18 | 0 | 2495 | 9.98 ans | 100.0 | 88.1 | 94.0 |
| DGS30 | taux_nominal_30a | 5.34 | 2026-09-18 | 0 | 2495 | 9.98 ans | 98.4 | 99.7 | 99.8 |
| DTWEXBGS | dollar_large | 119.5 | 2026-09-18 | 0 | 2490 | 9.98 ans | 45.6 | 31.0 | 62.1 |
| INDPRO | activite_industrielle | 103.1 | 2026-08-01 | 48 | 120 | 9.91 ans | 100.0 | 100.0 | 92.5 |
| NASDAQ100 | prix_actions_tech | 2.964e+04 | 2026-09-18 | 0 | 2510 | 9.98 ans | 90.1 | 98.0 | 99.0 |
| OVXCLS | volatilite_implicite_petrole | 50.39 | 2026-09-18 | 0 | 2511 | 9.98 ans | 51.2 | 80.3 | 84.8 |
| PAYEMS | emploi | 1.591e+05 | 2026-08-01 | 48 | 120 | 9.91 ans | 100.0 | 100.0 | 100.0 |
| SP500 | prix_actions | 7650 | 2026-09-18 | 0 | 2509 | 9.98 ans | 90.5 | 98.1 | 99.0 |
| T10Y2Y | pente_courbe | 0.25 | 2026-09-18 | 0 | 2495 | 9.98 ans | 0.4 | 54.5 | 40.2 |
| T10YIE | point_mort_10a | 2.33 | 2026-09-18 | 0 | 2495 | 9.98 ans | 61.9 | 52.2 | 73.1 |
| T5YIFR | point_mort_5a5a | 2.35 | 2026-09-18 | 0 | 2495 | 9.98 ans | 100.0 | 83.8 | 91.6 |
| UNRATE | chomage | 4.1 | 2026-08-01 | 48 | 119 | 9.91 ans | 16.7 | 65.0 | 55.5 |
| VIXCLS | volatilite_implicite | 14.81 | 2026-09-18 | 0 | 2542 | 9.98 ans | 6.7 | 20.6 | 32.1 |
| VXDCLS | volatilite_implicite_dow | 14.03 | 2026-09-18 | 0 | 2512 | 9.98 ans | 17.1 | 25.6 | 31.5 |
| VXVCLS | volatilite_implicite_3m | 18.24 | 2026-09-18 | 0 | 2509 | 9.98 ans | 7.9 | 26.7 | 41.5 |

**Couples obligatoires contrôlés :** CPIAUCSL/CPILFESL, DGS10/DFII10, DGS10/T10YIE, BAMLH0A0HYM2/BAMLC0A0CM, UNRATE/PAYEMS, VIXCLS/SP500 — 0 manquement(s).

**Inflation en trois chiffres (contrôle 2, E-005).** Global +3.71 % sur un an (CPIAUCSL, 2026-08-01) · sous-jacent +2.76 % (CPILFESL) · **écart hors sous-jacent +95 pb**. Contribution énergie NON publiée : `CPIENGSL` est absente du dépôt. Lacune nommée avec le code FRED qui la comble (R-028) ; elle n'est pas présentée comme une limite de méthode. L'écart ci-dessus est l'écart global/sous-jacent, pas la contribution énergie.

---

## 4. IDENTITÉS COMPTABLES ET REDONDANCES (vérifiées numériquement)

| identité | vérifiable | n dates | résidu absolu max | tolérance | vérifiée |
|---|:---:|---:|---:|---:|:---:|
| T10YIE = DGS10 - DFII10 | oui | 2495 | 0.0000 | 0.02 | OUI |
| T10Y2Y = DGS10 - DGS2 | oui | 2495 | 0.0000 | 0.02 | OUI |

**Redondances détectées (11) — deux séries liées ne comptent jamais pour deux confirmations indépendantes :**

- identité comptable : T10YIE = DGS10 - DFII10 — T10YIE, DGS10, DFII10 (résidu max 0.0000)
- identité comptable : T10Y2Y = DGS10 - DGS2 — T10Y2Y, DGS10, DGS2 (résidu max 0.0000)
- corrélation des variations à 60 séances : BAMLC0A0CM / BAMLH0A0HYM2 = +0.941 sur 724 points (seuil 0.9)
- corrélation des variations à 60 séances : DGS10 / DGS30 = +0.967 sur 2435 points (seuil 0.9)
- corrélation des variations à 60 séances : INDPRO / PAYEMS = +0.913 sur 117 points (seuil 0.9)
- corrélation des variations à 60 séances : INDPRO / UNRATE = -0.917 sur 116 points (seuil 0.9)
- corrélation des variations à 60 séances : NASDAQ100 / SP500 = +0.902 sur 2449 points (seuil 0.9)
- corrélation des variations à 60 séances : PAYEMS / UNRATE = -0.983 sur 116 points (seuil 0.9)
- corrélation des variations à 60 séances : VIXCLS / VXDCLS = +0.930 sur 2449 points (seuil 0.9)
- corrélation des variations à 60 séances : VIXCLS / VXVCLS = +0.958 sur 2449 points (seuil 0.9)
- corrélation des variations à 60 séances : VXDCLS / VXVCLS = +0.934 sur 2449 points (seuil 0.9)

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

**DCOILBRENTEU** (log) — σ à 60 pas = **0.24546** · estimateurs croisés : racine-h 0.24785, blocs disjoints 0.23947 (écart relatif 3.5 %) · dérive d'échantillon +0.01493 (+0.06 σ) · 2469 variations chevauchantes, 41 blocs indépendants · 2016-09-26 → 2026-09-15

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.3682 | 84 | 1 | 0.0340 | 0.0668 | 0.51 | oui |
| -1.0 | -0.3682 | -0.1841 | 156 | 3 | 0.0632 | 0.1598 | 0.40 ⚠ | oui |
| -0.5 | -0.1841 | -0.0614 | 502 | 8 | 0.2033 | 0.1747 | 1.16 | oui |
| +0.0 | -0.0614 | +0.0614 | 761 | 13 | 0.3082 | 0.1974 | 1.56 | oui |
| +0.5 | +0.0614 | +0.1841 | 616 | 10 | 0.2495 | 0.1747 | 1.43 | oui |
| +1.0 | +0.1841 | +0.3682 | 225 | 4 | 0.0911 | 0.1598 | 0.57 | oui |
| +2.0 | +0.3682 | +∞ | 125 | 2 | 0.0506 | 0.0668 | 0.76 | oui |

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

**DGS10** (niveau) — σ à 60 pas = **0.42394** · estimateurs croisés : racine-h 0.41374, blocs disjoints 0.41632 (écart relatif 2.5 %) · dérive d'échantillon +0.06470 (+0.15 σ) · 2435 variations chevauchantes, 41 blocs indépendants · 2016-09-26 → 2026-09-18

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.6359 | 123 | 2 | 0.0505 | 0.0668 | 0.76 | oui |
| -1.0 | -0.6359 | -0.3180 | 284 | 5 | 0.1166 | 0.1598 | 0.73 | oui |
| -0.5 | -0.3180 | -0.1060 | 371 | 6 | 0.1524 | 0.1747 | 0.87 | oui |
| +0.0 | -0.1060 | +0.1060 | 528 | 9 | 0.2168 | 0.1974 | 1.10 | oui |
| +0.5 | +0.1060 | +0.3180 | 555 | 9 | 0.2279 | 0.1747 | 1.30 | oui |
| +1.0 | +0.3180 | +0.6359 | 367 | 6 | 0.1507 | 0.1598 | 0.94 | oui |
| +2.0 | +0.6359 | +∞ | 207 | 3 | 0.0850 | 0.0668 | 1.27 | oui |

**DGS2** (niveau) — σ à 60 pas = **0.49497** · estimateurs croisés : racine-h 0.42059, blocs disjoints 0.50571 (écart relatif 20.2 %) · dérive d'échantillon +0.08168 (+0.17 σ) · 2435 variations chevauchantes, 41 blocs indépendants · 2016-09-26 → 2026-09-18

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.7425 | 115 | 2 | 0.0472 | 0.0668 | 0.71 | oui |
| -1.0 | -0.7425 | -0.3712 | 228 | 4 | 0.0936 | 0.1598 | 0.59 | oui |
| -0.5 | -0.3712 | -0.1237 | 323 | 5 | 0.1326 | 0.1747 | 0.76 | oui |
| +0.0 | -0.1237 | +0.1237 | 739 | 12 | 0.3035 | 0.1974 | 1.54 | oui |
| +0.5 | +0.1237 | +0.3712 | 483 | 8 | 0.1984 | 0.1747 | 1.14 | oui |
| +1.0 | +0.3712 | +0.7425 | 349 | 6 | 0.1433 | 0.1598 | 0.90 | oui |
| +2.0 | +0.7425 | +∞ | 198 | 3 | 0.0813 | 0.0668 | 1.22 | oui |

**DGS30** (niveau) — σ à 60 pas = **0.36596** · estimateurs croisés : racine-h 0.39198, blocs disjoints 0.35585 (écart relatif 10.2 %) · dérive d'échantillon +0.05948 (+0.16 σ) · 2435 variations chevauchantes, 41 blocs indépendants · 2016-09-26 → 2026-09-18

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.5489 | 128 | 2 | 0.0526 | 0.0668 | 0.79 | oui |
| -1.0 | -0.5489 | -0.2745 | 276 | 5 | 0.1133 | 0.1598 | 0.71 | oui |
| -0.5 | -0.2745 | -0.0915 | 338 | 6 | 0.1388 | 0.1747 | 0.79 | oui |
| +0.0 | -0.0915 | +0.0915 | 629 | 10 | 0.2583 | 0.1974 | 1.31 | oui |
| +0.5 | +0.0915 | +0.2745 | 461 | 8 | 0.1893 | 0.1747 | 1.08 | oui |
| +1.0 | +0.2745 | +0.5489 | 392 | 7 | 0.1610 | 0.1598 | 1.01 | oui |
| +2.0 | +0.5489 | +∞ | 211 | 4 | 0.0867 | 0.0668 | 1.30 | oui |

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

**NASDAQ100** (log) — σ à 60 pas = **0.08872** · estimateurs croisés : racine-h 0.11127, blocs disjoints 0.08263 (écart relatif 34.7 %) · dérive d'échantillon +0.04409 (+0.50 σ) · 2450 variations chevauchantes, 41 blocs indépendants · 2016-09-26 → 2026-09-18

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.1331 | 108 | 2 | 0.0441 | 0.0668 | 0.66 | oui |
| -1.0 | -0.1331 | -0.0665 | 167 | 3 | 0.0682 | 0.1598 | 0.43 ⚠ | oui |
| -0.5 | -0.0665 | -0.0222 | 186 | 3 | 0.0759 | 0.1747 | 0.43 ⚠ | oui |
| +0.0 | -0.0222 | +0.0222 | 361 | 6 | 0.1473 | 0.1974 | 0.75 | oui |
| +0.5 | +0.0222 | +0.0665 | 581 | 10 | 0.2371 | 0.1747 | 1.36 | oui |
| +1.0 | +0.0665 | +0.1331 | 731 | 12 | 0.2984 | 0.1598 | 1.87 | oui |
| +2.0 | +0.1331 | +∞ | 316 | 5 | 0.1290 | 0.0668 | 1.93 | oui |

**SP500** (log) — σ à 60 pas = **0.06917** · estimateurs croisés : racine-h 0.08845, blocs disjoints 0.06115 (écart relatif 44.7 %) · dérive d'échantillon +0.03065 (+0.44 σ) · 2449 variations chevauchantes, 41 blocs indépendants · 2016-09-26 → 2026-09-18

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.1038 | 115 | 2 | 0.0470 | 0.0668 | 0.70 | oui |
| -1.0 | -0.1038 | -0.0519 | 158 | 3 | 0.0645 | 0.1598 | 0.40 ⚠ | oui |
| -0.5 | -0.0519 | -0.0173 | 176 | 3 | 0.0719 | 0.1747 | 0.41 ⚠ | oui |
| +0.0 | -0.0173 | +0.0173 | 293 | 5 | 0.1196 | 0.1974 | 0.61 | oui |
| +0.5 | +0.0173 | +0.0519 | 745 | 12 | 0.3042 | 0.1747 | 1.74 | oui |
| +1.0 | +0.0519 | +0.1038 | 752 | 13 | 0.3071 | 0.1598 | 1.92 | oui |
| +2.0 | +0.1038 | +∞ | 210 | 4 | 0.0857 | 0.0668 | 1.28 | oui |

**VIXCLS** (log) — σ à 60 pas = **0.34690** · estimateurs croisés : racine-h 0.61279, blocs disjoints 0.27119 (écart relatif 126.0 %) · dérive d'échantillon +0.00320 (+0.01 σ) · 2482 variations chevauchantes, 41 blocs indépendants · 2016-09-26 → 2026-09-18

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.5204 | 77 | 1 | 0.0310 | 0.0668 | 0.46 ⚠ | oui |
| -1.0 | -0.5204 | -0.2602 | 388 | 6 | 0.1563 | 0.1598 | 0.98 | oui |
| -0.5 | -0.2602 | -0.0867 | 605 | 10 | 0.2438 | 0.1747 | 1.40 | oui |
| +0.0 | -0.0867 | +0.0867 | 614 | 10 | 0.2474 | 0.1974 | 1.25 | oui |
| +0.5 | +0.0867 | +0.2602 | 373 | 6 | 0.1503 | 0.1747 | 0.86 | oui |
| +1.0 | +0.2602 | +0.5204 | 248 | 4 | 0.0999 | 0.1598 | 0.63 | oui |
| +2.0 | +0.5204 | +∞ | 177 | 3 | 0.0713 | 0.0668 | 1.07 | oui |

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
| M005-DEXJPUS-HAUSSE-ALIGNE | REFUSEE | +0.002 | -0.067 | -0.067 | +0.047 | +0.64 | -0.73 | 0.88:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-HAUSSE-CONTRARIEN | REFUSEE | +0.002 | -0.067 | -0.067 | +0.047 | +0.64 | -0.73 | 0.88:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-BAISSE-ALIGNE | REFUSEE | -0.002 | +0.067 | +0.067 | -0.047 | +0.73 | -0.64 | 1.14:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-BAISSE-CONTRARIEN | REFUSEE | -0.002 | +0.067 | +0.067 | -0.047 | +0.73 | -0.64 | 1.14:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-HAUSSE-ALIGNE | REFUSEE | -0.062 | -0.075 | -0.036 | -0.073 | +0.50 | -0.61 | 0.82:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-HAUSSE-CONTRARIEN | REFUSEE | -0.062 | -0.075 | -0.036 | -0.073 | +0.50 | -0.61 | 0.82:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-BAISSE-ALIGNE | REFUSEE | +0.062 | +0.075 | +0.036 | +0.073 | +0.61 | -0.50 | 1.22:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DEXUSEU-BAISSE-CONTRARIEN | REFUSEE | +0.062 | +0.075 | +0.036 | +0.073 | +0.61 | -0.50 | 1.22:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DGS10-HAUSSE-ALIGNE | REFUSEE | +0.011 | -0.025 | -0.044 | +0.057 | +0.49 | -0.57 | 0.85:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-HAUSSE-CONTRARIEN | REFUSEE | +0.011 | -0.025 | -0.044 | +0.057 | +0.49 | -0.57 | 0.85:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-BAISSE-ALIGNE | REFUSEE | -0.011 | +0.025 | +0.044 | -0.057 | +0.57 | -0.49 | 1.18:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-BAISSE-CONTRARIEN | REFUSEE | -0.011 | +0.025 | +0.044 | -0.057 | +0.57 | -0.49 | 1.18:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-HAUSSE-ALIGNE | REFUSEE | -0.006 | -0.016 | -0.021 | +0.006 | +0.13 | -0.17 | 0.78:1 | 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-HAUSSE-CONTRARIEN | REFUSEE | -0.006 | -0.016 | -0.021 | +0.006 | +0.13 | -0.17 | 0.78:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-BAISSE-ALIGNE | REFUSEE | +0.006 | +0.016 | +0.021 | -0.006 | +0.17 | -0.13 | 1.28:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-BAISSE-CONTRARIEN | REFUSEE | +0.006 | +0.016 | +0.021 | -0.006 | +0.17 | -0.13 | 1.28:1 | 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-HAUSSE-ALIGNE | REFUSEE | +0.018 | -0.040 | -0.090 | +0.124 | +0.78 | -0.97 | 0.80:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-HAUSSE-CONTRARIEN | REFUSEE | +0.018 | -0.040 | -0.090 | +0.124 | +0.78 | -0.97 | 0.80:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-BAISSE-ALIGNE | REFUSEE | -0.018 | +0.040 | +0.090 | -0.124 | +0.97 | -0.78 | 1.26:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-BAISSE-CONTRARIEN | REFUSEE | -0.018 | +0.040 | +0.090 | -0.124 | +0.97 | -0.78 | 1.26:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-HAUSSE-ALIGNE | REFUSEE | -0.064 | -0.072 | -0.079 | -0.052 | +0.35 | -0.48 | 0.74:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-HAUSSE-CONTRARIEN | REFUSEE | -0.064 | -0.072 | -0.079 | -0.052 | +0.35 | -0.48 | 0.74:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-BAISSE-ALIGNE | REFUSEE | +0.064 | +0.072 | +0.079 | +0.052 | +0.48 | -0.35 | 1.36:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DTWEXBGS-BAISSE-CONTRARIEN | REFUSEE | +0.064 | +0.072 | +0.079 | +0.052 | +0.48 | -0.35 | 1.36:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-HAUSSE-ALIGNE | REFUSEE | +0.304 | -0.035 | +0.452 | +0.185 | +1.48 | -1.37 | 1.08:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-HAUSSE-CONTRARIEN | REFUSEE | +0.304 | -0.035 | +0.452 | +0.185 | +1.48 | -1.37 | 1.08:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-BAISSE-ALIGNE | REFUSEE | -0.304 | +0.035 | -0.452 | -0.185 | +1.37 | -1.48 | 0.93:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-NASDAQ100-BAISSE-CONTRARIEN | REFUSEE | -0.304 | +0.035 | -0.452 | -0.185 | +1.37 | -1.48 | 0.93:1 | 12_esperance_positive, 13_esperance_non_portee_par_derive, 14_esperance_stable_dans_le_temps |
| M005-SP500-HAUSSE-ALIGNE | REFUSEE | +0.187 | -0.044 | +0.219 | +0.155 | +1.11 | -1.11 | 1.01:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-SP500-HAUSSE-CONTRARIEN | REFUSEE | +0.187 | -0.044 | +0.219 | +0.155 | +1.11 | -1.11 | 1.01:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-SP500-BAISSE-ALIGNE | REFUSEE | -0.187 | +0.044 | -0.219 | -0.155 | +1.11 | -1.11 | 1.00:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-SP500-BAISSE-CONTRARIEN | REFUSEE | -0.187 | +0.044 | -0.219 | -0.155 | +1.11 | -1.11 | 1.00:1 | 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |

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