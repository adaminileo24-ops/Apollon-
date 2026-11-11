# BRIEF MACRO n° 005 — arrêté au 2026-11-09

*Produit par `apollon_macro.py` le 2026-11-11T00:15:31+00:00. Aucune valeur de ce document n'est saisie à la main : chacune porte sa série, sa date et sa profondeur. Bloc à copier tel quel.*

**Grille de scénarios (R-029, §11), déclarée avant toute lecture de données et empreintée :** `[-2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0]` · empreinte SHA-256 `6aaeb3863c875923…` · symétrique : True · horizon 60 séances (3 mois pour les séries mensuelles).

---

## 1. CONCLUSION, ÉNONCÉE D'ABORD

**40 candidats déclarés d'avance (10 instruments × 2 directions × 2 règles de confirmation). 40 évalués. 0 thèse(s) survivent aux quinze critères.**

**Abstention. Aucune thèse ne survit.** Ce n'est pas un silence : c'est un résultat, produit par le même portier que celui qui aurait admis une thèse. Le détail des échecs, critère par critère, figure au §6. La Section Macro ne transmet rien à la Section Risque ce cycle.

**Position détenue (contrôle 9, E-020) — 100 % cash, testée sur la même grille.** Espérance excédentaire du cash : +0.000 % de NAV. Référence 60/40 : +1.303 % (hors dérive : -0.224 %). **Écart du cash contre la référence : -1.303 % de NAV** sur 60 séances.

---

## 2. CE QUI A CHANGÉ — MÉCANISME, PAS CONTENU

Fait, étiqueté : les briefs 001 à 004 étaient rédigés par un agent. Celui-ci est produit par un moteur. Le paramètre libre de la Section Macro — la grille de scénarios — n'est plus accessible à l'agent : il est déclaré en tête de fichier, symétrique par construction, et son empreinte SHA-256 est vérifiée avant chaque usage. Sur le brief 004, ce paramètre avait porté le ratio annoncé de 1,29:1 à 3,0:1.

---

## 3. M1 · M2 · M3 · M4 — ÉTAT DES SÉRIES (FAIT)

Toutes les valeurs sont des FAITS lus dans le dépôt. Le retard est compté en séances ouvrées depuis la date d'arrêté unique. Les couples obligatoires sont vérifiés par le rendu : ce bloc ne peut pas être émis si un membre d'un couple manque.

| série | rôle déclaré | valeur | date | retard | n obs | profondeur | pct 1 an | pct 5 ans | pct complet |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| BAMLC0A0CM | risque_credit_ig | 0.91 | 2026-11-09 | 0 | 783 | 2.99 ans | 96.4 | REFUSÉ (insuffisante, -38 %) | 67.9 |
| BAMLH0A0HYM2 | risque_credit_hy | 3.34 | 2026-11-09 | 0 | 784 | 2.99 ans | 96.4 | REFUSÉ (insuffisante, -38 %) | 83.7 |
| CPIAUCSL | inflation_globale | 337.5 | 2026-10-01 | 39 | 119 | 9.91 ans | 100.0 | 100.0 | 100.0 |
| CPILFESL | inflation_sous_jacente | 339.9 | 2026-10-01 | 39 | 119 | 9.91 ans | 100.0 | 100.0 | 100.0 |
| DCOILBRENTEU | prix_energie | 107 | 2026-11-03 | 4 | 2529 | 9.97 ans | 70.2 | 87.3 | 93.7 |
| DCOILWTICO | prix_energie_wti | 99.64 | 2026-11-03 | 4 | 2493 | 9.97 ans | 81.3 | 89.2 | 94.5 |
| DEXJPUS | devise_usdjpy | 158.2 | 2026-11-06 | 1 | 2493 | 9.98 ans | 52.8 | 89.2 | 94.5 |
| DEXUSEU | devise_eurusd | 1.115 | 2026-11-06 | 1 | 2493 | 9.98 ans | 1.6 | 61.5 | 44.2 |
| DFF | politique_monetaire | 3.88 | 2026-11-09 | 0 | 3649 | 9.99 ans | 100.0 | 28.8 | 70.9 |
| DFII10 | taux_reel_10a | 2.66 | 2026-11-09 | 0 | 2497 | 9.98 ans | 90.9 | 98.2 | 99.1 |
| DGS10 | taux_nominal_10a | 4.88 | 2026-11-09 | 0 | 2497 | 9.98 ans | 84.5 | 96.6 | 98.3 |
| DGS2 | taux_nominal_2a | 4.56 | 2026-11-09 | 0 | 2497 | 9.98 ans | 85.3 | 77.9 | 88.8 |
| DGS30 | taux_nominal_30a | 5.26 | 2026-11-09 | 0 | 2497 | 9.98 ans | 81.7 | 96.3 | 98.2 |
| DTWEXBGS | dollar_large | 121.9 | 2026-11-06 | 1 | 2491 | 9.98 ans | 99.2 | 68.4 | 82.1 |
| INDPRO | activite_industrielle | 104 | 2026-09-01 | 69 | 119 | 9.83 ans | 100.0 | 100.0 | 95.8 |
| NASDAQ100 | prix_actions_tech | 2.791e+04 | 2026-11-09 | 0 | 2511 | 9.98 ans | 50.0 | 90.0 | 95.0 |
| OVXCLS | volatilite_implicite_petrole | 57.2 | 2026-11-09 | 0 | 2512 | 9.98 ans | 58.7 | 88.9 | 90.9 |
| PAYEMS | emploi | 1.593e+05 | 2026-10-01 | 39 | 120 | 9.91 ans | 100.0 | 100.0 | 100.0 |
| SP500 | prix_actions | 7550 | 2026-11-09 | 0 | 2510 | 9.98 ans | 70.2 | 94.0 | 97.0 |
| T10Y2Y | pente_courbe | 0.32 | 2026-11-09 | 0 | 2497 | 9.98 ans | 10.3 | 60.3 | 47.1 |
| T10YIE | point_mort_10a | 2.22 | 2026-11-09 | 0 | 2497 | 9.98 ans | 4.8 | 13.1 | 49.8 |
| T5YIFR | point_mort_5a5a | 2.19 | 2026-11-09 | 0 | 2497 | 9.98 ans | 36.5 | 21.3 | 51.9 |
| UNRATE | chomage | 4.1 | 2026-10-01 | 39 | 119 | 9.91 ans | 25.0 | 66.7 | 56.3 |
| VIXCLS | volatilite_implicite | 19.92 | 2026-11-09 | 0 | 2543 | 9.98 ans | 81.0 | 67.1 | 68.5 |
| VXDCLS | volatilite_implicite_dow | 17.42 | 2026-11-09 | 0 | 2513 | 9.98 ans | 76.6 | 63.1 | 61.8 |
| VXVCLS | volatilite_implicite_3m | 20.85 | 2026-11-09 | 0 | 2510 | 9.98 ans | 71.0 | 58.5 | 62.2 |

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
- corrélation des variations à 60 séances : BAMLC0A0CM / BAMLH0A0HYM2 = +0.939 sur 723 points (seuil 0.9)
- corrélation des variations à 60 séances : DGS10 / DGS30 = +0.966 sur 2437 points (seuil 0.9)
- corrélation des variations à 60 séances : INDPRO / PAYEMS = +0.913 sur 116 points (seuil 0.9)
- corrélation des variations à 60 séances : INDPRO / UNRATE = -0.917 sur 115 points (seuil 0.9)
- corrélation des variations à 60 séances : NASDAQ100 / SP500 = +0.904 sur 2450 points (seuil 0.9)
- corrélation des variations à 60 séances : PAYEMS / UNRATE = -0.983 sur 116 points (seuil 0.9)
- corrélation des variations à 60 séances : VIXCLS / VXDCLS = +0.929 sur 2450 points (seuil 0.9)
- corrélation des variations à 60 séances : VIXCLS / VXVCLS = +0.958 sur 2450 points (seuil 0.9)
- corrélation des variations à 60 séances : VXDCLS / VXVCLS = +0.933 sur 2450 points (seuil 0.9)

---

## 5. GRILLE, σ MESURÉ, ET DOUBLE CONFRONTATION DES PROBABILITÉS

σ est **mesuré** sur chaque série, jamais choisi. Les probabilités sont les **fréquences historiques** dans chaque bande, jamais un jugement. L'effectif de chaque bande est publié ; sous 20 observations la bande est déclarée NON ESTIMABLE. La colonne « emp./gauss. » est la double confrontation exigée par §11.5 : tout écart supérieur à un facteur 2 est déclaré (⚠).

**BAMLH0A0HYM2** (niveau) — σ à 60 pas = **0.44800** · estimateurs croisés : racine-h 0.53735, blocs disjoints 0.39380 (écart relatif 36.5 %) · dérive d'échantillon -0.05477 (-0.12 σ) · 724 variations chevauchantes, 12 blocs indépendants · 2023-11-13 → 2026-11-09

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.6720 | 37 | 1 | 0.0511 | 0.0668 | 0.76 | oui |
| -1.0 | -0.6720 | -0.3360 | 111 | 2 | 0.1533 | 0.1598 | 0.96 | oui |
| -0.5 | -0.3360 | -0.1120 | 189 | 3 | 0.2610 | 0.1747 | 1.49 | oui |
| +0.0 | -0.1120 | +0.1120 | 195 | 3 | 0.2693 | 0.1974 | 1.36 | oui |
| +0.5 | +0.1120 | +0.3360 | 80 | 1 | 0.1105 | 0.1747 | 0.63 | oui |
| +1.0 | +0.3360 | +0.6720 | 78 | 1 | 0.1077 | 0.1598 | 0.67 | oui |
| +2.0 | +0.6720 | +∞ | 34 | 1 | 0.0470 | 0.0668 | 0.70 | oui |

**DCOILBRENTEU** (log) — σ à 60 pas = **0.24936** · estimateurs croisés : racine-h 0.25064, blocs disjoints 0.19754 (écart relatif 26.9 %) · dérive d'échantillon +0.01848 (+0.07 σ) · 2469 variations chevauchantes, 41 blocs indépendants · 2016-11-14 → 2026-11-03

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.3740 | 83 | 1 | 0.0336 | 0.0668 | 0.50 | oui |
| -1.0 | -0.3740 | -0.1870 | 154 | 3 | 0.0624 | 0.1598 | 0.39 ⚠ | oui |
| -0.5 | -0.1870 | -0.0623 | 498 | 8 | 0.2017 | 0.1747 | 1.15 | oui |
| +0.0 | -0.0623 | +0.0623 | 774 | 13 | 0.3135 | 0.1974 | 1.59 | oui |
| +0.5 | +0.0623 | +0.1870 | 597 | 10 | 0.2418 | 0.1747 | 1.38 | oui |
| +1.0 | +0.1870 | +0.3740 | 221 | 4 | 0.0895 | 0.1598 | 0.56 | oui |
| +2.0 | +0.3740 | +∞ | 142 | 2 | 0.0575 | 0.0668 | 0.86 | oui |

**DCOILWTICO** — non scénarisable : convention log inapplicable : 1 observation(s) non strictement positive(s), minimum -36.98 le 2020-04-20. Le prix a été négatif : aucun log-rendement n'existe. La série est déclarée NON SCÉNARISABLE plutôt que corrigée en silence.

**DEXJPUS** (log) — σ à 60 pas = **0.04138** · estimateurs croisés : racine-h 0.04354, blocs disjoints 0.03535 (écart relatif 23.2 %) · dérive d'échantillon +0.00796 (+0.19 σ) · 2433 variations chevauchantes, 41 blocs indépendants · 2016-11-14 → 2026-11-06

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0621 | 108 | 2 | 0.0444 | 0.0668 | 0.66 | oui |
| -1.0 | -0.0621 | -0.0310 | 249 | 4 | 0.1023 | 0.1598 | 0.64 | oui |
| -0.5 | -0.0310 | -0.0103 | 390 | 6 | 0.1603 | 0.1747 | 0.92 | oui |
| +0.0 | -0.0103 | +0.0103 | 497 | 8 | 0.2043 | 0.1974 | 1.03 | oui |
| +0.5 | +0.0103 | +0.0310 | 532 | 9 | 0.2187 | 0.1747 | 1.25 | oui |
| +1.0 | +0.0310 | +0.0621 | 473 | 8 | 0.1944 | 0.1598 | 1.22 | oui |
| +2.0 | +0.0621 | +∞ | 184 | 3 | 0.0756 | 0.0668 | 1.13 | oui |

**DEXUSEU** (log) — σ à 60 pas = **0.03426** · estimateurs croisés : racine-h 0.03455, blocs disjoints 0.03413 (écart relatif 1.2 %) · dérive d'échantillon +0.00176 (+0.05 σ) · 2433 variations chevauchantes, 41 blocs indépendants · 2016-11-14 → 2026-11-06

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0514 | 130 | 2 | 0.0534 | 0.0668 | 0.80 | oui |
| -1.0 | -0.0514 | -0.0257 | 321 | 5 | 0.1319 | 0.1598 | 0.83 | oui |
| -0.5 | -0.0257 | -0.0086 | 510 | 8 | 0.2096 | 0.1747 | 1.20 | oui |
| +0.0 | -0.0086 | +0.0086 | 617 | 10 | 0.2536 | 0.1974 | 1.28 | oui |
| +0.5 | +0.0086 | +0.0257 | 321 | 5 | 0.1319 | 0.1747 | 0.76 | oui |
| +1.0 | +0.0257 | +0.0514 | 307 | 5 | 0.1262 | 0.1598 | 0.79 | oui |
| +2.0 | +0.0514 | +∞ | 227 | 4 | 0.0933 | 0.0668 | 1.40 | oui |

**DGS10** (niveau) — σ à 60 pas = **0.42116** · estimateurs croisés : racine-h 0.41461, blocs disjoints 0.43899 (écart relatif 5.9 %) · dérive d'échantillon +0.06260 (+0.15 σ) · 2437 variations chevauchantes, 41 blocs indépendants · 2016-11-14 → 2026-11-09

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.6317 | 123 | 2 | 0.0505 | 0.0668 | 0.76 | oui |
| -1.0 | -0.6317 | -0.3159 | 284 | 5 | 0.1165 | 0.1598 | 0.73 | oui |
| -0.5 | -0.3159 | -0.1053 | 371 | 6 | 0.1522 | 0.1747 | 0.87 | oui |
| +0.0 | -0.1053 | +0.1053 | 528 | 9 | 0.2167 | 0.1974 | 1.10 | oui |
| +0.5 | +0.1053 | +0.3159 | 561 | 9 | 0.2302 | 0.1747 | 1.32 | oui |
| +1.0 | +0.3159 | +0.6317 | 369 | 6 | 0.1514 | 0.1598 | 0.95 | oui |
| +2.0 | +0.6317 | +∞ | 201 | 3 | 0.0825 | 0.0668 | 1.23 | oui |

**DGS2** (niveau) — σ à 60 pas = **0.49667** · estimateurs croisés : racine-h 0.42326, blocs disjoints 0.49377 (écart relatif 17.3 %) · dérive d'échantillon +0.08406 (+0.17 σ) · 2437 variations chevauchantes, 41 blocs indépendants · 2016-11-14 → 2026-11-09

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.7450 | 115 | 2 | 0.0472 | 0.0668 | 0.71 | oui |
| -1.0 | -0.7450 | -0.3725 | 228 | 4 | 0.0936 | 0.1598 | 0.59 | oui |
| -0.5 | -0.3725 | -0.1242 | 323 | 5 | 0.1325 | 0.1747 | 0.76 | oui |
| +0.0 | -0.1242 | +0.1242 | 739 | 12 | 0.3032 | 0.1974 | 1.54 | oui |
| +0.5 | +0.1242 | +0.3725 | 469 | 8 | 0.1924 | 0.1747 | 1.10 | oui |
| +1.0 | +0.3725 | +0.7450 | 362 | 6 | 0.1485 | 0.1598 | 0.93 | oui |
| +2.0 | +0.7450 | +∞ | 201 | 3 | 0.0825 | 0.0668 | 1.23 | oui |

**DGS30** (niveau) — σ à 60 pas = **0.36352** · estimateurs croisés : racine-h 0.39134, blocs disjoints 0.38798 (écart relatif 7.7 %) · dérive d'échantillon +0.05705 (+0.16 σ) · 2437 variations chevauchantes, 41 blocs indépendants · 2016-11-14 → 2026-11-09

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.5453 | 128 | 2 | 0.0525 | 0.0668 | 0.79 | oui |
| -1.0 | -0.5453 | -0.2726 | 276 | 5 | 0.1133 | 0.1598 | 0.71 | oui |
| -0.5 | -0.2726 | -0.0909 | 338 | 6 | 0.1387 | 0.1747 | 0.79 | oui |
| +0.0 | -0.0909 | +0.0909 | 633 | 11 | 0.2597 | 0.1974 | 1.32 | oui |
| +0.5 | +0.0909 | +0.2726 | 469 | 8 | 0.1924 | 0.1747 | 1.10 | oui |
| +1.0 | +0.2726 | +0.5453 | 386 | 6 | 0.1584 | 0.1598 | 0.99 | oui |
| +2.0 | +0.5453 | +∞ | 207 | 3 | 0.0849 | 0.0668 | 1.27 | oui |

**DTWEXBGS** (log) — σ à 60 pas = **0.02570** · estimateurs croisés : racine-h 0.02390, blocs disjoints 0.02503 (écart relatif 7.5 %) · dérive d'échantillon +0.00052 (+0.02 σ) · 2431 variations chevauchantes, 41 blocs indépendants · 2016-11-14 → 2026-11-06

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0386 | 171 | 3 | 0.0703 | 0.0668 | 1.05 | oui |
| -1.0 | -0.0386 | -0.0193 | 378 | 6 | 0.1555 | 0.1598 | 0.97 | oui |
| -0.5 | -0.0193 | -0.0064 | 359 | 6 | 0.1477 | 0.1747 | 0.85 | oui |
| +0.0 | -0.0064 | +0.0064 | 551 | 9 | 0.2267 | 0.1974 | 1.15 | oui |
| +0.5 | +0.0064 | +0.0193 | 471 | 8 | 0.1937 | 0.1747 | 1.11 | oui |
| +1.0 | +0.0193 | +0.0386 | 296 | 5 | 0.1218 | 0.1598 | 0.76 | oui |
| +2.0 | +0.0386 | +∞ | 205 | 3 | 0.0843 | 0.0668 | 1.26 | oui |

**NASDAQ100** (log) — σ à 60 pas = **0.08888** · estimateurs croisés : racine-h 0.11225, blocs disjoints 0.09885 (écart relatif 26.3 %) · dérive d'échantillon +0.04368 (+0.49 σ) · 2451 variations chevauchantes, 41 blocs indépendants · 2016-11-14 → 2026-11-09

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.1333 | 108 | 2 | 0.0441 | 0.0668 | 0.66 | oui |
| -1.0 | -0.1333 | -0.0667 | 169 | 3 | 0.0690 | 0.1598 | 0.43 ⚠ | oui |
| -0.5 | -0.0667 | -0.0222 | 191 | 3 | 0.0779 | 0.1747 | 0.45 ⚠ | oui |
| +0.0 | -0.0222 | +0.0222 | 355 | 6 | 0.1448 | 0.1974 | 0.73 | oui |
| +0.5 | +0.0222 | +0.0667 | 595 | 10 | 0.2428 | 0.1747 | 1.39 | oui |
| +1.0 | +0.0667 | +0.1333 | 719 | 12 | 0.2933 | 0.1598 | 1.84 | oui |
| +2.0 | +0.1333 | +∞ | 314 | 5 | 0.1281 | 0.0668 | 1.92 | oui |

**SP500** (log) — σ à 60 pas = **0.06914** · estimateurs croisés : racine-h 0.08884, blocs disjoints 0.08229 (écart relatif 28.5 %) · dérive d'échantillon +0.03006 (+0.43 σ) · 2450 variations chevauchantes, 41 blocs indépendants · 2016-11-14 → 2026-11-09

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.1037 | 115 | 2 | 0.0469 | 0.0668 | 0.70 | oui |
| -1.0 | -0.1037 | -0.0519 | 160 | 3 | 0.0653 | 0.1598 | 0.41 ⚠ | oui |
| -0.5 | -0.0519 | -0.0173 | 179 | 3 | 0.0731 | 0.1747 | 0.42 ⚠ | oui |
| +0.0 | -0.0173 | +0.0173 | 298 | 5 | 0.1216 | 0.1974 | 0.62 | oui |
| +0.5 | +0.0173 | +0.0519 | 759 | 13 | 0.3098 | 0.1747 | 1.77 | oui |
| +1.0 | +0.0519 | +0.1037 | 729 | 12 | 0.2976 | 0.1598 | 1.86 | oui |
| +2.0 | +0.1037 | +∞ | 210 | 4 | 0.0857 | 0.0668 | 1.28 | oui |

**VIXCLS** (log) — σ à 60 pas = **0.34562** · estimateurs croisés : racine-h 0.61871, blocs disjoints 0.40073 (écart relatif 79.0 %) · dérive d'échantillon +0.00751 (+0.02 σ) · 2483 variations chevauchantes, 41 blocs indépendants · 2016-11-14 → 2026-11-09

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.5184 | 74 | 1 | 0.0298 | 0.0668 | 0.45 ⚠ | oui |
| -1.0 | -0.5184 | -0.2592 | 379 | 6 | 0.1526 | 0.1598 | 0.96 | oui |
| -0.5 | -0.2592 | -0.0864 | 600 | 10 | 0.2416 | 0.1747 | 1.38 | oui |
| +0.0 | -0.0864 | +0.0864 | 620 | 10 | 0.2497 | 0.1974 | 1.26 | oui |
| +0.5 | +0.0864 | +0.2592 | 378 | 6 | 0.1522 | 0.1747 | 0.87 | oui |
| +1.0 | +0.2592 | +0.5184 | 252 | 4 | 0.1015 | 0.1598 | 0.64 | oui |
| +2.0 | +0.5184 | +∞ | 180 | 3 | 0.0725 | 0.0668 | 1.09 | oui |

---

## 6. TEST D'ASYMÉTRIE — DÉFINITION UNIQUE (R-030), L'ESPÉRANCE DÉCIDE

> Test d'admission : **espérance calculée sur la grille symétrique complète, les deux queues incluses**. Le rapport gain maximal / perte maximale est publié **pour information** et ne peut fonder aucune admission seul (T-001, faute E-018). Le rapport gain maximal / perte du scénario central est **interdit**. Une seule formulation, appliquée à tous les candidats, position détenue comprise.

| candidat | verdict | espérance % NAV | sans dérive | 1re moitié | 2e moitié | gain max | perte max | ratio (info) | critères échoués |
|---|:---:|---:|---:|---:|---:|---:|---:|---:|---|
| M005-DCOILBRENTEU-HAUSSE-ALIGNE | REFUSEE | +0.278 | +0.128 | +0.249 | +0.242 | +5.10 | -3.22 | 1.59:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DCOILBRENTEU-HAUSSE-CONTRARIEN | REFUSEE | +0.278 | +0.128 | +0.249 | +0.242 | +5.10 | -3.22 | 1.59:1 | 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DCOILBRENTEU-BAISSE-ALIGNE | REFUSEE | -0.278 | -0.128 | -0.249 | -0.242 | +3.22 | -5.10 | 0.63:1 | 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILBRENTEU-BAISSE-CONTRARIEN | REFUSEE | -0.278 | -0.128 | -0.249 | -0.242 | +3.22 | -5.10 | 0.63:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-HAUSSE-ALIGNE | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-HAUSSE-CONTRARIEN | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-BAISSE-ALIGNE | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-BAISSE-CONTRARIEN | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-HAUSSE-ALIGNE | REFUSEE | -0.007 | -0.067 | -0.082 | +0.036 | +0.62 | -0.71 | 0.87:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-HAUSSE-CONTRARIEN | REFUSEE | -0.007 | -0.067 | -0.082 | +0.036 | +0.62 | -0.71 | 0.87:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-BAISSE-ALIGNE | REFUSEE | +0.007 | +0.067 | +0.082 | -0.036 | +0.71 | -0.62 | 1.15:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-BAISSE-CONTRARIEN | REFUSEE | +0.007 | +0.067 | +0.082 | -0.036 | +0.71 | -0.62 | 1.15:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-HAUSSE-ALIGNE | REFUSEE | -0.060 | -0.075 | -0.029 | -0.072 | +0.49 | -0.60 | 0.82:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-HAUSSE-CONTRARIEN | REFUSEE | -0.060 | -0.075 | -0.029 | -0.072 | +0.49 | -0.60 | 0.82:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-BAISSE-ALIGNE | REFUSEE | +0.060 | +0.075 | +0.029 | +0.072 | +0.60 | -0.49 | 1.22:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DEXUSEU-BAISSE-CONTRARIEN | REFUSEE | +0.060 | +0.075 | +0.029 | +0.072 | +0.60 | -0.49 | 1.22:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DGS10-HAUSSE-ALIGNE | REFUSEE | +0.013 | -0.022 | -0.050 | +0.064 | +0.49 | -0.57 | 0.86:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-HAUSSE-CONTRARIEN | REFUSEE | +0.013 | -0.022 | -0.050 | +0.064 | +0.49 | -0.57 | 0.86:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-BAISSE-ALIGNE | REFUSEE | -0.013 | +0.022 | +0.050 | -0.064 | +0.57 | -0.49 | 1.16:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-BAISSE-CONTRARIEN | REFUSEE | -0.013 | +0.022 | +0.050 | -0.064 | +0.57 | -0.49 | 1.16:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-HAUSSE-ALIGNE | REFUSEE | -0.002 | -0.012 | -0.019 | +0.009 | +0.14 | -0.17 | 0.82:1 | 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-HAUSSE-CONTRARIEN | REFUSEE | -0.002 | -0.012 | -0.019 | +0.009 | +0.14 | -0.17 | 0.82:1 | 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-BAISSE-ALIGNE | REFUSEE | +0.002 | +0.012 | +0.019 | -0.009 | +0.17 | -0.14 | 1.22:1 | 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-BAISSE-CONTRARIEN | REFUSEE | +0.002 | +0.012 | +0.019 | -0.009 | +0.17 | -0.14 | 1.22:1 | 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-HAUSSE-ALIGNE | REFUSEE | +0.017 | -0.037 | -0.103 | +0.136 | +0.78 | -0.98 | 0.80:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-HAUSSE-CONTRARIEN | REFUSEE | +0.017 | -0.037 | -0.103 | +0.136 | +0.78 | -0.98 | 0.80:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-BAISSE-ALIGNE | REFUSEE | -0.017 | +0.037 | +0.103 | -0.136 | +0.98 | -0.78 | 1.25:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-BAISSE-CONTRARIEN | REFUSEE | -0.017 | +0.037 | +0.103 | -0.136 | +0.98 | -0.78 | 1.25:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-HAUSSE-ALIGNE | REFUSEE | -0.068 | -0.072 | -0.087 | -0.053 | +0.35 | -0.47 | 0.73:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-HAUSSE-CONTRARIEN | REFUSEE | -0.068 | -0.072 | -0.087 | -0.053 | +0.35 | -0.47 | 0.73:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-BAISSE-ALIGNE | REFUSEE | +0.068 | +0.072 | +0.087 | +0.053 | +0.47 | -0.35 | 1.36:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DTWEXBGS-BAISSE-CONTRARIEN | REFUSEE | +0.068 | +0.072 | +0.087 | +0.053 | +0.47 | -0.35 | 1.36:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-HAUSSE-ALIGNE | REFUSEE | +0.300 | -0.036 | +0.448 | +0.191 | +1.48 | -1.38 | 1.08:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-HAUSSE-CONTRARIEN | REFUSEE | +0.300 | -0.036 | +0.448 | +0.191 | +1.48 | -1.38 | 1.08:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-BAISSE-ALIGNE | REFUSEE | -0.300 | +0.036 | -0.448 | -0.191 | +1.38 | -1.48 | 0.93:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-NASDAQ100-BAISSE-CONTRARIEN | REFUSEE | -0.300 | +0.036 | -0.448 | -0.191 | +1.38 | -1.48 | 0.93:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 14_esperance_stable_dans_le_temps |
| M005-SP500-HAUSSE-ALIGNE | REFUSEE | +0.182 | -0.044 | +0.210 | +0.154 | +1.11 | -1.11 | 1.00:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-SP500-HAUSSE-CONTRARIEN | REFUSEE | +0.182 | -0.044 | +0.210 | +0.154 | +1.11 | -1.11 | 1.00:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-SP500-BAISSE-ALIGNE | REFUSEE | -0.182 | +0.044 | -0.210 | -0.154 | +1.11 | -1.11 | 1.00:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-SP500-BAISSE-CONTRARIEN | REFUSEE | -0.182 | +0.044 | -0.210 | -0.154 | +1.11 | -1.11 | 1.00:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |

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
| 8_confirmations_independantes | 16 |
| 9_test_execute_et_vrai | 16 |
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

- `BAMLC0A0CM` : percentile REFUSÉ sur 5 ans — profondeur réelle 783 obs / 2.99 ans (début 2023-11-13). R-011 : un percentile calculé sur une série tronquée est sans valeur.
- `BAMLH0A0HYM2` : percentile REFUSÉ sur 5 ans — profondeur réelle 784 obs / 2.99 ans (début 2023-11-13). R-011 : un percentile calculé sur une série tronquée est sans valeur.
- `BAMLH0A0HYM2` : instrument NON ADMISSIBLE — P&L non calculable depuis le dépôt : l'OAS est un spread, et le dépôt ne contient pas le rendement de l'indice, donc pas la duration de spread. Aucune valeur ne peut être produite sans un chiffre extérieur aux données (E-002).
- `BAMLC0A0CM` : instrument NON ADMISSIBLE — P&L non calculable depuis le dépôt : l'OAS est un spread, et le dépôt ne contient pas le rendement de l'indice, donc pas la duration de spread. Aucune valeur ne peut être produite sans un chiffre extérieur aux données (E-002).
- Retards sur la date d'arrêté unique (E-014) : DCOILBRENTEU 4 séance(s), DCOILWTICO 4 séance(s), DEXJPUS 1 séance(s), DEXUSEU 1 séance(s), DTWEXBGS 1 séance(s)

**Vérification tierce (R-032) : NON SATISFAITE pour ce brief.** Le moteur ne dispose d'aucune source extérieure au dépôt. Trois estimateurs **internes** de σ sont publiés côte à côte au §5 ; ce sont des contrôles de cohérence interne, **pas** une vérification tierce, et ils ne sont pas présentés comme telle.

**Ce que ce moteur ne peut pas faire.** Il ne prouve aucune capacité prédictive : la règle de confirmation est une règle de percentile, déclarée et symétrique, pas un modèle validé hors échantillon. Il ne corrige pas la multiplicité : 40 candidats sont évalués et aucune pénalité de sélection n'est appliquée à l'espérance — c'est une limite déclarée, pas un oubli. Il ne voit ni les événements politiques, ni les décisions de banques centrales : le dépôt ne contient que des séries FRED, et toute affirmation de politique monétaire non adossée à `DFF` est refusée (critère 15, faute E-006).

---

*Fin du brief 005. Produit mécaniquement. Ne constitue pas un conseil en investissement.*