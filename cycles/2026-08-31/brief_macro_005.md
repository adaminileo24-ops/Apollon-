# BRIEF MACRO n° 005 — arrêté au 2026-08-27

*Produit par `apollon_macro.py` le 2026-08-31T11:36:35+00:00. Aucune valeur de ce document n'est saisie à la main : chacune porte sa série, sa date et sa profondeur. Bloc à copier tel quel.*

**Grille de scénarios (R-029, §11), déclarée avant toute lecture de données et empreintée :** `[-2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0]` · empreinte SHA-256 `6aaeb3863c875923…` · symétrique : True · horizon 60 séances (3 mois pour les séries mensuelles).

---

## 1. CONCLUSION, ÉNONCÉE D'ABORD

**40 candidats déclarés d'avance (10 instruments × 2 directions × 2 règles de confirmation). 40 évalués. 0 thèse(s) survivent aux quinze critères.**

**Abstention. Aucune thèse ne survit.** Ce n'est pas un silence : c'est un résultat, produit par le même portier que celui qui aurait admis une thèse. Le détail des échecs, critère par critère, figure au §6. La Section Macro ne transmet rien à la Section Risque ce cycle.

**Position détenue (contrôle 9, E-020) — 100 % cash, testée sur la même grille.** Espérance excédentaire du cash : +0.000 % de NAV. Référence 60/40 : +1.364 % (hors dérive : -0.169 %). **Écart du cash contre la référence : -1.364 % de NAV** sur 60 séances.

---

## 2. CE QUI A CHANGÉ — MÉCANISME, PAS CONTENU

Fait, étiqueté : les briefs 001 à 004 étaient rédigés par un agent. Celui-ci est produit par un moteur. Le paramètre libre de la Section Macro — la grille de scénarios — n'est plus accessible à l'agent : il est déclaré en tête de fichier, symétrique par construction, et son empreinte SHA-256 est vérifiée avant chaque usage. Sur le brief 004, ce paramètre avait porté le ratio annoncé de 1,29:1 à 3,0:1.

---

## 3. M1 · M2 · M3 · M4 — ÉTAT DES SÉRIES (FAIT)

Toutes les valeurs sont des FAITS lus dans le dépôt. Le retard est compté en séances ouvrées depuis la date d'arrêté unique. Les couples obligatoires sont vérifiés par le rendu : ce bloc ne peut pas être émis si un membre d'un couple manque.

| série | rôle déclaré | valeur | date | retard | n obs | profondeur | pct 1 an | pct 5 ans | pct complet |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| BAMLC0A0CM | risque_credit_ig | 0.79 | 2026-08-27 | 0 | 786 | 3.00 ans | 58.3 | REFUSÉ (insuffisante, -38 %) | 23.4 |
| BAMLH0A0HYM2 | risque_credit_hy | 2.63 | 2026-08-27 | 0 | 787 | 3.00 ans | 0.8 | REFUSÉ (insuffisante, -38 %) | 1.9 |
| CPIAUCSL | inflation_globale | 332.8 | 2026-07-01 | 57 | 118 | 9.83 ans | 91.7 | 98.3 | 99.2 |
| CPILFESL | inflation_sous_jacente | 336.8 | 2026-07-01 | 57 | 118 | 9.83 ans | 100.0 | 100.0 | 100.0 |
| DCOILBRENTEU | prix_energie | 88.24 | 2026-08-25 | 2 | 2531 | 9.98 ans | 64.7 | 71.4 | 85.8 |
| DCOILWTICO | prix_energie_wti | 83.9 | 2026-08-25 | 2 | 2494 | 9.98 ans | 65.5 | 71.7 | 85.7 |
| DEXJPUS | devise_usdjpy | 158.9 | 2026-08-21 | 4 | 2488 | 9.97 ans | 67.1 | 92.4 | 96.1 |
| DEXUSEU | devise_eurusd | 1.168 | 2026-08-21 | 4 | 2488 | 9.97 ans | 61.9 | 88.1 | 74.9 |
| DFF | politique_monetaire | 3.63 | 2026-08-27 | 0 | 3647 | 9.98 ans | 44.8 | 9.0 | 64.9 |
| DFII10 | taux_reel_10a | 2.34 | 2026-08-27 | 0 | 2495 | 9.98 ans | 88.9 | 96.4 | 98.2 |
| DGS10 | taux_nominal_10a | 4.67 | 2026-08-27 | 0 | 2495 | 9.98 ans | 94.0 | 96.8 | 98.4 |
| DGS2 | taux_nominal_2a | 4.2 | 2026-08-27 | 0 | 2495 | 9.98 ans | 92.1 | 62.7 | 81.2 |
| DGS30 | taux_nominal_30a | 5.19 | 2026-08-27 | 0 | 2495 | 9.98 ans | 94.0 | 98.8 | 99.4 |
| DTWEXBGS | dollar_large | 118.1 | 2026-08-21 | 4 | 2486 | 9.97 ans | 9.1 | 17.0 | 53.3 |
| INDPRO | activite_industrielle | 103 | 2026-07-01 | 57 | 119 | 9.83 ans | 100.0 | 100.0 | 92.4 |
| NASDAQ100 | prix_actions_tech | 2.964e+04 | 2026-08-27 | 0 | 2510 | 9.98 ans | 90.1 | 98.0 | 99.0 |
| OVXCLS | volatilite_implicite_petrole | 46.22 | 2026-08-27 | 0 | 2511 | 9.98 ans | 45.6 | 69.3 | 77.7 |
| PAYEMS | emploi | 1.589e+05 | 2026-07-01 | 57 | 119 | 9.83 ans | 83.3 | 96.7 | 98.3 |
| SP500 | prix_actions | 7731 | 2026-08-27 | 0 | 2509 | 9.98 ans | 97.2 | 99.4 | 99.7 |
| T10Y2Y | pente_courbe | 0.47 | 2026-08-27 | 0 | 2495 | 9.98 ans | 24.6 | 68.5 | 55.2 |
| T10YIE | point_mort_10a | 2.33 | 2026-08-27 | 0 | 2495 | 9.98 ans | 59.9 | 52.5 | 73.5 |
| T5YIFR | point_mort_5a5a | 2.35 | 2026-08-27 | 0 | 2495 | 9.98 ans | 99.6 | 83.8 | 91.6 |
| UNRATE | chomage | 4.1 | 2026-07-01 | 57 | 118 | 9.83 ans | 8.3 | 63.3 | 55.1 |
| VIXCLS | volatilite_implicite | 14.51 | 2026-08-27 | 0 | 2541 | 9.98 ans | 4.0 | 18.0 | 30.1 |
| VXDCLS | volatilite_implicite_dow | 13.05 | 2026-08-27 | 0 | 2512 | 9.98 ans | 0.8 | 15.5 | 21.0 |
| VXVCLS | volatilite_implicite_3m | 17.56 | 2026-08-27 | 0 | 2509 | 9.98 ans | 0.4 | 20.8 | 37.2 |

**Couples obligatoires contrôlés :** CPIAUCSL/CPILFESL, DGS10/DFII10, DGS10/T10YIE, BAMLH0A0HYM2/BAMLC0A0CM, UNRATE/PAYEMS, VIXCLS/SP500 — 0 manquement(s).

**Inflation en trois chiffres (contrôle 2, E-005).** Global +3.54 % sur un an (CPIAUCSL, 2026-07-01) · sous-jacent +2.79 % (CPILFESL) · **écart hors sous-jacent +75 pb**. Contribution énergie NON publiée : `CPIENGSL` est absente du dépôt. Lacune nommée avec le code FRED qui la comble (R-028) ; elle n'est pas présentée comme une limite de méthode. L'écart ci-dessus est l'écart global/sous-jacent, pas la contribution énergie.

---

## 4. IDENTITÉS COMPTABLES ET REDONDANCES (vérifiées numériquement)

| identité | vérifiable | n dates | résidu absolu max | tolérance | vérifiée |
|---|:---:|---:|---:|---:|:---:|
| T10YIE = DGS10 - DFII10 | oui | 2495 | 0.0000 | 0.02 | OUI |
| T10Y2Y = DGS10 - DGS2 | oui | 2495 | 0.0000 | 0.02 | OUI |

**Redondances détectées (11) — deux séries liées ne comptent jamais pour deux confirmations indépendantes :**

- identité comptable : T10YIE = DGS10 - DFII10 — T10YIE, DGS10, DFII10 (résidu max 0.0000)
- identité comptable : T10Y2Y = DGS10 - DGS2 — T10Y2Y, DGS10, DGS2 (résidu max 0.0000)
- corrélation des variations à 60 séances : BAMLC0A0CM / BAMLH0A0HYM2 = +0.938 sur 726 points (seuil 0.9)
- corrélation des variations à 60 séances : DGS10 / DGS30 = +0.967 sur 2435 points (seuil 0.9)
- corrélation des variations à 60 séances : INDPRO / PAYEMS = +0.914 sur 116 points (seuil 0.9)
- corrélation des variations à 60 séances : INDPRO / UNRATE = -0.918 sur 115 points (seuil 0.9)
- corrélation des variations à 60 séances : NASDAQ100 / SP500 = +0.903 sur 2449 points (seuil 0.9)
- corrélation des variations à 60 séances : PAYEMS / UNRATE = -0.983 sur 115 points (seuil 0.9)
- corrélation des variations à 60 séances : VIXCLS / VXDCLS = +0.930 sur 2449 points (seuil 0.9)
- corrélation des variations à 60 séances : VIXCLS / VXVCLS = +0.959 sur 2449 points (seuil 0.9)
- corrélation des variations à 60 séances : VXDCLS / VXVCLS = +0.934 sur 2449 points (seuil 0.9)

---

## 5. GRILLE, σ MESURÉ, ET DOUBLE CONFRONTATION DES PROBABILITÉS

σ est **mesuré** sur chaque série, jamais choisi. Les probabilités sont les **fréquences historiques** dans chaque bande, jamais un jugement. L'effectif de chaque bande est publié ; sous 20 observations la bande est déclarée NON ESTIMABLE. La colonne « emp./gauss. » est la double confrontation exigée par §11.5 : tout écart supérieur à un facteur 2 est déclaré (⚠).

**BAMLH0A0HYM2** (niveau) — σ à 60 pas = **0.45598** · estimateurs croisés : racine-h 0.53917, blocs disjoints 0.72862 (écart relatif 59.8 %) · dérive d'échantillon -0.11260 (-0.25 σ) · 727 variations chevauchantes, 12 blocs indépendants · 2023-08-29 → 2026-08-27

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.6840 | 55 | 1 | 0.0757 | 0.0668 | 1.13 | oui |
| -1.0 | -0.6840 | -0.3420 | 125 | 2 | 0.1719 | 0.1598 | 1.08 | oui |
| -0.5 | -0.3420 | -0.1140 | 187 | 3 | 0.2572 | 0.1747 | 1.47 | oui |
| +0.0 | -0.1140 | +0.1140 | 199 | 3 | 0.2737 | 0.1974 | 1.39 | oui |
| +0.5 | +0.1140 | +0.3420 | 81 | 1 | 0.1114 | 0.1747 | 0.64 | oui |
| +1.0 | +0.3420 | +0.6840 | 51 | 1 | 0.0702 | 0.1598 | 0.44 ⚠ | oui |
| +2.0 | +0.6840 | +∞ | 29 | 0 | 0.0399 | 0.0668 | 0.60 | oui |

**DCOILBRENTEU** (log) — σ à 60 pas = **0.24471** · estimateurs croisés : racine-h 0.24684, blocs disjoints 0.18952 (écart relatif 30.2 %) · dérive d'échantillon +0.01457 (+0.06 σ) · 2471 variations chevauchantes, 41 blocs indépendants · 2016-09-02 → 2026-08-25

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.3671 | 84 | 1 | 0.0340 | 0.0668 | 0.51 | oui |
| -1.0 | -0.3671 | -0.1835 | 156 | 3 | 0.0631 | 0.1598 | 0.40 ⚠ | oui |
| -0.5 | -0.1835 | -0.0612 | 500 | 8 | 0.2023 | 0.1747 | 1.16 | oui |
| +0.0 | -0.0612 | +0.0612 | 761 | 13 | 0.3080 | 0.1974 | 1.56 | oui |
| +0.5 | +0.0612 | +0.1835 | 624 | 10 | 0.2525 | 0.1747 | 1.45 | oui |
| +1.0 | +0.1835 | +0.3671 | 224 | 4 | 0.0907 | 0.1598 | 0.57 | oui |
| +2.0 | +0.3671 | +∞ | 122 | 2 | 0.0494 | 0.0668 | 0.74 | oui |

**DCOILWTICO** — non scénarisable : convention log inapplicable : 1 observation(s) non strictement positive(s), minimum -36.98 le 2020-04-20. Le prix a été négatif : aucun log-rendement n'existe. La série est déclarée NON SCÉNARISABLE plutôt que corrigée en silence.

**DEXJPUS** (log) — σ à 60 pas = **0.04363** · estimateurs croisés : racine-h 0.04389, blocs disjoints 0.03692 (écart relatif 18.9 %) · dérive d'échantillon +0.01061 (+0.24 σ) · 2428 variations chevauchantes, 40 blocs indépendants · 2016-09-02 → 2026-08-21

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0654 | 97 | 2 | 0.0400 | 0.0668 | 0.60 | oui |
| -1.0 | -0.0654 | -0.0327 | 220 | 4 | 0.0906 | 0.1598 | 0.57 | oui |
| -0.5 | -0.0327 | -0.0109 | 385 | 6 | 0.1586 | 0.1747 | 0.91 | oui |
| +0.0 | -0.0109 | +0.0109 | 504 | 8 | 0.2076 | 0.1974 | 1.05 | oui |
| +0.5 | +0.0109 | +0.0327 | 556 | 9 | 0.2290 | 0.1747 | 1.31 | oui |
| +1.0 | +0.0327 | +0.0654 | 469 | 8 | 0.1932 | 0.1598 | 1.21 | oui |
| +2.0 | +0.0654 | +∞ | 197 | 3 | 0.0811 | 0.0668 | 1.21 | oui |

**DEXUSEU** (log) — σ à 60 pas = **0.03493** · estimateurs croisés : racine-h 0.03472, blocs disjoints 0.03189 (écart relatif 9.5 %) · dérive d'échantillon +0.00109 (+0.03 σ) · 2428 variations chevauchantes, 40 blocs indépendants · 2016-09-02 → 2026-08-21

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0524 | 139 | 2 | 0.0572 | 0.0668 | 0.86 | oui |
| -1.0 | -0.0524 | -0.0262 | 326 | 5 | 0.1343 | 0.1598 | 0.84 | oui |
| -0.5 | -0.0262 | -0.0087 | 511 | 9 | 0.2105 | 0.1747 | 1.20 | oui |
| +0.0 | -0.0087 | +0.0087 | 601 | 10 | 0.2475 | 0.1974 | 1.25 | oui |
| +0.5 | +0.0087 | +0.0262 | 331 | 6 | 0.1363 | 0.1747 | 0.78 | oui |
| +1.0 | +0.0262 | +0.0524 | 301 | 5 | 0.1240 | 0.1598 | 0.78 | oui |
| +2.0 | +0.0524 | +∞ | 219 | 4 | 0.0902 | 0.0668 | 1.35 | oui |

**DGS10** (niveau) — σ à 60 pas = **0.42735** · estimateurs croisés : racine-h 0.41333, blocs disjoints 0.40394 (écart relatif 5.8 %) · dérive d'échantillon +0.06745 (+0.16 σ) · 2435 variations chevauchantes, 41 blocs indépendants · 2016-09-02 → 2026-08-27

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.6410 | 118 | 2 | 0.0485 | 0.0668 | 0.73 | oui |
| -1.0 | -0.6410 | -0.3205 | 277 | 5 | 0.1138 | 0.1598 | 0.71 | oui |
| -0.5 | -0.3205 | -0.1068 | 383 | 6 | 0.1573 | 0.1747 | 0.90 | oui |
| +0.0 | -0.1068 | +0.1068 | 528 | 9 | 0.2168 | 0.1974 | 1.10 | oui |
| +0.5 | +0.1068 | +0.3205 | 566 | 9 | 0.2324 | 0.1747 | 1.33 | oui |
| +1.0 | +0.3205 | +0.6410 | 347 | 6 | 0.1425 | 0.1598 | 0.89 | oui |
| +2.0 | +0.6410 | +∞ | 216 | 4 | 0.0887 | 0.0668 | 1.33 | oui |

**DGS2** (niveau) — σ à 60 pas = **0.49495** · estimateurs croisés : racine-h 0.41895, blocs disjoints 0.47467 (écart relatif 18.1 %) · dérive d'échantillon +0.08179 (+0.17 σ) · 2435 variations chevauchantes, 41 blocs indépendants · 2016-09-02 → 2026-08-27

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.7424 | 115 | 2 | 0.0472 | 0.0668 | 0.71 | oui |
| -1.0 | -0.7424 | -0.3712 | 228 | 4 | 0.0936 | 0.1598 | 0.59 | oui |
| -0.5 | -0.3712 | -0.1237 | 323 | 5 | 0.1326 | 0.1747 | 0.76 | oui |
| +0.0 | -0.1237 | +0.1237 | 739 | 12 | 0.3035 | 0.1974 | 1.54 | oui |
| +0.5 | +0.1237 | +0.3712 | 481 | 8 | 0.1975 | 0.1747 | 1.13 | oui |
| +1.0 | +0.3712 | +0.7424 | 351 | 6 | 0.1441 | 0.1598 | 0.90 | oui |
| +2.0 | +0.7424 | +∞ | 198 | 3 | 0.0813 | 0.0668 | 1.22 | oui |

**DGS30** (niveau) — σ à 60 pas = **0.36920** · estimateurs croisés : racine-h 0.39229, blocs disjoints 0.34297 (écart relatif 14.4 %) · dérive d'échantillon +0.06200 (+0.17 σ) · 2435 variations chevauchantes, 41 blocs indépendants · 2016-09-02 → 2026-08-27

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.5538 | 127 | 2 | 0.0522 | 0.0668 | 0.78 | oui |
| -1.0 | -0.5538 | -0.2769 | 277 | 5 | 0.1138 | 0.1598 | 0.71 | oui |
| -0.5 | -0.2769 | -0.0923 | 338 | 6 | 0.1388 | 0.1747 | 0.79 | oui |
| +0.0 | -0.0923 | +0.0923 | 629 | 10 | 0.2583 | 0.1974 | 1.31 | oui |
| +0.5 | +0.0923 | +0.2769 | 456 | 8 | 0.1873 | 0.1747 | 1.07 | oui |
| +1.0 | +0.2769 | +0.5538 | 387 | 6 | 0.1589 | 0.1598 | 0.99 | oui |
| +2.0 | +0.5538 | +∞ | 221 | 4 | 0.0908 | 0.0668 | 1.36 | oui |

**DTWEXBGS** (log) — σ à 60 pas = **0.02628** · estimateurs croisés : racine-h 0.02415, blocs disjoints 0.02421 (écart relatif 8.8 %) · dérive d'échantillon +0.00127 (+0.05 σ) · 2426 variations chevauchantes, 40 blocs indépendants · 2016-09-02 → 2026-08-21

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0394 | 156 | 3 | 0.0643 | 0.0668 | 0.96 | oui |
| -1.0 | -0.0394 | -0.0197 | 384 | 6 | 0.1583 | 0.1598 | 0.99 | oui |
| -0.5 | -0.0197 | -0.0066 | 348 | 6 | 0.1434 | 0.1747 | 0.82 | oui |
| +0.0 | -0.0066 | +0.0066 | 541 | 9 | 0.2230 | 0.1974 | 1.13 | oui |
| +0.5 | +0.0066 | +0.0197 | 464 | 8 | 0.1913 | 0.1747 | 1.10 | oui |
| +1.0 | +0.0197 | +0.0394 | 311 | 5 | 0.1282 | 0.1598 | 0.80 | oui |
| +2.0 | +0.0394 | +∞ | 222 | 4 | 0.0915 | 0.0668 | 1.37 | oui |

**NASDAQ100** (log) — σ à 60 pas = **0.08863** · estimateurs croisés : racine-h 0.11134, blocs disjoints 0.11023 (écart relatif 25.6 %) · dérive d'échantillon +0.04424 (+0.50 σ) · 2450 variations chevauchantes, 41 blocs indépendants · 2016-09-02 → 2026-08-27

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.1329 | 109 | 2 | 0.0445 | 0.0668 | 0.67 | oui |
| -1.0 | -0.1329 | -0.0665 | 166 | 3 | 0.0678 | 0.1598 | 0.42 ⚠ | oui |
| -0.5 | -0.0665 | -0.0222 | 181 | 3 | 0.0739 | 0.1747 | 0.42 ⚠ | oui |
| +0.0 | -0.0222 | +0.0222 | 363 | 6 | 0.1482 | 0.1974 | 0.75 | oui |
| +0.5 | +0.0222 | +0.0665 | 584 | 10 | 0.2384 | 0.1747 | 1.36 | oui |
| +1.0 | +0.0665 | +0.1329 | 731 | 12 | 0.2984 | 0.1598 | 1.87 | oui |
| +2.0 | +0.1329 | +∞ | 316 | 5 | 0.1290 | 0.0668 | 1.93 | oui |

**SP500** (log) — σ à 60 pas = **0.06918** · estimateurs croisés : racine-h 0.08857, blocs disjoints 0.08722 (écart relatif 28.0 %) · dérive d'échantillon +0.03070 (+0.44 σ) · 2449 variations chevauchantes, 41 blocs indépendants · 2016-09-02 → 2026-08-27

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.1038 | 115 | 2 | 0.0470 | 0.0668 | 0.70 | oui |
| -1.0 | -0.1038 | -0.0519 | 158 | 3 | 0.0645 | 0.1598 | 0.40 ⚠ | oui |
| -0.5 | -0.0519 | -0.0173 | 176 | 3 | 0.0719 | 0.1747 | 0.41 ⚠ | oui |
| +0.0 | -0.0173 | +0.0173 | 293 | 5 | 0.1196 | 0.1974 | 0.61 | oui |
| +0.5 | +0.0173 | +0.0519 | 743 | 12 | 0.3034 | 0.1747 | 1.74 | oui |
| +1.0 | +0.0519 | +0.1038 | 754 | 13 | 0.3079 | 0.1598 | 1.93 | oui |
| +2.0 | +0.1038 | +∞ | 210 | 4 | 0.0857 | 0.0668 | 1.28 | oui |

**VIXCLS** (log) — σ à 60 pas = **0.34702** · estimateurs croisés : racine-h 0.61631, blocs disjoints 0.40739 (écart relatif 77.6 %) · dérive d'échantillon +0.00345 (+0.01 σ) · 2481 variations chevauchantes, 41 blocs indépendants · 2016-09-02 → 2026-08-27

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.5205 | 77 | 1 | 0.0310 | 0.0668 | 0.46 ⚠ | oui |
| -1.0 | -0.5205 | -0.2603 | 389 | 6 | 0.1568 | 0.1598 | 0.98 | oui |
| -0.5 | -0.2603 | -0.0868 | 602 | 10 | 0.2426 | 0.1747 | 1.39 | oui |
| +0.0 | -0.0868 | +0.0868 | 612 | 10 | 0.2467 | 0.1974 | 1.25 | oui |
| +0.5 | +0.0868 | +0.2603 | 376 | 6 | 0.1516 | 0.1747 | 0.87 | oui |
| +1.0 | +0.2603 | +0.5205 | 248 | 4 | 0.1000 | 0.1598 | 0.63 | oui |
| +2.0 | +0.5205 | +∞ | 177 | 3 | 0.0713 | 0.0668 | 1.07 | oui |

---

## 6. TEST D'ASYMÉTRIE — DÉFINITION UNIQUE (R-030), L'ESPÉRANCE DÉCIDE

> Test d'admission : **espérance calculée sur la grille symétrique complète, les deux queues incluses**. Le rapport gain maximal / perte maximale est publié **pour information** et ne peut fonder aucune admission seul (T-001, faute E-018). Le rapport gain maximal / perte du scénario central est **interdit**. Une seule formulation, appliquée à tous les candidats, position détenue comprise.

| candidat | verdict | espérance % NAV | sans dérive | 1re moitié | 2e moitié | gain max | perte max | ratio (info) | critères échoués |
|---|:---:|---:|---:|---:|---:|---:|---:|---:|---|
| M005-DCOILBRENTEU-HAUSSE-ALIGNE | REFUSEE | +0.243 | +0.125 | +0.271 | +0.086 | +4.98 | -3.17 | 1.57:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DCOILBRENTEU-HAUSSE-CONTRARIEN | REFUSEE | +0.243 | +0.125 | +0.271 | +0.086 | +4.98 | -3.17 | 1.57:1 | 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DCOILBRENTEU-BAISSE-ALIGNE | REFUSEE | -0.243 | -0.125 | -0.271 | -0.086 | +3.17 | -4.98 | 0.64:1 | 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILBRENTEU-BAISSE-CONTRARIEN | REFUSEE | -0.243 | -0.125 | -0.271 | -0.086 | +3.17 | -4.98 | 0.64:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-HAUSSE-ALIGNE | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-HAUSSE-CONTRARIEN | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-BAISSE-ALIGNE | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-BAISSE-CONTRARIEN | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-HAUSSE-ALIGNE | REFUSEE | +0.014 | -0.062 | -0.054 | +0.060 | +0.66 | -0.74 | 0.90:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-HAUSSE-CONTRARIEN | REFUSEE | +0.014 | -0.062 | -0.054 | +0.060 | +0.66 | -0.74 | 0.90:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-BAISSE-ALIGNE | REFUSEE | -0.014 | +0.062 | +0.054 | -0.060 | +0.74 | -0.66 | 1.12:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-BAISSE-CONTRARIEN | REFUSEE | -0.014 | +0.062 | +0.054 | -0.060 | +0.74 | -0.66 | 1.12:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-HAUSSE-ALIGNE | REFUSEE | -0.059 | -0.069 | -0.033 | -0.071 | +0.51 | -0.61 | 0.84:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-HAUSSE-CONTRARIEN | REFUSEE | -0.059 | -0.069 | -0.033 | -0.071 | +0.51 | -0.61 | 0.84:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-BAISSE-ALIGNE | REFUSEE | +0.059 | +0.069 | +0.033 | +0.071 | +0.61 | -0.51 | 1.19:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DEXUSEU-BAISSE-CONTRARIEN | REFUSEE | +0.059 | +0.069 | +0.033 | +0.071 | +0.61 | -0.51 | 1.19:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DGS10-HAUSSE-ALIGNE | REFUSEE | +0.015 | -0.023 | -0.034 | +0.059 | +0.50 | -0.58 | 0.86:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-HAUSSE-CONTRARIEN | REFUSEE | +0.015 | -0.023 | -0.034 | +0.059 | +0.50 | -0.58 | 0.86:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-BAISSE-ALIGNE | REFUSEE | -0.015 | +0.023 | +0.034 | -0.059 | +0.58 | -0.50 | 1.17:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-BAISSE-CONTRARIEN | REFUSEE | -0.015 | +0.023 | +0.034 | -0.059 | +0.58 | -0.50 | 1.17:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-HAUSSE-ALIGNE | REFUSEE | +0.000 | -0.010 | -0.014 | +0.012 | +0.14 | -0.16 | 0.84:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-HAUSSE-CONTRARIEN | REFUSEE | +0.000 | -0.010 | -0.014 | +0.012 | +0.14 | -0.16 | 0.84:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-BAISSE-ALIGNE | REFUSEE | -0.000 | +0.010 | +0.014 | -0.012 | +0.16 | -0.14 | 1.18:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-BAISSE-CONTRARIEN | REFUSEE | -0.000 | +0.010 | +0.014 | -0.012 | +0.16 | -0.14 | 1.18:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-HAUSSE-ALIGNE | REFUSEE | +0.019 | -0.040 | -0.079 | +0.120 | +0.79 | -1.00 | 0.79:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-HAUSSE-CONTRARIEN | REFUSEE | +0.019 | -0.040 | -0.079 | +0.120 | +0.79 | -1.00 | 0.79:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-BAISSE-ALIGNE | REFUSEE | -0.019 | +0.040 | +0.079 | -0.120 | +1.00 | -0.79 | 1.26:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-BAISSE-CONTRARIEN | REFUSEE | -0.019 | +0.040 | +0.079 | -0.120 | +1.00 | -0.79 | 1.26:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-HAUSSE-ALIGNE | REFUSEE | -0.056 | -0.067 | -0.070 | -0.043 | +0.36 | -0.48 | 0.76:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-HAUSSE-CONTRARIEN | REFUSEE | -0.056 | -0.067 | -0.070 | -0.043 | +0.36 | -0.48 | 0.76:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-BAISSE-ALIGNE | REFUSEE | +0.056 | +0.067 | +0.070 | +0.043 | +0.48 | -0.36 | 1.32:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DTWEXBGS-BAISSE-CONTRARIEN | REFUSEE | +0.056 | +0.067 | +0.070 | +0.043 | +0.48 | -0.36 | 1.32:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-HAUSSE-ALIGNE | REFUSEE | +0.309 | -0.030 | +0.445 | +0.194 | +1.48 | -1.37 | 1.08:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-HAUSSE-CONTRARIEN | REFUSEE | +0.309 | -0.030 | +0.445 | +0.194 | +1.48 | -1.37 | 1.08:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-BAISSE-ALIGNE | REFUSEE | -0.309 | +0.030 | -0.445 | -0.194 | +1.37 | -1.48 | 0.92:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-NASDAQ100-BAISSE-CONTRARIEN | REFUSEE | -0.309 | +0.030 | -0.445 | -0.194 | +1.37 | -1.48 | 0.92:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-SP500-HAUSSE-ALIGNE | REFUSEE | +0.192 | -0.038 | +0.220 | +0.161 | +1.12 | -1.10 | 1.01:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-SP500-HAUSSE-CONTRARIEN | REFUSEE | +0.192 | -0.038 | +0.220 | +0.161 | +1.12 | -1.10 | 1.01:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-SP500-BAISSE-ALIGNE | REFUSEE | -0.192 | +0.038 | -0.220 | -0.161 | +1.10 | -1.12 | 0.99:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-SP500-BAISSE-CONTRARIEN | REFUSEE | -0.192 | +0.038 | -0.220 | -0.161 | +1.10 | -1.12 | 0.99:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |

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
| 8_confirmations_independantes | 20 |
| 9_test_execute_et_vrai | 20 |
| 10_invalidation_fait_date | 12 |
| 11_invalidation_non_deja_survenue | 26 |
| 12_esperance_positive | 22 |
| 13_esperance_non_portee_par_derive | 28 |
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

- `BAMLC0A0CM` : percentile REFUSÉ sur 5 ans — profondeur réelle 786 obs / 3.00 ans (début 2023-08-29). R-011 : un percentile calculé sur une série tronquée est sans valeur.
- `BAMLH0A0HYM2` : percentile REFUSÉ sur 5 ans — profondeur réelle 787 obs / 3.00 ans (début 2023-08-29). R-011 : un percentile calculé sur une série tronquée est sans valeur.
- `BAMLH0A0HYM2` : instrument NON ADMISSIBLE — P&L non calculable depuis le dépôt : l'OAS est un spread, et le dépôt ne contient pas le rendement de l'indice, donc pas la duration de spread. Aucune valeur ne peut être produite sans un chiffre extérieur aux données (E-002).
- `BAMLC0A0CM` : instrument NON ADMISSIBLE — P&L non calculable depuis le dépôt : l'OAS est un spread, et le dépôt ne contient pas le rendement de l'indice, donc pas la duration de spread. Aucune valeur ne peut être produite sans un chiffre extérieur aux données (E-002).
- Retards sur la date d'arrêté unique (E-014) : DCOILBRENTEU 2 séance(s), DCOILWTICO 2 séance(s), DEXJPUS 4 séance(s), DEXUSEU 4 séance(s), DTWEXBGS 4 séance(s)

**Vérification tierce (R-032) : NON SATISFAITE pour ce brief.** Le moteur ne dispose d'aucune source extérieure au dépôt. Trois estimateurs **internes** de σ sont publiés côte à côte au §5 ; ce sont des contrôles de cohérence interne, **pas** une vérification tierce, et ils ne sont pas présentés comme telle.

**Ce que ce moteur ne peut pas faire.** Il ne prouve aucune capacité prédictive : la règle de confirmation est une règle de percentile, déclarée et symétrique, pas un modèle validé hors échantillon. Il ne corrige pas la multiplicité : 40 candidats sont évalués et aucune pénalité de sélection n'est appliquée à l'espérance — c'est une limite déclarée, pas un oubli. Il ne voit ni les événements politiques, ni les décisions de banques centrales : le dépôt ne contient que des séries FRED, et toute affirmation de politique monétaire non adossée à `DFF` est refusée (critère 15, faute E-006).

---

*Fin du brief 005. Produit mécaniquement. Ne constitue pas un conseil en investissement.*