# BRIEF MACRO n° 005 — arrêté au 2026-10-14

*Produit par `apollon_macro.py` le 2026-10-16T09:49:08+00:00. Aucune valeur de ce document n'est saisie à la main : chacune porte sa série, sa date et sa profondeur. Bloc à copier tel quel.*

**Grille de scénarios (R-029, §11), déclarée avant toute lecture de données et empreintée :** `[-2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0]` · empreinte SHA-256 `6aaeb3863c875923…` · symétrique : True · horizon 60 séances (3 mois pour les séries mensuelles).

---

## 1. CONCLUSION, ÉNONCÉE D'ABORD

**40 candidats déclarés d'avance (10 instruments × 2 directions × 2 règles de confirmation). 40 évalués. 0 thèse(s) survivent aux quinze critères.**

**Abstention. Aucune thèse ne survit.** Ce n'est pas un silence : c'est un résultat, produit par le même portier que celui qui aurait admis une thèse. Le détail des échecs, critère par critère, figure au §6. La Section Macro ne transmet rien à la Section Risque ce cycle.

**Position détenue (contrôle 9, E-020) — 100 % cash, testée sur la même grille.** Espérance excédentaire du cash : +0.000 % de NAV. Référence 60/40 : +1.358 % (hors dérive : -0.188 %). **Écart du cash contre la référence : -1.358 % de NAV** sur 60 séances.

---

## 2. CE QUI A CHANGÉ — MÉCANISME, PAS CONTENU

Fait, étiqueté : les briefs 001 à 004 étaient rédigés par un agent. Celui-ci est produit par un moteur. Le paramètre libre de la Section Macro — la grille de scénarios — n'est plus accessible à l'agent : il est déclaré en tête de fichier, symétrique par construction, et son empreinte SHA-256 est vérifiée avant chaque usage. Sur le brief 004, ce paramètre avait porté le ratio annoncé de 1,29:1 à 3,0:1.

---

## 3. M1 · M2 · M3 · M4 — ÉTAT DES SÉRIES (FAIT)

Toutes les valeurs sont des FAITS lus dans le dépôt. Le retard est compté en séances ouvrées depuis la date d'arrêté unique. Les couples obligatoires sont vérifiés par le rendu : ce bloc ne peut pas être émis si un membre d'un couple manque.

| série | rôle déclaré | valeur | date | retard | n obs | profondeur | pct 1 an | pct 5 ans | pct complet |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| BAMLC0A0CM | risque_credit_ig | 0.84 | 2026-10-14 | 0 | 785 | 3.00 ans | 88.1 | REFUSÉ (insuffisante, -38 %) | 51.0 |
| BAMLH0A0HYM2 | risque_credit_hy | 3.25 | 2026-10-14 | 0 | 786 | 3.00 ans | 97.6 | REFUSÉ (insuffisante, -38 %) | 77.4 |
| CPIAUCSL | inflation_globale | 336.3 | 2026-09-01 | 43 | 119 | 9.92 ans | 100.0 | 100.0 | 100.0 |
| CPILFESL | inflation_sous_jacente | 338.9 | 2026-09-01 | 43 | 119 | 9.92 ans | 100.0 | 100.0 | 100.0 |
| DCOILBRENTEU | prix_energie | 126.5 | 2026-10-14 | 0 | 2534 | 9.99 ans | 96.4 | 98.6 | 99.3 |
| DCOILWTICO | prix_energie_wti | 101.9 | 2026-10-14 | 0 | 2498 | 9.99 ans | 91.3 | 91.8 | 95.9 |
| DEXJPUS | devise_usdjpy | 158.3 | 2026-10-09 | 3 | 2492 | 9.97 ans | 56.3 | 90.0 | 94.9 |
| DEXUSEU | devise_eurusd | 1.119 | 2026-10-09 | 3 | 2492 | 9.97 ans | 1.2 | 62.3 | 46.7 |
| DFF | politique_monetaire | 3.88 | 2026-10-14 | 0 | 3649 | 9.99 ans | 100.0 | 26.7 | 70.9 |
| DFII10 | taux_reel_10a | 2.84 | 2026-10-14 | 0 | 2497 | 9.99 ans | 95.2 | 99.0 | 99.5 |
| DGS10 | taux_nominal_10a | 5.19 | 2026-10-14 | 0 | 2497 | 9.99 ans | 95.6 | 99.1 | 99.6 |
| DGS2 | taux_nominal_2a | 4.82 | 2026-10-14 | 0 | 2497 | 9.99 ans | 97.2 | 89.5 | 94.7 |
| DGS30 | taux_nominal_30a | 5.52 | 2026-10-14 | 0 | 2497 | 9.99 ans | 95.6 | 99.1 | 99.6 |
| DTWEXBGS | dollar_large | 121.6 | 2026-10-09 | 3 | 2490 | 9.97 ans | 96.8 | 65.6 | 80.6 |
| INDPRO | activite_industrielle | 103.1 | 2026-08-01 | 74 | 119 | 9.83 ans | 100.0 | 100.0 | 92.4 |
| NASDAQ100 | prix_actions_tech | 2.995e+04 | 2026-10-14 | 0 | 2512 | 9.99 ans | 86.9 | 97.4 | 98.7 |
| OVXCLS | volatilite_implicite_petrole | 48.62 | 2026-10-14 | 0 | 2513 | 9.99 ans | 41.7 | 75.1 | 81.5 |
| PAYEMS | emploi | 1.59e+05 | 2026-09-01 | 43 | 120 | 9.92 ans | 100.0 | 100.0 | 100.0 |
| SP500 | prix_actions | 7719 | 2026-10-14 | 0 | 2511 | 9.99 ans | 91.3 | 98.3 | 99.1 |
| T10Y2Y | pente_courbe | 0.37 | 2026-10-14 | 0 | 2497 | 9.99 ans | 14.7 | 63.5 | 49.4 |
| T10YIE | point_mort_10a | 2.35 | 2026-10-14 | 0 | 2497 | 9.99 ans | 74.2 | 61.0 | 77.9 |
| T5YIFR | point_mort_5a5a | 2.34 | 2026-10-14 | 0 | 2497 | 9.99 ans | 94.8 | 80.8 | 90.1 |
| UNRATE | chomage | 4.2 | 2026-09-01 | 43 | 119 | 9.92 ans | 33.3 | 78.3 | 63.9 |
| VIXCLS | volatilite_implicite | 16.87 | 2026-10-14 | 0 | 2544 | 9.99 ans | 46.0 | 42.1 | 49.4 |
| VXDCLS | volatilite_implicite_dow | 15.2 | 2026-10-14 | 0 | 2514 | 9.99 ans | 38.5 | 38.7 | 42.7 |
| VXVCLS | volatilite_implicite_3m | 18.79 | 2026-10-14 | 0 | 2511 | 9.99 ans | 23.0 | 34.4 | 45.4 |

**Couples obligatoires contrôlés :** CPIAUCSL/CPILFESL, DGS10/DFII10, DGS10/T10YIE, BAMLH0A0HYM2/BAMLC0A0CM, UNRATE/PAYEMS, VIXCLS/SP500 — 0 manquement(s).

**Inflation en trois chiffres (contrôle 2, E-005).** Global +4.02 % sur un an (CPIAUCSL, 2026-09-01) · sous-jacent +2.79 % (CPILFESL) · **écart hors sous-jacent +123 pb**. Contribution énergie NON publiée : `CPIENGSL` est absente du dépôt. Lacune nommée avec le code FRED qui la comble (R-028) ; elle n'est pas présentée comme une limite de méthode. L'écart ci-dessus est l'écart global/sous-jacent, pas la contribution énergie.

---

## 4. IDENTITÉS COMPTABLES ET REDONDANCES (vérifiées numériquement)

| identité | vérifiable | n dates | résidu absolu max | tolérance | vérifiée |
|---|:---:|---:|---:|---:|:---:|
| T10YIE = DGS10 - DFII10 | oui | 2497 | 0.0000 | 0.02 | OUI |
| T10Y2Y = DGS10 - DGS2 | oui | 2497 | 0.0000 | 0.02 | OUI |

**Redondances détectées (11) — deux séries liées ne comptent jamais pour deux confirmations indépendantes :**

- identité comptable : T10YIE = DGS10 - DFII10 — T10YIE, DGS10, DFII10 (résidu max 0.0000)
- identité comptable : T10Y2Y = DGS10 - DGS2 — T10Y2Y, DGS10, DGS2 (résidu max 0.0000)
- corrélation des variations à 60 séances : BAMLC0A0CM / BAMLH0A0HYM2 = +0.938 sur 725 points (seuil 0.9)
- corrélation des variations à 60 séances : DGS10 / DGS30 = +0.967 sur 2437 points (seuil 0.9)
- corrélation des variations à 60 séances : INDPRO / PAYEMS = +0.913 sur 116 points (seuil 0.9)
- corrélation des variations à 60 séances : INDPRO / UNRATE = -0.918 sur 115 points (seuil 0.9)
- corrélation des variations à 60 séances : NASDAQ100 / SP500 = +0.903 sur 2451 points (seuil 0.9)
- corrélation des variations à 60 séances : PAYEMS / UNRATE = -0.983 sur 116 points (seuil 0.9)
- corrélation des variations à 60 séances : VIXCLS / VXDCLS = +0.929 sur 2451 points (seuil 0.9)
- corrélation des variations à 60 séances : VIXCLS / VXVCLS = +0.958 sur 2451 points (seuil 0.9)
- corrélation des variations à 60 séances : VXDCLS / VXVCLS = +0.933 sur 2451 points (seuil 0.9)

---

## 5. GRILLE, σ MESURÉ, ET DOUBLE CONFRONTATION DES PROBABILITÉS

σ est **mesuré** sur chaque série, jamais choisi. Les probabilités sont les **fréquences historiques** dans chaque bande, jamais un jugement. L'effectif de chaque bande est publié ; sous 20 observations la bande est déclarée NON ESTIMABLE. La colonne « emp./gauss. » est la double confrontation exigée par §11.5 : tout écart supérieur à un facteur 2 est déclaré (⚠).

**BAMLH0A0HYM2** (niveau) — σ à 60 pas = **0.45185** · estimateurs croisés : racine-h 0.54030, blocs disjoints 0.36902 (écart relatif 46.4 %) · dérive d'échantillon -0.09021 (-0.20 σ) · 726 variations chevauchantes, 12 blocs indépendants · 2023-10-16 → 2026-10-14

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.6778 | 51 | 1 | 0.0702 | 0.0668 | 1.05 | oui |
| -1.0 | -0.6778 | -0.3389 | 117 | 2 | 0.1612 | 0.1598 | 1.01 | oui |
| -0.5 | -0.3389 | -0.1130 | 189 | 3 | 0.2603 | 0.1747 | 1.49 | oui |
| +0.0 | -0.1130 | +0.1130 | 195 | 3 | 0.2686 | 0.1974 | 1.36 | oui |
| +0.5 | +0.1130 | +0.3389 | 80 | 1 | 0.1102 | 0.1747 | 0.63 | oui |
| +1.0 | +0.3389 | +0.6778 | 65 | 1 | 0.0895 | 0.1598 | 0.56 | oui |
| +2.0 | +0.6778 | +∞ | 29 | 0 | 0.0399 | 0.0668 | 0.60 | oui |

**DCOILBRENTEU** (log) — σ à 60 pas = **0.24880** · estimateurs croisés : racine-h 0.24951, blocs disjoints 0.31343 (écart relatif 26.0 %) · dérive d'échantillon +0.01824 (+0.07 σ) · 2474 variations chevauchantes, 41 blocs indépendants · 2016-10-18 → 2026-10-14

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.3732 | 83 | 1 | 0.0335 | 0.0668 | 0.50 | oui |
| -1.0 | -0.3732 | -0.1866 | 155 | 3 | 0.0627 | 0.1598 | 0.39 ⚠ | oui |
| -0.5 | -0.1866 | -0.0622 | 499 | 8 | 0.2017 | 0.1747 | 1.15 | oui |
| +0.0 | -0.0622 | +0.0622 | 772 | 13 | 0.3120 | 0.1974 | 1.58 | oui |
| +0.5 | +0.0622 | +0.1866 | 603 | 10 | 0.2437 | 0.1747 | 1.40 | oui |
| +1.0 | +0.1866 | +0.3732 | 219 | 4 | 0.0885 | 0.1598 | 0.55 | oui |
| +2.0 | +0.3732 | +∞ | 143 | 2 | 0.0578 | 0.0668 | 0.87 | oui |

**DCOILWTICO** — non scénarisable : convention log inapplicable : 1 observation(s) non strictement positive(s), minimum -36.98 le 2020-04-20. Le prix a été négatif : aucun log-rendement n'existe. La série est déclarée NON SCÉNARISABLE plutôt que corrigée en silence.

**DEXJPUS** (log) — σ à 60 pas = **0.04180** · estimateurs croisés : racine-h 0.04380, blocs disjoints 0.04971 (écart relatif 18.9 %) · dérive d'échantillon +0.00871 (+0.21 σ) · 2432 variations chevauchantes, 41 blocs indépendants · 2016-10-18 → 2026-10-09

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0627 | 104 | 2 | 0.0428 | 0.0668 | 0.64 | oui |
| -1.0 | -0.0627 | -0.0313 | 243 | 4 | 0.0999 | 0.1598 | 0.63 | oui |
| -0.5 | -0.0313 | -0.0104 | 387 | 6 | 0.1591 | 0.1747 | 0.91 | oui |
| +0.0 | -0.0104 | +0.0104 | 494 | 8 | 0.2031 | 0.1974 | 1.03 | oui |
| +0.5 | +0.0104 | +0.0313 | 535 | 9 | 0.2200 | 0.1747 | 1.26 | oui |
| +1.0 | +0.0313 | +0.0627 | 477 | 8 | 0.1961 | 0.1598 | 1.23 | oui |
| +2.0 | +0.0627 | +∞ | 192 | 3 | 0.0789 | 0.0668 | 1.18 | oui |

**DEXUSEU** (log) — σ à 60 pas = **0.03425** · estimateurs croisés : racine-h 0.03468, blocs disjoints 0.03665 (écart relatif 7.0 %) · dérive d'échantillon +0.00177 (+0.05 σ) · 2432 variations chevauchantes, 41 blocs indépendants · 2016-10-18 → 2026-10-09

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0514 | 130 | 2 | 0.0535 | 0.0668 | 0.80 | oui |
| -1.0 | -0.0514 | -0.0257 | 321 | 5 | 0.1320 | 0.1598 | 0.83 | oui |
| -0.5 | -0.0257 | -0.0086 | 509 | 8 | 0.2093 | 0.1747 | 1.20 | oui |
| +0.0 | -0.0086 | +0.0086 | 617 | 10 | 0.2537 | 0.1974 | 1.29 | oui |
| +0.5 | +0.0086 | +0.0257 | 321 | 5 | 0.1320 | 0.1747 | 0.76 | oui |
| +1.0 | +0.0257 | +0.0514 | 307 | 5 | 0.1262 | 0.1598 | 0.79 | oui |
| +2.0 | +0.0514 | +∞ | 227 | 4 | 0.0933 | 0.0668 | 1.40 | oui |

**DGS10** (niveau) — σ à 60 pas = **0.42328** · estimateurs croisés : racine-h 0.41448, blocs disjoints 0.45118 (écart relatif 8.9 %) · dérive d'échantillon +0.06474 (+0.15 σ) · 2437 variations chevauchantes, 41 blocs indépendants · 2016-10-18 → 2026-10-14

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.6349 | 123 | 2 | 0.0505 | 0.0668 | 0.76 | oui |
| -1.0 | -0.6349 | -0.3175 | 284 | 5 | 0.1165 | 0.1598 | 0.73 | oui |
| -0.5 | -0.3175 | -0.1058 | 371 | 6 | 0.1522 | 0.1747 | 0.87 | oui |
| +0.0 | -0.1058 | +0.1058 | 528 | 9 | 0.2167 | 0.1974 | 1.10 | oui |
| +0.5 | +0.1058 | +0.3175 | 555 | 9 | 0.2277 | 0.1747 | 1.30 | oui |
| +1.0 | +0.3175 | +0.6349 | 364 | 6 | 0.1494 | 0.1598 | 0.93 | oui |
| +2.0 | +0.6349 | +∞ | 212 | 4 | 0.0870 | 0.0668 | 1.30 | oui |

**DGS2** (niveau) — σ à 60 pas = **0.49643** · estimateurs croisés : racine-h 0.42186, blocs disjoints 0.51660 (écart relatif 22.5 %) · dérive d'échantillon +0.08368 (+0.17 σ) · 2437 variations chevauchantes, 41 blocs indépendants · 2016-10-18 → 2026-10-14

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.7446 | 115 | 2 | 0.0472 | 0.0668 | 0.71 | oui |
| -1.0 | -0.7446 | -0.3723 | 228 | 4 | 0.0936 | 0.1598 | 0.59 | oui |
| -0.5 | -0.3723 | -0.1241 | 323 | 5 | 0.1325 | 0.1747 | 0.76 | oui |
| +0.0 | -0.1241 | +0.1241 | 739 | 12 | 0.3032 | 0.1974 | 1.54 | oui |
| +0.5 | +0.1241 | +0.3723 | 478 | 8 | 0.1961 | 0.1747 | 1.12 | oui |
| +1.0 | +0.3723 | +0.7446 | 353 | 6 | 0.1449 | 0.1598 | 0.91 | oui |
| +2.0 | +0.7446 | +∞ | 201 | 3 | 0.0825 | 0.0668 | 1.23 | oui |

**DGS30** (niveau) — σ à 60 pas = **0.36507** · estimateurs croisés : racine-h 0.39249, blocs disjoints 0.38994 (écart relatif 7.5 %) · dérive d'échantillon +0.05928 (+0.16 σ) · 2437 variations chevauchantes, 41 blocs indépendants · 2016-10-18 → 2026-10-14

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.5476 | 128 | 2 | 0.0525 | 0.0668 | 0.79 | oui |
| -1.0 | -0.5476 | -0.2738 | 276 | 5 | 0.1133 | 0.1598 | 0.71 | oui |
| -0.5 | -0.2738 | -0.0913 | 338 | 6 | 0.1387 | 0.1747 | 0.79 | oui |
| +0.0 | -0.0913 | +0.0913 | 629 | 10 | 0.2581 | 0.1974 | 1.31 | oui |
| +0.5 | +0.0913 | +0.2738 | 461 | 8 | 0.1892 | 0.1747 | 1.08 | oui |
| +1.0 | +0.2738 | +0.5476 | 394 | 7 | 0.1617 | 0.1598 | 1.01 | oui |
| +2.0 | +0.5476 | +∞ | 211 | 4 | 0.0866 | 0.0668 | 1.30 | oui |

**DTWEXBGS** (log) — σ à 60 pas = **0.02577** · estimateurs croisés : racine-h 0.02408, blocs disjoints 0.02672 (écart relatif 10.9 %) · dérive d'échantillon +0.00061 (+0.02 σ) · 2430 variations chevauchantes, 40 blocs indépendants · 2016-10-18 → 2026-10-09

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0387 | 169 | 3 | 0.0695 | 0.0668 | 1.04 | oui |
| -1.0 | -0.0387 | -0.0193 | 380 | 6 | 0.1564 | 0.1598 | 0.98 | oui |
| -0.5 | -0.0193 | -0.0064 | 358 | 6 | 0.1473 | 0.1747 | 0.84 | oui |
| +0.0 | -0.0064 | +0.0064 | 548 | 9 | 0.2255 | 0.1974 | 1.14 | oui |
| +0.5 | +0.0064 | +0.0193 | 465 | 8 | 0.1914 | 0.1747 | 1.10 | oui |
| +1.0 | +0.0193 | +0.0387 | 304 | 5 | 0.1251 | 0.1598 | 0.78 | oui |
| +2.0 | +0.0387 | +∞ | 206 | 3 | 0.0848 | 0.0668 | 1.27 | oui |

**NASDAQ100** (log) — σ à 60 pas = **0.08867** · estimateurs croisés : racine-h 0.11137, blocs disjoints 0.07419 (écart relatif 50.1 %) · dérive d'échantillon +0.04421 (+0.50 σ) · 2452 variations chevauchantes, 41 blocs indépendants · 2016-10-18 → 2026-10-14

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.1330 | 109 | 2 | 0.0445 | 0.0668 | 0.67 | oui |
| -1.0 | -0.1330 | -0.0665 | 166 | 3 | 0.0677 | 0.1598 | 0.42 ⚠ | oui |
| -0.5 | -0.0665 | -0.0222 | 186 | 3 | 0.0759 | 0.1747 | 0.43 ⚠ | oui |
| +0.0 | -0.0222 | +0.0222 | 353 | 6 | 0.1440 | 0.1974 | 0.73 | oui |
| +0.5 | +0.0222 | +0.0665 | 590 | 10 | 0.2406 | 0.1747 | 1.38 | oui |
| +1.0 | +0.0665 | +0.1330 | 732 | 12 | 0.2985 | 0.1598 | 1.87 | oui |
| +2.0 | +0.1330 | +∞ | 316 | 5 | 0.1289 | 0.0668 | 1.93 | oui |

**SP500** (log) — σ à 60 pas = **0.06913** · estimateurs croisés : racine-h 0.08844, blocs disjoints 0.05562 (écart relatif 59.0 %) · dérive d'échantillon +0.03054 (+0.44 σ) · 2451 variations chevauchantes, 41 blocs indépendants · 2016-10-18 → 2026-10-14

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.1037 | 115 | 2 | 0.0469 | 0.0668 | 0.70 | oui |
| -1.0 | -0.1037 | -0.0518 | 158 | 3 | 0.0645 | 0.1598 | 0.40 ⚠ | oui |
| -0.5 | -0.0518 | -0.0173 | 176 | 3 | 0.0718 | 0.1747 | 0.41 ⚠ | oui |
| +0.0 | -0.0173 | +0.0173 | 293 | 5 | 0.1195 | 0.1974 | 0.61 | oui |
| +0.5 | +0.0173 | +0.0518 | 750 | 12 | 0.3060 | 0.1747 | 1.75 | oui |
| +1.0 | +0.0518 | +0.1037 | 749 | 12 | 0.3056 | 0.1598 | 1.91 | oui |
| +2.0 | +0.1037 | +∞ | 210 | 4 | 0.0857 | 0.0668 | 1.28 | oui |

**VIXCLS** (log) — σ à 60 pas = **0.34644** · estimateurs croisés : racine-h 0.61199, blocs disjoints 0.34324 (écart relatif 78.3 %) · dérive d'échantillon +0.00377 (+0.01 σ) · 2484 variations chevauchantes, 41 blocs indépendants · 2016-10-18 → 2026-10-14

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.5197 | 77 | 1 | 0.0310 | 0.0668 | 0.46 ⚠ | oui |
| -1.0 | -0.5197 | -0.2598 | 384 | 6 | 0.1546 | 0.1598 | 0.97 | oui |
| -0.5 | -0.2598 | -0.0866 | 606 | 10 | 0.2440 | 0.1747 | 1.40 | oui |
| +0.0 | -0.0866 | +0.0866 | 618 | 10 | 0.2488 | 0.1974 | 1.26 | oui |
| +0.5 | +0.0866 | +0.2598 | 373 | 6 | 0.1502 | 0.1747 | 0.86 | oui |
| +1.0 | +0.2598 | +0.5197 | 248 | 4 | 0.0998 | 0.1598 | 0.62 | oui |
| +2.0 | +0.5197 | +∞ | 178 | 3 | 0.0717 | 0.0668 | 1.07 | oui |

---

## 6. TEST D'ASYMÉTRIE — DÉFINITION UNIQUE (R-030), L'ESPÉRANCE DÉCIDE

> Test d'admission : **espérance calculée sur la grille symétrique complète, les deux queues incluses**. Le rapport gain maximal / perte maximale est publié **pour information** et ne peut fonder aucune admission seul (T-001, faute E-018). Le rapport gain maximal / perte du scénario central est **interdit**. Une seule formulation, appliquée à tous les candidats, position détenue comprise.

| candidat | verdict | espérance % NAV | sans dérive | 1re moitié | 2e moitié | gain max | perte max | ratio (info) | critères échoués |
|---|:---:|---:|---:|---:|---:|---:|---:|---:|---|
| M005-DCOILBRENTEU-HAUSSE-ALIGNE | REFUSEE | +0.278 | +0.129 | +0.253 | +0.205 | +5.08 | -3.21 | 1.58:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DCOILBRENTEU-HAUSSE-CONTRARIEN | REFUSEE | +0.278 | +0.129 | +0.253 | +0.205 | +5.08 | -3.21 | 1.58:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DCOILBRENTEU-BAISSE-ALIGNE | REFUSEE | -0.278 | -0.129 | -0.253 | -0.205 | +3.21 | -5.08 | 0.63:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILBRENTEU-BAISSE-CONTRARIEN | REFUSEE | -0.278 | -0.129 | -0.253 | -0.205 | +3.21 | -5.08 | 0.63:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-HAUSSE-ALIGNE | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-HAUSSE-CONTRARIEN | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-BAISSE-ALIGNE | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-BAISSE-CONTRARIEN | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-HAUSSE-ALIGNE | REFUSEE | -0.001 | -0.067 | -0.076 | +0.040 | +0.62 | -0.72 | 0.87:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-HAUSSE-CONTRARIEN | REFUSEE | -0.001 | -0.067 | -0.076 | +0.040 | +0.62 | -0.72 | 0.87:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-BAISSE-ALIGNE | REFUSEE | +0.001 | +0.067 | +0.076 | -0.040 | +0.72 | -0.62 | 1.15:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-BAISSE-CONTRARIEN | REFUSEE | +0.001 | +0.067 | +0.076 | -0.040 | +0.72 | -0.62 | 1.15:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-HAUSSE-ALIGNE | REFUSEE | -0.060 | -0.075 | -0.030 | -0.071 | +0.49 | -0.60 | 0.82:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-HAUSSE-CONTRARIEN | REFUSEE | -0.060 | -0.075 | -0.030 | -0.071 | +0.49 | -0.60 | 0.82:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-BAISSE-ALIGNE | REFUSEE | +0.060 | +0.075 | +0.030 | +0.071 | +0.60 | -0.49 | 1.22:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DEXUSEU-BAISSE-CONTRARIEN | REFUSEE | +0.060 | +0.075 | +0.030 | +0.071 | +0.60 | -0.49 | 1.22:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DGS10-HAUSSE-ALIGNE | REFUSEE | +0.008 | -0.028 | -0.052 | +0.058 | +0.48 | -0.57 | 0.84:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-HAUSSE-CONTRARIEN | REFUSEE | +0.008 | -0.028 | -0.052 | +0.058 | +0.48 | -0.57 | 0.84:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-BAISSE-ALIGNE | REFUSEE | -0.008 | +0.028 | +0.052 | -0.058 | +0.57 | -0.48 | 1.19:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-BAISSE-CONTRARIEN | REFUSEE | -0.008 | +0.028 | +0.052 | -0.058 | +0.57 | -0.48 | 1.19:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-HAUSSE-ALIGNE | REFUSEE | -0.007 | -0.017 | -0.024 | +0.005 | +0.13 | -0.17 | 0.77:1 | 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-HAUSSE-CONTRARIEN | REFUSEE | -0.007 | -0.017 | -0.024 | +0.005 | +0.13 | -0.17 | 0.77:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-BAISSE-ALIGNE | REFUSEE | +0.007 | +0.017 | +0.024 | -0.005 | +0.17 | -0.13 | 1.30:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-BAISSE-CONTRARIEN | REFUSEE | +0.007 | +0.017 | +0.024 | -0.005 | +0.17 | -0.13 | 1.30:1 | 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-HAUSSE-ALIGNE | REFUSEE | +0.014 | -0.043 | -0.099 | +0.126 | +0.76 | -0.96 | 0.79:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-HAUSSE-CONTRARIEN | REFUSEE | +0.014 | -0.043 | -0.099 | +0.126 | +0.76 | -0.96 | 0.79:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-BAISSE-ALIGNE | REFUSEE | -0.014 | +0.043 | +0.099 | -0.126 | +0.96 | -0.76 | 1.26:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-BAISSE-CONTRARIEN | REFUSEE | -0.014 | +0.043 | +0.099 | -0.126 | +0.96 | -0.76 | 1.26:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-HAUSSE-ALIGNE | REFUSEE | -0.067 | -0.072 | -0.085 | -0.053 | +0.35 | -0.48 | 0.73:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-HAUSSE-CONTRARIEN | REFUSEE | -0.067 | -0.072 | -0.085 | -0.053 | +0.35 | -0.48 | 0.73:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-BAISSE-ALIGNE | REFUSEE | +0.067 | +0.072 | +0.085 | +0.053 | +0.48 | -0.35 | 1.36:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DTWEXBGS-BAISSE-CONTRARIEN | REFUSEE | +0.067 | +0.072 | +0.085 | +0.053 | +0.48 | -0.35 | 1.36:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-HAUSSE-ALIGNE | REFUSEE | +0.305 | -0.034 | +0.451 | +0.183 | +1.48 | -1.37 | 1.08:1 | 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-HAUSSE-CONTRARIEN | REFUSEE | +0.305 | -0.034 | +0.451 | +0.183 | +1.48 | -1.37 | 1.08:1 | 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-BAISSE-ALIGNE | REFUSEE | -0.305 | +0.034 | -0.451 | -0.183 | +1.37 | -1.48 | 0.93:1 | 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-NASDAQ100-BAISSE-CONTRARIEN | REFUSEE | -0.305 | +0.034 | -0.451 | -0.183 | +1.37 | -1.48 | 0.93:1 | 12_esperance_positive, 13_esperance_non_portee_par_derive, 14_esperance_stable_dans_le_temps |
| M005-SP500-HAUSSE-ALIGNE | REFUSEE | +0.186 | -0.044 | +0.214 | +0.152 | +1.11 | -1.11 | 1.00:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-SP500-HAUSSE-CONTRARIEN | REFUSEE | +0.186 | -0.044 | +0.214 | +0.152 | +1.11 | -1.11 | 1.00:1 | 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-SP500-BAISSE-ALIGNE | REFUSEE | -0.186 | +0.044 | -0.214 | -0.152 | +1.11 | -1.11 | 1.00:1 | 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-SP500-BAISSE-CONTRARIEN | REFUSEE | -0.186 | +0.044 | -0.214 | -0.152 | +1.11 | -1.11 | 1.00:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |

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

- `BAMLC0A0CM` : percentile REFUSÉ sur 5 ans — profondeur réelle 785 obs / 3.00 ans (début 2023-10-16). R-011 : un percentile calculé sur une série tronquée est sans valeur.
- `BAMLH0A0HYM2` : percentile REFUSÉ sur 5 ans — profondeur réelle 786 obs / 3.00 ans (début 2023-10-16). R-011 : un percentile calculé sur une série tronquée est sans valeur.
- `BAMLH0A0HYM2` : instrument NON ADMISSIBLE — P&L non calculable depuis le dépôt : l'OAS est un spread, et le dépôt ne contient pas le rendement de l'indice, donc pas la duration de spread. Aucune valeur ne peut être produite sans un chiffre extérieur aux données (E-002).
- `BAMLC0A0CM` : instrument NON ADMISSIBLE — P&L non calculable depuis le dépôt : l'OAS est un spread, et le dépôt ne contient pas le rendement de l'indice, donc pas la duration de spread. Aucune valeur ne peut être produite sans un chiffre extérieur aux données (E-002).
- Retards sur la date d'arrêté unique (E-014) : DEXJPUS 3 séance(s), DEXUSEU 3 séance(s), DTWEXBGS 3 séance(s)

**Vérification tierce (R-032) : NON SATISFAITE pour ce brief.** Le moteur ne dispose d'aucune source extérieure au dépôt. Trois estimateurs **internes** de σ sont publiés côte à côte au §5 ; ce sont des contrôles de cohérence interne, **pas** une vérification tierce, et ils ne sont pas présentés comme telle.

**Ce que ce moteur ne peut pas faire.** Il ne prouve aucune capacité prédictive : la règle de confirmation est une règle de percentile, déclarée et symétrique, pas un modèle validé hors échantillon. Il ne corrige pas la multiplicité : 40 candidats sont évalués et aucune pénalité de sélection n'est appliquée à l'espérance — c'est une limite déclarée, pas un oubli. Il ne voit ni les événements politiques, ni les décisions de banques centrales : le dépôt ne contient que des séries FRED, et toute affirmation de politique monétaire non adossée à `DFF` est refusée (critère 15, faute E-006).

---

*Fin du brief 005. Produit mécaniquement. Ne constitue pas un conseil en investissement.*