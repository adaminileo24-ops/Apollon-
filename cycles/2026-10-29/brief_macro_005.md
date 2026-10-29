# BRIEF MACRO n° 005 — arrêté au 2026-10-27

*Produit par `apollon_macro.py` le 2026-10-29T11:31:12+00:00. Aucune valeur de ce document n'est saisie à la main : chacune porte sa série, sa date et sa profondeur. Bloc à copier tel quel.*

**Grille de scénarios (R-029, §11), déclarée avant toute lecture de données et empreintée :** `[-2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0]` · empreinte SHA-256 `6aaeb3863c875923…` · symétrique : True · horizon 60 séances (3 mois pour les séries mensuelles).

---

## 1. CONCLUSION, ÉNONCÉE D'ABORD

**40 candidats déclarés d'avance (10 instruments × 2 directions × 2 règles de confirmation). 40 évalués. 0 thèse(s) survivent aux quinze critères.**

**Abstention. Aucune thèse ne survit.** Ce n'est pas un silence : c'est un résultat, produit par le même portier que celui qui aurait admis une thèse. Le détail des échecs, critère par critère, figure au §6. La Section Macro ne transmet rien à la Section Risque ce cycle.

**Position détenue (contrôle 9, E-020) — 100 % cash, testée sur la même grille.** Espérance excédentaire du cash : +0.000 % de NAV. Référence 60/40 : +1.334 % (hors dérive : -0.207 %). **Écart du cash contre la référence : -1.334 % de NAV** sur 60 séances.

---

## 2. CE QUI A CHANGÉ — MÉCANISME, PAS CONTENU

Fait, étiqueté : les briefs 001 à 004 étaient rédigés par un agent. Celui-ci est produit par un moteur. Le paramètre libre de la Section Macro — la grille de scénarios — n'est plus accessible à l'agent : il est déclaré en tête de fichier, symétrique par construction, et son empreinte SHA-256 est vérifiée avant chaque usage. Sur le brief 004, ce paramètre avait porté le ratio annoncé de 1,29:1 à 3,0:1.

---

## 3. M1 · M2 · M3 · M4 — ÉTAT DES SÉRIES (FAIT)

Toutes les valeurs sont des FAITS lus dans le dépôt. Le retard est compté en séances ouvrées depuis la date d'arrêté unique. Les couples obligatoires sont vérifiés par le rendu : ce bloc ne peut pas être émis si un membre d'un couple manque.

| série | rôle déclaré | valeur | date | retard | n obs | profondeur | pct 1 an | pct 5 ans | pct complet |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| BAMLC0A0CM | risque_credit_ig | 0.88 | 2026-10-27 | 0 | 784 | 2.99 ans | 95.2 | REFUSÉ (insuffisante, -38 %) | 59.4 |
| BAMLH0A0HYM2 | risque_credit_hy | 3.18 | 2026-10-27 | 0 | 785 | 2.99 ans | 90.1 | REFUSÉ (insuffisante, -38 %) | 68.4 |
| CPIAUCSL | inflation_globale | 336.3 | 2026-09-01 | 56 | 119 | 9.92 ans | 100.0 | 100.0 | 100.0 |
| CPILFESL | inflation_sous_jacente | 338.9 | 2026-09-01 | 56 | 119 | 9.92 ans | 100.0 | 100.0 | 100.0 |
| DCOILBRENTEU | prix_energie | 123.1 | 2026-10-27 | 0 | 2534 | 9.99 ans | 91.7 | 97.1 | 98.5 |
| DCOILWTICO | prix_energie_wti | 103.4 | 2026-10-27 | 0 | 2498 | 9.99 ans | 89.3 | 92.3 | 96.1 |
| DEXJPUS | devise_usdjpy | 156.9 | 2026-10-23 | 2 | 2492 | 9.98 ans | 34.5 | 82.9 | 91.4 |
| DEXUSEU | devise_eurusd | 1.12 | 2026-10-23 | 2 | 2492 | 9.98 ans | 2.4 | 62.8 | 47.0 |
| DFF | politique_monetaire | 3.88 | 2026-10-27 | 0 | 3649 | 9.99 ans | 100.0 | 27.8 | 70.9 |
| DFII10 | taux_reel_10a | 2.64 | 2026-10-27 | 0 | 2497 | 9.99 ans | 90.5 | 98.1 | 99.0 |
| DGS10 | taux_nominal_10a | 4.99 | 2026-10-27 | 0 | 2497 | 9.99 ans | 90.1 | 98.0 | 99.0 |
| DGS2 | taux_nominal_2a | 4.7 | 2026-10-27 | 0 | 2497 | 9.99 ans | 90.5 | 83.6 | 91.7 |
| DGS30 | taux_nominal_30a | 5.3 | 2026-10-27 | 0 | 2497 | 9.99 ans | 88.5 | 97.7 | 98.8 |
| DTWEXBGS | dollar_large | 121.3 | 2026-10-23 | 2 | 2490 | 9.98 ans | 90.9 | 61.4 | 78.4 |
| INDPRO | activite_industrielle | 104 | 2026-09-01 | 56 | 120 | 9.92 ans | 100.0 | 100.0 | 95.8 |
| NASDAQ100 | prix_actions_tech | 2.965e+04 | 2026-10-27 | 0 | 2512 | 9.99 ans | 82.1 | 96.4 | 98.2 |
| OVXCLS | volatilite_implicite_petrole | 55.44 | 2026-10-27 | 0 | 2513 | 9.99 ans | 57.1 | 87.9 | 90.1 |
| PAYEMS | emploi | 1.59e+05 | 2026-09-01 | 56 | 120 | 9.92 ans | 100.0 | 100.0 | 100.0 |
| SP500 | prix_actions | 7723 | 2026-10-27 | 0 | 2511 | 9.99 ans | 90.5 | 98.1 | 99.0 |
| T10Y2Y | pente_courbe | 0.29 | 2026-10-27 | 0 | 2497 | 9.99 ans | 4.4 | 57.7 | 44.8 |
| T10YIE | point_mort_10a | 2.35 | 2026-10-27 | 0 | 2497 | 9.99 ans | 73.8 | 61.6 | 77.9 |
| T5YIFR | point_mort_5a5a | 2.25 | 2026-10-27 | 0 | 2497 | 9.99 ans | 67.1 | 42.5 | 68.8 |
| UNRATE | chomage | 4.2 | 2026-09-01 | 56 | 119 | 9.92 ans | 33.3 | 78.3 | 63.9 |
| VIXCLS | volatilite_implicite | 17.52 | 2026-10-27 | 0 | 2544 | 9.99 ans | 57.1 | 49.3 | 54.3 |
| VXDCLS | volatilite_implicite_dow | 16.67 | 2026-10-27 | 0 | 2514 | 9.99 ans | 67.1 | 56.6 | 56.4 |
| VXVCLS | volatilite_implicite_3m | 19.57 | 2026-10-27 | 0 | 2511 | 9.99 ans | 44.0 | 44.0 | 51.4 |

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
- corrélation des variations à 60 séances : BAMLC0A0CM / BAMLH0A0HYM2 = +0.936 sur 724 points (seuil 0.9)
- corrélation des variations à 60 séances : DGS10 / DGS30 = +0.966 sur 2437 points (seuil 0.9)
- corrélation des variations à 60 séances : INDPRO / PAYEMS = +0.912 sur 117 points (seuil 0.9)
- corrélation des variations à 60 séances : INDPRO / UNRATE = -0.917 sur 116 points (seuil 0.9)
- corrélation des variations à 60 séances : NASDAQ100 / SP500 = +0.903 sur 2451 points (seuil 0.9)
- corrélation des variations à 60 séances : PAYEMS / UNRATE = -0.983 sur 116 points (seuil 0.9)
- corrélation des variations à 60 séances : VIXCLS / VXDCLS = +0.929 sur 2451 points (seuil 0.9)
- corrélation des variations à 60 séances : VIXCLS / VXVCLS = +0.958 sur 2451 points (seuil 0.9)
- corrélation des variations à 60 séances : VXDCLS / VXVCLS = +0.933 sur 2451 points (seuil 0.9)

---

## 5. GRILLE, σ MESURÉ, ET DOUBLE CONFRONTATION DES PROBABILITÉS

σ est **mesuré** sur chaque série, jamais choisi. Les probabilités sont les **fréquences historiques** dans chaque bande, jamais un jugement. L'effectif de chaque bande est publié ; sous 20 observations la bande est déclarée NON ESTIMABLE. La colonne « emp./gauss. » est la double confrontation exigée par §11.5 : tout écart supérieur à un facteur 2 est déclaré (⚠).

**BAMLH0A0HYM2** (niveau) — σ à 60 pas = **0.44744** · estimateurs croisés : racine-h 0.53986, blocs disjoints 0.35300 (écart relatif 52.9 %) · dérive d'échantillon -0.07252 (-0.16 σ) · 725 variations chevauchantes, 12 blocs indépendants · 2023-10-30 → 2026-10-27

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.6712 | 41 | 1 | 0.0566 | 0.0668 | 0.85 | oui |
| -1.0 | -0.6712 | -0.3356 | 117 | 2 | 0.1614 | 0.1598 | 1.01 | oui |
| -0.5 | -0.3356 | -0.1119 | 189 | 3 | 0.2607 | 0.1747 | 1.49 | oui |
| +0.0 | -0.1119 | +0.1119 | 195 | 3 | 0.2690 | 0.1974 | 1.36 | oui |
| +0.5 | +0.1119 | +0.3356 | 80 | 1 | 0.1103 | 0.1747 | 0.63 | oui |
| +1.0 | +0.3356 | +0.6712 | 74 | 1 | 0.1021 | 0.1598 | 0.64 | oui |
| +2.0 | +0.6712 | +∞ | 29 | 0 | 0.0400 | 0.0668 | 0.60 | oui |

**DCOILBRENTEU** (log) — σ à 60 pas = **0.24924** · estimateurs croisés : racine-h 0.24981, blocs disjoints 0.21279 (écart relatif 17.4 %) · dérive d'échantillon +0.01887 (+0.08 σ) · 2474 variations chevauchantes, 41 blocs indépendants · 2016-10-31 → 2026-10-27

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.3739 | 83 | 1 | 0.0335 | 0.0668 | 0.50 | oui |
| -1.0 | -0.3739 | -0.1869 | 155 | 3 | 0.0627 | 0.1598 | 0.39 ⚠ | oui |
| -0.5 | -0.1869 | -0.0623 | 497 | 8 | 0.2009 | 0.1747 | 1.15 | oui |
| +0.0 | -0.0623 | +0.0623 | 774 | 13 | 0.3129 | 0.1974 | 1.58 | oui |
| +0.5 | +0.0623 | +0.1869 | 596 | 10 | 0.2409 | 0.1747 | 1.38 | oui |
| +1.0 | +0.1869 | +0.3739 | 226 | 4 | 0.0914 | 0.1598 | 0.57 | oui |
| +2.0 | +0.3739 | +∞ | 143 | 2 | 0.0578 | 0.0668 | 0.87 | oui |

**DCOILWTICO** — non scénarisable : convention log inapplicable : 1 observation(s) non strictement positive(s), minimum -36.98 le 2020-04-20. Le prix a été négatif : aucun log-rendement n'existe. La série est déclarée NON SCÉNARISABLE plutôt que corrigée en silence.

**DEXJPUS** (log) — σ à 60 pas = **0.04159** · estimateurs croisés : racine-h 0.04379, blocs disjoints 0.04445 (écart relatif 6.9 %) · dérive d'échantillon +0.00826 (+0.20 σ) · 2432 variations chevauchantes, 41 blocs indépendants · 2016-10-31 → 2026-10-23

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0624 | 105 | 2 | 0.0432 | 0.0668 | 0.65 | oui |
| -1.0 | -0.0624 | -0.0312 | 249 | 4 | 0.1024 | 0.1598 | 0.64 | oui |
| -0.5 | -0.0312 | -0.0104 | 391 | 7 | 0.1608 | 0.1747 | 0.92 | oui |
| +0.0 | -0.0104 | +0.0104 | 490 | 8 | 0.2015 | 0.1974 | 1.02 | oui |
| +0.5 | +0.0104 | +0.0312 | 537 | 9 | 0.2208 | 0.1747 | 1.26 | oui |
| +1.0 | +0.0312 | +0.0624 | 471 | 8 | 0.1937 | 0.1598 | 1.21 | oui |
| +2.0 | +0.0624 | +∞ | 189 | 3 | 0.0777 | 0.0668 | 1.16 | oui |

**DEXUSEU** (log) — σ à 60 pas = **0.03424** · estimateurs croisés : racine-h 0.03469, blocs disjoints 0.03590 (écart relatif 4.8 %) · dérive d'échantillon +0.00179 (+0.05 σ) · 2432 variations chevauchantes, 41 blocs indépendants · 2016-10-31 → 2026-10-23

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0514 | 130 | 2 | 0.0535 | 0.0668 | 0.80 | oui |
| -1.0 | -0.0514 | -0.0257 | 318 | 5 | 0.1308 | 0.1598 | 0.82 | oui |
| -0.5 | -0.0257 | -0.0086 | 512 | 9 | 0.2105 | 0.1747 | 1.21 | oui |
| +0.0 | -0.0086 | +0.0086 | 617 | 10 | 0.2537 | 0.1974 | 1.29 | oui |
| +0.5 | +0.0086 | +0.0257 | 321 | 5 | 0.1320 | 0.1747 | 0.76 | oui |
| +1.0 | +0.0257 | +0.0514 | 307 | 5 | 0.1262 | 0.1598 | 0.79 | oui |
| +2.0 | +0.0514 | +∞ | 227 | 4 | 0.0933 | 0.0668 | 1.40 | oui |

**DGS10** (niveau) — σ à 60 pas = **0.42213** · estimateurs croisés : racine-h 0.41559, blocs disjoints 0.49139 (écart relatif 18.2 %) · dérive d'échantillon +0.06368 (+0.15 σ) · 2437 variations chevauchantes, 41 blocs indépendants · 2016-10-31 → 2026-10-27

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.6332 | 123 | 2 | 0.0505 | 0.0668 | 0.76 | oui |
| -1.0 | -0.6332 | -0.3166 | 284 | 5 | 0.1165 | 0.1598 | 0.73 | oui |
| -0.5 | -0.3166 | -0.1055 | 371 | 6 | 0.1522 | 0.1747 | 0.87 | oui |
| +0.0 | -0.1055 | +0.1055 | 528 | 9 | 0.2167 | 0.1974 | 1.10 | oui |
| +0.5 | +0.1055 | +0.3166 | 556 | 9 | 0.2281 | 0.1747 | 1.31 | oui |
| +1.0 | +0.3166 | +0.6332 | 370 | 6 | 0.1518 | 0.1598 | 0.95 | oui |
| +2.0 | +0.6332 | +∞ | 205 | 3 | 0.0841 | 0.0668 | 1.26 | oui |

**DGS2** (niveau) — σ à 60 pas = **0.49663** · estimateurs croisés : racine-h 0.42276, blocs disjoints 0.54531 (écart relatif 29.0 %) · dérive d'échantillon +0.08399 (+0.17 σ) · 2437 variations chevauchantes, 41 blocs indépendants · 2016-10-31 → 2026-10-27

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.7449 | 115 | 2 | 0.0472 | 0.0668 | 0.71 | oui |
| -1.0 | -0.7449 | -0.3725 | 228 | 4 | 0.0936 | 0.1598 | 0.59 | oui |
| -0.5 | -0.3725 | -0.1242 | 323 | 5 | 0.1325 | 0.1747 | 0.76 | oui |
| +0.0 | -0.1242 | +0.1242 | 739 | 12 | 0.3032 | 0.1974 | 1.54 | oui |
| +0.5 | +0.1242 | +0.3725 | 471 | 8 | 0.1933 | 0.1747 | 1.11 | oui |
| +1.0 | +0.3725 | +0.7449 | 360 | 6 | 0.1477 | 0.1598 | 0.92 | oui |
| +2.0 | +0.7449 | +∞ | 201 | 3 | 0.0825 | 0.0668 | 1.23 | oui |

**DGS30** (niveau) — σ à 60 pas = **0.36422** · estimateurs croisés : racine-h 0.39321, blocs disjoints 0.42108 (écart relatif 15.6 %) · dérive d'échantillon +0.05820 (+0.16 σ) · 2437 variations chevauchantes, 41 blocs indépendants · 2016-10-31 → 2026-10-27

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.5463 | 128 | 2 | 0.0525 | 0.0668 | 0.79 | oui |
| -1.0 | -0.5463 | -0.2732 | 276 | 5 | 0.1133 | 0.1598 | 0.71 | oui |
| -0.5 | -0.2732 | -0.0911 | 338 | 6 | 0.1387 | 0.1747 | 0.79 | oui |
| +0.0 | -0.0911 | +0.0911 | 630 | 10 | 0.2585 | 0.1974 | 1.31 | oui |
| +0.5 | +0.0911 | +0.2732 | 465 | 8 | 0.1908 | 0.1747 | 1.09 | oui |
| +1.0 | +0.2732 | +0.5463 | 392 | 7 | 0.1609 | 0.1598 | 1.01 | oui |
| +2.0 | +0.5463 | +∞ | 208 | 3 | 0.0854 | 0.0668 | 1.28 | oui |

**DTWEXBGS** (log) — σ à 60 pas = **0.02570** · estimateurs croisés : racine-h 0.02408, blocs disjoints 0.02946 (écart relatif 22.3 %) · dérive d'échantillon +0.00051 (+0.02 σ) · 2430 variations chevauchantes, 40 blocs indépendants · 2016-10-31 → 2026-10-23

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0386 | 171 | 3 | 0.0704 | 0.0668 | 1.05 | oui |
| -1.0 | -0.0386 | -0.0193 | 378 | 6 | 0.1556 | 0.1598 | 0.97 | oui |
| -0.5 | -0.0193 | -0.0064 | 359 | 6 | 0.1477 | 0.1747 | 0.85 | oui |
| +0.0 | -0.0064 | +0.0064 | 552 | 9 | 0.2272 | 0.1974 | 1.15 | oui |
| +0.5 | +0.0064 | +0.0193 | 468 | 8 | 0.1926 | 0.1747 | 1.10 | oui |
| +1.0 | +0.0193 | +0.0386 | 297 | 5 | 0.1222 | 0.1598 | 0.76 | oui |
| +2.0 | +0.0386 | +∞ | 205 | 3 | 0.0844 | 0.0668 | 1.26 | oui |

**NASDAQ100** (log) — σ à 60 pas = **0.08867** · estimateurs croisés : racine-h 0.11156, blocs disjoints 0.09541 (écart relatif 25.8 %) · dérive d'échantillon +0.04419 (+0.50 σ) · 2452 variations chevauchantes, 41 blocs indépendants · 2016-10-31 → 2026-10-27

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.1330 | 109 | 2 | 0.0445 | 0.0668 | 0.67 | oui |
| -1.0 | -0.1330 | -0.0665 | 166 | 3 | 0.0677 | 0.1598 | 0.42 ⚠ | oui |
| -0.5 | -0.0665 | -0.0222 | 186 | 3 | 0.0759 | 0.1747 | 0.43 ⚠ | oui |
| +0.0 | -0.0222 | +0.0222 | 353 | 6 | 0.1440 | 0.1974 | 0.73 | oui |
| +0.5 | +0.0222 | +0.0665 | 590 | 10 | 0.2406 | 0.1747 | 1.38 | oui |
| +1.0 | +0.0665 | +0.1330 | 732 | 12 | 0.2985 | 0.1598 | 1.87 | oui |
| +2.0 | +0.1330 | +∞ | 316 | 5 | 0.1289 | 0.0668 | 1.93 | oui |

**SP500** (log) — σ à 60 pas = **0.06910** · estimateurs croisés : racine-h 0.08849, blocs disjoints 0.06737 (écart relatif 31.3 %) · dérive d'échantillon +0.03043 (+0.44 σ) · 2451 variations chevauchantes, 41 blocs indépendants · 2016-10-31 → 2026-10-27

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.1037 | 115 | 2 | 0.0469 | 0.0668 | 0.70 | oui |
| -1.0 | -0.1037 | -0.0518 | 158 | 3 | 0.0645 | 0.1598 | 0.40 ⚠ | oui |
| -0.5 | -0.0518 | -0.0173 | 176 | 3 | 0.0718 | 0.1747 | 0.41 ⚠ | oui |
| +0.0 | -0.0173 | +0.0173 | 294 | 5 | 0.1200 | 0.1974 | 0.61 | oui |
| +0.5 | +0.0173 | +0.0518 | 758 | 13 | 0.3093 | 0.1747 | 1.77 | oui |
| +1.0 | +0.0518 | +0.1037 | 739 | 12 | 0.3015 | 0.1598 | 1.89 | oui |
| +2.0 | +0.1037 | +∞ | 211 | 4 | 0.0861 | 0.0668 | 1.29 | oui |

**VIXCLS** (log) — σ à 60 pas = **0.34620** · estimateurs croisés : racine-h 0.61297, blocs disjoints 0.37058 (écart relatif 77.1 %) · dérive d'échantillon +0.00461 (+0.01 σ) · 2484 variations chevauchantes, 41 blocs indépendants · 2016-10-31 → 2026-10-27

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.5193 | 77 | 1 | 0.0310 | 0.0668 | 0.46 ⚠ | oui |
| -1.0 | -0.5193 | -0.2596 | 383 | 6 | 0.1542 | 0.1598 | 0.96 | oui |
| -0.5 | -0.2596 | -0.0865 | 601 | 10 | 0.2419 | 0.1747 | 1.39 | oui |
| +0.0 | -0.0865 | +0.0865 | 621 | 10 | 0.2500 | 0.1974 | 1.27 | oui |
| +0.5 | +0.0865 | +0.2596 | 376 | 6 | 0.1514 | 0.1747 | 0.87 | oui |
| +1.0 | +0.2596 | +0.5193 | 248 | 4 | 0.0998 | 0.1598 | 0.62 | oui |
| +2.0 | +0.5193 | +∞ | 178 | 3 | 0.0717 | 0.0668 | 1.07 | oui |

---

## 6. TEST D'ASYMÉTRIE — DÉFINITION UNIQUE (R-030), L'ESPÉRANCE DÉCIDE

> Test d'admission : **espérance calculée sur la grille symétrique complète, les deux queues incluses**. Le rapport gain maximal / perte maximale est publié **pour information** et ne peut fonder aucune admission seul (T-001, faute E-018). Le rapport gain maximal / perte du scénario central est **interdit**. Une seule formulation, appliquée à tous les candidats, position détenue comprise.

| candidat | verdict | espérance % NAV | sans dérive | 1re moitié | 2e moitié | gain max | perte max | ratio (info) | critères échoués |
|---|:---:|---:|---:|---:|---:|---:|---:|---:|---|
| M005-DCOILBRENTEU-HAUSSE-ALIGNE | REFUSEE | +0.283 | +0.130 | +0.256 | +0.233 | +5.10 | -3.21 | 1.59:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DCOILBRENTEU-HAUSSE-CONTRARIEN | REFUSEE | +0.283 | +0.130 | +0.256 | +0.233 | +5.10 | -3.21 | 1.59:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DCOILBRENTEU-BAISSE-ALIGNE | REFUSEE | -0.283 | -0.130 | -0.256 | -0.233 | +3.21 | -5.10 | 0.63:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILBRENTEU-BAISSE-CONTRARIEN | REFUSEE | -0.283 | -0.130 | -0.256 | -0.233 | +3.21 | -5.10 | 0.63:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-HAUSSE-ALIGNE | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-HAUSSE-CONTRARIEN | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-BAISSE-ALIGNE | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-BAISSE-CONTRARIEN | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-HAUSSE-ALIGNE | REFUSEE | -0.004 | -0.066 | -0.079 | +0.038 | +0.62 | -0.71 | 0.87:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-HAUSSE-CONTRARIEN | REFUSEE | -0.004 | -0.066 | -0.079 | +0.038 | +0.62 | -0.71 | 0.87:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-BAISSE-ALIGNE | REFUSEE | +0.004 | +0.066 | +0.079 | -0.038 | +0.71 | -0.62 | 1.15:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-BAISSE-CONTRARIEN | REFUSEE | +0.004 | +0.066 | +0.079 | -0.038 | +0.71 | -0.62 | 1.15:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-HAUSSE-ALIGNE | REFUSEE | -0.060 | -0.075 | -0.030 | -0.072 | +0.49 | -0.60 | 0.82:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-HAUSSE-CONTRARIEN | REFUSEE | -0.060 | -0.075 | -0.030 | -0.072 | +0.49 | -0.60 | 0.82:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-BAISSE-ALIGNE | REFUSEE | +0.060 | +0.075 | +0.030 | +0.072 | +0.60 | -0.49 | 1.22:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DEXUSEU-BAISSE-CONTRARIEN | REFUSEE | +0.060 | +0.075 | +0.030 | +0.072 | +0.60 | -0.49 | 1.22:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DGS10-HAUSSE-ALIGNE | REFUSEE | +0.011 | -0.024 | -0.050 | +0.062 | +0.49 | -0.57 | 0.85:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-HAUSSE-CONTRARIEN | REFUSEE | +0.011 | -0.024 | -0.050 | +0.062 | +0.49 | -0.57 | 0.85:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-BAISSE-ALIGNE | REFUSEE | -0.011 | +0.024 | +0.050 | -0.062 | +0.57 | -0.49 | 1.17:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-BAISSE-CONTRARIEN | REFUSEE | -0.011 | +0.024 | +0.050 | -0.062 | +0.57 | -0.49 | 1.17:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-HAUSSE-ALIGNE | REFUSEE | -0.004 | -0.015 | -0.022 | +0.007 | +0.13 | -0.17 | 0.79:1 | 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-HAUSSE-CONTRARIEN | REFUSEE | -0.004 | -0.015 | -0.022 | +0.007 | +0.13 | -0.17 | 0.79:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-BAISSE-ALIGNE | REFUSEE | +0.004 | +0.015 | +0.022 | -0.007 | +0.17 | -0.13 | 1.26:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-BAISSE-CONTRARIEN | REFUSEE | +0.004 | +0.015 | +0.022 | -0.007 | +0.17 | -0.13 | 1.26:1 | 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-HAUSSE-ALIGNE | REFUSEE | +0.018 | -0.038 | -0.100 | +0.135 | +0.78 | -0.97 | 0.80:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-HAUSSE-CONTRARIEN | REFUSEE | +0.018 | -0.038 | -0.100 | +0.135 | +0.78 | -0.97 | 0.80:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-BAISSE-ALIGNE | REFUSEE | -0.018 | +0.038 | +0.100 | -0.135 | +0.97 | -0.78 | 1.25:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-BAISSE-CONTRARIEN | REFUSEE | -0.018 | +0.038 | +0.100 | -0.135 | +0.97 | -0.78 | 1.25:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-HAUSSE-ALIGNE | REFUSEE | -0.068 | -0.072 | -0.086 | -0.054 | +0.35 | -0.47 | 0.73:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-HAUSSE-CONTRARIEN | REFUSEE | -0.068 | -0.072 | -0.086 | -0.054 | +0.35 | -0.47 | 0.73:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-BAISSE-ALIGNE | REFUSEE | +0.068 | +0.072 | +0.086 | +0.054 | +0.47 | -0.35 | 1.36:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DTWEXBGS-BAISSE-CONTRARIEN | REFUSEE | +0.068 | +0.072 | +0.086 | +0.054 | +0.47 | -0.35 | 1.36:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-HAUSSE-ALIGNE | REFUSEE | +0.305 | -0.034 | +0.449 | +0.185 | +1.48 | -1.37 | 1.08:1 | 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-HAUSSE-CONTRARIEN | REFUSEE | +0.305 | -0.034 | +0.449 | +0.185 | +1.48 | -1.37 | 1.08:1 | 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-BAISSE-ALIGNE | REFUSEE | -0.305 | +0.034 | -0.449 | -0.185 | +1.37 | -1.48 | 0.93:1 | 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-NASDAQ100-BAISSE-CONTRARIEN | REFUSEE | -0.305 | +0.034 | -0.449 | -0.185 | +1.37 | -1.48 | 0.93:1 | 12_esperance_positive, 13_esperance_non_portee_par_derive, 14_esperance_stable_dans_le_temps |
| M005-SP500-HAUSSE-ALIGNE | REFUSEE | +0.185 | -0.044 | +0.212 | +0.152 | +1.11 | -1.11 | 1.00:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-SP500-HAUSSE-CONTRARIEN | REFUSEE | +0.185 | -0.044 | +0.212 | +0.152 | +1.11 | -1.11 | 1.00:1 | 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-SP500-BAISSE-ALIGNE | REFUSEE | -0.185 | +0.044 | -0.212 | -0.152 | +1.11 | -1.11 | 1.00:1 | 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-SP500-BAISSE-CONTRARIEN | REFUSEE | -0.185 | +0.044 | -0.212 | -0.152 | +1.11 | -1.11 | 1.00:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |

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

- `BAMLC0A0CM` : percentile REFUSÉ sur 5 ans — profondeur réelle 784 obs / 2.99 ans (début 2023-10-30). R-011 : un percentile calculé sur une série tronquée est sans valeur.
- `BAMLH0A0HYM2` : percentile REFUSÉ sur 5 ans — profondeur réelle 785 obs / 2.99 ans (début 2023-10-30). R-011 : un percentile calculé sur une série tronquée est sans valeur.
- `BAMLH0A0HYM2` : instrument NON ADMISSIBLE — P&L non calculable depuis le dépôt : l'OAS est un spread, et le dépôt ne contient pas le rendement de l'indice, donc pas la duration de spread. Aucune valeur ne peut être produite sans un chiffre extérieur aux données (E-002).
- `BAMLC0A0CM` : instrument NON ADMISSIBLE — P&L non calculable depuis le dépôt : l'OAS est un spread, et le dépôt ne contient pas le rendement de l'indice, donc pas la duration de spread. Aucune valeur ne peut être produite sans un chiffre extérieur aux données (E-002).
- Retards sur la date d'arrêté unique (E-014) : DEXJPUS 2 séance(s), DEXUSEU 2 séance(s), DTWEXBGS 2 séance(s)

**Vérification tierce (R-032) : NON SATISFAITE pour ce brief.** Le moteur ne dispose d'aucune source extérieure au dépôt. Trois estimateurs **internes** de σ sont publiés côte à côte au §5 ; ce sont des contrôles de cohérence interne, **pas** une vérification tierce, et ils ne sont pas présentés comme telle.

**Ce que ce moteur ne peut pas faire.** Il ne prouve aucune capacité prédictive : la règle de confirmation est une règle de percentile, déclarée et symétrique, pas un modèle validé hors échantillon. Il ne corrige pas la multiplicité : 40 candidats sont évalués et aucune pénalité de sélection n'est appliquée à l'espérance — c'est une limite déclarée, pas un oubli. Il ne voit ni les événements politiques, ni les décisions de banques centrales : le dépôt ne contient que des séries FRED, et toute affirmation de politique monétaire non adossée à `DFF` est refusée (critère 15, faute E-006).

---

*Fin du brief 005. Produit mécaniquement. Ne constitue pas un conseil en investissement.*