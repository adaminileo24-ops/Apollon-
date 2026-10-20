# BRIEF MACRO n° 005 — arrêté au 2026-10-19

*Produit par `apollon_macro.py` le 2026-10-20T22:40:44+00:00. Aucune valeur de ce document n'est saisie à la main : chacune porte sa série, sa date et sa profondeur. Bloc à copier tel quel.*

**Grille de scénarios (R-029, §11), déclarée avant toute lecture de données et empreintée :** `[-2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0]` · empreinte SHA-256 `6aaeb3863c875923…` · symétrique : True · horizon 60 séances (3 mois pour les séries mensuelles).

---

## 1. CONCLUSION, ÉNONCÉE D'ABORD

**40 candidats déclarés d'avance (10 instruments × 2 directions × 2 règles de confirmation). 40 évalués. 0 thèse(s) survivent aux quinze critères.**

**Abstention. Aucune thèse ne survit.** Ce n'est pas un silence : c'est un résultat, produit par le même portier que celui qui aurait admis une thèse. Le détail des échecs, critère par critère, figure au §6. La Section Macro ne transmet rien à la Section Risque ce cycle.

**Position détenue (contrôle 9, E-020) — 100 % cash, testée sur la même grille.** Espérance excédentaire du cash : +0.000 % de NAV. Référence 60/40 : +1.353 % (hors dérive : -0.198 %). **Écart du cash contre la référence : -1.353 % de NAV** sur 60 séances.

---

## 2. CE QUI A CHANGÉ — MÉCANISME, PAS CONTENU

Fait, étiqueté : les briefs 001 à 004 étaient rédigés par un agent. Celui-ci est produit par un moteur. Le paramètre libre de la Section Macro — la grille de scénarios — n'est plus accessible à l'agent : il est déclaré en tête de fichier, symétrique par construction, et son empreinte SHA-256 est vérifiée avant chaque usage. Sur le brief 004, ce paramètre avait porté le ratio annoncé de 1,29:1 à 3,0:1.

---

## 3. M1 · M2 · M3 · M4 — ÉTAT DES SÉRIES (FAIT)

Toutes les valeurs sont des FAITS lus dans le dépôt. Le retard est compté en séances ouvrées depuis la date d'arrêté unique. Les couples obligatoires sont vérifiés par le rendu : ce bloc ne peut pas être émis si un membre d'un couple manque.

| série | rôle déclaré | valeur | date | retard | n obs | profondeur | pct 1 an | pct 5 ans | pct complet |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| BAMLC0A0CM | risque_credit_ig | 0.87 | 2026-10-19 | 0 | 783 | 2.99 ans | 94.8 | REFUSÉ (insuffisante, -38 %) | 56.2 |
| BAMLH0A0HYM2 | risque_credit_hy | 3.29 | 2026-10-19 | 0 | 784 | 2.99 ans | 98.8 | REFUSÉ (insuffisante, -38 %) | 80.5 |
| CPIAUCSL | inflation_globale | 336.3 | 2026-09-01 | 48 | 119 | 9.92 ans | 100.0 | 100.0 | 100.0 |
| CPILFESL | inflation_sous_jacente | 338.9 | 2026-09-01 | 48 | 119 | 9.92 ans | 100.0 | 100.0 | 100.0 |
| DCOILBRENTEU | prix_energie | 126.5 | 2026-10-14 | 3 | 2530 | 9.97 ans | 96.4 | 98.6 | 99.3 |
| DCOILWTICO | prix_energie_wti | 101.9 | 2026-10-14 | 3 | 2494 | 9.97 ans | 91.3 | 91.8 | 95.9 |
| DEXJPUS | devise_usdjpy | 158 | 2026-10-16 | 1 | 2492 | 9.98 ans | 49.6 | 88.4 | 94.1 |
| DEXUSEU | devise_eurusd | 1.123 | 2026-10-16 | 1 | 2492 | 9.98 ans | 3.2 | 63.3 | 48.9 |
| DFF | politique_monetaire | 3.88 | 2026-10-19 | 0 | 3650 | 9.99 ans | 100.0 | 27.1 | 70.9 |
| DFII10 | taux_reel_10a | 2.8 | 2026-10-19 | 0 | 2496 | 9.98 ans | 94.4 | 98.9 | 99.4 |
| DGS10 | taux_nominal_10a | 5.15 | 2026-10-19 | 0 | 2496 | 9.98 ans | 94.4 | 98.9 | 99.4 |
| DGS2 | taux_nominal_2a | 4.77 | 2026-10-19 | 0 | 2496 | 9.98 ans | 94.8 | 87.3 | 93.6 |
| DGS30 | taux_nominal_30a | 5.48 | 2026-10-19 | 0 | 2496 | 9.98 ans | 94.8 | 99.0 | 99.5 |
| DTWEXBGS | dollar_large | 121.4 | 2026-10-16 | 1 | 2490 | 9.98 ans | 93.7 | 62.8 | 79.2 |
| INDPRO | activite_industrielle | 104 | 2026-09-01 | 48 | 120 | 9.92 ans | 100.0 | 100.0 | 95.8 |
| NASDAQ100 | prix_actions_tech | 2.953e+04 | 2026-10-19 | 0 | 2511 | 9.98 ans | 79.8 | 96.0 | 98.0 |
| OVXCLS | volatilite_implicite_petrole | 50.22 | 2026-10-19 | 0 | 2512 | 9.98 ans | 46.0 | 78.8 | 84.1 |
| PAYEMS | emploi | 1.59e+05 | 2026-09-01 | 48 | 120 | 9.92 ans | 100.0 | 100.0 | 100.0 |
| SP500 | prix_actions | 7691 | 2026-10-19 | 0 | 2510 | 9.98 ans | 87.7 | 97.5 | 98.8 |
| T10Y2Y | pente_courbe | 0.38 | 2026-10-19 | 0 | 2496 | 9.98 ans | 17.1 | 64.2 | 50.0 |
| T10YIE | point_mort_10a | 2.35 | 2026-10-19 | 0 | 2496 | 9.98 ans | 74.2 | 61.2 | 77.9 |
| T5YIFR | point_mort_5a5a | 2.32 | 2026-10-19 | 0 | 2496 | 9.98 ans | 86.1 | 73.4 | 86.3 |
| UNRATE | chomage | 4.2 | 2026-09-01 | 48 | 119 | 9.92 ans | 33.3 | 78.3 | 63.9 |
| VIXCLS | volatilite_implicite | 18.44 | 2026-10-19 | 0 | 2543 | 9.98 ans | 69.0 | 55.9 | 60.0 |
| VXDCLS | volatilite_implicite_dow | 16 | 2026-10-19 | 0 | 2513 | 9.98 ans | 57.5 | 49.8 | 51.1 |
| VXVCLS | volatilite_implicite_3m | 19.6 | 2026-10-19 | 0 | 2510 | 9.98 ans | 44.4 | 44.3 | 51.9 |

**Couples obligatoires contrôlés :** CPIAUCSL/CPILFESL, DGS10/DFII10, DGS10/T10YIE, BAMLH0A0HYM2/BAMLC0A0CM, UNRATE/PAYEMS, VIXCLS/SP500 — 0 manquement(s).

**Inflation en trois chiffres (contrôle 2, E-005).** Global +4.02 % sur un an (CPIAUCSL, 2026-09-01) · sous-jacent +2.79 % (CPILFESL) · **écart hors sous-jacent +123 pb**. Contribution énergie NON publiée : `CPIENGSL` est absente du dépôt. Lacune nommée avec le code FRED qui la comble (R-028) ; elle n'est pas présentée comme une limite de méthode. L'écart ci-dessus est l'écart global/sous-jacent, pas la contribution énergie.

---

## 4. IDENTITÉS COMPTABLES ET REDONDANCES (vérifiées numériquement)

| identité | vérifiable | n dates | résidu absolu max | tolérance | vérifiée |
|---|:---:|---:|---:|---:|:---:|
| T10YIE = DGS10 - DFII10 | oui | 2496 | 0.0000 | 0.02 | OUI |
| T10Y2Y = DGS10 - DGS2 | oui | 2496 | 0.0000 | 0.02 | OUI |

**Redondances détectées (11) — deux séries liées ne comptent jamais pour deux confirmations indépendantes :**

- identité comptable : T10YIE = DGS10 - DFII10 — T10YIE, DGS10, DFII10 (résidu max 0.0000)
- identité comptable : T10Y2Y = DGS10 - DGS2 — T10Y2Y, DGS10, DGS2 (résidu max 0.0000)
- corrélation des variations à 60 séances : BAMLC0A0CM / BAMLH0A0HYM2 = +0.937 sur 723 points (seuil 0.9)
- corrélation des variations à 60 séances : DGS10 / DGS30 = +0.966 sur 2436 points (seuil 0.9)
- corrélation des variations à 60 séances : INDPRO / PAYEMS = +0.912 sur 117 points (seuil 0.9)
- corrélation des variations à 60 séances : INDPRO / UNRATE = -0.917 sur 116 points (seuil 0.9)
- corrélation des variations à 60 séances : NASDAQ100 / SP500 = +0.903 sur 2450 points (seuil 0.9)
- corrélation des variations à 60 séances : PAYEMS / UNRATE = -0.983 sur 116 points (seuil 0.9)
- corrélation des variations à 60 séances : VIXCLS / VXDCLS = +0.929 sur 2450 points (seuil 0.9)
- corrélation des variations à 60 séances : VIXCLS / VXVCLS = +0.958 sur 2450 points (seuil 0.9)
- corrélation des variations à 60 séances : VXDCLS / VXVCLS = +0.933 sur 2450 points (seuil 0.9)

---

## 5. GRILLE, σ MESURÉ, ET DOUBLE CONFRONTATION DES PROBABILITÉS

σ est **mesuré** sur chaque série, jamais choisi. Les probabilités sont les **fréquences historiques** dans chaque bande, jamais un jugement. L'effectif de chaque bande est publié ; sous 20 observations la bande est déclarée NON ESTIMABLE. La colonne « emp./gauss. » est la double confrontation exigée par §11.5 : tout écart supérieur à un facteur 2 est déclaré (⚠).

**BAMLH0A0HYM2** (niveau) — σ à 60 pas = **0.45003** · estimateurs croisés : racine-h 0.53930, blocs disjoints 0.42130 (écart relatif 28.0 %) · dérive d'échantillon -0.08293 (-0.18 σ) · 724 variations chevauchantes, 12 blocs indépendants · 2023-10-23 → 2026-10-19

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.6750 | 46 | 1 | 0.0635 | 0.0668 | 0.95 | oui |
| -1.0 | -0.6750 | -0.3375 | 117 | 2 | 0.1616 | 0.1598 | 1.01 | oui |
| -0.5 | -0.3375 | -0.1125 | 189 | 3 | 0.2610 | 0.1747 | 1.49 | oui |
| +0.0 | -0.1125 | +0.1125 | 195 | 3 | 0.2693 | 0.1974 | 1.36 | oui |
| +0.5 | +0.1125 | +0.3375 | 80 | 1 | 0.1105 | 0.1747 | 0.63 | oui |
| +1.0 | +0.3375 | +0.6750 | 68 | 1 | 0.0939 | 0.1598 | 0.59 | oui |
| +2.0 | +0.6750 | +∞ | 29 | 0 | 0.0401 | 0.0668 | 0.60 | oui |

**DCOILBRENTEU** (log) — σ à 60 pas = **0.24900** · estimateurs croisés : racine-h 0.24959, blocs disjoints 0.25026 (écart relatif 0.5 %) · dérive d'échantillon +0.01815 (+0.07 σ) · 2470 variations chevauchantes, 41 blocs indépendants · 2016-10-24 → 2026-10-14

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.3735 | 83 | 1 | 0.0336 | 0.0668 | 0.50 | oui |
| -1.0 | -0.3735 | -0.1867 | 155 | 3 | 0.0628 | 0.1598 | 0.39 ⚠ | oui |
| -0.5 | -0.1867 | -0.0622 | 498 | 8 | 0.2016 | 0.1747 | 1.15 | oui |
| +0.0 | -0.0622 | +0.0622 | 772 | 13 | 0.3126 | 0.1974 | 1.58 | oui |
| +0.5 | +0.0622 | +0.1867 | 600 | 10 | 0.2429 | 0.1747 | 1.39 | oui |
| +1.0 | +0.1867 | +0.3735 | 219 | 4 | 0.0887 | 0.1598 | 0.55 | oui |
| +2.0 | +0.3735 | +∞ | 143 | 2 | 0.0579 | 0.0668 | 0.87 | oui |

**DCOILWTICO** — non scénarisable : convention log inapplicable : 1 observation(s) non strictement positive(s), minimum -36.98 le 2020-04-20. Le prix a été négatif : aucun log-rendement n'existe. La série est déclarée NON SCÉNARISABLE plutôt que corrigée en silence.

**DEXJPUS** (log) — σ à 60 pas = **0.04169** · estimateurs croisés : racine-h 0.04379, blocs disjoints 0.05085 (écart relatif 22.0 %) · dérive d'échantillon +0.00851 (+0.20 σ) · 2432 variations chevauchantes, 41 blocs indépendants · 2016-10-24 → 2026-10-16

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0625 | 105 | 2 | 0.0432 | 0.0668 | 0.65 | oui |
| -1.0 | -0.0625 | -0.0313 | 244 | 4 | 0.1003 | 0.1598 | 0.63 | oui |
| -0.5 | -0.0313 | -0.0104 | 389 | 6 | 0.1600 | 0.1747 | 0.92 | oui |
| +0.0 | -0.0104 | +0.0104 | 494 | 8 | 0.2031 | 0.1974 | 1.03 | oui |
| +0.5 | +0.0104 | +0.0313 | 535 | 9 | 0.2200 | 0.1747 | 1.26 | oui |
| +1.0 | +0.0313 | +0.0625 | 473 | 8 | 0.1945 | 0.1598 | 1.22 | oui |
| +2.0 | +0.0625 | +∞ | 192 | 3 | 0.0789 | 0.0668 | 1.18 | oui |

**DEXUSEU** (log) — σ à 60 pas = **0.03425** · estimateurs croisés : racine-h 0.03470, blocs disjoints 0.03570 (écart relatif 4.2 %) · dérive d'échantillon +0.00178 (+0.05 σ) · 2432 variations chevauchantes, 41 blocs indépendants · 2016-10-24 → 2026-10-16

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0514 | 130 | 2 | 0.0535 | 0.0668 | 0.80 | oui |
| -1.0 | -0.0514 | -0.0257 | 318 | 5 | 0.1308 | 0.1598 | 0.82 | oui |
| -0.5 | -0.0257 | -0.0086 | 512 | 9 | 0.2105 | 0.1747 | 1.21 | oui |
| +0.0 | -0.0086 | +0.0086 | 617 | 10 | 0.2537 | 0.1974 | 1.29 | oui |
| +0.5 | +0.0086 | +0.0257 | 321 | 5 | 0.1320 | 0.1747 | 0.76 | oui |
| +1.0 | +0.0257 | +0.0514 | 307 | 5 | 0.1262 | 0.1598 | 0.79 | oui |
| +2.0 | +0.0514 | +∞ | 227 | 4 | 0.0933 | 0.0668 | 1.40 | oui |

**DGS10** (niveau) — σ à 60 pas = **0.42285** · estimateurs croisés : racine-h 0.41487, blocs disjoints 0.49730 (écart relatif 19.9 %) · dérive d'échantillon +0.06421 (+0.15 σ) · 2436 variations chevauchantes, 41 blocs indépendants · 2016-10-24 → 2026-10-19

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.6343 | 123 | 2 | 0.0505 | 0.0668 | 0.76 | oui |
| -1.0 | -0.6343 | -0.3171 | 284 | 5 | 0.1166 | 0.1598 | 0.73 | oui |
| -0.5 | -0.3171 | -0.1057 | 371 | 6 | 0.1523 | 0.1747 | 0.87 | oui |
| +0.0 | -0.1057 | +0.1057 | 528 | 9 | 0.2167 | 0.1974 | 1.10 | oui |
| +0.5 | +0.1057 | +0.3171 | 555 | 9 | 0.2278 | 0.1747 | 1.30 | oui |
| +1.0 | +0.3171 | +0.6343 | 366 | 6 | 0.1502 | 0.1598 | 0.94 | oui |
| +2.0 | +0.6343 | +∞ | 209 | 3 | 0.0858 | 0.0668 | 1.28 | oui |

**DGS2** (niveau) — σ à 60 pas = **0.49654** · estimateurs croisés : racine-h 0.42204, blocs disjoints 0.53668 (écart relatif 27.2 %) · dérive d'échantillon +0.08364 (+0.17 σ) · 2436 variations chevauchantes, 41 blocs indépendants · 2016-10-24 → 2026-10-19

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.7448 | 115 | 2 | 0.0472 | 0.0668 | 0.71 | oui |
| -1.0 | -0.7448 | -0.3724 | 228 | 4 | 0.0936 | 0.1598 | 0.59 | oui |
| -0.5 | -0.3724 | -0.1241 | 323 | 5 | 0.1326 | 0.1747 | 0.76 | oui |
| +0.0 | -0.1241 | +0.1241 | 739 | 12 | 0.3034 | 0.1974 | 1.54 | oui |
| +0.5 | +0.1241 | +0.3724 | 476 | 8 | 0.1954 | 0.1747 | 1.12 | oui |
| +1.0 | +0.3724 | +0.7448 | 354 | 6 | 0.1453 | 0.1598 | 0.91 | oui |
| +2.0 | +0.7448 | +∞ | 201 | 3 | 0.0825 | 0.0668 | 1.24 | oui |

**DGS30** (niveau) — σ à 60 pas = **0.36479** · estimateurs croisés : racine-h 0.39283, blocs disjoints 0.44499 (écart relatif 22.0 %) · dérive d'échantillon +0.05884 (+0.16 σ) · 2436 variations chevauchantes, 41 blocs indépendants · 2016-10-24 → 2026-10-19

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.5472 | 128 | 2 | 0.0525 | 0.0668 | 0.79 | oui |
| -1.0 | -0.5472 | -0.2736 | 276 | 5 | 0.1133 | 0.1598 | 0.71 | oui |
| -0.5 | -0.2736 | -0.0912 | 338 | 6 | 0.1388 | 0.1747 | 0.79 | oui |
| +0.0 | -0.0912 | +0.0912 | 629 | 10 | 0.2582 | 0.1974 | 1.31 | oui |
| +0.5 | +0.0912 | +0.2736 | 461 | 8 | 0.1892 | 0.1747 | 1.08 | oui |
| +1.0 | +0.2736 | +0.5472 | 394 | 7 | 0.1617 | 0.1598 | 1.01 | oui |
| +2.0 | +0.5472 | +∞ | 210 | 4 | 0.0862 | 0.0668 | 1.29 | oui |

**DTWEXBGS** (log) — σ à 60 pas = **0.02573** · estimateurs croisés : racine-h 0.02408, blocs disjoints 0.02755 (écart relatif 14.4 %) · dérive d'échantillon +0.00056 (+0.02 σ) · 2430 variations chevauchantes, 40 blocs indépendants · 2016-10-24 → 2026-10-16

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0386 | 170 | 3 | 0.0700 | 0.0668 | 1.05 | oui |
| -1.0 | -0.0386 | -0.0193 | 379 | 6 | 0.1560 | 0.1598 | 0.98 | oui |
| -0.5 | -0.0193 | -0.0064 | 359 | 6 | 0.1477 | 0.1747 | 0.85 | oui |
| +0.0 | -0.0064 | +0.0064 | 547 | 9 | 0.2251 | 0.1974 | 1.14 | oui |
| +0.5 | +0.0064 | +0.0193 | 469 | 8 | 0.1930 | 0.1747 | 1.10 | oui |
| +1.0 | +0.0193 | +0.0386 | 302 | 5 | 0.1243 | 0.1598 | 0.78 | oui |
| +2.0 | +0.0386 | +∞ | 204 | 3 | 0.0840 | 0.0668 | 1.26 | oui |

**NASDAQ100** (log) — σ à 60 pas = **0.08869** · estimateurs croisés : racine-h 0.11147, blocs disjoints 0.08148 (écart relatif 36.8 %) · dérive d'échantillon +0.04420 (+0.50 σ) · 2451 variations chevauchantes, 41 blocs indépendants · 2016-10-24 → 2026-10-19

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.1330 | 108 | 2 | 0.0441 | 0.0668 | 0.66 | oui |
| -1.0 | -0.1330 | -0.0665 | 167 | 3 | 0.0681 | 0.1598 | 0.43 ⚠ | oui |
| -0.5 | -0.0665 | -0.0222 | 186 | 3 | 0.0759 | 0.1747 | 0.43 ⚠ | oui |
| +0.0 | -0.0222 | +0.0222 | 353 | 6 | 0.1440 | 0.1974 | 0.73 | oui |
| +0.5 | +0.0222 | +0.0665 | 589 | 10 | 0.2403 | 0.1747 | 1.38 | oui |
| +1.0 | +0.0665 | +0.1330 | 732 | 12 | 0.2987 | 0.1598 | 1.87 | oui |
| +2.0 | +0.1330 | +∞ | 316 | 5 | 0.1289 | 0.0668 | 1.93 | oui |

**SP500** (log) — σ à 60 pas = **0.06913** · estimateurs croisés : racine-h 0.08847, blocs disjoints 0.06060 (écart relatif 46.0 %) · dérive d'échantillon +0.03050 (+0.44 σ) · 2450 variations chevauchantes, 41 blocs indépendants · 2016-10-24 → 2026-10-19

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.1037 | 115 | 2 | 0.0469 | 0.0668 | 0.70 | oui |
| -1.0 | -0.1037 | -0.0518 | 158 | 3 | 0.0645 | 0.1598 | 0.40 ⚠ | oui |
| -0.5 | -0.0518 | -0.0173 | 176 | 3 | 0.0718 | 0.1747 | 0.41 ⚠ | oui |
| +0.0 | -0.0173 | +0.0173 | 293 | 5 | 0.1196 | 0.1974 | 0.61 | oui |
| +0.5 | +0.0173 | +0.0518 | 753 | 13 | 0.3073 | 0.1747 | 1.76 | oui |
| +1.0 | +0.0518 | +0.1037 | 745 | 12 | 0.3041 | 0.1598 | 1.90 | oui |
| +2.0 | +0.1037 | +∞ | 210 | 4 | 0.0857 | 0.0668 | 1.28 | oui |

**VIXCLS** (log) — σ à 60 pas = **0.34643** · estimateurs croisés : racine-h 0.61283, blocs disjoints 0.37086 (écart relatif 76.9 %) · dérive d'échantillon +0.00400 (+0.01 σ) · 2483 variations chevauchantes, 41 blocs indépendants · 2016-10-24 → 2026-10-19

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.5196 | 77 | 1 | 0.0310 | 0.0668 | 0.46 ⚠ | oui |
| -1.0 | -0.5196 | -0.2598 | 383 | 6 | 0.1542 | 0.1598 | 0.97 | oui |
| -0.5 | -0.2598 | -0.0866 | 605 | 10 | 0.2437 | 0.1747 | 1.39 | oui |
| +0.0 | -0.0866 | +0.0866 | 619 | 10 | 0.2493 | 0.1974 | 1.26 | oui |
| +0.5 | +0.0866 | +0.2598 | 373 | 6 | 0.1502 | 0.1747 | 0.86 | oui |
| +1.0 | +0.2598 | +0.5196 | 248 | 4 | 0.0999 | 0.1598 | 0.62 | oui |
| +2.0 | +0.5196 | +∞ | 178 | 3 | 0.0717 | 0.0668 | 1.07 | oui |

---

## 6. TEST D'ASYMÉTRIE — DÉFINITION UNIQUE (R-030), L'ESPÉRANCE DÉCIDE

> Test d'admission : **espérance calculée sur la grille symétrique complète, les deux queues incluses**. Le rapport gain maximal / perte maximale est publié **pour information** et ne peut fonder aucune admission seul (T-001, faute E-018). Le rapport gain maximal / perte du scénario central est **interdit**. Une seule formulation, appliquée à tous les candidats, position détenue comprise.

| candidat | verdict | espérance % NAV | sans dérive | 1re moitié | 2e moitié | gain max | perte max | ratio (info) | critères échoués |
|---|:---:|---:|---:|---:|---:|---:|---:|---:|---|
| M005-DCOILBRENTEU-HAUSSE-ALIGNE | REFUSEE | +0.278 | +0.130 | +0.254 | +0.205 | +5.09 | -3.21 | 1.58:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DCOILBRENTEU-HAUSSE-CONTRARIEN | REFUSEE | +0.278 | +0.130 | +0.254 | +0.205 | +5.09 | -3.21 | 1.58:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DCOILBRENTEU-BAISSE-ALIGNE | REFUSEE | -0.278 | -0.130 | -0.254 | -0.205 | +3.21 | -5.09 | 0.63:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILBRENTEU-BAISSE-CONTRARIEN | REFUSEE | -0.278 | -0.130 | -0.254 | -0.205 | +3.21 | -5.09 | 0.63:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-HAUSSE-ALIGNE | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-HAUSSE-CONTRARIEN | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-BAISSE-ALIGNE | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-BAISSE-CONTRARIEN | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-HAUSSE-ALIGNE | REFUSEE | -0.002 | -0.066 | -0.077 | +0.039 | +0.62 | -0.71 | 0.87:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-HAUSSE-CONTRARIEN | REFUSEE | -0.002 | -0.066 | -0.077 | +0.039 | +0.62 | -0.71 | 0.87:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-BAISSE-ALIGNE | REFUSEE | +0.002 | +0.066 | +0.077 | -0.039 | +0.71 | -0.62 | 1.15:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-BAISSE-CONTRARIEN | REFUSEE | +0.002 | +0.066 | +0.077 | -0.039 | +0.71 | -0.62 | 1.15:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-HAUSSE-ALIGNE | REFUSEE | -0.060 | -0.075 | -0.030 | -0.071 | +0.49 | -0.60 | 0.82:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-HAUSSE-CONTRARIEN | REFUSEE | -0.060 | -0.075 | -0.030 | -0.071 | +0.49 | -0.60 | 0.82:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-BAISSE-ALIGNE | REFUSEE | +0.060 | +0.075 | +0.030 | +0.071 | +0.60 | -0.49 | 1.22:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DEXUSEU-BAISSE-CONTRARIEN | REFUSEE | +0.060 | +0.075 | +0.030 | +0.071 | +0.60 | -0.49 | 1.22:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DGS10-HAUSSE-ALIGNE | REFUSEE | +0.008 | -0.026 | -0.052 | +0.058 | +0.48 | -0.57 | 0.84:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-HAUSSE-CONTRARIEN | REFUSEE | +0.008 | -0.026 | -0.052 | +0.058 | +0.48 | -0.57 | 0.84:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-BAISSE-ALIGNE | REFUSEE | -0.008 | +0.026 | +0.052 | -0.058 | +0.57 | -0.48 | 1.19:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-BAISSE-CONTRARIEN | REFUSEE | -0.008 | +0.026 | +0.052 | -0.058 | +0.57 | -0.48 | 1.19:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-HAUSSE-ALIGNE | REFUSEE | -0.006 | -0.016 | -0.023 | +0.006 | +0.13 | -0.17 | 0.78:1 | 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-HAUSSE-CONTRARIEN | REFUSEE | -0.006 | -0.016 | -0.023 | +0.006 | +0.13 | -0.17 | 0.78:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-BAISSE-ALIGNE | REFUSEE | +0.006 | +0.016 | +0.023 | -0.006 | +0.17 | -0.13 | 1.29:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-BAISSE-CONTRARIEN | REFUSEE | +0.006 | +0.016 | +0.023 | -0.006 | +0.17 | -0.13 | 1.29:1 | 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-HAUSSE-ALIGNE | REFUSEE | +0.014 | -0.043 | -0.100 | +0.128 | +0.76 | -0.96 | 0.79:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-HAUSSE-CONTRARIEN | REFUSEE | +0.014 | -0.043 | -0.100 | +0.128 | +0.76 | -0.96 | 0.79:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-BAISSE-ALIGNE | REFUSEE | -0.014 | +0.043 | +0.100 | -0.128 | +0.96 | -0.76 | 1.26:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-BAISSE-CONTRARIEN | REFUSEE | -0.014 | +0.043 | +0.100 | -0.128 | +0.96 | -0.76 | 1.26:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-HAUSSE-ALIGNE | REFUSEE | -0.067 | -0.072 | -0.086 | -0.053 | +0.35 | -0.48 | 0.73:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-HAUSSE-CONTRARIEN | REFUSEE | -0.067 | -0.072 | -0.086 | -0.053 | +0.35 | -0.48 | 0.73:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-BAISSE-ALIGNE | REFUSEE | +0.067 | +0.072 | +0.086 | +0.053 | +0.48 | -0.35 | 1.36:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DTWEXBGS-BAISSE-CONTRARIEN | REFUSEE | +0.067 | +0.072 | +0.086 | +0.053 | +0.48 | -0.35 | 1.36:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-HAUSSE-ALIGNE | REFUSEE | +0.305 | -0.034 | +0.450 | +0.183 | +1.48 | -1.37 | 1.08:1 | 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-HAUSSE-CONTRARIEN | REFUSEE | +0.305 | -0.034 | +0.450 | +0.183 | +1.48 | -1.37 | 1.08:1 | 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-BAISSE-ALIGNE | REFUSEE | -0.305 | +0.034 | -0.450 | -0.183 | +1.37 | -1.48 | 0.93:1 | 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-NASDAQ100-BAISSE-CONTRARIEN | REFUSEE | -0.305 | +0.034 | -0.450 | -0.183 | +1.37 | -1.48 | 0.93:1 | 12_esperance_positive, 13_esperance_non_portee_par_derive, 14_esperance_stable_dans_le_temps |
| M005-SP500-HAUSSE-ALIGNE | REFUSEE | +0.186 | -0.044 | +0.213 | +0.151 | +1.11 | -1.11 | 1.00:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-SP500-HAUSSE-CONTRARIEN | REFUSEE | +0.186 | -0.044 | +0.213 | +0.151 | +1.11 | -1.11 | 1.00:1 | 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-SP500-BAISSE-ALIGNE | REFUSEE | -0.186 | +0.044 | -0.213 | -0.151 | +1.11 | -1.11 | 1.00:1 | 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-SP500-BAISSE-CONTRARIEN | REFUSEE | -0.186 | +0.044 | -0.213 | -0.151 | +1.11 | -1.11 | 1.00:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |

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

- `BAMLC0A0CM` : percentile REFUSÉ sur 5 ans — profondeur réelle 783 obs / 2.99 ans (début 2023-10-23). R-011 : un percentile calculé sur une série tronquée est sans valeur.
- `BAMLH0A0HYM2` : percentile REFUSÉ sur 5 ans — profondeur réelle 784 obs / 2.99 ans (début 2023-10-23). R-011 : un percentile calculé sur une série tronquée est sans valeur.
- `BAMLH0A0HYM2` : instrument NON ADMISSIBLE — P&L non calculable depuis le dépôt : l'OAS est un spread, et le dépôt ne contient pas le rendement de l'indice, donc pas la duration de spread. Aucune valeur ne peut être produite sans un chiffre extérieur aux données (E-002).
- `BAMLC0A0CM` : instrument NON ADMISSIBLE — P&L non calculable depuis le dépôt : l'OAS est un spread, et le dépôt ne contient pas le rendement de l'indice, donc pas la duration de spread. Aucune valeur ne peut être produite sans un chiffre extérieur aux données (E-002).
- Retards sur la date d'arrêté unique (E-014) : DCOILBRENTEU 3 séance(s), DCOILWTICO 3 séance(s), DEXJPUS 1 séance(s), DEXUSEU 1 séance(s), DTWEXBGS 1 séance(s)

**Vérification tierce (R-032) : NON SATISFAITE pour ce brief.** Le moteur ne dispose d'aucune source extérieure au dépôt. Trois estimateurs **internes** de σ sont publiés côte à côte au §5 ; ce sont des contrôles de cohérence interne, **pas** une vérification tierce, et ils ne sont pas présentés comme telle.

**Ce que ce moteur ne peut pas faire.** Il ne prouve aucune capacité prédictive : la règle de confirmation est une règle de percentile, déclarée et symétrique, pas un modèle validé hors échantillon. Il ne corrige pas la multiplicité : 40 candidats sont évalués et aucune pénalité de sélection n'est appliquée à l'espérance — c'est une limite déclarée, pas un oubli. Il ne voit ni les événements politiques, ni les décisions de banques centrales : le dépôt ne contient que des séries FRED, et toute affirmation de politique monétaire non adossée à `DFF` est refusée (critère 15, faute E-006).

---

*Fin du brief 005. Produit mécaniquement. Ne constitue pas un conseil en investissement.*