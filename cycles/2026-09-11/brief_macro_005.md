# BRIEF MACRO n° 005 — arrêté au 2026-09-09

*Produit par `apollon_macro.py` le 2026-09-11T09:41:34+00:00. Aucune valeur de ce document n'est saisie à la main : chacune porte sa série, sa date et sa profondeur. Bloc à copier tel quel.*

**Grille de scénarios (R-029, §11), déclarée avant toute lecture de données et empreintée :** `[-2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0]` · empreinte SHA-256 `6aaeb3863c875923…` · symétrique : True · horizon 60 séances (3 mois pour les séries mensuelles).

---

## 1. CONCLUSION, ÉNONCÉE D'ABORD

**40 candidats déclarés d'avance (10 instruments × 2 directions × 2 règles de confirmation). 40 évalués. 0 thèse(s) survivent aux quinze critères.**

**Abstention. Aucune thèse ne survit.** Ce n'est pas un silence : c'est un résultat, produit par le même portier que celui qui aurait admis une thèse. Le détail des échecs, critère par critère, figure au §6. La Section Macro ne transmet rien à la Section Risque ce cycle.

**Position détenue (contrôle 9, E-020) — 100 % cash, testée sur la même grille.** Espérance excédentaire du cash : +0.000 % de NAV. Référence 60/40 : +1.388 % (hors dérive : -0.159 %). **Écart du cash contre la référence : -1.388 % de NAV** sur 60 séances.

---

## 2. CE QUI A CHANGÉ — MÉCANISME, PAS CONTENU

Fait, étiqueté : les briefs 001 à 004 étaient rédigés par un agent. Celui-ci est produit par un moteur. Le paramètre libre de la Section Macro — la grille de scénarios — n'est plus accessible à l'agent : il est déclaré en tête de fichier, symétrique par construction, et son empreinte SHA-256 est vérifiée avant chaque usage. Sur le brief 004, ce paramètre avait porté le ratio annoncé de 1,29:1 à 3,0:1.

---

## 3. M1 · M2 · M3 · M4 — ÉTAT DES SÉRIES (FAIT)

Toutes les valeurs sont des FAITS lus dans le dépôt. Le retard est compté en séances ouvrées depuis la date d'arrêté unique. Les couples obligatoires sont vérifiés par le rendu : ce bloc ne peut pas être émis si un membre d'un couple manque.

| série | rôle déclaré | valeur | date | retard | n obs | profondeur | pct 1 an | pct 5 ans | pct complet |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| BAMLC0A0CM | risque_credit_ig | 0.81 | 2026-09-09 | 0 | 786 | 3.00 ans | 77.4 | REFUSÉ (insuffisante, -38 %) | 37.3 |
| BAMLH0A0HYM2 | risque_credit_hy | 2.71 | 2026-09-09 | 0 | 787 | 3.00 ans | 19.4 | REFUSÉ (insuffisante, -38 %) | 12.8 |
| CPIAUCSL | inflation_globale | 332.8 | 2026-07-01 | 70 | 118 | 9.83 ans | 91.7 | 98.3 | 99.2 |
| CPILFESL | inflation_sous_jacente | 336.8 | 2026-07-01 | 70 | 118 | 9.83 ans | 100.0 | 100.0 | 100.0 |
| DCOILBRENTEU | prix_energie | 109.5 | 2026-09-09 | 0 | 2534 | 9.99 ans | 87.3 | 91.7 | 95.9 |
| DCOILWTICO | prix_energie_wti | 97.26 | 2026-09-09 | 0 | 2498 | 9.99 ans | 85.3 | 89.0 | 94.5 |
| DEXJPUS | devise_usdjpy | 156.1 | 2026-09-04 | 3 | 2492 | 9.97 ans | 34.5 | 82.0 | 90.9 |
| DEXUSEU | devise_eurusd | 1.162 | 2026-09-04 | 3 | 2492 | 9.97 ans | 44.8 | 83.4 | 70.3 |
| DFF | politique_monetaire | 3.63 | 2026-09-09 | 0 | 3649 | 9.99 ans | 50.0 | 10.0 | 64.9 |
| DFII10 | taux_reel_10a | 2.46 | 2026-09-09 | 0 | 2497 | 9.99 ans | 99.6 | 99.6 | 99.8 |
| DGS10 | taux_nominal_10a | 4.83 | 2026-09-09 | 0 | 2497 | 9.99 ans | 100.0 | 99.3 | 99.6 |
| DGS2 | taux_nominal_2a | 4.43 | 2026-09-09 | 0 | 2497 | 9.99 ans | 100.0 | 76.5 | 88.1 |
| DGS30 | taux_nominal_30a | 5.28 | 2026-09-09 | 0 | 2497 | 9.99 ans | 99.6 | 99.9 | 100.0 |
| DTWEXBGS | dollar_large | 118.1 | 2026-09-04 | 3 | 2490 | 9.97 ans | 9.5 | 16.4 | 53.1 |
| INDPRO | activite_industrielle | 103 | 2026-07-01 | 70 | 119 | 9.83 ans | 100.0 | 100.0 | 92.4 |
| NASDAQ100 | prix_actions_tech | 2.942e+04 | 2026-09-09 | 0 | 2512 | 9.99 ans | 82.9 | 96.6 | 98.3 |
| OVXCLS | volatilite_implicite_petrole | 49.85 | 2026-09-09 | 0 | 2513 | 9.99 ans | 53.2 | 79.7 | 84.3 |
| PAYEMS | emploi | 1.591e+05 | 2026-08-01 | 39 | 120 | 9.91 ans | 100.0 | 100.0 | 100.0 |
| SP500 | prix_actions | 7636 | 2026-09-09 | 0 | 2511 | 9.99 ans | 90.5 | 98.1 | 99.0 |
| T10Y2Y | pente_courbe | 0.4 | 2026-09-09 | 0 | 2497 | 9.99 ans | 14.3 | 64.2 | 50.2 |
| T10YIE | point_mort_10a | 2.37 | 2026-09-09 | 0 | 2497 | 9.99 ans | 82.9 | 67.4 | 82.0 |
| T5YIFR | point_mort_5a5a | 2.33 | 2026-09-09 | 0 | 2497 | 9.99 ans | 96.8 | 78.3 | 88.8 |
| UNRATE | chomage | 4.1 | 2026-08-01 | 39 | 119 | 9.91 ans | 16.7 | 65.0 | 55.5 |
| VIXCLS | volatilite_implicite | 16.46 | 2026-09-09 | 0 | 2544 | 9.99 ans | 36.1 | 37.5 | 46.5 |
| VXDCLS | volatilite_implicite_dow | 15.5 | 2026-09-09 | 0 | 2514 | 9.99 ans | 43.3 | 41.8 | 46.1 |
| VXVCLS | volatilite_implicite_3m | 18.87 | 2026-09-09 | 0 | 2511 | 9.99 ans | 20.2 | 33.0 | 45.9 |

**Couples obligatoires contrôlés :** CPIAUCSL/CPILFESL, DGS10/DFII10, DGS10/T10YIE, BAMLH0A0HYM2/BAMLC0A0CM, UNRATE/PAYEMS, VIXCLS/SP500 — 0 manquement(s).

**Inflation en trois chiffres (contrôle 2, E-005).** Global +3.54 % sur un an (CPIAUCSL, 2026-07-01) · sous-jacent +2.79 % (CPILFESL) · **écart hors sous-jacent +75 pb**. Contribution énergie NON publiée : `CPIENGSL` est absente du dépôt. Lacune nommée avec le code FRED qui la comble (R-028) ; elle n'est pas présentée comme une limite de méthode. L'écart ci-dessus est l'écart global/sous-jacent, pas la contribution énergie.

---

## 4. IDENTITÉS COMPTABLES ET REDONDANCES (vérifiées numériquement)

| identité | vérifiable | n dates | résidu absolu max | tolérance | vérifiée |
|---|:---:|---:|---:|---:|:---:|
| T10YIE = DGS10 - DFII10 | oui | 2497 | 0.0000 | 0.02 | OUI |
| T10Y2Y = DGS10 - DGS2 | oui | 2497 | 0.0000 | 0.02 | OUI |

**Redondances détectées (11) — deux séries liées ne comptent jamais pour deux confirmations indépendantes :**

- identité comptable : T10YIE = DGS10 - DFII10 — T10YIE, DGS10, DFII10 (résidu max 0.0000)
- identité comptable : T10Y2Y = DGS10 - DGS2 — T10Y2Y, DGS10, DGS2 (résidu max 0.0000)
- corrélation des variations à 60 séances : BAMLC0A0CM / BAMLH0A0HYM2 = +0.938 sur 726 points (seuil 0.9)
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

**BAMLH0A0HYM2** (niveau) — σ à 60 pas = **0.45571** · estimateurs croisés : racine-h 0.53847, blocs disjoints 0.65564 (écart relatif 43.9 %) · dérive d'échantillon -0.11400 (-0.25 σ) · 727 variations chevauchantes, 12 blocs indépendants · 2023-09-11 → 2026-09-09

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.6836 | 55 | 1 | 0.0757 | 0.0668 | 1.13 | oui |
| -1.0 | -0.6836 | -0.3418 | 125 | 2 | 0.1719 | 0.1598 | 1.08 | oui |
| -0.5 | -0.3418 | -0.1139 | 192 | 3 | 0.2641 | 0.1747 | 1.51 | oui |
| +0.0 | -0.1139 | +0.1139 | 195 | 3 | 0.2682 | 0.1974 | 1.36 | oui |
| +0.5 | +0.1139 | +0.3418 | 80 | 1 | 0.1100 | 0.1747 | 0.63 | oui |
| +1.0 | +0.3418 | +0.6836 | 51 | 1 | 0.0702 | 0.1598 | 0.44 ⚠ | oui |
| +2.0 | +0.6836 | +∞ | 29 | 0 | 0.0399 | 0.0668 | 0.60 | oui |

**DCOILBRENTEU** (log) — σ à 60 pas = **0.24472** · estimateurs croisés : racine-h 0.24690, blocs disjoints 0.22117 (écart relatif 11.6 %) · dérive d'échantillon +0.01468 (+0.06 σ) · 2474 variations chevauchantes, 41 blocs indépendants · 2016-09-13 → 2026-09-09

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.3671 | 84 | 1 | 0.0340 | 0.0668 | 0.51 | oui |
| -1.0 | -0.3671 | -0.1835 | 156 | 3 | 0.0631 | 0.1598 | 0.39 ⚠ | oui |
| -0.5 | -0.1835 | -0.0612 | 503 | 8 | 0.2033 | 0.1747 | 1.16 | oui |
| +0.0 | -0.0612 | +0.0612 | 759 | 13 | 0.3068 | 0.1974 | 1.55 | oui |
| +0.5 | +0.0612 | +0.1835 | 624 | 10 | 0.2522 | 0.1747 | 1.44 | oui |
| +1.0 | +0.1835 | +0.3671 | 226 | 4 | 0.0914 | 0.1598 | 0.57 | oui |
| +2.0 | +0.3671 | +∞ | 122 | 2 | 0.0493 | 0.0668 | 0.74 | oui |

**DCOILWTICO** — non scénarisable : convention log inapplicable : 1 observation(s) non strictement positive(s), minimum -36.98 le 2020-04-20. Le prix a été négatif : aucun log-rendement n'existe. La série est déclarée NON SCÉNARISABLE plutôt que corrigée en silence.

**DEXJPUS** (log) — σ à 60 pas = **0.04336** · estimateurs croisés : racine-h 0.04388, blocs disjoints 0.04080 (écart relatif 7.5 %) · dérive d'échantillon +0.01030 (+0.24 σ) · 2432 variations chevauchantes, 41 blocs indépendants · 2016-09-13 → 2026-09-04

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0650 | 99 | 2 | 0.0407 | 0.0668 | 0.61 | oui |
| -1.0 | -0.0650 | -0.0325 | 218 | 4 | 0.0896 | 0.1598 | 0.56 | oui |
| -0.5 | -0.0325 | -0.0108 | 390 | 6 | 0.1604 | 0.1747 | 0.92 | oui |
| +0.0 | -0.0108 | +0.0108 | 509 | 8 | 0.2093 | 0.1974 | 1.06 | oui |
| +0.5 | +0.0108 | +0.0325 | 554 | 9 | 0.2278 | 0.1747 | 1.30 | oui |
| +1.0 | +0.0325 | +0.0650 | 470 | 8 | 0.1933 | 0.1598 | 1.21 | oui |
| +2.0 | +0.0650 | +∞ | 192 | 3 | 0.0789 | 0.0668 | 1.18 | oui |

**DEXUSEU** (log) — σ à 60 pas = **0.03481** · estimateurs croisés : racine-h 0.03469, blocs disjoints 0.03395 (écart relatif 2.5 %) · dérive d'échantillon +0.00122 (+0.03 σ) · 2432 variations chevauchantes, 41 blocs indépendants · 2016-09-13 → 2026-09-04

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0522 | 138 | 2 | 0.0567 | 0.0668 | 0.85 | oui |
| -1.0 | -0.0522 | -0.0261 | 321 | 5 | 0.1320 | 0.1598 | 0.83 | oui |
| -0.5 | -0.0261 | -0.0087 | 513 | 9 | 0.2109 | 0.1747 | 1.21 | oui |
| +0.0 | -0.0087 | +0.0087 | 609 | 10 | 0.2504 | 0.1974 | 1.27 | oui |
| +0.5 | +0.0087 | +0.0261 | 330 | 6 | 0.1357 | 0.1747 | 0.78 | oui |
| +1.0 | +0.0261 | +0.0522 | 302 | 5 | 0.1242 | 0.1598 | 0.78 | oui |
| +2.0 | +0.0522 | +∞ | 219 | 4 | 0.0900 | 0.0668 | 1.35 | oui |

**DGS10** (niveau) — σ à 60 pas = **0.42583** · estimateurs croisés : racine-h 0.41297, blocs disjoints 0.39779 (écart relatif 7.0 %) · dérive d'échantillon +0.06634 (+0.16 σ) · 2437 variations chevauchantes, 41 blocs indépendants · 2016-09-13 → 2026-09-09

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.6387 | 123 | 2 | 0.0505 | 0.0668 | 0.76 | oui |
| -1.0 | -0.6387 | -0.3194 | 284 | 5 | 0.1165 | 0.1598 | 0.73 | oui |
| -0.5 | -0.3194 | -0.1065 | 371 | 6 | 0.1522 | 0.1747 | 0.87 | oui |
| +0.0 | -0.1065 | +0.1065 | 528 | 9 | 0.2167 | 0.1974 | 1.10 | oui |
| +0.5 | +0.1065 | +0.3194 | 555 | 9 | 0.2277 | 0.1747 | 1.30 | oui |
| +1.0 | +0.3194 | +0.6387 | 360 | 6 | 0.1477 | 0.1598 | 0.92 | oui |
| +2.0 | +0.6387 | +∞ | 216 | 4 | 0.0886 | 0.0668 | 1.33 | oui |

**DGS2** (niveau) — σ à 60 pas = **0.49469** · estimateurs croisés : racine-h 0.41940, blocs disjoints 0.46933 (écart relatif 18.0 %) · dérive d'échantillon +0.08175 (+0.17 σ) · 2437 variations chevauchantes, 41 blocs indépendants · 2016-09-13 → 2026-09-09

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.7420 | 115 | 2 | 0.0472 | 0.0668 | 0.71 | oui |
| -1.0 | -0.7420 | -0.3710 | 228 | 4 | 0.0936 | 0.1598 | 0.59 | oui |
| -0.5 | -0.3710 | -0.1237 | 323 | 5 | 0.1325 | 0.1747 | 0.76 | oui |
| +0.0 | -0.1237 | +0.1237 | 739 | 12 | 0.3032 | 0.1974 | 1.54 | oui |
| +0.5 | +0.1237 | +0.3710 | 484 | 8 | 0.1986 | 0.1747 | 1.14 | oui |
| +1.0 | +0.3710 | +0.7420 | 350 | 6 | 0.1436 | 0.1598 | 0.90 | oui |
| +2.0 | +0.7420 | +∞ | 198 | 3 | 0.0812 | 0.0668 | 1.22 | oui |

**DGS30** (niveau) — σ à 60 pas = **0.36757** · estimateurs croisés : racine-h 0.39165, blocs disjoints 0.33539 (écart relatif 16.8 %) · dérive d'échantillon +0.06092 (+0.17 σ) · 2437 variations chevauchantes, 41 blocs indépendants · 2016-09-13 → 2026-09-09

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.5514 | 127 | 2 | 0.0521 | 0.0668 | 0.78 | oui |
| -1.0 | -0.5514 | -0.2757 | 277 | 5 | 0.1137 | 0.1598 | 0.71 | oui |
| -0.5 | -0.2757 | -0.0919 | 338 | 6 | 0.1387 | 0.1747 | 0.79 | oui |
| +0.0 | -0.0919 | +0.0919 | 629 | 10 | 0.2581 | 0.1974 | 1.31 | oui |
| +0.5 | +0.0919 | +0.2757 | 461 | 8 | 0.1892 | 0.1747 | 1.08 | oui |
| +1.0 | +0.2757 | +0.5514 | 390 | 6 | 0.1600 | 0.1598 | 1.00 | oui |
| +2.0 | +0.5514 | +∞ | 215 | 4 | 0.0882 | 0.0668 | 1.32 | oui |

**DTWEXBGS** (log) — σ à 60 pas = **0.02617** · estimateurs croisés : racine-h 0.02408, blocs disjoints 0.02540 (écart relatif 8.7 %) · dérive d'échantillon +0.00111 (+0.04 σ) · 2430 variations chevauchantes, 40 blocs indépendants · 2016-09-13 → 2026-09-04

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0392 | 157 | 3 | 0.0646 | 0.0668 | 0.97 | oui |
| -1.0 | -0.0392 | -0.0196 | 385 | 6 | 0.1584 | 0.1598 | 0.99 | oui |
| -0.5 | -0.0196 | -0.0065 | 353 | 6 | 0.1453 | 0.1747 | 0.83 | oui |
| +0.0 | -0.0065 | +0.0065 | 544 | 9 | 0.2239 | 0.1974 | 1.13 | oui |
| +0.5 | +0.0065 | +0.0196 | 463 | 8 | 0.1905 | 0.1747 | 1.09 | oui |
| +1.0 | +0.0196 | +0.0392 | 312 | 5 | 0.1284 | 0.1598 | 0.80 | oui |
| +2.0 | +0.0392 | +∞ | 216 | 4 | 0.0889 | 0.0668 | 1.33 | oui |

**NASDAQ100** (log) — σ à 60 pas = **0.08862** · estimateurs croisés : racine-h 0.11122, blocs disjoints 0.09015 (écart relatif 25.5 %) · dérive d'échantillon +0.04419 (+0.50 σ) · 2452 variations chevauchantes, 41 blocs indépendants · 2016-09-13 → 2026-09-09

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.1329 | 109 | 2 | 0.0445 | 0.0668 | 0.67 | oui |
| -1.0 | -0.1329 | -0.0665 | 166 | 3 | 0.0677 | 0.1598 | 0.42 ⚠ | oui |
| -0.5 | -0.0665 | -0.0222 | 183 | 3 | 0.0746 | 0.1747 | 0.43 ⚠ | oui |
| +0.0 | -0.0222 | +0.0222 | 362 | 6 | 0.1476 | 0.1974 | 0.75 | oui |
| +0.5 | +0.0222 | +0.0665 | 585 | 10 | 0.2386 | 0.1747 | 1.37 | oui |
| +1.0 | +0.0665 | +0.1329 | 731 | 12 | 0.2981 | 0.1598 | 1.87 | oui |
| +2.0 | +0.1329 | +∞ | 316 | 5 | 0.1289 | 0.0668 | 1.93 | oui |

**SP500** (log) — σ à 60 pas = **0.06915** · estimateurs croisés : racine-h 0.08843, blocs disjoints 0.06975 (écart relatif 27.9 %) · dérive d'échantillon +0.03075 (+0.44 σ) · 2451 variations chevauchantes, 41 blocs indépendants · 2016-09-13 → 2026-09-09

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.1037 | 115 | 2 | 0.0469 | 0.0668 | 0.70 | oui |
| -1.0 | -0.1037 | -0.0519 | 158 | 3 | 0.0645 | 0.1598 | 0.40 ⚠ | oui |
| -0.5 | -0.0519 | -0.0173 | 176 | 3 | 0.0718 | 0.1747 | 0.41 ⚠ | oui |
| +0.0 | -0.0173 | +0.0173 | 290 | 5 | 0.1183 | 0.1974 | 0.60 | oui |
| +0.5 | +0.0173 | +0.0519 | 745 | 12 | 0.3040 | 0.1747 | 1.74 | oui |
| +1.0 | +0.0519 | +0.1037 | 757 | 13 | 0.3089 | 0.1598 | 1.93 | oui |
| +2.0 | +0.1037 | +∞ | 210 | 4 | 0.0857 | 0.0668 | 1.28 | oui |

**VIXCLS** (log) — σ à 60 pas = **0.34699** · estimateurs croisés : racine-h 0.61329, blocs disjoints 0.30994 (écart relatif 97.9 %) · dérive d'échantillon +0.00273 (+0.01 σ) · 2484 variations chevauchantes, 41 blocs indépendants · 2016-09-13 → 2026-09-09

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.5205 | 77 | 1 | 0.0310 | 0.0668 | 0.46 ⚠ | oui |
| -1.0 | -0.5205 | -0.2602 | 391 | 7 | 0.1574 | 0.1598 | 0.98 | oui |
| -0.5 | -0.2602 | -0.0867 | 605 | 10 | 0.2436 | 0.1747 | 1.39 | oui |
| +0.0 | -0.0867 | +0.0867 | 613 | 10 | 0.2468 | 0.1974 | 1.25 | oui |
| +0.5 | +0.0867 | +0.2602 | 373 | 6 | 0.1502 | 0.1747 | 0.86 | oui |
| +1.0 | +0.2602 | +0.5205 | 248 | 4 | 0.0998 | 0.1598 | 0.62 | oui |
| +2.0 | +0.5205 | +∞ | 177 | 3 | 0.0713 | 0.0668 | 1.07 | oui |

---

## 6. TEST D'ASYMÉTRIE — DÉFINITION UNIQUE (R-030), L'ESPÉRANCE DÉCIDE

> Test d'admission : **espérance calculée sur la grille symétrique complète, les deux queues incluses**. Le rapport gain maximal / perte maximale est publié **pour information** et ne peut fonder aucune admission seul (T-001, faute E-018). Le rapport gain maximal / perte du scénario central est **interdit**. Une seule formulation, appliquée à tous les candidats, position détenue comprise.

| candidat | verdict | espérance % NAV | sans dérive | 1re moitié | 2e moitié | gain max | perte max | ratio (info) | critères échoués |
|---|:---:|---:|---:|---:|---:|---:|---:|---:|---|
| M005-DCOILBRENTEU-HAUSSE-ALIGNE | REFUSEE | +0.243 | +0.124 | +0.268 | +0.086 | +4.98 | -3.17 | 1.57:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DCOILBRENTEU-HAUSSE-CONTRARIEN | REFUSEE | +0.243 | +0.124 | +0.268 | +0.086 | +4.98 | -3.17 | 1.57:1 | 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DCOILBRENTEU-BAISSE-ALIGNE | REFUSEE | -0.243 | -0.124 | -0.268 | -0.086 | +3.17 | -4.98 | 0.64:1 | 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILBRENTEU-BAISSE-CONTRARIEN | REFUSEE | -0.243 | -0.124 | -0.268 | -0.086 | +3.17 | -4.98 | 0.64:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-HAUSSE-ALIGNE | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-HAUSSE-CONTRARIEN | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-BAISSE-ALIGNE | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-BAISSE-CONTRARIEN | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-HAUSSE-ALIGNE | REFUSEE | +0.012 | -0.063 | -0.058 | +0.057 | +0.66 | -0.73 | 0.89:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-HAUSSE-CONTRARIEN | REFUSEE | +0.012 | -0.063 | -0.058 | +0.057 | +0.66 | -0.73 | 0.89:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-BAISSE-ALIGNE | REFUSEE | -0.012 | +0.063 | +0.058 | -0.057 | +0.73 | -0.66 | 1.12:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-BAISSE-CONTRARIEN | REFUSEE | -0.012 | +0.063 | +0.058 | -0.057 | +0.73 | -0.66 | 1.12:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-HAUSSE-ALIGNE | REFUSEE | -0.059 | -0.070 | -0.033 | -0.070 | +0.51 | -0.61 | 0.84:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-HAUSSE-CONTRARIEN | REFUSEE | -0.059 | -0.070 | -0.033 | -0.070 | +0.51 | -0.61 | 0.84:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-BAISSE-ALIGNE | REFUSEE | +0.059 | +0.070 | +0.033 | +0.070 | +0.61 | -0.51 | 1.20:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DEXUSEU-BAISSE-CONTRARIEN | REFUSEE | +0.059 | +0.070 | +0.033 | +0.070 | +0.61 | -0.51 | 1.20:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DGS10-HAUSSE-ALIGNE | REFUSEE | +0.011 | -0.026 | -0.040 | +0.055 | +0.49 | -0.58 | 0.85:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-HAUSSE-CONTRARIEN | REFUSEE | +0.011 | -0.026 | -0.040 | +0.055 | +0.49 | -0.58 | 0.85:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-BAISSE-ALIGNE | REFUSEE | -0.011 | +0.026 | +0.040 | -0.055 | +0.58 | -0.49 | 1.18:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-BAISSE-CONTRARIEN | REFUSEE | -0.011 | +0.026 | +0.040 | -0.055 | +0.58 | -0.49 | 1.18:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-HAUSSE-ALIGNE | REFUSEE | -0.004 | -0.015 | -0.019 | +0.007 | +0.13 | -0.17 | 0.80:1 | 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-HAUSSE-CONTRARIEN | REFUSEE | -0.004 | -0.015 | -0.019 | +0.007 | +0.13 | -0.17 | 0.80:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-BAISSE-ALIGNE | REFUSEE | +0.004 | +0.015 | +0.019 | -0.007 | +0.17 | -0.13 | 1.26:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-BAISSE-CONTRARIEN | REFUSEE | +0.004 | +0.015 | +0.019 | -0.007 | +0.17 | -0.13 | 1.26:1 | 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-HAUSSE-ALIGNE | REFUSEE | +0.015 | -0.042 | -0.086 | +0.119 | +0.78 | -0.99 | 0.79:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-HAUSSE-CONTRARIEN | REFUSEE | +0.015 | -0.042 | -0.086 | +0.119 | +0.78 | -0.99 | 0.79:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-BAISSE-ALIGNE | REFUSEE | -0.015 | +0.042 | +0.086 | -0.119 | +0.99 | -0.78 | 1.27:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-BAISSE-CONTRARIEN | REFUSEE | -0.015 | +0.042 | +0.086 | -0.119 | +0.99 | -0.78 | 1.27:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-HAUSSE-ALIGNE | REFUSEE | -0.058 | -0.067 | -0.071 | -0.045 | +0.36 | -0.48 | 0.76:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-HAUSSE-CONTRARIEN | REFUSEE | -0.058 | -0.067 | -0.071 | -0.045 | +0.36 | -0.48 | 0.76:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-BAISSE-ALIGNE | REFUSEE | +0.058 | +0.067 | +0.071 | +0.045 | +0.48 | -0.36 | 1.32:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DTWEXBGS-BAISSE-CONTRARIEN | REFUSEE | +0.058 | +0.067 | +0.071 | +0.045 | +0.48 | -0.36 | 1.32:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-HAUSSE-ALIGNE | REFUSEE | +0.309 | -0.030 | +0.452 | +0.192 | +1.48 | -1.37 | 1.08:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-HAUSSE-CONTRARIEN | REFUSEE | +0.309 | -0.030 | +0.452 | +0.192 | +1.48 | -1.37 | 1.08:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-BAISSE-ALIGNE | REFUSEE | -0.309 | +0.030 | -0.452 | -0.192 | +1.37 | -1.48 | 0.92:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-NASDAQ100-BAISSE-CONTRARIEN | REFUSEE | -0.309 | +0.030 | -0.452 | -0.192 | +1.37 | -1.48 | 0.92:1 | 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-SP500-HAUSSE-ALIGNE | REFUSEE | +0.193 | -0.038 | +0.223 | +0.161 | +1.12 | -1.10 | 1.01:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-SP500-HAUSSE-CONTRARIEN | REFUSEE | +0.193 | -0.038 | +0.223 | +0.161 | +1.12 | -1.10 | 1.01:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-SP500-BAISSE-ALIGNE | REFUSEE | -0.193 | +0.038 | -0.223 | -0.161 | +1.10 | -1.12 | 0.99:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-SP500-BAISSE-CONTRARIEN | REFUSEE | -0.193 | +0.038 | -0.223 | -0.161 | +1.10 | -1.12 | 0.99:1 | 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |

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
| 8_confirmations_independantes | 26 |
| 9_test_execute_et_vrai | 26 |
| 10_invalidation_fait_date | 12 |
| 11_invalidation_non_deja_survenue | 22 |
| 12_esperance_positive | 22 |
| 13_esperance_non_portee_par_derive | 24 |
| 14_esperance_stable_dans_le_temps | 30 |
| 16_arete_conditionnelle_mesuree | 40 |
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

- `BAMLC0A0CM` : percentile REFUSÉ sur 5 ans — profondeur réelle 786 obs / 3.00 ans (début 2023-09-11). R-011 : un percentile calculé sur une série tronquée est sans valeur.
- `BAMLH0A0HYM2` : percentile REFUSÉ sur 5 ans — profondeur réelle 787 obs / 3.00 ans (début 2023-09-11). R-011 : un percentile calculé sur une série tronquée est sans valeur.
- `BAMLH0A0HYM2` : instrument NON ADMISSIBLE — P&L non calculable depuis le dépôt : l'OAS est un spread, et le dépôt ne contient pas le rendement de l'indice, donc pas la duration de spread. Aucune valeur ne peut être produite sans un chiffre extérieur aux données (E-002).
- `BAMLC0A0CM` : instrument NON ADMISSIBLE — P&L non calculable depuis le dépôt : l'OAS est un spread, et le dépôt ne contient pas le rendement de l'indice, donc pas la duration de spread. Aucune valeur ne peut être produite sans un chiffre extérieur aux données (E-002).
- Retards sur la date d'arrêté unique (E-014) : DEXJPUS 3 séance(s), DEXUSEU 3 séance(s), DTWEXBGS 3 séance(s)

**Vérification tierce (R-032) : NON SATISFAITE pour ce brief.** Le moteur ne dispose d'aucune source extérieure au dépôt. Trois estimateurs **internes** de σ sont publiés côte à côte au §5 ; ce sont des contrôles de cohérence interne, **pas** une vérification tierce, et ils ne sont pas présentés comme telle.

**Ce que ce moteur ne peut pas faire.** Il ne prouve aucune capacité prédictive : la règle de confirmation est une règle de percentile, déclarée et symétrique, pas un modèle validé hors échantillon. Il ne corrige pas la multiplicité : 40 candidats sont évalués et aucune pénalité de sélection n'est appliquée à l'espérance — c'est une limite déclarée, pas un oubli. Il ne voit ni les événements politiques, ni les décisions de banques centrales : le dépôt ne contient que des séries FRED, et toute affirmation de politique monétaire non adossée à `DFF` est refusée (critère 15, faute E-006).

---

*Fin du brief 005. Produit mécaniquement. Ne constitue pas un conseil en investissement.*