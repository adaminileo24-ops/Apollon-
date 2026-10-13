# BRIEF MACRO n° 005 — arrêté au 2026-10-09

*Produit par `apollon_macro.py` le 2026-10-13T23:26:35+00:00. Aucune valeur de ce document n'est saisie à la main : chacune porte sa série, sa date et sa profondeur. Bloc à copier tel quel.*

**Grille de scénarios (R-029, §11), déclarée avant toute lecture de données et empreintée :** `[-2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0]` · empreinte SHA-256 `6aaeb3863c875923…` · symétrique : True · horizon 60 séances (3 mois pour les séries mensuelles).

---

## 1. CONCLUSION, ÉNONCÉE D'ABORD

**40 candidats déclarés d'avance (10 instruments × 2 directions × 2 règles de confirmation). 40 évalués. 0 thèse(s) survivent aux quinze critères.**

**Abstention. Aucune thèse ne survit.** Ce n'est pas un silence : c'est un résultat, produit par le même portier que celui qui aurait admis une thèse. Le détail des échecs, critère par critère, figure au §6. La Section Macro ne transmet rien à la Section Risque ce cycle.

**Position détenue (contrôle 9, E-020) — 100 % cash, testée sur la même grille.** Espérance excédentaire du cash : +0.000 % de NAV. Référence 60/40 : +1.364 % (hors dérive : -0.182 %). **Écart du cash contre la référence : -1.364 % de NAV** sur 60 séances.

---

## 2. CE QUI A CHANGÉ — MÉCANISME, PAS CONTENU

Fait, étiqueté : les briefs 001 à 004 étaient rédigés par un agent. Celui-ci est produit par un moteur. Le paramètre libre de la Section Macro — la grille de scénarios — n'est plus accessible à l'agent : il est déclaré en tête de fichier, symétrique par construction, et son empreinte SHA-256 est vérifiée avant chaque usage. Sur le brief 004, ce paramètre avait porté le ratio annoncé de 1,29:1 à 3,0:1.

---

## 3. M1 · M2 · M3 · M4 — ÉTAT DES SÉRIES (FAIT)

Toutes les valeurs sont des FAITS lus dans le dépôt. Le retard est compté en séances ouvrées depuis la date d'arrêté unique. Les couples obligatoires sont vérifiés par le rendu : ce bloc ne peut pas être émis si un membre d'un couple manque.

| série | rôle déclaré | valeur | date | retard | n obs | profondeur | pct 1 an | pct 5 ans | pct complet |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| BAMLC0A0CM | risque_credit_ig | 0.83 | 2026-10-09 | 0 | 782 | 2.98 ans | 83.7 | REFUSÉ (insuffisante, -38 %) | 47.2 |
| BAMLH0A0HYM2 | risque_credit_hy | 3.11 | 2026-10-09 | 0 | 783 | 2.98 ans | 86.5 | REFUSÉ (insuffisante, -38 %) | 57.9 |
| CPIAUCSL | inflation_globale | 334.1 | 2026-08-01 | 69 | 118 | 9.83 ans | 100.0 | 100.0 | 100.0 |
| CPILFESL | inflation_sous_jacente | 337.8 | 2026-08-01 | 69 | 118 | 9.83 ans | 100.0 | 100.0 | 100.0 |
| DCOILBRENTEU | prix_energie | 125.4 | 2026-10-06 | 3 | 2529 | 9.97 ans | 97.2 | 98.5 | 99.2 |
| DCOILWTICO | prix_energie_wti | 96.24 | 2026-10-06 | 3 | 2493 | 9.97 ans | 79.0 | 87.3 | 93.6 |
| DEXJPUS | devise_usdjpy | 158.3 | 2026-10-09 | 0 | 2493 | 9.98 ans | 56.3 | 90.0 | 94.9 |
| DEXUSEU | devise_eurusd | 1.119 | 2026-10-09 | 0 | 2493 | 9.98 ans | 1.2 | 62.3 | 46.7 |
| DFF | politique_monetaire | 3.88 | 2026-10-09 | 0 | 3647 | 9.98 ans | 100.0 | 26.3 | 70.9 |
| DFII10 | taux_reel_10a | 2.91 | 2026-10-09 | 0 | 2496 | 9.98 ans | 98.4 | 99.7 | 99.8 |
| DGS10 | taux_nominal_10a | 5.24 | 2026-10-09 | 0 | 2496 | 9.98 ans | 97.6 | 99.5 | 99.8 |
| DGS2 | taux_nominal_2a | 4.8 | 2026-10-09 | 0 | 2496 | 9.98 ans | 96.8 | 88.4 | 94.2 |
| DGS30 | taux_nominal_30a | 5.6 | 2026-10-09 | 0 | 2496 | 9.98 ans | 97.6 | 99.5 | 99.8 |
| DTWEXBGS | dollar_large | 121.6 | 2026-10-09 | 0 | 2491 | 9.98 ans | 96.8 | 65.6 | 80.6 |
| INDPRO | activite_industrielle | 103.1 | 2026-08-01 | 69 | 119 | 9.83 ans | 100.0 | 100.0 | 92.4 |
| NASDAQ100 | prix_actions_tech | 3.088e+04 | 2026-10-09 | 0 | 2510 | 9.98 ans | 98.8 | 99.8 | 99.9 |
| OVXCLS | volatilite_implicite_petrole | 48.9 | 2026-10-09 | 0 | 2511 | 9.98 ans | 43.7 | 76.5 | 82.2 |
| PAYEMS | emploi | 1.59e+05 | 2026-09-01 | 38 | 120 | 9.92 ans | 100.0 | 100.0 | 100.0 |
| SP500 | prix_actions | 7812 | 2026-10-09 | 0 | 2509 | 9.98 ans | 99.6 | 99.9 | 100.0 |
| T10Y2Y | pente_courbe | 0.44 | 2026-10-09 | 0 | 2496 | 9.98 ans | 26.6 | 67.9 | 53.2 |
| T10YIE | point_mort_10a | 2.33 | 2026-10-09 | 0 | 2496 | 9.98 ans | 62.7 | 51.9 | 72.6 |
| T5YIFR | point_mort_5a5a | 2.32 | 2026-10-09 | 0 | 2496 | 9.98 ans | 87.3 | 73.7 | 86.4 |
| UNRATE | chomage | 4.2 | 2026-09-01 | 38 | 119 | 9.92 ans | 33.3 | 78.3 | 63.9 |
| VIXCLS | volatilite_implicite | 14.84 | 2026-10-09 | 0 | 2542 | 9.98 ans | 7.5 | 21.1 | 32.1 |
| VXDCLS | volatilite_implicite_dow | 15.12 | 2026-10-09 | 0 | 2512 | 9.98 ans | 35.7 | 37.6 | 42.0 |
| VXVCLS | volatilite_implicite_3m | 17.77 | 2026-10-09 | 0 | 2509 | 9.98 ans | 5.2 | 22.7 | 37.7 |

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
- corrélation des variations à 60 séances : BAMLC0A0CM / BAMLH0A0HYM2 = +0.939 sur 722 points (seuil 0.9)
- corrélation des variations à 60 séances : DGS10 / DGS30 = +0.967 sur 2436 points (seuil 0.9)
- corrélation des variations à 60 séances : INDPRO / PAYEMS = +0.913 sur 116 points (seuil 0.9)
- corrélation des variations à 60 séances : INDPRO / UNRATE = -0.918 sur 115 points (seuil 0.9)
- corrélation des variations à 60 séances : NASDAQ100 / SP500 = +0.903 sur 2449 points (seuil 0.9)
- corrélation des variations à 60 séances : PAYEMS / UNRATE = -0.983 sur 116 points (seuil 0.9)
- corrélation des variations à 60 séances : VIXCLS / VXDCLS = +0.929 sur 2449 points (seuil 0.9)
- corrélation des variations à 60 séances : VIXCLS / VXVCLS = +0.958 sur 2449 points (seuil 0.9)
- corrélation des variations à 60 séances : VXDCLS / VXVCLS = +0.934 sur 2449 points (seuil 0.9)

---

## 5. GRILLE, σ MESURÉ, ET DOUBLE CONFRONTATION DES PROBABILITÉS

σ est **mesuré** sur chaque série, jamais choisi. Les probabilités sont les **fréquences historiques** dans chaque bande, jamais un jugement. L'effectif de chaque bande est publié ; sous 20 observations la bande est déclarée NON ESTIMABLE. La colonne « emp./gauss. » est la double confrontation exigée par §11.5 : tout écart supérieur à un facteur 2 est déclaré (⚠).

**BAMLH0A0HYM2** (niveau) — σ à 60 pas = **0.45123** · estimateurs croisés : racine-h 0.54056, blocs disjoints 0.36902 (écart relatif 46.5 %) · dérive d'échantillon -0.09260 (-0.21 σ) · 723 variations chevauchantes, 12 blocs indépendants · 2023-10-16 → 2026-10-09

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.6768 | 51 | 1 | 0.0705 | 0.0668 | 1.06 | oui |
| -1.0 | -0.6768 | -0.3384 | 117 | 2 | 0.1618 | 0.1598 | 1.01 | oui |
| -0.5 | -0.3384 | -0.1128 | 189 | 3 | 0.2614 | 0.1747 | 1.50 | oui |
| +0.0 | -0.1128 | +0.1128 | 195 | 3 | 0.2697 | 0.1974 | 1.37 | oui |
| +0.5 | +0.1128 | +0.3384 | 80 | 1 | 0.1107 | 0.1747 | 0.63 | oui |
| +1.0 | +0.3384 | +0.6768 | 62 | 1 | 0.0858 | 0.1598 | 0.54 | oui |
| +2.0 | +0.6768 | +∞ | 29 | 0 | 0.0401 | 0.0668 | 0.60 | oui |

**DCOILBRENTEU** (log) — σ à 60 pas = **0.24832** · estimateurs croisés : racine-h 0.24965, blocs disjoints 0.31075 (écart relatif 25.1 %) · dérive d'échantillon +0.01733 (+0.07 σ) · 2469 variations chevauchantes, 41 blocs indépendants · 2016-10-17 → 2026-10-06

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.3725 | 83 | 1 | 0.0336 | 0.0668 | 0.50 | oui |
| -1.0 | -0.3725 | -0.1862 | 155 | 3 | 0.0628 | 0.1598 | 0.39 ⚠ | oui |
| -0.5 | -0.1862 | -0.0621 | 500 | 8 | 0.2025 | 0.1747 | 1.16 | oui |
| +0.0 | -0.0621 | +0.0621 | 771 | 13 | 0.3123 | 0.1974 | 1.58 | oui |
| +0.5 | +0.0621 | +0.1862 | 602 | 10 | 0.2438 | 0.1747 | 1.40 | oui |
| +1.0 | +0.1862 | +0.3725 | 218 | 4 | 0.0883 | 0.1598 | 0.55 | oui |
| +2.0 | +0.3725 | +∞ | 140 | 2 | 0.0567 | 0.0668 | 0.85 | oui |

**DCOILWTICO** — non scénarisable : convention log inapplicable : 1 observation(s) non strictement positive(s), minimum -36.98 le 2020-04-20. Le prix a été négatif : aucun log-rendement n'existe. La série est déclarée NON SCÉNARISABLE plutôt que corrigée en silence.

**DEXJPUS** (log) — σ à 60 pas = **0.04183** · estimateurs croisés : racine-h 0.04379, blocs disjoints 0.05006 (écart relatif 19.7 %) · dérive d'échantillon +0.00874 (+0.21 σ) · 2433 variations chevauchantes, 41 blocs indépendants · 2016-10-17 → 2026-10-09

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0627 | 104 | 2 | 0.0427 | 0.0668 | 0.64 | oui |
| -1.0 | -0.0627 | -0.0314 | 243 | 4 | 0.0999 | 0.1598 | 0.62 | oui |
| -0.5 | -0.0314 | -0.0105 | 387 | 6 | 0.1591 | 0.1747 | 0.91 | oui |
| +0.0 | -0.0105 | +0.0105 | 494 | 8 | 0.2030 | 0.1974 | 1.03 | oui |
| +0.5 | +0.0105 | +0.0314 | 536 | 9 | 0.2203 | 0.1747 | 1.26 | oui |
| +1.0 | +0.0314 | +0.0627 | 476 | 8 | 0.1956 | 0.1598 | 1.22 | oui |
| +2.0 | +0.0627 | +∞ | 193 | 3 | 0.0793 | 0.0668 | 1.19 | oui |

**DEXUSEU** (log) — σ à 60 pas = **0.03425** · estimateurs croisés : racine-h 0.03467, blocs disjoints 0.03842 (écart relatif 12.2 %) · dérive d'échantillon +0.00176 (+0.05 σ) · 2433 variations chevauchantes, 41 blocs indépendants · 2016-10-17 → 2026-10-09

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0514 | 130 | 2 | 0.0534 | 0.0668 | 0.80 | oui |
| -1.0 | -0.0514 | -0.0257 | 322 | 5 | 0.1323 | 0.1598 | 0.83 | oui |
| -0.5 | -0.0257 | -0.0086 | 509 | 8 | 0.2092 | 0.1747 | 1.20 | oui |
| +0.0 | -0.0086 | +0.0086 | 617 | 10 | 0.2536 | 0.1974 | 1.28 | oui |
| +0.5 | +0.0086 | +0.0257 | 321 | 5 | 0.1319 | 0.1747 | 0.76 | oui |
| +1.0 | +0.0257 | +0.0514 | 307 | 5 | 0.1262 | 0.1598 | 0.79 | oui |
| +2.0 | +0.0514 | +∞ | 227 | 4 | 0.0933 | 0.0668 | 1.40 | oui |

**DGS10** (niveau) — σ à 60 pas = **0.42322** · estimateurs croisés : racine-h 0.41454, blocs disjoints 0.45255 (écart relatif 9.2 %) · dérive d'échantillon +0.06452 (+0.15 σ) · 2436 variations chevauchantes, 41 blocs indépendants · 2016-10-17 → 2026-10-09

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.6348 | 123 | 2 | 0.0505 | 0.0668 | 0.76 | oui |
| -1.0 | -0.6348 | -0.3174 | 284 | 5 | 0.1166 | 0.1598 | 0.73 | oui |
| -0.5 | -0.3174 | -0.1058 | 371 | 6 | 0.1523 | 0.1747 | 0.87 | oui |
| +0.0 | -0.1058 | +0.1058 | 528 | 9 | 0.2167 | 0.1974 | 1.10 | oui |
| +0.5 | +0.1058 | +0.3174 | 555 | 9 | 0.2278 | 0.1747 | 1.30 | oui |
| +1.0 | +0.3174 | +0.6348 | 364 | 6 | 0.1494 | 0.1598 | 0.93 | oui |
| +2.0 | +0.6348 | +∞ | 211 | 4 | 0.0866 | 0.0668 | 1.30 | oui |

**DGS2** (niveau) — σ à 60 pas = **0.49634** · estimateurs croisés : racine-h 0.42192, blocs disjoints 0.52061 (écart relatif 23.4 %) · dérive d'échantillon +0.08338 (+0.17 σ) · 2436 variations chevauchantes, 41 blocs indépendants · 2016-10-17 → 2026-10-09

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.7445 | 115 | 2 | 0.0472 | 0.0668 | 0.71 | oui |
| -1.0 | -0.7445 | -0.3723 | 228 | 4 | 0.0936 | 0.1598 | 0.59 | oui |
| -0.5 | -0.3723 | -0.1241 | 323 | 5 | 0.1326 | 0.1747 | 0.76 | oui |
| +0.0 | -0.1241 | +0.1241 | 739 | 12 | 0.3034 | 0.1974 | 1.54 | oui |
| +0.5 | +0.1241 | +0.3723 | 478 | 8 | 0.1962 | 0.1747 | 1.12 | oui |
| +1.0 | +0.3723 | +0.7445 | 352 | 6 | 0.1445 | 0.1598 | 0.90 | oui |
| +2.0 | +0.7445 | +∞ | 201 | 3 | 0.0825 | 0.0668 | 1.24 | oui |

**DGS30** (niveau) — σ à 60 pas = **0.36506** · estimateurs croisés : racine-h 0.39247, blocs disjoints 0.39247 (écart relatif 7.5 %) · dérive d'échantillon +0.05912 (+0.16 σ) · 2436 variations chevauchantes, 41 blocs indépendants · 2016-10-17 → 2026-10-09

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.5476 | 128 | 2 | 0.0525 | 0.0668 | 0.79 | oui |
| -1.0 | -0.5476 | -0.2738 | 276 | 5 | 0.1133 | 0.1598 | 0.71 | oui |
| -0.5 | -0.2738 | -0.0913 | 338 | 6 | 0.1388 | 0.1747 | 0.79 | oui |
| +0.0 | -0.0913 | +0.0913 | 629 | 10 | 0.2582 | 0.1974 | 1.31 | oui |
| +0.5 | +0.0913 | +0.2738 | 461 | 8 | 0.1892 | 0.1747 | 1.08 | oui |
| +1.0 | +0.2738 | +0.5476 | 393 | 7 | 0.1613 | 0.1598 | 1.01 | oui |
| +2.0 | +0.5476 | +∞ | 211 | 4 | 0.0866 | 0.0668 | 1.30 | oui |

**DTWEXBGS** (log) — σ à 60 pas = **0.02578** · estimateurs croisés : racine-h 0.02408, blocs disjoints 0.02780 (écart relatif 15.4 %) · dérive d'échantillon +0.00062 (+0.02 σ) · 2431 variations chevauchantes, 41 blocs indépendants · 2016-10-17 → 2026-10-09

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0387 | 168 | 3 | 0.0691 | 0.0668 | 1.03 | oui |
| -1.0 | -0.0387 | -0.0193 | 381 | 6 | 0.1567 | 0.1598 | 0.98 | oui |
| -0.5 | -0.0193 | -0.0064 | 358 | 6 | 0.1473 | 0.1747 | 0.84 | oui |
| +0.0 | -0.0064 | +0.0064 | 549 | 9 | 0.2258 | 0.1974 | 1.14 | oui |
| +0.5 | +0.0064 | +0.0193 | 464 | 8 | 0.1909 | 0.1747 | 1.09 | oui |
| +1.0 | +0.0193 | +0.0387 | 306 | 5 | 0.1259 | 0.1598 | 0.79 | oui |
| +2.0 | +0.0387 | +∞ | 205 | 3 | 0.0843 | 0.0668 | 1.26 | oui |

**NASDAQ100** (log) — σ à 60 pas = **0.08871** · estimateurs croisés : racine-h 0.11137, blocs disjoints 0.07858 (écart relatif 41.7 %) · dérive d'échantillon +0.04420 (+0.50 σ) · 2450 variations chevauchantes, 41 blocs indépendants · 2016-10-17 → 2026-10-09

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.1331 | 108 | 2 | 0.0441 | 0.0668 | 0.66 | oui |
| -1.0 | -0.1331 | -0.0665 | 167 | 3 | 0.0682 | 0.1598 | 0.43 ⚠ | oui |
| -0.5 | -0.0665 | -0.0222 | 186 | 3 | 0.0759 | 0.1747 | 0.43 ⚠ | oui |
| +0.0 | -0.0222 | +0.0222 | 353 | 6 | 0.1441 | 0.1974 | 0.73 | oui |
| +0.5 | +0.0222 | +0.0665 | 589 | 10 | 0.2404 | 0.1747 | 1.38 | oui |
| +1.0 | +0.0665 | +0.1331 | 731 | 12 | 0.2984 | 0.1598 | 1.87 | oui |
| +2.0 | +0.1331 | +∞ | 316 | 5 | 0.1290 | 0.0668 | 1.93 | oui |

**SP500** (log) — σ à 60 pas = **0.06916** · estimateurs croisés : racine-h 0.08846, blocs disjoints 0.06162 (écart relatif 43.6 %) · dérive d'échantillon +0.03054 (+0.44 σ) · 2449 variations chevauchantes, 41 blocs indépendants · 2016-10-17 → 2026-10-09

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.1037 | 115 | 2 | 0.0470 | 0.0668 | 0.70 | oui |
| -1.0 | -0.1037 | -0.0519 | 158 | 3 | 0.0645 | 0.1598 | 0.40 ⚠ | oui |
| -0.5 | -0.0519 | -0.0173 | 176 | 3 | 0.0719 | 0.1747 | 0.41 ⚠ | oui |
| +0.0 | -0.0173 | +0.0173 | 293 | 5 | 0.1196 | 0.1974 | 0.61 | oui |
| +0.5 | +0.0173 | +0.0519 | 749 | 12 | 0.3058 | 0.1747 | 1.75 | oui |
| +1.0 | +0.0519 | +0.1037 | 748 | 12 | 0.3054 | 0.1598 | 1.91 | oui |
| +2.0 | +0.1037 | +∞ | 210 | 4 | 0.0857 | 0.0668 | 1.28 | oui |

**VIXCLS** (log) — σ à 60 pas = **0.34661** · estimateurs croisés : racine-h 0.61209, blocs disjoints 0.38633 (écart relatif 76.6 %) · dérive d'échantillon +0.00375 (+0.01 σ) · 2482 variations chevauchantes, 41 blocs indépendants · 2016-10-17 → 2026-10-09

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.5199 | 77 | 1 | 0.0310 | 0.0668 | 0.46 ⚠ | oui |
| -1.0 | -0.5199 | -0.2600 | 384 | 6 | 0.1547 | 0.1598 | 0.97 | oui |
| -0.5 | -0.2600 | -0.0867 | 605 | 10 | 0.2438 | 0.1747 | 1.40 | oui |
| +0.0 | -0.0867 | +0.0867 | 617 | 10 | 0.2486 | 0.1974 | 1.26 | oui |
| +0.5 | +0.0867 | +0.2600 | 373 | 6 | 0.1503 | 0.1747 | 0.86 | oui |
| +1.0 | +0.2600 | +0.5199 | 248 | 4 | 0.0999 | 0.1598 | 0.63 | oui |
| +2.0 | +0.5199 | +∞ | 178 | 3 | 0.0717 | 0.0668 | 1.07 | oui |

---

## 6. TEST D'ASYMÉTRIE — DÉFINITION UNIQUE (R-030), L'ESPÉRANCE DÉCIDE

> Test d'admission : **espérance calculée sur la grille symétrique complète, les deux queues incluses**. Le rapport gain maximal / perte maximale est publié **pour information** et ne peut fonder aucune admission seul (T-001, faute E-018). Le rapport gain maximal / perte du scénario central est **interdit**. Une seule formulation, appliquée à tous les candidats, position détenue comprise.

| candidat | verdict | espérance % NAV | sans dérive | 1re moitié | 2e moitié | gain max | perte max | ratio (info) | critères échoués |
|---|:---:|---:|---:|---:|---:|---:|---:|---:|---|
| M005-DCOILBRENTEU-HAUSSE-ALIGNE | REFUSEE | +0.270 | +0.128 | +0.251 | +0.170 | +5.07 | -3.21 | 1.58:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DCOILBRENTEU-HAUSSE-CONTRARIEN | REFUSEE | +0.270 | +0.128 | +0.251 | +0.170 | +5.07 | -3.21 | 1.58:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DCOILBRENTEU-BAISSE-ALIGNE | REFUSEE | -0.270 | -0.128 | -0.251 | -0.170 | +3.21 | -5.07 | 0.63:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILBRENTEU-BAISSE-CONTRARIEN | REFUSEE | -0.270 | -0.128 | -0.251 | -0.170 | +3.21 | -5.07 | 0.63:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-HAUSSE-ALIGNE | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-HAUSSE-CONTRARIEN | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-BAISSE-ALIGNE | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-BAISSE-CONTRARIEN | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-HAUSSE-ALIGNE | REFUSEE | -0.001 | -0.067 | -0.076 | +0.040 | +0.62 | -0.72 | 0.87:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-HAUSSE-CONTRARIEN | REFUSEE | -0.001 | -0.067 | -0.076 | +0.040 | +0.62 | -0.72 | 0.87:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-BAISSE-ALIGNE | REFUSEE | +0.001 | +0.067 | +0.076 | -0.040 | +0.72 | -0.62 | 1.15:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-BAISSE-CONTRARIEN | REFUSEE | +0.001 | +0.067 | +0.076 | -0.040 | +0.72 | -0.62 | 1.15:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-HAUSSE-ALIGNE | REFUSEE | -0.060 | -0.075 | -0.030 | -0.072 | +0.49 | -0.60 | 0.82:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-HAUSSE-CONTRARIEN | REFUSEE | -0.060 | -0.075 | -0.030 | -0.072 | +0.49 | -0.60 | 0.82:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-BAISSE-ALIGNE | REFUSEE | +0.060 | +0.075 | +0.030 | +0.072 | +0.60 | -0.49 | 1.22:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DEXUSEU-BAISSE-CONTRARIEN | REFUSEE | +0.060 | +0.075 | +0.030 | +0.072 | +0.60 | -0.49 | 1.22:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DGS10-HAUSSE-ALIGNE | REFUSEE | +0.007 | -0.029 | -0.053 | +0.056 | +0.48 | -0.57 | 0.84:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-HAUSSE-CONTRARIEN | REFUSEE | +0.007 | -0.029 | -0.053 | +0.056 | +0.48 | -0.57 | 0.84:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-BAISSE-ALIGNE | REFUSEE | -0.007 | +0.029 | +0.053 | -0.056 | +0.57 | -0.48 | 1.20:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-BAISSE-CONTRARIEN | REFUSEE | -0.007 | +0.029 | +0.053 | -0.056 | +0.57 | -0.48 | 1.20:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-HAUSSE-ALIGNE | REFUSEE | -0.006 | -0.017 | -0.023 | +0.005 | +0.13 | -0.17 | 0.77:1 | 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-HAUSSE-CONTRARIEN | REFUSEE | -0.006 | -0.017 | -0.023 | +0.005 | +0.13 | -0.17 | 0.77:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-BAISSE-ALIGNE | REFUSEE | +0.006 | +0.017 | +0.023 | -0.005 | +0.17 | -0.13 | 1.30:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-BAISSE-CONTRARIEN | REFUSEE | +0.006 | +0.017 | +0.023 | -0.005 | +0.17 | -0.13 | 1.30:1 | 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-HAUSSE-ALIGNE | REFUSEE | +0.012 | -0.045 | -0.100 | +0.123 | +0.75 | -0.95 | 0.79:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-HAUSSE-CONTRARIEN | REFUSEE | +0.012 | -0.045 | -0.100 | +0.123 | +0.75 | -0.95 | 0.79:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-BAISSE-ALIGNE | REFUSEE | -0.012 | +0.045 | +0.100 | -0.123 | +0.95 | -0.75 | 1.27:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-BAISSE-CONTRARIEN | REFUSEE | -0.012 | +0.045 | +0.100 | -0.123 | +0.95 | -0.75 | 1.27:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-HAUSSE-ALIGNE | REFUSEE | -0.067 | -0.072 | -0.084 | -0.053 | +0.35 | -0.48 | 0.73:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-HAUSSE-CONTRARIEN | REFUSEE | -0.067 | -0.072 | -0.084 | -0.053 | +0.35 | -0.48 | 0.73:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-BAISSE-ALIGNE | REFUSEE | +0.067 | +0.072 | +0.084 | +0.053 | +0.48 | -0.35 | 1.36:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DTWEXBGS-BAISSE-CONTRARIEN | REFUSEE | +0.067 | +0.072 | +0.084 | +0.053 | +0.48 | -0.35 | 1.36:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-HAUSSE-ALIGNE | REFUSEE | +0.305 | -0.034 | +0.452 | +0.182 | +1.48 | -1.37 | 1.08:1 | 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-HAUSSE-CONTRARIEN | REFUSEE | +0.305 | -0.034 | +0.452 | +0.182 | +1.48 | -1.37 | 1.08:1 | 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-BAISSE-ALIGNE | REFUSEE | -0.305 | +0.034 | -0.452 | -0.182 | +1.37 | -1.48 | 0.93:1 | 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-NASDAQ100-BAISSE-CONTRARIEN | REFUSEE | -0.305 | +0.034 | -0.452 | -0.182 | +1.37 | -1.48 | 0.93:1 | 12_esperance_positive, 13_esperance_non_portee_par_derive, 14_esperance_stable_dans_le_temps |
| M005-SP500-HAUSSE-ALIGNE | REFUSEE | +0.186 | -0.043 | +0.214 | +0.153 | +1.11 | -1.11 | 1.00:1 | 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-SP500-HAUSSE-CONTRARIEN | REFUSEE | +0.186 | -0.043 | +0.214 | +0.153 | +1.11 | -1.11 | 1.00:1 | 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-SP500-BAISSE-ALIGNE | REFUSEE | -0.186 | +0.043 | -0.214 | -0.153 | +1.11 | -1.11 | 1.00:1 | 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-SP500-BAISSE-CONTRARIEN | REFUSEE | -0.186 | +0.043 | -0.214 | -0.153 | +1.11 | -1.11 | 1.00:1 | 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |

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

- `BAMLC0A0CM` : percentile REFUSÉ sur 5 ans — profondeur réelle 782 obs / 2.98 ans (début 2023-10-16). R-011 : un percentile calculé sur une série tronquée est sans valeur.
- `BAMLH0A0HYM2` : percentile REFUSÉ sur 5 ans — profondeur réelle 783 obs / 2.98 ans (début 2023-10-16). R-011 : un percentile calculé sur une série tronquée est sans valeur.
- `BAMLH0A0HYM2` : instrument NON ADMISSIBLE — P&L non calculable depuis le dépôt : l'OAS est un spread, et le dépôt ne contient pas le rendement de l'indice, donc pas la duration de spread. Aucune valeur ne peut être produite sans un chiffre extérieur aux données (E-002).
- `BAMLC0A0CM` : instrument NON ADMISSIBLE — P&L non calculable depuis le dépôt : l'OAS est un spread, et le dépôt ne contient pas le rendement de l'indice, donc pas la duration de spread. Aucune valeur ne peut être produite sans un chiffre extérieur aux données (E-002).
- Retards sur la date d'arrêté unique (E-014) : DCOILBRENTEU 3 séance(s), DCOILWTICO 3 séance(s)

**Vérification tierce (R-032) : NON SATISFAITE pour ce brief.** Le moteur ne dispose d'aucune source extérieure au dépôt. Trois estimateurs **internes** de σ sont publiés côte à côte au §5 ; ce sont des contrôles de cohérence interne, **pas** une vérification tierce, et ils ne sont pas présentés comme telle.

**Ce que ce moteur ne peut pas faire.** Il ne prouve aucune capacité prédictive : la règle de confirmation est une règle de percentile, déclarée et symétrique, pas un modèle validé hors échantillon. Il ne corrige pas la multiplicité : 40 candidats sont évalués et aucune pénalité de sélection n'est appliquée à l'espérance — c'est une limite déclarée, pas un oubli. Il ne voit ni les événements politiques, ni les décisions de banques centrales : le dépôt ne contient que des séries FRED, et toute affirmation de politique monétaire non adossée à `DFF` est refusée (critère 15, faute E-006).

---

*Fin du brief 005. Produit mécaniquement. Ne constitue pas un conseil en investissement.*