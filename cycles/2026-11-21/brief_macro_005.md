# BRIEF MACRO n° 005 — arrêté au 2026-11-19

*Produit par `apollon_macro.py` le 2026-11-21T00:57:40+00:00. Aucune valeur de ce document n'est saisie à la main : chacune porte sa série, sa date et sa profondeur. Bloc à copier tel quel.*

**Grille de scénarios (R-029, §11), déclarée avant toute lecture de données et empreintée :** `[-2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0]` · empreinte SHA-256 `6aaeb3863c875923…` · symétrique : True · horizon 60 séances (3 mois pour les séries mensuelles).

---

## 1. CONCLUSION, ÉNONCÉE D'ABORD

**40 candidats déclarés d'avance (10 instruments × 2 directions × 2 règles de confirmation). 40 évalués. 0 thèse(s) survivent aux quinze critères.**

**Abstention. Aucune thèse ne survit.** Ce n'est pas un silence : c'est un résultat, produit par le même portier que celui qui aurait admis une thèse. Le détail des échecs, critère par critère, figure au §6. La Section Macro ne transmet rien à la Section Risque ce cycle.

**Position détenue (contrôle 9, E-020) — 100 % cash, testée sur la même grille.** Espérance excédentaire du cash : +0.000 % de NAV. Référence 60/40 : +1.297 % (hors dérive : -0.204 %). **Écart du cash contre la référence : -1.297 % de NAV** sur 60 séances.

---

## 2. CE QUI A CHANGÉ — MÉCANISME, PAS CONTENU

Fait, étiqueté : les briefs 001 à 004 étaient rédigés par un agent. Celui-ci est produit par un moteur. Le paramètre libre de la Section Macro — la grille de scénarios — n'est plus accessible à l'agent : il est déclaré en tête de fichier, symétrique par construction, et son empreinte SHA-256 est vérifiée avant chaque usage. Sur le brief 004, ce paramètre avait porté le ratio annoncé de 1,29:1 à 3,0:1.

---

## 3. M1 · M2 · M3 · M4 — ÉTAT DES SÉRIES (FAIT)

Toutes les valeurs sont des FAITS lus dans le dépôt. Le retard est compté en séances ouvrées depuis la date d'arrêté unique. Les couples obligatoires sont vérifiés par le rendu : ce bloc ne peut pas être émis si un membre d'un couple manque.

| série | rôle déclaré | valeur | date | retard | n obs | profondeur | pct 1 an | pct 5 ans | pct complet |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| BAMLC0A0CM | risque_credit_ig | 0.94 | 2026-11-19 | 0 | 785 | 3.00 ans | 100.0 | REFUSÉ (insuffisante, -38 %) | 78.7 |
| BAMLH0A0HYM2 | risque_credit_hy | 3.52 | 2026-11-19 | 0 | 786 | 3.00 ans | 100.0 | REFUSÉ (insuffisante, -38 %) | 92.0 |
| CPIAUCSL | inflation_globale | 337.5 | 2026-10-01 | 49 | 119 | 9.91 ans | 100.0 | 100.0 | 100.0 |
| CPILFESL | inflation_sous_jacente | 339.9 | 2026-10-01 | 49 | 119 | 9.91 ans | 100.0 | 100.0 | 100.0 |
| DCOILBRENTEU | prix_energie | 92.94 | 2026-11-17 | 2 | 2532 | 9.98 ans | 52.0 | 75.4 | 87.8 |
| DCOILWTICO | prix_energie_wti | 89.53 | 2026-11-17 | 2 | 2496 | 9.98 ans | 52.8 | 77.8 | 88.8 |
| DEXJPUS | devise_usdjpy | 159.9 | 2026-11-13 | 4 | 2490 | 9.97 ans | 82.9 | 95.8 | 97.9 |
| DEXUSEU | devise_eurusd | 1.103 | 2026-11-13 | 4 | 2490 | 9.97 ans | 0.4 | 56.8 | 37.6 |
| DFF | politique_monetaire | 3.88 | 2026-11-19 | 0 | 3649 | 9.99 ans | 100.0 | 29.6 | 70.9 |
| DFII10 | taux_reel_10a | 2.88 | 2026-11-19 | 0 | 2497 | 9.99 ans | 95.6 | 99.1 | 99.6 |
| DGS10 | taux_nominal_10a | 5.04 | 2026-11-19 | 0 | 2497 | 9.99 ans | 89.7 | 97.9 | 99.0 |
| DGS2 | taux_nominal_2a | 4.76 | 2026-11-19 | 0 | 2497 | 9.99 ans | 90.9 | 86.3 | 93.1 |
| DGS30 | taux_nominal_30a | 5.4 | 2026-11-19 | 0 | 2497 | 9.99 ans | 90.5 | 98.1 | 99.0 |
| DTWEXBGS | dollar_large | 122.7 | 2026-11-13 | 4 | 2488 | 9.97 ans | 100.0 | 75.3 | 86.1 |
| INDPRO | activite_industrielle | 103.4 | 2026-10-01 | 49 | 120 | 9.91 ans | 91.7 | 98.3 | 94.2 |
| NASDAQ100 | prix_actions_tech | 2.652e+04 | 2026-11-19 | 0 | 2512 | 9.99 ans | 40.9 | 88.2 | 94.1 |
| OVXCLS | volatilite_implicite_petrole | 50.67 | 2026-11-19 | 0 | 2513 | 9.99 ans | 40.5 | 78.6 | 84.0 |
| PAYEMS | emploi | 1.593e+05 | 2026-10-01 | 49 | 120 | 9.91 ans | 100.0 | 100.0 | 100.0 |
| SP500 | prix_actions | 7176 | 2026-11-19 | 0 | 2511 | 9.99 ans | 44.0 | 88.8 | 94.4 |
| T10Y2Y | pente_courbe | 0.28 | 2026-11-19 | 0 | 2497 | 9.99 ans | 5.6 | 57.4 | 43.7 |
| T10YIE | point_mort_10a | 2.16 | 2026-11-19 | 0 | 2497 | 9.99 ans | 0.4 | 4.1 | 43.7 |
| T5YIFR | point_mort_5a5a | 2.1 | 2026-11-19 | 0 | 2497 | 9.99 ans | 2.8 | 4.7 | 34.1 |
| UNRATE | chomage | 4.1 | 2026-10-01 | 49 | 119 | 9.91 ans | 25.0 | 66.7 | 56.3 |
| VIXCLS | volatilite_implicite | 28.44 | 2026-11-19 | 0 | 2544 | 9.99 ans | 98.8 | 92.9 | 92.1 |
| VXDCLS | volatilite_implicite_dow | 23.91 | 2026-11-19 | 0 | 2514 | 9.99 ans | 94.4 | 90.7 | 87.6 |
| VXVCLS | volatilite_implicite_3m | 27.03 | 2026-11-19 | 0 | 2511 | 9.99 ans | 97.6 | 87.8 | 85.4 |

**Couples obligatoires contrôlés :** CPIAUCSL/CPILFESL, DGS10/DFII10, DGS10/T10YIE, BAMLH0A0HYM2/BAMLC0A0CM, UNRATE/PAYEMS, VIXCLS/SP500 — 0 manquement(s).

**Inflation en trois chiffres (contrôle 2, E-005).** Global +4.08 % sur un an (CPIAUCSL, 2026-10-01) · sous-jacent +2.87 % (CPILFESL) · **écart hors sous-jacent +121 pb**. Contribution énergie NON publiée : `CPIENGSL` est absente du dépôt. Lacune nommée avec le code FRED qui la comble (R-028) ; elle n'est pas présentée comme une limite de méthode. L'écart ci-dessus est l'écart global/sous-jacent, pas la contribution énergie.

---

## 4. IDENTITÉS COMPTABLES ET REDONDANCES (vérifiées numériquement)

| identité | vérifiable | n dates | résidu absolu max | tolérance | vérifiée |
|---|:---:|---:|---:|---:|:---:|
| T10YIE = DGS10 - DFII10 | oui | 2497 | 0.0000 | 0.02 | OUI |
| T10Y2Y = DGS10 - DGS2 | oui | 2497 | 0.0000 | 0.02 | OUI |

**Redondances détectées (11) — deux séries liées ne comptent jamais pour deux confirmations indépendantes :**

- identité comptable : T10YIE = DGS10 - DFII10 — T10YIE, DGS10, DFII10 (résidu max 0.0000)
- identité comptable : T10Y2Y = DGS10 - DGS2 — T10Y2Y, DGS10, DGS2 (résidu max 0.0000)
- corrélation des variations à 60 séances : BAMLC0A0CM / BAMLH0A0HYM2 = +0.939 sur 725 points (seuil 0.9)
- corrélation des variations à 60 séances : DGS10 / DGS30 = +0.966 sur 2437 points (seuil 0.9)
- corrélation des variations à 60 séances : INDPRO / PAYEMS = +0.913 sur 117 points (seuil 0.9)
- corrélation des variations à 60 séances : INDPRO / UNRATE = -0.917 sur 116 points (seuil 0.9)
- corrélation des variations à 60 séances : NASDAQ100 / SP500 = +0.904 sur 2451 points (seuil 0.9)
- corrélation des variations à 60 séances : PAYEMS / UNRATE = -0.983 sur 116 points (seuil 0.9)
- corrélation des variations à 60 séances : VIXCLS / VXDCLS = +0.929 sur 2451 points (seuil 0.9)
- corrélation des variations à 60 séances : VIXCLS / VXVCLS = +0.958 sur 2451 points (seuil 0.9)
- corrélation des variations à 60 séances : VXDCLS / VXVCLS = +0.933 sur 2451 points (seuil 0.9)

---

## 5. GRILLE, σ MESURÉ, ET DOUBLE CONFRONTATION DES PROBABILITÉS

σ est **mesuré** sur chaque série, jamais choisi. Les probabilités sont les **fréquences historiques** dans chaque bande, jamais un jugement. L'effectif de chaque bande est publié ; sous 20 observations la bande est déclarée NON ESTIMABLE. La colonne « emp./gauss. » est la double confrontation exigée par §11.5 : tout écart supérieur à un facteur 2 est déclaré (⚠).

**BAMLH0A0HYM2** (niveau) — σ à 60 pas = **0.45104** · estimateurs croisés : racine-h 0.53670, blocs disjoints 0.75741 (écart relatif 67.9 %) · dérive d'échantillon -0.04281 (-0.09 σ) · 726 variations chevauchantes, 12 blocs indépendants · 2023-11-21 → 2026-11-19

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.6766 | 36 | 1 | 0.0496 | 0.0668 | 0.74 | oui |
| -1.0 | -0.6766 | -0.3383 | 106 | 2 | 0.1460 | 0.1598 | 0.91 | oui |
| -0.5 | -0.3383 | -0.1128 | 189 | 3 | 0.2603 | 0.1747 | 1.49 | oui |
| +0.0 | -0.1128 | +0.1128 | 195 | 3 | 0.2686 | 0.1974 | 1.36 | oui |
| +0.5 | +0.1128 | +0.3383 | 80 | 1 | 0.1102 | 0.1747 | 0.63 | oui |
| +1.0 | +0.3383 | +0.6766 | 83 | 1 | 0.1143 | 0.1598 | 0.72 | oui |
| +2.0 | +0.6766 | +∞ | 37 | 1 | 0.0510 | 0.0668 | 0.76 | oui |

**DCOILBRENTEU** (log) — σ à 60 pas = **0.24902** · estimateurs croisés : racine-h 0.25193, blocs disjoints 0.17959 (écart relatif 40.3 %) · dérive d'échantillon +0.01791 (+0.07 σ) · 2472 variations chevauchantes, 41 blocs indépendants · 2016-11-23 → 2026-11-17

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.3735 | 83 | 1 | 0.0336 | 0.0668 | 0.50 | oui |
| -1.0 | -0.3735 | -0.1868 | 155 | 3 | 0.0627 | 0.1598 | 0.39 ⚠ | oui |
| -0.5 | -0.1868 | -0.0623 | 498 | 8 | 0.2015 | 0.1747 | 1.15 | oui |
| +0.0 | -0.0623 | +0.0623 | 782 | 13 | 0.3163 | 0.1974 | 1.60 | oui |
| +0.5 | +0.0623 | +0.1868 | 594 | 10 | 0.2403 | 0.1747 | 1.38 | oui |
| +1.0 | +0.1868 | +0.3735 | 217 | 4 | 0.0878 | 0.1598 | 0.55 | oui |
| +2.0 | +0.3735 | +∞ | 143 | 2 | 0.0578 | 0.0668 | 0.87 | oui |

**DCOILWTICO** — non scénarisable : convention log inapplicable : 1 observation(s) non strictement positive(s), minimum -36.98 le 2020-04-20. Le prix a été négatif : aucun log-rendement n'existe. La série est déclarée NON SCÉNARISABLE plutôt que corrigée en silence.

**DEXJPUS** (log) — σ à 60 pas = **0.04138** · estimateurs croisés : racine-h 0.04349, blocs disjoints 0.03726 (écart relatif 16.7 %) · dérive d'échantillon +0.00787 (+0.19 σ) · 2430 variations chevauchantes, 40 blocs indépendants · 2016-11-23 → 2026-11-13

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0621 | 108 | 2 | 0.0444 | 0.0668 | 0.67 | oui |
| -1.0 | -0.0621 | -0.0310 | 249 | 4 | 0.1025 | 0.1598 | 0.64 | oui |
| -0.5 | -0.0310 | -0.0103 | 390 | 6 | 0.1605 | 0.1747 | 0.92 | oui |
| +0.0 | -0.0103 | +0.0103 | 501 | 8 | 0.2062 | 0.1974 | 1.04 | oui |
| +0.5 | +0.0103 | +0.0310 | 529 | 9 | 0.2177 | 0.1747 | 1.25 | oui |
| +1.0 | +0.0310 | +0.0621 | 469 | 8 | 0.1930 | 0.1598 | 1.21 | oui |
| +2.0 | +0.0621 | +∞ | 184 | 3 | 0.0757 | 0.0668 | 1.13 | oui |

**DEXUSEU** (log) — σ à 60 pas = **0.03432** · estimateurs croisés : racine-h 0.03458, blocs disjoints 0.03260 (écart relatif 6.1 %) · dérive d'échantillon +0.00171 (+0.05 σ) · 2430 variations chevauchantes, 40 blocs indépendants · 2016-11-23 → 2026-11-13

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0515 | 130 | 2 | 0.0535 | 0.0668 | 0.80 | oui |
| -1.0 | -0.0515 | -0.0257 | 323 | 5 | 0.1329 | 0.1598 | 0.83 | oui |
| -0.5 | -0.0257 | -0.0086 | 509 | 8 | 0.2095 | 0.1747 | 1.20 | oui |
| +0.0 | -0.0086 | +0.0086 | 614 | 10 | 0.2527 | 0.1974 | 1.28 | oui |
| +0.5 | +0.0086 | +0.0257 | 321 | 5 | 0.1321 | 0.1747 | 0.76 | oui |
| +1.0 | +0.0257 | +0.0515 | 307 | 5 | 0.1263 | 0.1598 | 0.79 | oui |
| +2.0 | +0.0515 | +∞ | 226 | 4 | 0.0930 | 0.0668 | 1.39 | oui |

**DGS10** (niveau) — σ à 60 pas = **0.42147** · estimateurs croisés : racine-h 0.41517, blocs disjoints 0.41573 (écart relatif 1.5 %) · dérive d'échantillon +0.06321 (+0.15 σ) · 2437 variations chevauchantes, 41 blocs indépendants · 2016-11-23 → 2026-11-19

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.6322 | 123 | 2 | 0.0505 | 0.0668 | 0.76 | oui |
| -1.0 | -0.6322 | -0.3161 | 284 | 5 | 0.1165 | 0.1598 | 0.73 | oui |
| -0.5 | -0.3161 | -0.1054 | 371 | 6 | 0.1522 | 0.1747 | 0.87 | oui |
| +0.0 | -0.1054 | +0.1054 | 527 | 9 | 0.2162 | 0.1974 | 1.10 | oui |
| +0.5 | +0.1054 | +0.3161 | 556 | 9 | 0.2281 | 0.1747 | 1.31 | oui |
| +1.0 | +0.3161 | +0.6322 | 375 | 6 | 0.1539 | 0.1598 | 0.96 | oui |
| +2.0 | +0.6322 | +∞ | 201 | 3 | 0.0825 | 0.0668 | 1.23 | oui |

**DGS2** (niveau) — σ à 60 pas = **0.49743** · estimateurs croisés : racine-h 0.42453, blocs disjoints 0.48790 (écart relatif 17.2 %) · dérive d'échantillon +0.08527 (+0.17 σ) · 2437 variations chevauchantes, 41 blocs indépendants · 2016-11-23 → 2026-11-19

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.7461 | 115 | 2 | 0.0472 | 0.0668 | 0.71 | oui |
| -1.0 | -0.7461 | -0.3731 | 228 | 4 | 0.0936 | 0.1598 | 0.59 | oui |
| -0.5 | -0.3731 | -0.1244 | 323 | 5 | 0.1325 | 0.1747 | 0.76 | oui |
| +0.0 | -0.1244 | +0.1244 | 739 | 12 | 0.3032 | 0.1974 | 1.54 | oui |
| +0.5 | +0.1244 | +0.3731 | 462 | 8 | 0.1896 | 0.1747 | 1.09 | oui |
| +1.0 | +0.3731 | +0.7461 | 369 | 6 | 0.1514 | 0.1598 | 0.95 | oui |
| +2.0 | +0.7461 | +∞ | 201 | 3 | 0.0825 | 0.0668 | 1.23 | oui |

**DGS30** (niveau) — σ à 60 pas = **0.36358** · estimateurs croisés : racine-h 0.39155, blocs disjoints 0.35298 (écart relatif 10.9 %) · dérive d'échantillon +0.05738 (+0.16 σ) · 2437 variations chevauchantes, 41 blocs indépendants · 2016-11-23 → 2026-11-19

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.5454 | 128 | 2 | 0.0525 | 0.0668 | 0.79 | oui |
| -1.0 | -0.5454 | -0.2727 | 276 | 5 | 0.1133 | 0.1598 | 0.71 | oui |
| -0.5 | -0.2727 | -0.0909 | 338 | 6 | 0.1387 | 0.1747 | 0.79 | oui |
| +0.0 | -0.0909 | +0.0909 | 627 | 10 | 0.2573 | 0.1974 | 1.30 | oui |
| +0.5 | +0.0909 | +0.2727 | 475 | 8 | 0.1949 | 0.1747 | 1.12 | oui |
| +1.0 | +0.2727 | +0.5454 | 386 | 6 | 0.1584 | 0.1598 | 0.99 | oui |
| +2.0 | +0.5454 | +∞ | 207 | 3 | 0.0849 | 0.0668 | 1.27 | oui |

**DTWEXBGS** (log) — σ à 60 pas = **0.02574** · estimateurs croisés : racine-h 0.02389, blocs disjoints 0.02347 (écart relatif 9.7 %) · dérive d'échantillon +0.00059 (+0.02 σ) · 2428 variations chevauchantes, 40 blocs indépendants · 2016-11-23 → 2026-11-13

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0386 | 170 | 3 | 0.0700 | 0.0668 | 1.05 | oui |
| -1.0 | -0.0386 | -0.0193 | 379 | 6 | 0.1561 | 0.1598 | 0.98 | oui |
| -0.5 | -0.0193 | -0.0064 | 354 | 6 | 0.1458 | 0.1747 | 0.83 | oui |
| +0.0 | -0.0064 | +0.0064 | 549 | 9 | 0.2261 | 0.1974 | 1.15 | oui |
| +0.5 | +0.0064 | +0.0193 | 472 | 8 | 0.1944 | 0.1747 | 1.11 | oui |
| +1.0 | +0.0193 | +0.0386 | 300 | 5 | 0.1236 | 0.1598 | 0.77 | oui |
| +2.0 | +0.0386 | +∞ | 204 | 3 | 0.0840 | 0.0668 | 1.26 | oui |

**NASDAQ100** (log) — σ à 60 pas = **0.08904** · estimateurs croisés : racine-h 0.11241, blocs disjoints 0.10362 (écart relatif 26.2 %) · dérive d'échantillon +0.04317 (+0.48 σ) · 2452 variations chevauchantes, 41 blocs indépendants · 2016-11-23 → 2026-11-19

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.1336 | 108 | 2 | 0.0440 | 0.0668 | 0.66 | oui |
| -1.0 | -0.1336 | -0.0668 | 174 | 3 | 0.0710 | 0.1598 | 0.44 ⚠ | oui |
| -0.5 | -0.0668 | -0.0223 | 194 | 3 | 0.0791 | 0.1747 | 0.45 ⚠ | oui |
| +0.0 | -0.0223 | +0.0223 | 355 | 6 | 0.1448 | 0.1974 | 0.73 | oui |
| +0.5 | +0.0223 | +0.0668 | 597 | 10 | 0.2435 | 0.1747 | 1.39 | oui |
| +1.0 | +0.0668 | +0.1336 | 710 | 12 | 0.2896 | 0.1598 | 1.81 | oui |
| +2.0 | +0.1336 | +∞ | 314 | 5 | 0.1281 | 0.0668 | 1.92 | oui |

**SP500** (log) — σ à 60 pas = **0.06919** · estimateurs croisés : racine-h 0.08896, blocs disjoints 0.08194 (écart relatif 28.6 %) · dérive d'échantillon +0.02974 (+0.43 σ) · 2451 variations chevauchantes, 41 blocs indépendants · 2016-11-23 → 2026-11-19

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.1038 | 114 | 2 | 0.0465 | 0.0668 | 0.70 | oui |
| -1.0 | -0.1038 | -0.0519 | 162 | 3 | 0.0661 | 0.1598 | 0.41 ⚠ | oui |
| -0.5 | -0.0519 | -0.0173 | 183 | 3 | 0.0747 | 0.1747 | 0.43 ⚠ | oui |
| +0.0 | -0.0173 | +0.0173 | 301 | 5 | 0.1228 | 0.1974 | 0.62 | oui |
| +0.5 | +0.0173 | +0.0519 | 762 | 13 | 0.3109 | 0.1747 | 1.78 | oui |
| +1.0 | +0.0519 | +0.1038 | 720 | 12 | 0.2938 | 0.1598 | 1.84 | oui |
| +2.0 | +0.1038 | +∞ | 209 | 3 | 0.0853 | 0.0668 | 1.28 | oui |

**VIXCLS** (log) — σ à 60 pas = **0.34610** · estimateurs croisés : racine-h 0.61992, blocs disjoints 0.42400 (écart relatif 79.1 %) · dérive d'échantillon +0.00905 (+0.03 σ) · 2484 variations chevauchantes, 41 blocs indépendants · 2016-11-23 → 2026-11-19

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.5191 | 74 | 1 | 0.0298 | 0.0668 | 0.45 ⚠ | oui |
| -1.0 | -0.5191 | -0.2596 | 377 | 6 | 0.1518 | 0.1598 | 0.95 | oui |
| -0.5 | -0.2596 | -0.0865 | 595 | 10 | 0.2395 | 0.1747 | 1.37 | oui |
| +0.0 | -0.0865 | +0.0865 | 620 | 10 | 0.2496 | 0.1974 | 1.26 | oui |
| +0.5 | +0.0865 | +0.2596 | 382 | 6 | 0.1538 | 0.1747 | 0.88 | oui |
| +1.0 | +0.2596 | +0.5191 | 255 | 4 | 0.1027 | 0.1598 | 0.64 | oui |
| +2.0 | +0.5191 | +∞ | 181 | 3 | 0.0729 | 0.0668 | 1.09 | oui |

---

## 6. TEST D'ASYMÉTRIE — DÉFINITION UNIQUE (R-030), L'ESPÉRANCE DÉCIDE

> Test d'admission : **espérance calculée sur la grille symétrique complète, les deux queues incluses**. Le rapport gain maximal / perte maximale est publié **pour information** et ne peut fonder aucune admission seul (T-001, faute E-018). Le rapport gain maximal / perte du scénario central est **interdit**. Une seule formulation, appliquée à tous les candidats, position détenue comprise.

| candidat | verdict | espérance % NAV | sans dérive | 1re moitié | 2e moitié | gain max | perte max | ratio (info) | critères échoués |
|---|:---:|---:|---:|---:|---:|---:|---:|---:|---|
| M005-DCOILBRENTEU-HAUSSE-ALIGNE | REFUSEE | +0.274 | +0.128 | +0.248 | +0.232 | +5.09 | -3.21 | 1.58:1 | 16_arete_conditionnelle_mesuree |
| M005-DCOILBRENTEU-HAUSSE-CONTRARIEN | REFUSEE | +0.274 | +0.128 | +0.248 | +0.232 | +5.09 | -3.21 | 1.58:1 | 16_arete_conditionnelle_mesuree |
| M005-DCOILBRENTEU-BAISSE-ALIGNE | REFUSEE | -0.274 | -0.128 | -0.248 | -0.232 | +3.21 | -5.09 | 0.63:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILBRENTEU-BAISSE-CONTRARIEN | REFUSEE | -0.274 | -0.128 | -0.248 | -0.232 | +3.21 | -5.09 | 0.63:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-HAUSSE-ALIGNE | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-HAUSSE-CONTRARIEN | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-BAISSE-ALIGNE | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-BAISSE-CONTRARIEN | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-HAUSSE-ALIGNE | REFUSEE | -0.008 | -0.067 | -0.082 | +0.036 | +0.62 | -0.71 | 0.87:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-HAUSSE-CONTRARIEN | REFUSEE | -0.008 | -0.067 | -0.082 | +0.036 | +0.62 | -0.71 | 0.87:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-BAISSE-ALIGNE | REFUSEE | +0.008 | +0.067 | +0.082 | -0.036 | +0.71 | -0.62 | 1.15:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-BAISSE-CONTRARIEN | REFUSEE | +0.008 | +0.067 | +0.082 | -0.036 | +0.71 | -0.62 | 1.15:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-HAUSSE-ALIGNE | REFUSEE | -0.060 | -0.074 | -0.030 | -0.073 | +0.49 | -0.60 | 0.82:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-HAUSSE-CONTRARIEN | REFUSEE | -0.060 | -0.074 | -0.030 | -0.073 | +0.49 | -0.60 | 0.82:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-BAISSE-ALIGNE | REFUSEE | +0.060 | +0.074 | +0.030 | +0.073 | +0.60 | -0.49 | 1.22:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DEXUSEU-BAISSE-CONTRARIEN | REFUSEE | +0.060 | +0.074 | +0.030 | +0.073 | +0.60 | -0.49 | 1.22:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DGS10-HAUSSE-ALIGNE | REFUSEE | +0.010 | -0.024 | -0.052 | +0.061 | +0.48 | -0.57 | 0.85:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-HAUSSE-CONTRARIEN | REFUSEE | +0.010 | -0.024 | -0.052 | +0.061 | +0.48 | -0.57 | 0.85:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-BAISSE-ALIGNE | REFUSEE | -0.010 | +0.024 | +0.052 | -0.061 | +0.57 | -0.48 | 1.18:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-BAISSE-CONTRARIEN | REFUSEE | -0.010 | +0.024 | +0.052 | -0.061 | +0.57 | -0.48 | 1.18:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-HAUSSE-ALIGNE | REFUSEE | -0.005 | -0.016 | -0.023 | +0.005 | +0.13 | -0.17 | 0.78:1 | 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-HAUSSE-CONTRARIEN | REFUSEE | -0.005 | -0.016 | -0.023 | +0.005 | +0.13 | -0.17 | 0.78:1 | 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-BAISSE-ALIGNE | REFUSEE | +0.005 | +0.016 | +0.023 | -0.005 | +0.17 | -0.13 | 1.28:1 | 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-BAISSE-CONTRARIEN | REFUSEE | +0.005 | +0.016 | +0.023 | -0.005 | +0.17 | -0.13 | 1.28:1 | 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-HAUSSE-ALIGNE | REFUSEE | +0.015 | -0.041 | -0.104 | +0.130 | +0.77 | -0.96 | 0.80:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-HAUSSE-CONTRARIEN | REFUSEE | +0.015 | -0.041 | -0.104 | +0.130 | +0.77 | -0.96 | 0.80:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-BAISSE-ALIGNE | REFUSEE | -0.015 | +0.041 | +0.104 | -0.130 | +0.96 | -0.77 | 1.26:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-BAISSE-CONTRARIEN | REFUSEE | -0.015 | +0.041 | +0.104 | -0.130 | +0.96 | -0.77 | 1.26:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-HAUSSE-ALIGNE | REFUSEE | -0.067 | -0.072 | -0.086 | -0.052 | +0.35 | -0.48 | 0.73:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-HAUSSE-CONTRARIEN | REFUSEE | -0.067 | -0.072 | -0.086 | -0.052 | +0.35 | -0.48 | 0.73:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-BAISSE-ALIGNE | REFUSEE | +0.067 | +0.072 | +0.086 | +0.052 | +0.48 | -0.35 | 1.36:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DTWEXBGS-BAISSE-CONTRARIEN | REFUSEE | +0.067 | +0.072 | +0.086 | +0.052 | +0.48 | -0.35 | 1.36:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-HAUSSE-ALIGNE | REFUSEE | +0.297 | -0.035 | +0.449 | +0.194 | +1.49 | -1.38 | 1.08:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-HAUSSE-CONTRARIEN | REFUSEE | +0.297 | -0.035 | +0.449 | +0.194 | +1.49 | -1.38 | 1.08:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-BAISSE-ALIGNE | REFUSEE | -0.297 | +0.035 | -0.449 | -0.194 | +1.38 | -1.49 | 0.93:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-NASDAQ100-BAISSE-CONTRARIEN | REFUSEE | -0.297 | +0.035 | -0.449 | -0.194 | +1.38 | -1.49 | 0.93:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 14_esperance_stable_dans_le_temps |
| M005-SP500-HAUSSE-ALIGNE | REFUSEE | +0.180 | -0.043 | +0.209 | +0.155 | +1.11 | -1.11 | 1.01:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-SP500-HAUSSE-CONTRARIEN | REFUSEE | +0.180 | -0.043 | +0.209 | +0.155 | +1.11 | -1.11 | 1.01:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-SP500-BAISSE-ALIGNE | REFUSEE | -0.180 | +0.043 | -0.209 | -0.155 | +1.11 | -1.11 | 0.99:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-SP500-BAISSE-CONTRARIEN | REFUSEE | -0.180 | +0.043 | -0.209 | -0.155 | +1.11 | -1.11 | 0.99:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |

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
| 8_confirmations_independantes | 2 |
| 9_test_execute_et_vrai | 2 |
| 10_invalidation_fait_date | 12 |
| 11_invalidation_non_deja_survenue | 26 |
| 12_esperance_positive | 22 |
| 13_esperance_non_portee_par_derive | 20 |
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

- `BAMLC0A0CM` : percentile REFUSÉ sur 5 ans — profondeur réelle 785 obs / 3.00 ans (début 2023-11-21). R-011 : un percentile calculé sur une série tronquée est sans valeur.
- `BAMLH0A0HYM2` : percentile REFUSÉ sur 5 ans — profondeur réelle 786 obs / 3.00 ans (début 2023-11-21). R-011 : un percentile calculé sur une série tronquée est sans valeur.
- `BAMLH0A0HYM2` : instrument NON ADMISSIBLE — P&L non calculable depuis le dépôt : l'OAS est un spread, et le dépôt ne contient pas le rendement de l'indice, donc pas la duration de spread. Aucune valeur ne peut être produite sans un chiffre extérieur aux données (E-002).
- `BAMLC0A0CM` : instrument NON ADMISSIBLE — P&L non calculable depuis le dépôt : l'OAS est un spread, et le dépôt ne contient pas le rendement de l'indice, donc pas la duration de spread. Aucune valeur ne peut être produite sans un chiffre extérieur aux données (E-002).
- Retards sur la date d'arrêté unique (E-014) : DCOILBRENTEU 2 séance(s), DCOILWTICO 2 séance(s), DEXJPUS 4 séance(s), DEXUSEU 4 séance(s), DTWEXBGS 4 séance(s)

**Vérification tierce (R-032) : NON SATISFAITE pour ce brief.** Le moteur ne dispose d'aucune source extérieure au dépôt. Trois estimateurs **internes** de σ sont publiés côte à côte au §5 ; ce sont des contrôles de cohérence interne, **pas** une vérification tierce, et ils ne sont pas présentés comme telle.

**Ce que ce moteur ne peut pas faire.** Il ne prouve aucune capacité prédictive : la règle de confirmation est une règle de percentile, déclarée et symétrique, pas un modèle validé hors échantillon. Il ne corrige pas la multiplicité : 40 candidats sont évalués et aucune pénalité de sélection n'est appliquée à l'espérance — c'est une limite déclarée, pas un oubli. Il ne voit ni les événements politiques, ni les décisions de banques centrales : le dépôt ne contient que des séries FRED, et toute affirmation de politique monétaire non adossée à `DFF` est refusée (critère 15, faute E-006).

---

*Fin du brief 005. Produit mécaniquement. Ne constitue pas un conseil en investissement.*