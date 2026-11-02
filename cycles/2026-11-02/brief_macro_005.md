# BRIEF MACRO n° 005 — arrêté au 2026-10-28

*Produit par `apollon_macro.py` le 2026-11-02T13:30:03+00:00. Aucune valeur de ce document n'est saisie à la main : chacune porte sa série, sa date et sa profondeur. Bloc à copier tel quel.*

**Grille de scénarios (R-029, §11), déclarée avant toute lecture de données et empreintée :** `[-2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0]` · empreinte SHA-256 `6aaeb3863c875923…` · symétrique : True · horizon 60 séances (3 mois pour les séries mensuelles).

---

## 1. CONCLUSION, ÉNONCÉE D'ABORD

**40 candidats déclarés d'avance (10 instruments × 2 directions × 2 règles de confirmation). 40 évalués. 0 thèse(s) survivent aux quinze critères.**

**Abstention. Aucune thèse ne survit.** Ce n'est pas un silence : c'est un résultat, produit par le même portier que celui qui aurait admis une thèse. Le détail des échecs, critère par critère, figure au §6. La Section Macro ne transmet rien à la Section Risque ce cycle.

**Position détenue (contrôle 9, E-020) — 100 % cash, testée sur la même grille.** Espérance excédentaire du cash : +0.000 % de NAV. Référence 60/40 : +1.337 % (hors dérive : -0.202 %). **Écart du cash contre la référence : -1.337 % de NAV** sur 60 séances.

---

## 2. CE QUI A CHANGÉ — MÉCANISME, PAS CONTENU

Fait, étiqueté : les briefs 001 à 004 étaient rédigés par un agent. Celui-ci est produit par un moteur. Le paramètre libre de la Section Macro — la grille de scénarios — n'est plus accessible à l'agent : il est déclaré en tête de fichier, symétrique par construction, et son empreinte SHA-256 est vérifiée avant chaque usage. Sur le brief 004, ce paramètre avait porté le ratio annoncé de 1,29:1 à 3,0:1.

---

## 3. M1 · M2 · M3 · M4 — ÉTAT DES SÉRIES (FAIT)

Toutes les valeurs sont des FAITS lus dans le dépôt. Le retard est compté en séances ouvrées depuis la date d'arrêté unique. Les couples obligatoires sont vérifiés par le rendu : ce bloc ne peut pas être émis si un membre d'un couple manque.

| série | rôle déclaré | valeur | date | retard | n obs | profondeur | pct 1 an | pct 5 ans | pct complet |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| BAMLC0A0CM | risque_credit_ig | 0.86 | 2026-10-28 | 0 | 784 | 2.99 ans | 90.9 | REFUSÉ (insuffisante, -38 %) | 54.7 |
| BAMLH0A0HYM2 | risque_credit_hy | 3.14 | 2026-10-28 | 0 | 785 | 2.99 ans | 86.1 | REFUSÉ (insuffisante, -38 %) | 62.0 |
| CPIAUCSL | inflation_globale | 336.3 | 2026-09-01 | 57 | 118 | 9.83 ans | 100.0 | 100.0 | 100.0 |
| CPILFESL | inflation_sous_jacente | 338.9 | 2026-09-01 | 57 | 118 | 9.83 ans | 100.0 | 100.0 | 100.0 |
| DCOILBRENTEU | prix_energie | 123.1 | 2026-10-27 | 1 | 2530 | 9.98 ans | 91.7 | 97.1 | 98.5 |
| DCOILWTICO | prix_energie_wti | 103.4 | 2026-10-27 | 1 | 2494 | 9.98 ans | 89.3 | 92.3 | 96.1 |
| DEXJPUS | devise_usdjpy | 156.9 | 2026-10-23 | 3 | 2488 | 9.97 ans | 34.5 | 82.9 | 91.4 |
| DEXUSEU | devise_eurusd | 1.12 | 2026-10-23 | 3 | 2488 | 9.97 ans | 2.4 | 62.8 | 46.9 |
| DFF | politique_monetaire | 3.88 | 2026-10-28 | 0 | 3646 | 9.98 ans | 100.0 | 27.9 | 70.8 |
| DFII10 | taux_reel_10a | 2.67 | 2026-10-28 | 0 | 2494 | 9.98 ans | 91.3 | 98.3 | 99.1 |
| DGS10 | taux_nominal_10a | 5.05 | 2026-10-28 | 0 | 2494 | 9.98 ans | 92.1 | 98.4 | 99.2 |
| DGS2 | taux_nominal_2a | 4.67 | 2026-10-28 | 0 | 2494 | 9.98 ans | 89.3 | 82.1 | 91.0 |
| DGS30 | taux_nominal_30a | 5.37 | 2026-10-28 | 0 | 2494 | 9.98 ans | 92.1 | 98.4 | 99.2 |
| DTWEXBGS | dollar_large | 121.3 | 2026-10-23 | 3 | 2486 | 9.97 ans | 90.9 | 61.4 | 78.4 |
| INDPRO | activite_industrielle | 104 | 2026-09-01 | 57 | 119 | 9.83 ans | 100.0 | 100.0 | 95.8 |
| NASDAQ100 | prix_actions_tech | 2.981e+04 | 2026-10-28 | 0 | 2509 | 9.98 ans | 85.3 | 97.1 | 98.5 |
| OVXCLS | volatilite_implicite_petrole | 58.59 | 2026-10-28 | 0 | 2510 | 9.98 ans | 64.3 | 90.3 | 91.7 |
| PAYEMS | emploi | 1.59e+05 | 2026-09-01 | 57 | 119 | 9.83 ans | 100.0 | 100.0 | 100.0 |
| SP500 | prix_actions | 7744 | 2026-10-28 | 0 | 2508 | 9.98 ans | 92.9 | 98.6 | 99.3 |
| T10Y2Y | pente_courbe | 0.38 | 2026-10-28 | 0 | 2494 | 9.98 ans | 19.8 | 64.8 | 50.3 |
| T10YIE | point_mort_10a | 2.38 | 2026-10-28 | 0 | 2494 | 9.98 ans | 87.7 | 71.3 | 83.8 |
| T5YIFR | point_mort_5a5a | 2.27 | 2026-10-28 | 0 | 2494 | 9.98 ans | 75.0 | 52.9 | 74.7 |
| UNRATE | chomage | 4.2 | 2026-09-01 | 57 | 118 | 9.83 ans | 33.3 | 78.3 | 64.4 |
| VIXCLS | volatilite_implicite | 16.91 | 2026-10-28 | 0 | 2541 | 9.98 ans | 47.6 | 43.0 | 49.7 |
| VXDCLS | volatilite_implicite_dow | 15.98 | 2026-10-28 | 0 | 2511 | 9.98 ans | 56.3 | 49.3 | 50.9 |
| VXVCLS | volatilite_implicite_3m | 19.22 | 2026-10-28 | 0 | 2508 | 9.98 ans | 33.3 | 39.0 | 48.1 |

**Couples obligatoires contrôlés :** CPIAUCSL/CPILFESL, DGS10/DFII10, DGS10/T10YIE, BAMLH0A0HYM2/BAMLC0A0CM, UNRATE/PAYEMS, VIXCLS/SP500 — 0 manquement(s).

**Inflation en trois chiffres (contrôle 2, E-005).** Global +4.02 % sur un an (CPIAUCSL, 2026-09-01) · sous-jacent +2.79 % (CPILFESL) · **écart hors sous-jacent +123 pb**. Contribution énergie NON publiée : `CPIENGSL` est absente du dépôt. Lacune nommée avec le code FRED qui la comble (R-028) ; elle n'est pas présentée comme une limite de méthode. L'écart ci-dessus est l'écart global/sous-jacent, pas la contribution énergie.

---

## 4. IDENTITÉS COMPTABLES ET REDONDANCES (vérifiées numériquement)

| identité | vérifiable | n dates | résidu absolu max | tolérance | vérifiée |
|---|:---:|---:|---:|---:|:---:|
| T10YIE = DGS10 - DFII10 | oui | 2494 | 0.0000 | 0.02 | OUI |
| T10Y2Y = DGS10 - DGS2 | oui | 2494 | 0.0000 | 0.02 | OUI |

**Redondances détectées (11) — deux séries liées ne comptent jamais pour deux confirmations indépendantes :**

- identité comptable : T10YIE = DGS10 - DFII10 — T10YIE, DGS10, DFII10 (résidu max 0.0000)
- identité comptable : T10Y2Y = DGS10 - DGS2 — T10Y2Y, DGS10, DGS2 (résidu max 0.0000)
- corrélation des variations à 60 séances : BAMLC0A0CM / BAMLH0A0HYM2 = +0.935 sur 724 points (seuil 0.9)
- corrélation des variations à 60 séances : DGS10 / DGS30 = +0.966 sur 2434 points (seuil 0.9)
- corrélation des variations à 60 séances : INDPRO / PAYEMS = +0.913 sur 116 points (seuil 0.9)
- corrélation des variations à 60 séances : INDPRO / UNRATE = -0.917 sur 115 points (seuil 0.9)
- corrélation des variations à 60 séances : NASDAQ100 / SP500 = +0.903 sur 2448 points (seuil 0.9)
- corrélation des variations à 60 séances : PAYEMS / UNRATE = -0.983 sur 115 points (seuil 0.9)
- corrélation des variations à 60 séances : VIXCLS / VXDCLS = +0.929 sur 2448 points (seuil 0.9)
- corrélation des variations à 60 séances : VIXCLS / VXVCLS = +0.958 sur 2448 points (seuil 0.9)
- corrélation des variations à 60 séances : VXDCLS / VXVCLS = +0.933 sur 2448 points (seuil 0.9)

---

## 5. GRILLE, σ MESURÉ, ET DOUBLE CONFRONTATION DES PROBABILITÉS

σ est **mesuré** sur chaque série, jamais choisi. Les probabilités sont les **fréquences historiques** dans chaque bande, jamais un jugement. L'effectif de chaque bande est publié ; sous 20 observations la bande est déclarée NON ESTIMABLE. La colonne « emp./gauss. » est la double confrontation exigée par §11.5 : tout écart supérieur à un facteur 2 est déclaré (⚠).

**BAMLH0A0HYM2** (niveau) — σ à 60 pas = **0.44646** · estimateurs croisés : racine-h 0.53953, blocs disjoints 0.37474 (écart relatif 44.0 %) · dérive d'échantillon -0.07062 (-0.16 σ) · 725 variations chevauchantes, 12 blocs indépendants · 2023-10-31 → 2026-10-28

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.6697 | 43 | 1 | 0.0593 | 0.0668 | 0.89 | oui |
| -1.0 | -0.6697 | -0.3348 | 114 | 2 | 0.1572 | 0.1598 | 0.98 | oui |
| -0.5 | -0.3348 | -0.1116 | 189 | 3 | 0.2607 | 0.1747 | 1.49 | oui |
| +0.0 | -0.1116 | +0.1116 | 195 | 3 | 0.2690 | 0.1974 | 1.36 | oui |
| +0.5 | +0.1116 | +0.3348 | 80 | 1 | 0.1103 | 0.1747 | 0.63 | oui |
| +1.0 | +0.3348 | +0.6697 | 74 | 1 | 0.1021 | 0.1598 | 0.64 | oui |
| +2.0 | +0.6697 | +∞ | 30 | 0 | 0.0414 | 0.0668 | 0.62 | oui |

**DCOILBRENTEU** (log) — σ à 60 pas = **0.24933** · estimateurs croisés : racine-h 0.24993, blocs disjoints 0.19006 (écart relatif 31.5 %) · dérive d'échantillon +0.01857 (+0.07 σ) · 2470 variations chevauchantes, 41 blocs indépendants · 2016-11-04 → 2026-10-27

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.3740 | 83 | 1 | 0.0336 | 0.0668 | 0.50 | oui |
| -1.0 | -0.3740 | -0.1870 | 154 | 3 | 0.0623 | 0.1598 | 0.39 ⚠ | oui |
| -0.5 | -0.1870 | -0.0623 | 498 | 8 | 0.2016 | 0.1747 | 1.15 | oui |
| +0.0 | -0.0623 | +0.0623 | 774 | 13 | 0.3134 | 0.1974 | 1.59 | oui |
| +0.5 | +0.0623 | +0.1870 | 595 | 10 | 0.2409 | 0.1747 | 1.38 | oui |
| +1.0 | +0.1870 | +0.3740 | 223 | 4 | 0.0903 | 0.1598 | 0.56 | oui |
| +2.0 | +0.3740 | +∞ | 143 | 2 | 0.0579 | 0.0668 | 0.87 | oui |

**DCOILWTICO** — non scénarisable : convention log inapplicable : 1 observation(s) non strictement positive(s), minimum -36.98 le 2020-04-20. Le prix a été négatif : aucun log-rendement n'existe. La série est déclarée NON SCÉNARISABLE plutôt que corrigée en silence.

**DEXJPUS** (log) — σ à 60 pas = **0.04152** · estimateurs croisés : racine-h 0.04377, blocs disjoints 0.03999 (écart relatif 9.5 %) · dérive d'échantillon +0.00814 (+0.20 σ) · 2428 variations chevauchantes, 40 blocs indépendants · 2016-11-04 → 2026-10-23

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0623 | 105 | 2 | 0.0432 | 0.0668 | 0.65 | oui |
| -1.0 | -0.0623 | -0.0311 | 249 | 4 | 0.1026 | 0.1598 | 0.64 | oui |
| -0.5 | -0.0311 | -0.0104 | 391 | 7 | 0.1610 | 0.1747 | 0.92 | oui |
| +0.0 | -0.0104 | +0.0104 | 490 | 8 | 0.2018 | 0.1974 | 1.02 | oui |
| +0.5 | +0.0104 | +0.0311 | 536 | 9 | 0.2208 | 0.1747 | 1.26 | oui |
| +1.0 | +0.0311 | +0.0623 | 472 | 8 | 0.1944 | 0.1598 | 1.22 | oui |
| +2.0 | +0.0623 | +∞ | 185 | 3 | 0.0762 | 0.0668 | 1.14 | oui |

**DEXUSEU** (log) — σ à 60 pas = **0.03426** · estimateurs croisés : racine-h 0.03468, blocs disjoints 0.03427 (écart relatif 1.2 %) · dérive d'échantillon +0.00183 (+0.05 σ) · 2428 variations chevauchantes, 40 blocs indépendants · 2016-11-04 → 2026-10-23

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0514 | 130 | 2 | 0.0535 | 0.0668 | 0.80 | oui |
| -1.0 | -0.0514 | -0.0257 | 315 | 5 | 0.1297 | 0.1598 | 0.81 | oui |
| -0.5 | -0.0257 | -0.0086 | 511 | 9 | 0.2105 | 0.1747 | 1.20 | oui |
| +0.0 | -0.0086 | +0.0086 | 617 | 10 | 0.2541 | 0.1974 | 1.29 | oui |
| +0.5 | +0.0086 | +0.0257 | 321 | 5 | 0.1322 | 0.1747 | 0.76 | oui |
| +1.0 | +0.0257 | +0.0514 | 307 | 5 | 0.1264 | 0.1598 | 0.79 | oui |
| +2.0 | +0.0514 | +∞ | 227 | 4 | 0.0935 | 0.0668 | 1.40 | oui |

**DGS10** (niveau) — σ à 60 pas = **0.42176** · estimateurs croisés : racine-h 0.41589, blocs disjoints 0.47149 (écart relatif 13.4 %) · dérive d'échantillon +0.06284 (+0.15 σ) · 2434 variations chevauchantes, 41 blocs indépendants · 2016-11-04 → 2026-10-28

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.6326 | 123 | 2 | 0.0505 | 0.0668 | 0.76 | oui |
| -1.0 | -0.6326 | -0.3163 | 284 | 5 | 0.1167 | 0.1598 | 0.73 | oui |
| -0.5 | -0.3163 | -0.1054 | 371 | 6 | 0.1524 | 0.1747 | 0.87 | oui |
| +0.0 | -0.1054 | +0.1054 | 528 | 9 | 0.2169 | 0.1974 | 1.10 | oui |
| +0.5 | +0.1054 | +0.3163 | 556 | 9 | 0.2284 | 0.1747 | 1.31 | oui |
| +1.0 | +0.3163 | +0.6326 | 370 | 6 | 0.1520 | 0.1598 | 0.95 | oui |
| +2.0 | +0.6326 | +∞ | 202 | 3 | 0.0830 | 0.0668 | 1.24 | oui |

**DGS2** (niveau) — σ à 60 pas = **0.49684** · estimateurs croisés : racine-h 0.42300, blocs disjoints 0.49618 (écart relatif 17.5 %) · dérive d'échantillon +0.08364 (+0.17 σ) · 2434 variations chevauchantes, 41 blocs indépendants · 2016-11-04 → 2026-10-28

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.7453 | 115 | 2 | 0.0472 | 0.0668 | 0.71 | oui |
| -1.0 | -0.7453 | -0.3726 | 228 | 4 | 0.0937 | 0.1598 | 0.59 | oui |
| -0.5 | -0.3726 | -0.1242 | 323 | 5 | 0.1327 | 0.1747 | 0.76 | oui |
| +0.0 | -0.1242 | +0.1242 | 739 | 12 | 0.3036 | 0.1974 | 1.54 | oui |
| +0.5 | +0.1242 | +0.3726 | 469 | 8 | 0.1927 | 0.1747 | 1.10 | oui |
| +1.0 | +0.3726 | +0.7453 | 359 | 6 | 0.1475 | 0.1598 | 0.92 | oui |
| +2.0 | +0.7453 | +∞ | 201 | 3 | 0.0826 | 0.0668 | 1.24 | oui |

**DGS30** (niveau) — σ à 60 pas = **0.36402** · estimateurs croisés : racine-h 0.39348, blocs disjoints 0.41679 (écart relatif 14.5 %) · dérive d'échantillon +0.05752 (+0.16 σ) · 2434 variations chevauchantes, 41 blocs indépendants · 2016-11-04 → 2026-10-28

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.5460 | 128 | 2 | 0.0526 | 0.0668 | 0.79 | oui |
| -1.0 | -0.5460 | -0.2730 | 276 | 5 | 0.1134 | 0.1598 | 0.71 | oui |
| -0.5 | -0.2730 | -0.0910 | 338 | 6 | 0.1389 | 0.1747 | 0.80 | oui |
| +0.0 | -0.0910 | +0.0910 | 630 | 10 | 0.2588 | 0.1974 | 1.31 | oui |
| +0.5 | +0.0910 | +0.2730 | 466 | 8 | 0.1915 | 0.1747 | 1.10 | oui |
| +1.0 | +0.2730 | +0.5460 | 388 | 6 | 0.1594 | 0.1598 | 1.00 | oui |
| +2.0 | +0.5460 | +∞ | 208 | 3 | 0.0855 | 0.0668 | 1.28 | oui |

**DTWEXBGS** (log) — σ à 60 pas = **0.02572** · estimateurs croisés : racine-h 0.02410, blocs disjoints 0.02713 (écart relatif 12.6 %) · dérive d'échantillon +0.00048 (+0.02 σ) · 2426 variations chevauchantes, 40 blocs indépendants · 2016-11-04 → 2026-10-23

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0386 | 170 | 3 | 0.0701 | 0.0668 | 1.05 | oui |
| -1.0 | -0.0386 | -0.0193 | 379 | 6 | 0.1562 | 0.1598 | 0.98 | oui |
| -0.5 | -0.0193 | -0.0064 | 359 | 6 | 0.1480 | 0.1747 | 0.85 | oui |
| +0.0 | -0.0064 | +0.0064 | 552 | 9 | 0.2275 | 0.1974 | 1.15 | oui |
| +0.5 | +0.0064 | +0.0193 | 466 | 8 | 0.1921 | 0.1747 | 1.10 | oui |
| +1.0 | +0.0193 | +0.0386 | 295 | 5 | 0.1216 | 0.1598 | 0.76 | oui |
| +2.0 | +0.0386 | +∞ | 205 | 3 | 0.0845 | 0.0668 | 1.26 | oui |

**NASDAQ100** (log) — σ à 60 pas = **0.08872** · estimateurs croisés : racine-h 0.11160, blocs disjoints 0.09103 (écart relatif 25.8 %) · dérive d'échantillon +0.04412 (+0.50 σ) · 2449 variations chevauchantes, 41 blocs indépendants · 2016-11-04 → 2026-10-28

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.1331 | 108 | 2 | 0.0441 | 0.0668 | 0.66 | oui |
| -1.0 | -0.1331 | -0.0665 | 167 | 3 | 0.0682 | 0.1598 | 0.43 ⚠ | oui |
| -0.5 | -0.0665 | -0.0222 | 186 | 3 | 0.0759 | 0.1747 | 0.43 ⚠ | oui |
| +0.0 | -0.0222 | +0.0222 | 354 | 6 | 0.1445 | 0.1974 | 0.73 | oui |
| +0.5 | +0.0222 | +0.0665 | 590 | 10 | 0.2409 | 0.1747 | 1.38 | oui |
| +1.0 | +0.0665 | +0.1331 | 728 | 12 | 0.2973 | 0.1598 | 1.86 | oui |
| +2.0 | +0.1331 | +∞ | 316 | 5 | 0.1290 | 0.0668 | 1.93 | oui |

**SP500** (log) — σ à 60 pas = **0.06911** · estimateurs croisés : racine-h 0.08852, blocs disjoints 0.06740 (écart relatif 31.3 %) · dérive d'échantillon +0.03034 (+0.44 σ) · 2448 variations chevauchantes, 41 blocs indépendants · 2016-11-04 → 2026-10-28

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.1037 | 115 | 2 | 0.0470 | 0.0668 | 0.70 | oui |
| -1.0 | -0.1037 | -0.0518 | 158 | 3 | 0.0645 | 0.1598 | 0.40 ⚠ | oui |
| -0.5 | -0.0518 | -0.0173 | 176 | 3 | 0.0719 | 0.1747 | 0.41 ⚠ | oui |
| +0.0 | -0.0173 | +0.0173 | 295 | 5 | 0.1205 | 0.1974 | 0.61 | oui |
| +0.5 | +0.0173 | +0.0518 | 758 | 13 | 0.3096 | 0.1747 | 1.77 | oui |
| +1.0 | +0.0518 | +0.1037 | 736 | 12 | 0.3007 | 0.1598 | 1.88 | oui |
| +2.0 | +0.1037 | +∞ | 210 | 4 | 0.0858 | 0.0668 | 1.28 | oui |

**VIXCLS** (log) — σ à 60 pas = **0.34579** · estimateurs croisés : racine-h 0.61284, blocs disjoints 0.36664 (écart relatif 77.2 %) · dérive d'échantillon +0.00546 (+0.02 σ) · 2481 variations chevauchantes, 41 blocs indépendants · 2016-11-04 → 2026-10-28

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.5187 | 76 | 1 | 0.0306 | 0.0668 | 0.46 ⚠ | oui |
| -1.0 | -0.5187 | -0.2593 | 381 | 6 | 0.1536 | 0.1598 | 0.96 | oui |
| -0.5 | -0.2593 | -0.0864 | 601 | 10 | 0.2422 | 0.1747 | 1.39 | oui |
| +0.0 | -0.0864 | +0.0864 | 621 | 10 | 0.2503 | 0.1974 | 1.27 | oui |
| +0.5 | +0.0864 | +0.2593 | 376 | 6 | 0.1516 | 0.1747 | 0.87 | oui |
| +1.0 | +0.2593 | +0.5187 | 248 | 4 | 0.1000 | 0.1598 | 0.63 | oui |
| +2.0 | +0.5187 | +∞ | 178 | 3 | 0.0717 | 0.0668 | 1.07 | oui |

---

## 6. TEST D'ASYMÉTRIE — DÉFINITION UNIQUE (R-030), L'ESPÉRANCE DÉCIDE

> Test d'admission : **espérance calculée sur la grille symétrique complète, les deux queues incluses**. Le rapport gain maximal / perte maximale est publié **pour information** et ne peut fonder aucune admission seul (T-001, faute E-018). Le rapport gain maximal / perte du scénario central est **interdit**. Une seule formulation, appliquée à tous les candidats, position détenue comprise.

| candidat | verdict | espérance % NAV | sans dérive | 1re moitié | 2e moitié | gain max | perte max | ratio (info) | critères échoués |
|---|:---:|---:|---:|---:|---:|---:|---:|---:|---|
| M005-DCOILBRENTEU-HAUSSE-ALIGNE | REFUSEE | +0.281 | +0.129 | +0.254 | +0.233 | +5.10 | -3.22 | 1.59:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DCOILBRENTEU-HAUSSE-CONTRARIEN | REFUSEE | +0.281 | +0.129 | +0.254 | +0.233 | +5.10 | -3.22 | 1.59:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DCOILBRENTEU-BAISSE-ALIGNE | REFUSEE | -0.281 | -0.129 | -0.254 | -0.233 | +3.22 | -5.10 | 0.63:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILBRENTEU-BAISSE-CONTRARIEN | REFUSEE | -0.281 | -0.129 | -0.254 | -0.233 | +3.22 | -5.10 | 0.63:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-HAUSSE-ALIGNE | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-HAUSSE-CONTRARIEN | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-BAISSE-ALIGNE | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-BAISSE-CONTRARIEN | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-HAUSSE-ALIGNE | REFUSEE | -0.006 | -0.067 | -0.081 | +0.037 | +0.62 | -0.71 | 0.87:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-HAUSSE-CONTRARIEN | REFUSEE | -0.006 | -0.067 | -0.081 | +0.037 | +0.62 | -0.71 | 0.87:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-BAISSE-ALIGNE | REFUSEE | +0.006 | +0.067 | +0.081 | -0.037 | +0.71 | -0.62 | 1.15:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-BAISSE-CONTRARIEN | REFUSEE | +0.006 | +0.067 | +0.081 | -0.037 | +0.71 | -0.62 | 1.15:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-HAUSSE-ALIGNE | REFUSEE | -0.059 | -0.074 | -0.029 | -0.071 | +0.49 | -0.60 | 0.82:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-HAUSSE-CONTRARIEN | REFUSEE | -0.059 | -0.074 | -0.029 | -0.071 | +0.49 | -0.60 | 0.82:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-BAISSE-ALIGNE | REFUSEE | +0.059 | +0.074 | +0.029 | +0.071 | +0.60 | -0.49 | 1.22:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DEXUSEU-BAISSE-CONTRARIEN | REFUSEE | +0.059 | +0.074 | +0.029 | +0.071 | +0.60 | -0.49 | 1.22:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DGS10-HAUSSE-ALIGNE | REFUSEE | +0.009 | -0.025 | -0.052 | +0.061 | +0.48 | -0.57 | 0.85:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-HAUSSE-CONTRARIEN | REFUSEE | +0.009 | -0.025 | -0.052 | +0.061 | +0.48 | -0.57 | 0.85:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-BAISSE-ALIGNE | REFUSEE | -0.009 | +0.025 | +0.052 | -0.061 | +0.57 | -0.48 | 1.18:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-BAISSE-CONTRARIEN | REFUSEE | -0.009 | +0.025 | +0.052 | -0.061 | +0.57 | -0.48 | 1.18:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-HAUSSE-ALIGNE | REFUSEE | -0.004 | -0.014 | -0.021 | +0.007 | +0.13 | -0.17 | 0.80:1 | 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-HAUSSE-CONTRARIEN | REFUSEE | -0.004 | -0.014 | -0.021 | +0.007 | +0.13 | -0.17 | 0.80:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-BAISSE-ALIGNE | REFUSEE | +0.004 | +0.014 | +0.021 | -0.007 | +0.17 | -0.13 | 1.25:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-BAISSE-CONTRARIEN | REFUSEE | +0.004 | +0.014 | +0.021 | -0.007 | +0.17 | -0.13 | 1.25:1 | 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-HAUSSE-ALIGNE | REFUSEE | +0.015 | -0.040 | -0.102 | +0.133 | +0.77 | -0.97 | 0.80:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-HAUSSE-CONTRARIEN | REFUSEE | +0.015 | -0.040 | -0.102 | +0.133 | +0.77 | -0.97 | 0.80:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-BAISSE-ALIGNE | REFUSEE | -0.015 | +0.040 | +0.102 | -0.133 | +0.97 | -0.77 | 1.26:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-BAISSE-CONTRARIEN | REFUSEE | -0.015 | +0.040 | +0.102 | -0.133 | +0.97 | -0.77 | 1.26:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-HAUSSE-ALIGNE | REFUSEE | -0.068 | -0.072 | -0.086 | -0.054 | +0.35 | -0.47 | 0.73:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-HAUSSE-CONTRARIEN | REFUSEE | -0.068 | -0.072 | -0.086 | -0.054 | +0.35 | -0.47 | 0.73:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-BAISSE-ALIGNE | REFUSEE | +0.068 | +0.072 | +0.086 | +0.054 | +0.47 | -0.35 | 1.36:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DTWEXBGS-BAISSE-CONTRARIEN | REFUSEE | +0.068 | +0.072 | +0.086 | +0.054 | +0.47 | -0.35 | 1.36:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-HAUSSE-ALIGNE | REFUSEE | +0.305 | -0.034 | +0.448 | +0.187 | +1.48 | -1.37 | 1.08:1 | 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-HAUSSE-CONTRARIEN | REFUSEE | +0.305 | -0.034 | +0.448 | +0.187 | +1.48 | -1.37 | 1.08:1 | 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-BAISSE-ALIGNE | REFUSEE | -0.305 | +0.034 | -0.448 | -0.187 | +1.37 | -1.48 | 0.93:1 | 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-NASDAQ100-BAISSE-CONTRARIEN | REFUSEE | -0.305 | +0.034 | -0.448 | -0.187 | +1.37 | -1.48 | 0.93:1 | 12_esperance_positive, 13_esperance_non_portee_par_derive, 14_esperance_stable_dans_le_temps |
| M005-SP500-HAUSSE-ALIGNE | REFUSEE | +0.185 | -0.043 | +0.211 | +0.153 | +1.11 | -1.11 | 1.00:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-SP500-HAUSSE-CONTRARIEN | REFUSEE | +0.185 | -0.043 | +0.211 | +0.153 | +1.11 | -1.11 | 1.00:1 | 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-SP500-BAISSE-ALIGNE | REFUSEE | -0.185 | +0.043 | -0.211 | -0.153 | +1.11 | -1.11 | 1.00:1 | 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-SP500-BAISSE-CONTRARIEN | REFUSEE | -0.185 | +0.043 | -0.211 | -0.153 | +1.11 | -1.11 | 1.00:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |

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

- `BAMLC0A0CM` : percentile REFUSÉ sur 5 ans — profondeur réelle 784 obs / 2.99 ans (début 2023-10-31). R-011 : un percentile calculé sur une série tronquée est sans valeur.
- `BAMLH0A0HYM2` : percentile REFUSÉ sur 5 ans — profondeur réelle 785 obs / 2.99 ans (début 2023-10-31). R-011 : un percentile calculé sur une série tronquée est sans valeur.
- `BAMLH0A0HYM2` : instrument NON ADMISSIBLE — P&L non calculable depuis le dépôt : l'OAS est un spread, et le dépôt ne contient pas le rendement de l'indice, donc pas la duration de spread. Aucune valeur ne peut être produite sans un chiffre extérieur aux données (E-002).
- `BAMLC0A0CM` : instrument NON ADMISSIBLE — P&L non calculable depuis le dépôt : l'OAS est un spread, et le dépôt ne contient pas le rendement de l'indice, donc pas la duration de spread. Aucune valeur ne peut être produite sans un chiffre extérieur aux données (E-002).
- Retards sur la date d'arrêté unique (E-014) : DCOILBRENTEU 1 séance(s), DCOILWTICO 1 séance(s), DEXJPUS 3 séance(s), DEXUSEU 3 séance(s), DTWEXBGS 3 séance(s)

**Vérification tierce (R-032) : NON SATISFAITE pour ce brief.** Le moteur ne dispose d'aucune source extérieure au dépôt. Trois estimateurs **internes** de σ sont publiés côte à côte au §5 ; ce sont des contrôles de cohérence interne, **pas** une vérification tierce, et ils ne sont pas présentés comme telle.

**Ce que ce moteur ne peut pas faire.** Il ne prouve aucune capacité prédictive : la règle de confirmation est une règle de percentile, déclarée et symétrique, pas un modèle validé hors échantillon. Il ne corrige pas la multiplicité : 40 candidats sont évalués et aucune pénalité de sélection n'est appliquée à l'espérance — c'est une limite déclarée, pas un oubli. Il ne voit ni les événements politiques, ni les décisions de banques centrales : le dépôt ne contient que des séries FRED, et toute affirmation de politique monétaire non adossée à `DFF` est refusée (critère 15, faute E-006).

---

*Fin du brief 005. Produit mécaniquement. Ne constitue pas un conseil en investissement.*