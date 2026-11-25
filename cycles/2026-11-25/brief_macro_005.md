# BRIEF MACRO n° 005 — arrêté au 2026-11-23

*Produit par `apollon_macro.py` le 2026-11-25T03:10:31+00:00. Aucune valeur de ce document n'est saisie à la main : chacune porte sa série, sa date et sa profondeur. Bloc à copier tel quel.*

**Grille de scénarios (R-029, §11), déclarée avant toute lecture de données et empreintée :** `[-2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0]` · empreinte SHA-256 `6aaeb3863c875923…` · symétrique : True · horizon 60 séances (3 mois pour les séries mensuelles).

---

## 1. CONCLUSION, ÉNONCÉE D'ABORD

**40 candidats déclarés d'avance (10 instruments × 2 directions × 2 règles de confirmation). 40 évalués. 0 thèse(s) survivent aux quinze critères.**

**Abstention. Aucune thèse ne survit.** Ce n'est pas un silence : c'est un résultat, produit par le même portier que celui qui aurait admis une thèse. Le détail des échecs, critère par critère, figure au §6. La Section Macro ne transmet rien à la Section Risque ce cycle.

**Position détenue (contrôle 9, E-020) — 100 % cash, testée sur la même grille.** Espérance excédentaire du cash : +0.000 % de NAV. Référence 60/40 : +1.275 % (hors dérive : -0.218 %). **Écart du cash contre la référence : -1.275 % de NAV** sur 60 séances.

---

## 2. CE QUI A CHANGÉ — MÉCANISME, PAS CONTENU

Fait, étiqueté : les briefs 001 à 004 étaient rédigés par un agent. Celui-ci est produit par un moteur. Le paramètre libre de la Section Macro — la grille de scénarios — n'est plus accessible à l'agent : il est déclaré en tête de fichier, symétrique par construction, et son empreinte SHA-256 est vérifiée avant chaque usage. Sur le brief 004, ce paramètre avait porté le ratio annoncé de 1,29:1 à 3,0:1.

---

## 3. M1 · M2 · M3 · M4 — ÉTAT DES SÉRIES (FAIT)

Toutes les valeurs sont des FAITS lus dans le dépôt. Le retard est compté en séances ouvrées depuis la date d'arrêté unique. Les couples obligatoires sont vérifiés par le rendu : ce bloc ne peut pas être émis si un membre d'un couple manque.

| série | rôle déclaré | valeur | date | retard | n obs | profondeur | pct 1 an | pct 5 ans | pct complet |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| BAMLC0A0CM | risque_credit_ig | 0.97 | 2026-11-23 | 0 | 783 | 2.99 ans | 99.6 | REFUSÉ (insuffisante, -38 %) | 85.1 |
| BAMLH0A0HYM2 | risque_credit_hy | 3.63 | 2026-11-23 | 0 | 784 | 2.99 ans | 99.6 | REFUSÉ (insuffisante, -38 %) | 94.6 |
| CPIAUCSL | inflation_globale | 337.5 | 2026-10-01 | 53 | 119 | 9.91 ans | 100.0 | 100.0 | 100.0 |
| CPILFESL | inflation_sous_jacente | 339.9 | 2026-10-01 | 53 | 119 | 9.91 ans | 100.0 | 100.0 | 100.0 |
| DCOILBRENTEU | prix_energie | 92.94 | 2026-11-17 | 4 | 2529 | 9.97 ans | 52.0 | 75.4 | 87.7 |
| DCOILWTICO | prix_energie_wti | 89.53 | 2026-11-17 | 4 | 2494 | 9.97 ans | 52.8 | 77.8 | 88.8 |
| DEXJPUS | devise_usdjpy | 158.8 | 2026-11-20 | 1 | 2493 | 9.98 ans | 57.1 | 90.3 | 95.1 |
| DEXUSEU | devise_eurusd | 1.098 | 2026-11-20 | 1 | 2493 | 9.98 ans | 1.2 | 54.5 | 35.0 |
| DFF | politique_monetaire | 3.88 | 2026-11-23 | 0 | 3649 | 9.99 ans | 100.0 | 29.9 | 70.9 |
| DFII10 | taux_reel_10a | 2.79 | 2026-11-23 | 0 | 2497 | 9.98 ans | 91.7 | 98.3 | 99.2 |
| DGS10 | taux_nominal_10a | 4.92 | 2026-11-23 | 0 | 2497 | 9.98 ans | 82.5 | 96.3 | 98.1 |
| DGS2 | taux_nominal_2a | 4.63 | 2026-11-23 | 0 | 2497 | 9.98 ans | 84.5 | 79.8 | 89.8 |
| DGS30 | taux_nominal_30a | 5.29 | 2026-11-23 | 0 | 2497 | 9.98 ans | 83.3 | 96.7 | 98.3 |
| DTWEXBGS | dollar_large | 123.6 | 2026-11-20 | 1 | 2491 | 9.98 ans | 100.0 | 82.9 | 90.6 |
| INDPRO | activite_industrielle | 102.2 | 2026-10-01 | 53 | 120 | 9.91 ans | 91.7 | 98.3 | 94.2 |
| NASDAQ100 | prix_actions_tech | 2.652e+04 | 2026-11-19 | 2 | 2510 | 9.97 ans | 40.9 | 88.2 | 94.1 |
| OVXCLS | volatilite_implicite_petrole | 49.19 | 2026-11-23 | 0 | 2513 | 9.98 ans | 33.7 | 75.2 | 81.8 |
| PAYEMS | emploi | 1.593e+05 | 2026-10-01 | 53 | 120 | 9.91 ans | 100.0 | 100.0 | 100.0 |
| SP500 | prix_actions | 7237 | 2026-11-23 | 0 | 2511 | 9.98 ans | 45.2 | 89.0 | 94.5 |
| T10Y2Y | pente_courbe | 0.29 | 2026-11-23 | 0 | 2497 | 9.98 ans | 7.5 | 58.3 | 45.1 |
| T10YIE | point_mort_10a | 2.13 | 2026-11-23 | 0 | 2497 | 9.98 ans | 0.4 | 2.5 | 41.3 |
| T5YIFR | point_mort_5a5a | 2.11 | 2026-11-23 | 0 | 2497 | 9.98 ans | 5.6 | 6.2 | 35.8 |
| UNRATE | chomage | 4.1 | 2026-10-01 | 53 | 119 | 9.91 ans | 25.0 | 66.7 | 56.3 |
| VIXCLS | volatilite_implicite | 26.62 | 2026-11-23 | 0 | 2544 | 9.98 ans | 95.6 | 89.5 | 88.8 |
| VXDCLS | volatilite_implicite_dow | 21.88 | 2026-11-23 | 0 | 2514 | 9.98 ans | 89.7 | 84.6 | 81.3 |
| VXVCLS | volatilite_implicite_3m | 25.5 | 2026-11-23 | 0 | 2511 | 9.98 ans | 92.9 | 82.1 | 81.2 |

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
- corrélation des variations à 60 séances : BAMLC0A0CM / BAMLH0A0HYM2 = +0.938 sur 723 points (seuil 0.9)
- corrélation des variations à 60 séances : DGS10 / DGS30 = +0.966 sur 2437 points (seuil 0.9)
- corrélation des variations à 60 séances : INDPRO / PAYEMS = +0.916 sur 117 points (seuil 0.9)
- corrélation des variations à 60 séances : INDPRO / UNRATE = -0.920 sur 116 points (seuil 0.9)
- corrélation des variations à 60 séances : NASDAQ100 / SP500 = +0.904 sur 2449 points (seuil 0.9)
- corrélation des variations à 60 séances : PAYEMS / UNRATE = -0.983 sur 116 points (seuil 0.9)
- corrélation des variations à 60 séances : VIXCLS / VXDCLS = +0.929 sur 2451 points (seuil 0.9)
- corrélation des variations à 60 séances : VIXCLS / VXVCLS = +0.958 sur 2451 points (seuil 0.9)
- corrélation des variations à 60 séances : VXDCLS / VXVCLS = +0.933 sur 2451 points (seuil 0.9)

---

## 5. GRILLE, σ MESURÉ, ET DOUBLE CONFRONTATION DES PROBABILITÉS

σ est **mesuré** sur chaque série, jamais choisi. Les probabilités sont les **fréquences historiques** dans chaque bande, jamais un jugement. L'effectif de chaque bande est publié ; sous 20 observations la bande est déclarée NON ESTIMABLE. La colonne « emp./gauss. » est la double confrontation exigée par §11.5 : tout écart supérieur à un facteur 2 est déclaré (⚠).

**BAMLH0A0HYM2** (niveau) — σ à 60 pas = **0.45394** · estimateurs croisés : racine-h 0.54223, blocs disjoints 0.75772 (écart relatif 66.9 %) · dérive d'échantillon -0.03692 (-0.08 σ) · 724 variations chevauchantes, 12 blocs indépendants · 2023-11-27 → 2026-11-23

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.6809 | 35 | 1 | 0.0483 | 0.0668 | 0.72 | oui |
| -1.0 | -0.6809 | -0.3405 | 98 | 2 | 0.1354 | 0.1598 | 0.85 | oui |
| -0.5 | -0.3405 | -0.1135 | 194 | 3 | 0.2680 | 0.1747 | 1.53 | oui |
| +0.0 | -0.1135 | +0.1135 | 195 | 3 | 0.2693 | 0.1974 | 1.36 | oui |
| +0.5 | +0.1135 | +0.3405 | 83 | 1 | 0.1146 | 0.1747 | 0.66 | oui |
| +1.0 | +0.3405 | +0.6809 | 81 | 1 | 0.1119 | 0.1598 | 0.70 | oui |
| +2.0 | +0.6809 | +∞ | 38 | 1 | 0.0525 | 0.0668 | 0.79 | oui |

**DCOILBRENTEU** (log) — σ à 60 pas = **0.24912** · estimateurs croisés : racine-h 0.25202, blocs disjoints 0.20798 (écart relatif 21.2 %) · dérive d'échantillon +0.01772 (+0.07 σ) · 2469 variations chevauchantes, 41 blocs indépendants · 2016-11-28 → 2026-11-17

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.3737 | 83 | 1 | 0.0336 | 0.0668 | 0.50 | oui |
| -1.0 | -0.3737 | -0.1868 | 155 | 3 | 0.0628 | 0.1598 | 0.39 ⚠ | oui |
| -0.5 | -0.1868 | -0.0623 | 498 | 8 | 0.2017 | 0.1747 | 1.15 | oui |
| +0.0 | -0.0623 | +0.0623 | 782 | 13 | 0.3167 | 0.1974 | 1.60 | oui |
| +0.5 | +0.0623 | +0.1868 | 591 | 10 | 0.2394 | 0.1747 | 1.37 | oui |
| +1.0 | +0.1868 | +0.3737 | 217 | 4 | 0.0879 | 0.1598 | 0.55 | oui |
| +2.0 | +0.3737 | +∞ | 143 | 2 | 0.0579 | 0.0668 | 0.87 | oui |

**DCOILWTICO** — non scénarisable : convention log inapplicable : 1 observation(s) non strictement positive(s), minimum -36.98 le 2020-04-20. Le prix a été négatif : aucun log-rendement n'existe. La série est déclarée NON SCÉNARISABLE plutôt que corrigée en silence.

**DEXJPUS** (log) — σ à 60 pas = **0.04135** · estimateurs croisés : racine-h 0.04346, blocs disjoints 0.03706 (écart relatif 17.3 %) · dérive d'échantillon +0.00787 (+0.19 σ) · 2433 variations chevauchantes, 41 blocs indépendants · 2016-11-28 → 2026-11-20

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0620 | 108 | 2 | 0.0444 | 0.0668 | 0.66 | oui |
| -1.0 | -0.0620 | -0.0310 | 249 | 4 | 0.1023 | 0.1598 | 0.64 | oui |
| -0.5 | -0.0310 | -0.0103 | 390 | 6 | 0.1603 | 0.1747 | 0.92 | oui |
| +0.0 | -0.0103 | +0.0103 | 504 | 8 | 0.2072 | 0.1974 | 1.05 | oui |
| +0.5 | +0.0103 | +0.0310 | 528 | 9 | 0.2170 | 0.1747 | 1.24 | oui |
| +1.0 | +0.0310 | +0.0620 | 470 | 8 | 0.1932 | 0.1598 | 1.21 | oui |
| +2.0 | +0.0620 | +∞ | 184 | 3 | 0.0756 | 0.0668 | 1.13 | oui |

**DEXUSEU** (log) — σ à 60 pas = **0.03441** · estimateurs croisés : racine-h 0.03457, blocs disjoints 0.03212 (écart relatif 7.6 %) · dérive d'échantillon +0.00158 (+0.05 σ) · 2433 variations chevauchantes, 41 blocs indépendants · 2016-11-28 → 2026-11-20

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0516 | 135 | 2 | 0.0555 | 0.0668 | 0.83 | oui |
| -1.0 | -0.0516 | -0.0258 | 322 | 5 | 0.1323 | 0.1598 | 0.83 | oui |
| -0.5 | -0.0258 | -0.0086 | 509 | 8 | 0.2092 | 0.1747 | 1.20 | oui |
| +0.0 | -0.0086 | +0.0086 | 613 | 10 | 0.2520 | 0.1974 | 1.28 | oui |
| +0.5 | +0.0086 | +0.0258 | 325 | 5 | 0.1336 | 0.1747 | 0.76 | oui |
| +1.0 | +0.0258 | +0.0516 | 303 | 5 | 0.1245 | 0.1598 | 0.78 | oui |
| +2.0 | +0.0516 | +∞ | 226 | 4 | 0.0929 | 0.0668 | 1.39 | oui |

**DGS10** (niveau) — σ à 60 pas = **0.42152** · estimateurs croisés : racine-h 0.41555, blocs disjoints 0.38800 (écart relatif 8.6 %) · dérive d'échantillon +0.06340 (+0.15 σ) · 2437 variations chevauchantes, 41 blocs indépendants · 2016-11-28 → 2026-11-23

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.6323 | 123 | 2 | 0.0505 | 0.0668 | 0.76 | oui |
| -1.0 | -0.6323 | -0.3161 | 284 | 5 | 0.1165 | 0.1598 | 0.73 | oui |
| -0.5 | -0.3161 | -0.1054 | 371 | 6 | 0.1522 | 0.1747 | 0.87 | oui |
| +0.0 | -0.1054 | +0.1054 | 525 | 9 | 0.2154 | 0.1974 | 1.09 | oui |
| +0.5 | +0.1054 | +0.3161 | 558 | 9 | 0.2290 | 0.1747 | 1.31 | oui |
| +1.0 | +0.3161 | +0.6323 | 375 | 6 | 0.1539 | 0.1598 | 0.96 | oui |
| +2.0 | +0.6323 | +∞ | 201 | 3 | 0.0825 | 0.0668 | 1.23 | oui |

**DGS2** (niveau) — σ à 60 pas = **0.49754** · estimateurs croisés : racine-h 0.42502, blocs disjoints 0.47179 (écart relatif 17.1 %) · dérive d'échantillon +0.08558 (+0.17 σ) · 2437 variations chevauchantes, 41 blocs indépendants · 2016-11-28 → 2026-11-23

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.7463 | 115 | 2 | 0.0472 | 0.0668 | 0.71 | oui |
| -1.0 | -0.7463 | -0.3732 | 228 | 4 | 0.0936 | 0.1598 | 0.59 | oui |
| -0.5 | -0.3732 | -0.1244 | 323 | 5 | 0.1325 | 0.1747 | 0.76 | oui |
| +0.0 | -0.1244 | +0.1244 | 737 | 12 | 0.3024 | 0.1974 | 1.53 | oui |
| +0.5 | +0.1244 | +0.3732 | 462 | 8 | 0.1896 | 0.1747 | 1.09 | oui |
| +1.0 | +0.3732 | +0.7463 | 371 | 6 | 0.1522 | 0.1598 | 0.95 | oui |
| +2.0 | +0.7463 | +∞ | 201 | 3 | 0.0825 | 0.0668 | 1.23 | oui |

**DGS30** (niveau) — σ à 60 pas = **0.36358** · estimateurs croisés : racine-h 0.39180, blocs disjoints 0.32655 (écart relatif 20.0 %) · dérive d'échantillon +0.05747 (+0.16 σ) · 2437 variations chevauchantes, 41 blocs indépendants · 2016-11-28 → 2026-11-23

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.5454 | 128 | 2 | 0.0525 | 0.0668 | 0.79 | oui |
| -1.0 | -0.5454 | -0.2727 | 276 | 5 | 0.1133 | 0.1598 | 0.71 | oui |
| -0.5 | -0.2727 | -0.0909 | 338 | 6 | 0.1387 | 0.1747 | 0.79 | oui |
| +0.0 | -0.0909 | +0.0909 | 625 | 10 | 0.2565 | 0.1974 | 1.30 | oui |
| +0.5 | +0.0909 | +0.2727 | 477 | 8 | 0.1957 | 0.1747 | 1.12 | oui |
| +1.0 | +0.2727 | +0.5454 | 386 | 6 | 0.1584 | 0.1598 | 0.99 | oui |
| +2.0 | +0.5454 | +∞ | 207 | 3 | 0.0849 | 0.0668 | 1.27 | oui |

**DTWEXBGS** (log) — σ à 60 pas = **0.02578** · estimateurs croisés : racine-h 0.02389, blocs disjoints 0.02290 (écart relatif 12.6 %) · dérive d'échantillon +0.00069 (+0.03 σ) · 2431 variations chevauchantes, 41 blocs indépendants · 2016-11-28 → 2026-11-20

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0387 | 168 | 3 | 0.0691 | 0.0668 | 1.03 | oui |
| -1.0 | -0.0387 | -0.0193 | 380 | 6 | 0.1563 | 0.1598 | 0.98 | oui |
| -0.5 | -0.0193 | -0.0064 | 352 | 6 | 0.1448 | 0.1747 | 0.83 | oui |
| +0.0 | -0.0064 | +0.0064 | 551 | 9 | 0.2267 | 0.1974 | 1.15 | oui |
| +0.5 | +0.0064 | +0.0193 | 471 | 8 | 0.1937 | 0.1747 | 1.11 | oui |
| +1.0 | +0.0193 | +0.0387 | 303 | 5 | 0.1246 | 0.1598 | 0.78 | oui |
| +2.0 | +0.0387 | +∞ | 206 | 3 | 0.0847 | 0.0668 | 1.27 | oui |

**NASDAQ100** (log) — σ à 60 pas = **0.08906** · estimateurs croisés : racine-h 0.11245, blocs disjoints 0.11154 (écart relatif 26.3 %) · dérive d'échantillon +0.04313 (+0.48 σ) · 2450 variations chevauchantes, 41 blocs indépendants · 2016-11-28 → 2026-11-19

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.1336 | 107 | 2 | 0.0437 | 0.0668 | 0.65 | oui |
| -1.0 | -0.1336 | -0.0668 | 175 | 3 | 0.0714 | 0.1598 | 0.45 ⚠ | oui |
| -0.5 | -0.0668 | -0.0223 | 194 | 3 | 0.0792 | 0.1747 | 0.45 ⚠ | oui |
| +0.0 | -0.0223 | +0.0223 | 355 | 6 | 0.1449 | 0.1974 | 0.73 | oui |
| +0.5 | +0.0223 | +0.0668 | 598 | 10 | 0.2441 | 0.1747 | 1.40 | oui |
| +1.0 | +0.0668 | +0.1336 | 709 | 12 | 0.2894 | 0.1598 | 1.81 | oui |
| +2.0 | +0.1336 | +∞ | 312 | 5 | 0.1273 | 0.0668 | 1.91 | oui |

**SP500** (log) — σ à 60 pas = **0.06927** · estimateurs croisés : racine-h 0.08943, blocs disjoints 0.09002 (écart relatif 30.0 %) · dérive d'échantillon +0.02961 (+0.43 σ) · 2451 variations chevauchantes, 41 blocs indépendants · 2016-11-28 → 2026-11-23

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.1039 | 115 | 2 | 0.0469 | 0.0668 | 0.70 | oui |
| -1.0 | -0.1039 | -0.0520 | 163 | 3 | 0.0665 | 0.1598 | 0.42 ⚠ | oui |
| -0.5 | -0.0520 | -0.0173 | 183 | 3 | 0.0747 | 0.1747 | 0.43 ⚠ | oui |
| +0.0 | -0.0173 | +0.0173 | 301 | 5 | 0.1228 | 0.1974 | 0.62 | oui |
| +0.5 | +0.0173 | +0.0520 | 762 | 13 | 0.3109 | 0.1747 | 1.78 | oui |
| +1.0 | +0.0520 | +0.1039 | 720 | 12 | 0.2938 | 0.1598 | 1.84 | oui |
| +2.0 | +0.1039 | +∞ | 207 | 3 | 0.0845 | 0.0668 | 1.26 | oui |

**VIXCLS** (log) — σ à 60 pas = **0.34676** · estimateurs croisés : racine-h 0.62257, blocs disjoints 0.39148 (écart relatif 79.5 %) · dérive d'échantillon +0.00970 (+0.03 σ) · 2484 variations chevauchantes, 41 blocs indépendants · 2016-11-28 → 2026-11-23

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.5201 | 74 | 1 | 0.0298 | 0.0668 | 0.45 ⚠ | oui |
| -1.0 | -0.5201 | -0.2601 | 374 | 6 | 0.1506 | 0.1598 | 0.94 | oui |
| -0.5 | -0.2601 | -0.0867 | 598 | 10 | 0.2407 | 0.1747 | 1.38 | oui |
| +0.0 | -0.0867 | +0.0867 | 618 | 10 | 0.2488 | 0.1974 | 1.26 | oui |
| +0.5 | +0.0867 | +0.2601 | 382 | 6 | 0.1538 | 0.1747 | 0.88 | oui |
| +1.0 | +0.2601 | +0.5201 | 255 | 4 | 0.1027 | 0.1598 | 0.64 | oui |
| +2.0 | +0.5201 | +∞ | 183 | 3 | 0.0737 | 0.0668 | 1.10 | oui |

---

## 6. TEST D'ASYMÉTRIE — DÉFINITION UNIQUE (R-030), L'ESPÉRANCE DÉCIDE

> Test d'admission : **espérance calculée sur la grille symétrique complète, les deux queues incluses**. Le rapport gain maximal / perte maximale est publié **pour information** et ne peut fonder aucune admission seul (T-001, faute E-018). Le rapport gain maximal / perte du scénario central est **interdit**. Une seule formulation, appliquée à tous les candidats, position détenue comprise.

| candidat | verdict | espérance % NAV | sans dérive | 1re moitié | 2e moitié | gain max | perte max | ratio (info) | critères échoués |
|---|:---:|---:|---:|---:|---:|---:|---:|---:|---|
| M005-DCOILBRENTEU-HAUSSE-ALIGNE | REFUSEE | +0.273 | +0.129 | +0.248 | +0.230 | +5.09 | -3.21 | 1.58:1 | 16_arete_conditionnelle_mesuree |
| M005-DCOILBRENTEU-HAUSSE-CONTRARIEN | REFUSEE | +0.273 | +0.129 | +0.248 | +0.230 | +5.09 | -3.21 | 1.58:1 | 16_arete_conditionnelle_mesuree |
| M005-DCOILBRENTEU-BAISSE-ALIGNE | REFUSEE | -0.273 | -0.129 | -0.248 | -0.230 | +3.21 | -5.09 | 0.63:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILBRENTEU-BAISSE-CONTRARIEN | REFUSEE | -0.273 | -0.129 | -0.248 | -0.230 | +3.21 | -5.09 | 0.63:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-HAUSSE-ALIGNE | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-HAUSSE-CONTRARIEN | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-BAISSE-ALIGNE | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-BAISSE-CONTRARIEN | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-HAUSSE-ALIGNE | REFUSEE | -0.008 | -0.067 | -0.080 | +0.036 | +0.62 | -0.71 | 0.87:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-HAUSSE-CONTRARIEN | REFUSEE | -0.008 | -0.067 | -0.080 | +0.036 | +0.62 | -0.71 | 0.87:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-BAISSE-ALIGNE | REFUSEE | +0.008 | +0.067 | +0.080 | -0.036 | +0.71 | -0.62 | 1.15:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-BAISSE-CONTRARIEN | REFUSEE | +0.008 | +0.067 | +0.080 | -0.036 | +0.71 | -0.62 | 1.15:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-HAUSSE-ALIGNE | REFUSEE | -0.061 | -0.075 | -0.031 | -0.075 | +0.50 | -0.61 | 0.82:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-HAUSSE-CONTRARIEN | REFUSEE | -0.061 | -0.075 | -0.031 | -0.075 | +0.50 | -0.61 | 0.82:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-BAISSE-ALIGNE | REFUSEE | +0.061 | +0.075 | +0.031 | +0.075 | +0.61 | -0.50 | 1.22:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DEXUSEU-BAISSE-CONTRARIEN | REFUSEE | +0.061 | +0.075 | +0.031 | +0.075 | +0.61 | -0.50 | 1.22:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DGS10-HAUSSE-ALIGNE | REFUSEE | +0.012 | -0.022 | -0.050 | +0.064 | +0.49 | -0.57 | 0.86:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-HAUSSE-CONTRARIEN | REFUSEE | +0.012 | -0.022 | -0.050 | +0.064 | +0.49 | -0.57 | 0.86:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-BAISSE-ALIGNE | REFUSEE | -0.012 | +0.022 | +0.050 | -0.064 | +0.57 | -0.49 | 1.17:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-BAISSE-CONTRARIEN | REFUSEE | -0.012 | +0.022 | +0.050 | -0.064 | +0.57 | -0.49 | 1.17:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-HAUSSE-ALIGNE | REFUSEE | -0.003 | -0.014 | -0.020 | +0.008 | +0.13 | -0.17 | 0.81:1 | 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-HAUSSE-CONTRARIEN | REFUSEE | -0.003 | -0.014 | -0.020 | +0.008 | +0.13 | -0.17 | 0.81:1 | 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-BAISSE-ALIGNE | REFUSEE | +0.003 | +0.014 | +0.020 | -0.008 | +0.17 | -0.13 | 1.24:1 | 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-BAISSE-CONTRARIEN | REFUSEE | +0.003 | +0.014 | +0.020 | -0.008 | +0.17 | -0.13 | 1.24:1 | 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-HAUSSE-ALIGNE | REFUSEE | +0.018 | -0.039 | -0.103 | +0.133 | +0.78 | -0.97 | 0.80:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-HAUSSE-CONTRARIEN | REFUSEE | +0.018 | -0.039 | -0.103 | +0.133 | +0.78 | -0.97 | 0.80:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-BAISSE-ALIGNE | REFUSEE | -0.018 | +0.039 | +0.103 | -0.133 | +0.97 | -0.78 | 1.25:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-BAISSE-CONTRARIEN | REFUSEE | -0.018 | +0.039 | +0.103 | -0.133 | +0.97 | -0.78 | 1.25:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-HAUSSE-ALIGNE | REFUSEE | -0.066 | -0.072 | -0.085 | -0.051 | +0.35 | -0.48 | 0.73:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-HAUSSE-CONTRARIEN | REFUSEE | -0.066 | -0.072 | -0.085 | -0.051 | +0.35 | -0.48 | 0.73:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-BAISSE-ALIGNE | REFUSEE | +0.066 | +0.072 | +0.085 | +0.051 | +0.48 | -0.35 | 1.36:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DTWEXBGS-BAISSE-CONTRARIEN | REFUSEE | +0.066 | +0.072 | +0.085 | +0.051 | +0.48 | -0.35 | 1.36:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-HAUSSE-ALIGNE | REFUSEE | +0.296 | -0.035 | +0.449 | +0.195 | +1.49 | -1.38 | 1.08:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-HAUSSE-CONTRARIEN | REFUSEE | +0.296 | -0.035 | +0.449 | +0.195 | +1.49 | -1.38 | 1.08:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-BAISSE-ALIGNE | REFUSEE | -0.296 | +0.035 | -0.449 | -0.195 | +1.38 | -1.49 | 0.93:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-NASDAQ100-BAISSE-CONTRARIEN | REFUSEE | -0.296 | +0.035 | -0.449 | -0.195 | +1.38 | -1.49 | 0.93:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 14_esperance_stable_dans_le_temps |
| M005-SP500-HAUSSE-ALIGNE | REFUSEE | +0.178 | -0.044 | +0.209 | +0.154 | +1.11 | -1.11 | 1.01:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-SP500-HAUSSE-CONTRARIEN | REFUSEE | +0.178 | -0.044 | +0.209 | +0.154 | +1.11 | -1.11 | 1.01:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-SP500-BAISSE-ALIGNE | REFUSEE | -0.178 | +0.044 | -0.209 | -0.154 | +1.11 | -1.11 | 0.99:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-SP500-BAISSE-CONTRARIEN | REFUSEE | -0.178 | +0.044 | -0.209 | -0.154 | +1.11 | -1.11 | 0.99:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |

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

- `BAMLC0A0CM` : percentile REFUSÉ sur 5 ans — profondeur réelle 783 obs / 2.99 ans (début 2023-11-27). R-011 : un percentile calculé sur une série tronquée est sans valeur.
- `BAMLH0A0HYM2` : percentile REFUSÉ sur 5 ans — profondeur réelle 784 obs / 2.99 ans (début 2023-11-27). R-011 : un percentile calculé sur une série tronquée est sans valeur.
- `BAMLH0A0HYM2` : instrument NON ADMISSIBLE — P&L non calculable depuis le dépôt : l'OAS est un spread, et le dépôt ne contient pas le rendement de l'indice, donc pas la duration de spread. Aucune valeur ne peut être produite sans un chiffre extérieur aux données (E-002).
- `BAMLC0A0CM` : instrument NON ADMISSIBLE — P&L non calculable depuis le dépôt : l'OAS est un spread, et le dépôt ne contient pas le rendement de l'indice, donc pas la duration de spread. Aucune valeur ne peut être produite sans un chiffre extérieur aux données (E-002).
- Retards sur la date d'arrêté unique (E-014) : DCOILBRENTEU 4 séance(s), DCOILWTICO 4 séance(s), DEXJPUS 1 séance(s), DEXUSEU 1 séance(s), DTWEXBGS 1 séance(s), NASDAQ100 2 séance(s)

**Vérification tierce (R-032) : NON SATISFAITE pour ce brief.** Le moteur ne dispose d'aucune source extérieure au dépôt. Trois estimateurs **internes** de σ sont publiés côte à côte au §5 ; ce sont des contrôles de cohérence interne, **pas** une vérification tierce, et ils ne sont pas présentés comme telle.

**Ce que ce moteur ne peut pas faire.** Il ne prouve aucune capacité prédictive : la règle de confirmation est une règle de percentile, déclarée et symétrique, pas un modèle validé hors échantillon. Il ne corrige pas la multiplicité : 40 candidats sont évalués et aucune pénalité de sélection n'est appliquée à l'espérance — c'est une limite déclarée, pas un oubli. Il ne voit ni les événements politiques, ni les décisions de banques centrales : le dépôt ne contient que des séries FRED, et toute affirmation de politique monétaire non adossée à `DFF` est refusée (critère 15, faute E-006).

---

*Fin du brief 005. Produit mécaniquement. Ne constitue pas un conseil en investissement.*