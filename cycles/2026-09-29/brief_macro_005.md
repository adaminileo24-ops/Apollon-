# BRIEF MACRO n° 005 — arrêté au 2026-09-22

*Produit par `apollon_macro.py` le 2026-09-29T11:22:28+00:00. Aucune valeur de ce document n'est saisie à la main : chacune porte sa série, sa date et sa profondeur. Bloc à copier tel quel.*

**Grille de scénarios (R-029, §11), déclarée avant toute lecture de données et empreintée :** `[-2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0]` · empreinte SHA-256 `6aaeb3863c875923…` · symétrique : True · horizon 60 séances (3 mois pour les séries mensuelles).

---

## 1. CONCLUSION, ÉNONCÉE D'ABORD

**40 candidats déclarés d'avance (10 instruments × 2 directions × 2 règles de confirmation). 40 évalués. 0 thèse(s) survivent aux quinze critères.**

**Abstention. Aucune thèse ne survit.** Ce n'est pas un silence : c'est un résultat, produit par le même portier que celui qui aurait admis une thèse. Le détail des échecs, critère par critère, figure au §6. La Section Macro ne transmet rien à la Section Risque ce cycle.

**Position détenue (contrôle 9, E-020) — 100 % cash, testée sur la même grille.** Espérance excédentaire du cash : +0.000 % de NAV. Référence 60/40 : +1.346 % (hors dérive : -0.209 %). **Écart du cash contre la référence : -1.346 % de NAV** sur 60 séances.

---

## 2. CE QUI A CHANGÉ — MÉCANISME, PAS CONTENU

Fait, étiqueté : les briefs 001 à 004 étaient rédigés par un agent. Celui-ci est produit par un moteur. Le paramètre libre de la Section Macro — la grille de scénarios — n'est plus accessible à l'agent : il est déclaré en tête de fichier, symétrique par construction, et son empreinte SHA-256 est vérifiée avant chaque usage. Sur le brief 004, ce paramètre avait porté le ratio annoncé de 1,29:1 à 3,0:1.

---

## 3. M1 · M2 · M3 · M4 — ÉTAT DES SÉRIES (FAIT)

Toutes les valeurs sont des FAITS lus dans le dépôt. Le retard est compté en séances ouvrées depuis la date d'arrêté unique. Les couples obligatoires sont vérifiés par le rendu : ce bloc ne peut pas être émis si un membre d'un couple manque.

| série | rôle déclaré | valeur | date | retard | n obs | profondeur | pct 1 an | pct 5 ans | pct complet |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| BAMLC0A0CM | risque_credit_ig | 0.77 | 2026-09-22 | 0 | 781 | 2.98 ans | 31.0 | REFUSÉ (insuffisante, -38 %) | 13.7 |
| BAMLH0A0HYM2 | risque_credit_hy | 2.68 | 2026-09-22 | 0 | 782 | 2.98 ans | 10.3 | REFUSÉ (insuffisante, -38 %) | 8.7 |
| CPIAUCSL | inflation_globale | 334.1 | 2026-08-01 | 52 | 118 | 9.83 ans | 100.0 | 100.0 | 100.0 |
| CPILFESL | inflation_sous_jacente | 337.8 | 2026-08-01 | 52 | 118 | 9.83 ans | 100.0 | 100.0 | 100.0 |
| DCOILBRENTEU | prix_energie | 114.9 | 2026-09-22 | 0 | 2529 | 9.97 ans | 88.9 | 94.2 | 97.1 |
| DCOILWTICO | prix_energie_wti | 96.41 | 2026-09-22 | 0 | 2493 | 9.97 ans | 81.0 | 87.8 | 93.8 |
| DEXJPUS | devise_usdjpy | 157.6 | 2026-09-22 | 0 | 2489 | 9.97 ans | 49.2 | 87.3 | 93.6 |
| DEXUSEU | devise_eurusd | 1.143 | 2026-09-22 | 0 | 2489 | 9.97 ans | 8.7 | 72.1 | 61.2 |
| DFF | politique_monetaire | 3.88 | 2026-09-22 | 0 | 3644 | 9.97 ans | 100.0 | 25.0 | 70.8 |
| DFII10 | taux_reel_10a | 2.63 | 2026-09-22 | 0 | 2492 | 9.97 ans | 99.2 | 99.8 | 99.9 |
| DGS10 | taux_nominal_10a | 4.96 | 2026-09-22 | 0 | 2492 | 9.97 ans | 98.4 | 99.6 | 99.8 |
| DGS2 | taux_nominal_2a | 4.71 | 2026-09-22 | 0 | 2492 | 9.97 ans | 98.8 | 86.0 | 92.9 |
| DGS30 | taux_nominal_30a | 5.29 | 2026-09-22 | 0 | 2492 | 9.97 ans | 97.2 | 99.4 | 99.7 |
| DTWEXBGS | dollar_large | 119.6 | 2026-09-22 | 0 | 2487 | 9.97 ans | 47.2 | 32.1 | 62.8 |
| INDPRO | activite_industrielle | 103.1 | 2026-08-01 | 52 | 119 | 9.83 ans | 100.0 | 100.0 | 92.4 |
| NASDAQ100 | prix_actions_tech | 3.073e+04 | 2026-09-22 | 0 | 2507 | 9.97 ans | 100.0 | 100.0 | 100.0 |
| OVXCLS | volatilite_implicite_petrole | 51.89 | 2026-09-22 | 0 | 2508 | 9.97 ans | 53.6 | 82.9 | 86.6 |
| PAYEMS | emploi | 1.591e+05 | 2026-08-01 | 52 | 119 | 9.83 ans | 100.0 | 100.0 | 100.0 |
| SP500 | prix_actions | 7765 | 2026-09-22 | 0 | 2506 | 9.97 ans | 98.8 | 99.8 | 99.9 |
| T10Y2Y | pente_courbe | 0.25 | 2026-09-22 | 0 | 2492 | 9.97 ans | 1.2 | 54.7 | 40.4 |
| T10YIE | point_mort_10a | 2.33 | 2026-09-22 | 0 | 2492 | 9.97 ans | 62.3 | 52.2 | 73.0 |
| T5YIFR | point_mort_5a5a | 2.34 | 2026-09-22 | 0 | 2492 | 9.97 ans | 98.0 | 81.5 | 90.4 |
| UNRATE | chomage | 4.1 | 2026-08-01 | 52 | 118 | 9.83 ans | 16.7 | 65.0 | 55.9 |
| VIXCLS | volatilite_implicite | 14.21 | 2026-09-22 | 0 | 2539 | 9.97 ans | 2.4 | 15.6 | 27.6 |
| VXDCLS | volatilite_implicite_dow | 14.56 | 2026-09-22 | 0 | 2509 | 9.97 ans | 26.2 | 31.9 | 36.9 |
| VXVCLS | volatilite_implicite_3m | 17.61 | 2026-09-22 | 0 | 2506 | 9.97 ans | 2.4 | 21.3 | 37.2 |

**Couples obligatoires contrôlés :** CPIAUCSL/CPILFESL, DGS10/DFII10, DGS10/T10YIE, BAMLH0A0HYM2/BAMLC0A0CM, UNRATE/PAYEMS, VIXCLS/SP500 — 0 manquement(s).

**Inflation en trois chiffres (contrôle 2, E-005).** Global +3.71 % sur un an (CPIAUCSL, 2026-08-01) · sous-jacent +2.76 % (CPILFESL) · **écart hors sous-jacent +95 pb**. Contribution énergie NON publiée : `CPIENGSL` est absente du dépôt. Lacune nommée avec le code FRED qui la comble (R-028) ; elle n'est pas présentée comme une limite de méthode. L'écart ci-dessus est l'écart global/sous-jacent, pas la contribution énergie.

---

## 4. IDENTITÉS COMPTABLES ET REDONDANCES (vérifiées numériquement)

| identité | vérifiable | n dates | résidu absolu max | tolérance | vérifiée |
|---|:---:|---:|---:|---:|:---:|
| T10YIE = DGS10 - DFII10 | oui | 2492 | 0.0000 | 0.02 | OUI |
| T10Y2Y = DGS10 - DGS2 | oui | 2492 | 0.0000 | 0.02 | OUI |

**Redondances détectées (11) — deux séries liées ne comptent jamais pour deux confirmations indépendantes :**

- identité comptable : T10YIE = DGS10 - DFII10 — T10YIE, DGS10, DFII10 (résidu max 0.0000)
- identité comptable : T10Y2Y = DGS10 - DGS2 — T10Y2Y, DGS10, DGS2 (résidu max 0.0000)
- corrélation des variations à 60 séances : BAMLC0A0CM / BAMLH0A0HYM2 = +0.941 sur 721 points (seuil 0.9)
- corrélation des variations à 60 séances : DGS10 / DGS30 = +0.966 sur 2432 points (seuil 0.9)
- corrélation des variations à 60 séances : INDPRO / PAYEMS = +0.913 sur 116 points (seuil 0.9)
- corrélation des variations à 60 séances : INDPRO / UNRATE = -0.918 sur 115 points (seuil 0.9)
- corrélation des variations à 60 séances : NASDAQ100 / SP500 = +0.903 sur 2446 points (seuil 0.9)
- corrélation des variations à 60 séances : PAYEMS / UNRATE = -0.983 sur 115 points (seuil 0.9)
- corrélation des variations à 60 séances : VIXCLS / VXDCLS = +0.930 sur 2446 points (seuil 0.9)
- corrélation des variations à 60 séances : VIXCLS / VXVCLS = +0.958 sur 2446 points (seuil 0.9)
- corrélation des variations à 60 séances : VXDCLS / VXVCLS = +0.934 sur 2446 points (seuil 0.9)

---

## 5. GRILLE, σ MESURÉ, ET DOUBLE CONFRONTATION DES PROBABILITÉS

σ est **mesuré** sur chaque série, jamais choisi. Les probabilités sont les **fréquences historiques** dans chaque bande, jamais un jugement. L'effectif de chaque bande est publié ; sous 20 observations la bande est déclarée NON ESTIMABLE. La colonne « emp./gauss. » est la double confrontation exigée par §11.5 : tout écart supérieur à un facteur 2 est déclaré (⚠).

**BAMLH0A0HYM2** (niveau) — σ à 60 pas = **0.45591** · estimateurs croisés : racine-h 0.53834, blocs disjoints 0.42420 (écart relatif 26.9 %) · dérive d'échantillon -0.11122 (-0.24 σ) · 722 variations chevauchantes, 12 blocs indépendants · 2023-09-29 → 2026-09-22

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.6839 | 55 | 1 | 0.0762 | 0.0668 | 1.14 | oui |
| -1.0 | -0.6839 | -0.3419 | 120 | 2 | 0.1662 | 0.1598 | 1.04 | oui |
| -0.5 | -0.3419 | -0.1140 | 194 | 3 | 0.2687 | 0.1747 | 1.54 | oui |
| +0.0 | -0.1140 | +0.1140 | 193 | 3 | 0.2673 | 0.1974 | 1.35 | oui |
| +0.5 | +0.1140 | +0.3419 | 80 | 1 | 0.1108 | 0.1747 | 0.63 | oui |
| +1.0 | +0.3419 | +0.6839 | 51 | 1 | 0.0706 | 0.1598 | 0.44 ⚠ | oui |
| +2.0 | +0.6839 | +∞ | 29 | 0 | 0.0402 | 0.0668 | 0.60 | oui |

**DCOILBRENTEU** (log) — σ à 60 pas = **0.24636** · estimateurs croisés : racine-h 0.24781, blocs disjoints 0.28493 (écart relatif 15.7 %) · dérive d'échantillon +0.01566 (+0.06 σ) · 2469 variations chevauchantes, 41 blocs indépendants · 2016-10-03 → 2026-09-22

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.3695 | 84 | 1 | 0.0340 | 0.0668 | 0.51 | oui |
| -1.0 | -0.3695 | -0.1848 | 155 | 3 | 0.0628 | 0.1598 | 0.39 ⚠ | oui |
| -0.5 | -0.1848 | -0.0616 | 503 | 8 | 0.2037 | 0.1747 | 1.17 | oui |
| +0.0 | -0.0616 | +0.0616 | 763 | 13 | 0.3090 | 0.1974 | 1.57 | oui |
| +0.5 | +0.0616 | +0.1848 | 614 | 10 | 0.2487 | 0.1747 | 1.42 | oui |
| +1.0 | +0.1848 | +0.3695 | 220 | 4 | 0.0891 | 0.1598 | 0.56 | oui |
| +2.0 | +0.3695 | +∞ | 130 | 2 | 0.0527 | 0.0668 | 0.79 | oui |

**DCOILWTICO** — non scénarisable : convention log inapplicable : 1 observation(s) non strictement positive(s), minimum -36.98 le 2020-04-20. Le prix a été négatif : aucun log-rendement n'existe. La série est déclarée NON SCÉNARISABLE plutôt que corrigée en silence.

**DEXJPUS** (log) — σ à 60 pas = **0.04231** · estimateurs croisés : racine-h 0.04391, blocs disjoints 0.04897 (écart relatif 15.7 %) · dérive d'échantillon +0.00933 (+0.22 σ) · 2429 variations chevauchantes, 40 blocs indépendants · 2016-10-03 → 2026-09-22

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0635 | 103 | 2 | 0.0424 | 0.0668 | 0.63 | oui |
| -1.0 | -0.0635 | -0.0317 | 239 | 4 | 0.0984 | 0.1598 | 0.62 | oui |
| -0.5 | -0.0317 | -0.0106 | 379 | 6 | 0.1560 | 0.1747 | 0.89 | oui |
| +0.0 | -0.0106 | +0.0106 | 496 | 8 | 0.2042 | 0.1974 | 1.03 | oui |
| +0.5 | +0.0106 | +0.0317 | 543 | 9 | 0.2235 | 0.1747 | 1.28 | oui |
| +1.0 | +0.0317 | +0.0635 | 476 | 8 | 0.1960 | 0.1598 | 1.23 | oui |
| +2.0 | +0.0635 | +∞ | 193 | 3 | 0.0795 | 0.0668 | 1.19 | oui |

**DEXUSEU** (log) — σ à 60 pas = **0.03443** · estimateurs croisés : racine-h 0.03467, blocs disjoints 0.03563 (écart relatif 3.5 %) · dérive d'échantillon +0.00163 (+0.05 σ) · 2429 variations chevauchantes, 40 blocs indépendants · 2016-10-03 → 2026-09-22

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0516 | 133 | 2 | 0.0548 | 0.0668 | 0.82 | oui |
| -1.0 | -0.0516 | -0.0258 | 323 | 5 | 0.1330 | 0.1598 | 0.83 | oui |
| -0.5 | -0.0258 | -0.0086 | 505 | 8 | 0.2079 | 0.1747 | 1.19 | oui |
| +0.0 | -0.0086 | +0.0086 | 614 | 10 | 0.2528 | 0.1974 | 1.28 | oui |
| +0.5 | +0.0086 | +0.0258 | 325 | 5 | 0.1338 | 0.1747 | 0.77 | oui |
| +1.0 | +0.0258 | +0.0516 | 304 | 5 | 0.1252 | 0.1598 | 0.78 | oui |
| +2.0 | +0.0516 | +∞ | 225 | 4 | 0.0926 | 0.0668 | 1.39 | oui |

**DGS10** (niveau) — σ à 60 pas = **0.42251** · estimateurs croisés : racine-h 0.41396, blocs disjoints 0.40534 (écart relatif 4.2 %) · dérive d'échantillon +0.06328 (+0.15 σ) · 2432 variations chevauchantes, 41 blocs indépendants · 2016-10-03 → 2026-09-22

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.6338 | 123 | 2 | 0.0506 | 0.0668 | 0.76 | oui |
| -1.0 | -0.6338 | -0.3169 | 284 | 5 | 0.1168 | 0.1598 | 0.73 | oui |
| -0.5 | -0.3169 | -0.1056 | 371 | 6 | 0.1525 | 0.1747 | 0.87 | oui |
| +0.0 | -0.1056 | +0.1056 | 528 | 9 | 0.2171 | 0.1974 | 1.10 | oui |
| +0.5 | +0.1056 | +0.3169 | 555 | 9 | 0.2282 | 0.1747 | 1.31 | oui |
| +1.0 | +0.3169 | +0.6338 | 369 | 6 | 0.1517 | 0.1598 | 0.95 | oui |
| +2.0 | +0.6338 | +∞ | 202 | 3 | 0.0831 | 0.0668 | 1.24 | oui |

**DGS2** (niveau) — σ à 60 pas = **0.49520** · estimateurs croisés : racine-h 0.42084, blocs disjoints 0.49914 (écart relatif 18.6 %) · dérive d'échantillon +0.08132 (+0.16 σ) · 2432 variations chevauchantes, 41 blocs indépendants · 2016-10-03 → 2026-09-22

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.7428 | 115 | 2 | 0.0473 | 0.0668 | 0.71 | oui |
| -1.0 | -0.7428 | -0.3714 | 228 | 4 | 0.0938 | 0.1598 | 0.59 | oui |
| -0.5 | -0.3714 | -0.1238 | 323 | 5 | 0.1328 | 0.1747 | 0.76 | oui |
| +0.0 | -0.1238 | +0.1238 | 739 | 12 | 0.3039 | 0.1974 | 1.54 | oui |
| +0.5 | +0.1238 | +0.3714 | 483 | 8 | 0.1986 | 0.1747 | 1.14 | oui |
| +1.0 | +0.3714 | +0.7428 | 346 | 6 | 0.1423 | 0.1598 | 0.89 | oui |
| +2.0 | +0.7428 | +∞ | 198 | 3 | 0.0814 | 0.0668 | 1.22 | oui |

**DGS30** (niveau) — σ à 60 pas = **0.36474** · estimateurs croisés : racine-h 0.39218, blocs disjoints 0.35007 (écart relatif 12.0 %) · dérive d'échantillon +0.05823 (+0.16 σ) · 2432 variations chevauchantes, 41 blocs indépendants · 2016-10-03 → 2026-09-22

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.5471 | 128 | 2 | 0.0526 | 0.0668 | 0.79 | oui |
| -1.0 | -0.5471 | -0.2736 | 276 | 5 | 0.1135 | 0.1598 | 0.71 | oui |
| -0.5 | -0.2736 | -0.0912 | 338 | 6 | 0.1390 | 0.1747 | 0.80 | oui |
| +0.0 | -0.0912 | +0.0912 | 629 | 10 | 0.2586 | 0.1974 | 1.31 | oui |
| +0.5 | +0.0912 | +0.2736 | 461 | 8 | 0.1896 | 0.1747 | 1.09 | oui |
| +1.0 | +0.2736 | +0.5471 | 394 | 7 | 0.1620 | 0.1598 | 1.01 | oui |
| +2.0 | +0.5471 | +∞ | 206 | 3 | 0.0847 | 0.0668 | 1.27 | oui |

**DTWEXBGS** (log) — σ à 60 pas = **0.02594** · estimateurs croisés : racine-h 0.02405, blocs disjoints 0.02817 (écart relatif 17.1 %) · dérive d'échantillon +0.00078 (+0.03 σ) · 2427 variations chevauchantes, 40 blocs indépendants · 2016-10-03 → 2026-09-22

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.0389 | 159 | 3 | 0.0655 | 0.0668 | 0.98 | oui |
| -1.0 | -0.0389 | -0.0195 | 387 | 6 | 0.1595 | 0.1598 | 1.00 | oui |
| -0.5 | -0.0195 | -0.0065 | 359 | 6 | 0.1479 | 0.1747 | 0.85 | oui |
| +0.0 | -0.0065 | +0.0065 | 542 | 9 | 0.2233 | 0.1974 | 1.13 | oui |
| +0.5 | +0.0065 | +0.0195 | 462 | 8 | 0.1904 | 0.1747 | 1.09 | oui |
| +1.0 | +0.0195 | +0.0389 | 309 | 5 | 0.1273 | 0.1598 | 0.80 | oui |
| +2.0 | +0.0389 | +∞ | 209 | 3 | 0.0861 | 0.0668 | 1.29 | oui |

**NASDAQ100** (log) — σ à 60 pas = **0.08877** · estimateurs croisés : racine-h 0.11140, blocs disjoints 0.08445 (écart relatif 31.9 %) · dérive d'échantillon +0.04415 (+0.50 σ) · 2447 variations chevauchantes, 41 blocs indépendants · 2016-10-03 → 2026-09-22

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.1332 | 108 | 2 | 0.0441 | 0.0668 | 0.66 | oui |
| -1.0 | -0.1332 | -0.0666 | 167 | 3 | 0.0682 | 0.1598 | 0.43 ⚠ | oui |
| -0.5 | -0.0666 | -0.0222 | 186 | 3 | 0.0760 | 0.1747 | 0.44 ⚠ | oui |
| +0.0 | -0.0222 | +0.0222 | 357 | 6 | 0.1459 | 0.1974 | 0.74 | oui |
| +0.5 | +0.0222 | +0.0666 | 584 | 10 | 0.2387 | 0.1747 | 1.37 | oui |
| +1.0 | +0.0666 | +0.1332 | 730 | 12 | 0.2983 | 0.1598 | 1.87 | oui |
| +2.0 | +0.1332 | +∞ | 315 | 5 | 0.1287 | 0.0668 | 1.93 | oui |

**SP500** (log) — σ à 60 pas = **0.06921** · estimateurs croisés : racine-h 0.08850, blocs disjoints 0.06841 (écart relatif 29.4 %) · dérive d'échantillon +0.03064 (+0.44 σ) · 2446 variations chevauchantes, 41 blocs indépendants · 2016-10-03 → 2026-09-22

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.1038 | 114 | 2 | 0.0466 | 0.0668 | 0.70 | oui |
| -1.0 | -0.1038 | -0.0519 | 159 | 3 | 0.0650 | 0.1598 | 0.41 ⚠ | oui |
| -0.5 | -0.0519 | -0.0173 | 176 | 3 | 0.0720 | 0.1747 | 0.41 ⚠ | oui |
| +0.0 | -0.0173 | +0.0173 | 293 | 5 | 0.1198 | 0.1974 | 0.61 | oui |
| +0.5 | +0.0173 | +0.0519 | 743 | 12 | 0.3038 | 0.1747 | 1.74 | oui |
| +1.0 | +0.0519 | +0.1038 | 752 | 13 | 0.3074 | 0.1598 | 1.92 | oui |
| +2.0 | +0.1038 | +∞ | 209 | 3 | 0.0854 | 0.0668 | 1.28 | oui |

**VIXCLS** (log) — σ à 60 pas = **0.34706** · estimateurs croisés : racine-h 0.61258, blocs disjoints 0.34737 (écart relatif 76.5 %) · dérive d'échantillon +0.00339 (+0.01 σ) · 2479 variations chevauchantes, 41 blocs indépendants · 2016-10-03 → 2026-09-22

| kσ | borne basse | borne haute | n | n indép. | p empirique | p gaussienne | emp./gauss. | estimable |
|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| -2.0 | −∞ | -0.5206 | 77 | 1 | 0.0311 | 0.0668 | 0.46 ⚠ | oui |
| -1.0 | -0.5206 | -0.2603 | 388 | 6 | 0.1565 | 0.1598 | 0.98 | oui |
| -0.5 | -0.2603 | -0.0868 | 603 | 10 | 0.2432 | 0.1747 | 1.39 | oui |
| +0.0 | -0.0868 | +0.0868 | 613 | 10 | 0.2473 | 0.1974 | 1.25 | oui |
| +0.5 | +0.0868 | +0.2603 | 373 | 6 | 0.1505 | 0.1747 | 0.86 | oui |
| +1.0 | +0.2603 | +0.5206 | 248 | 4 | 0.1000 | 0.1598 | 0.63 | oui |
| +2.0 | +0.5206 | +∞ | 177 | 3 | 0.0714 | 0.0668 | 1.07 | oui |

---

## 6. TEST D'ASYMÉTRIE — DÉFINITION UNIQUE (R-030), L'ESPÉRANCE DÉCIDE

> Test d'admission : **espérance calculée sur la grille symétrique complète, les deux queues incluses**. Le rapport gain maximal / perte maximale est publié **pour information** et ne peut fonder aucune admission seul (T-001, faute E-018). Le rapport gain maximal / perte du scénario central est **interdit**. Une seule formulation, appliquée à tous les candidats, position détenue comprise.

| candidat | verdict | espérance % NAV | sans dérive | 1re moitié | 2e moitié | gain max | perte max | ratio (info) | critères échoués |
|---|:---:|---:|---:|---:|---:|---:|---:|---:|---|
| M005-DCOILBRENTEU-HAUSSE-ALIGNE | REFUSEE | +0.250 | +0.125 | +0.256 | +0.124 | +5.02 | -3.19 | 1.58:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DCOILBRENTEU-HAUSSE-CONTRARIEN | REFUSEE | +0.250 | +0.125 | +0.256 | +0.124 | +5.02 | -3.19 | 1.58:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DCOILBRENTEU-BAISSE-ALIGNE | REFUSEE | -0.250 | -0.125 | -0.256 | -0.124 | +3.19 | -5.02 | 0.63:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILBRENTEU-BAISSE-CONTRARIEN | REFUSEE | -0.250 | -0.125 | -0.256 | -0.124 | +3.19 | -5.02 | 0.63:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-HAUSSE-ALIGNE | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-HAUSSE-CONTRARIEN | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-BAISSE-ALIGNE | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DCOILWTICO-BAISSE-CONTRARIEN | REFUSEE | n/d | n/d | n/d | n/d | n/d | n/d | n/d | 5_bandes_estimables, 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-HAUSSE-ALIGNE | REFUSEE | +0.002 | -0.066 | -0.072 | +0.045 | +0.63 | -0.72 | 0.87:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-HAUSSE-CONTRARIEN | REFUSEE | +0.002 | -0.066 | -0.072 | +0.045 | +0.63 | -0.72 | 0.87:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-BAISSE-ALIGNE | REFUSEE | -0.002 | +0.066 | +0.072 | -0.045 | +0.72 | -0.63 | 1.14:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXJPUS-BAISSE-CONTRARIEN | REFUSEE | -0.002 | +0.066 | +0.072 | -0.045 | +0.72 | -0.63 | 1.14:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-HAUSSE-ALIGNE | REFUSEE | -0.061 | -0.075 | -0.033 | -0.072 | +0.50 | -0.61 | 0.82:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-HAUSSE-CONTRARIEN | REFUSEE | -0.061 | -0.075 | -0.033 | -0.072 | +0.50 | -0.61 | 0.82:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DEXUSEU-BAISSE-ALIGNE | REFUSEE | +0.061 | +0.075 | +0.033 | +0.072 | +0.61 | -0.50 | 1.22:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DEXUSEU-BAISSE-CONTRARIEN | REFUSEE | +0.061 | +0.075 | +0.033 | +0.072 | +0.61 | -0.50 | 1.22:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DGS10-HAUSSE-ALIGNE | REFUSEE | +0.011 | -0.023 | -0.045 | +0.058 | +0.49 | -0.57 | 0.85:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-HAUSSE-CONTRARIEN | REFUSEE | +0.011 | -0.023 | -0.045 | +0.058 | +0.49 | -0.57 | 0.85:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-BAISSE-ALIGNE | REFUSEE | -0.011 | +0.023 | +0.045 | -0.058 | +0.57 | -0.49 | 1.17:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS10-BAISSE-CONTRARIEN | REFUSEE | -0.011 | +0.023 | +0.045 | -0.058 | +0.57 | -0.49 | 1.17:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-HAUSSE-ALIGNE | REFUSEE | -0.005 | -0.015 | -0.021 | +0.007 | +0.13 | -0.17 | 0.79:1 | 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-HAUSSE-CONTRARIEN | REFUSEE | -0.005 | -0.015 | -0.021 | +0.007 | +0.13 | -0.17 | 0.79:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-BAISSE-ALIGNE | REFUSEE | +0.005 | +0.015 | +0.021 | -0.007 | +0.17 | -0.13 | 1.27:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS2-BAISSE-CONTRARIEN | REFUSEE | +0.005 | +0.015 | +0.021 | -0.007 | +0.17 | -0.13 | 1.27:1 | 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-HAUSSE-ALIGNE | REFUSEE | +0.017 | -0.037 | -0.093 | +0.126 | +0.78 | -0.98 | 0.80:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-HAUSSE-CONTRARIEN | REFUSEE | +0.017 | -0.037 | -0.093 | +0.126 | +0.78 | -0.98 | 0.80:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-BAISSE-ALIGNE | REFUSEE | -0.017 | +0.037 | +0.093 | -0.126 | +0.98 | -0.78 | 1.25:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DGS30-BAISSE-CONTRARIEN | REFUSEE | -0.017 | +0.037 | +0.093 | -0.126 | +0.98 | -0.78 | 1.25:1 | 11_invalidation_non_deja_survenue, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-HAUSSE-ALIGNE | REFUSEE | -0.065 | -0.072 | -0.081 | -0.052 | +0.35 | -0.48 | 0.74:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-HAUSSE-CONTRARIEN | REFUSEE | -0.065 | -0.072 | -0.081 | -0.052 | +0.35 | -0.48 | 0.74:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 12_esperance_positive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-DTWEXBGS-BAISSE-ALIGNE | REFUSEE | +0.065 | +0.072 | +0.081 | +0.052 | +0.48 | -0.35 | 1.36:1 | 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-DTWEXBGS-BAISSE-CONTRARIEN | REFUSEE | +0.065 | +0.072 | +0.081 | +0.052 | +0.48 | -0.35 | 1.36:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 10_invalidation_fait_date, 11_invalidation_non_deja_survenue, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-HAUSSE-ALIGNE | REFUSEE | +0.304 | -0.034 | +0.454 | +0.185 | +1.48 | -1.38 | 1.08:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-HAUSSE-CONTRARIEN | REFUSEE | +0.304 | -0.034 | +0.454 | +0.185 | +1.48 | -1.38 | 1.08:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-NASDAQ100-BAISSE-ALIGNE | REFUSEE | -0.304 | +0.034 | -0.454 | -0.185 | +1.38 | -1.48 | 0.93:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-NASDAQ100-BAISSE-CONTRARIEN | REFUSEE | -0.304 | +0.034 | -0.454 | -0.185 | +1.38 | -1.48 | 0.93:1 | 12_esperance_positive, 13_esperance_non_portee_par_derive, 14_esperance_stable_dans_le_temps |
| M005-SP500-HAUSSE-ALIGNE | REFUSEE | +0.187 | -0.043 | +0.218 | +0.155 | +1.11 | -1.11 | 1.01:1 | 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-SP500-HAUSSE-CONTRARIEN | REFUSEE | +0.187 | -0.043 | +0.218 | +0.155 | +1.11 | -1.11 | 1.01:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree |
| M005-SP500-BAISSE-ALIGNE | REFUSEE | -0.187 | +0.043 | -0.218 | -0.155 | +1.11 | -1.11 | 0.99:1 | 8_confirmations_independantes, 9_test_execute_et_vrai, 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |
| M005-SP500-BAISSE-CONTRARIEN | REFUSEE | -0.187 | +0.043 | -0.218 | -0.155 | +1.11 | -1.11 | 0.99:1 | 12_esperance_positive, 13_esperance_non_portee_par_derive, 16_arete_conditionnelle_mesuree, 14_esperance_stable_dans_le_temps |

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
| 8_confirmations_independantes | 24 |
| 9_test_execute_et_vrai | 24 |
| 10_invalidation_fait_date | 12 |
| 11_invalidation_non_deja_survenue | 22 |
| 12_esperance_positive | 22 |
| 13_esperance_non_portee_par_derive | 24 |
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

- `BAMLC0A0CM` : percentile REFUSÉ sur 5 ans — profondeur réelle 781 obs / 2.98 ans (début 2023-09-29). R-011 : un percentile calculé sur une série tronquée est sans valeur.
- `BAMLH0A0HYM2` : percentile REFUSÉ sur 5 ans — profondeur réelle 782 obs / 2.98 ans (début 2023-09-29). R-011 : un percentile calculé sur une série tronquée est sans valeur.
- `BAMLH0A0HYM2` : instrument NON ADMISSIBLE — P&L non calculable depuis le dépôt : l'OAS est un spread, et le dépôt ne contient pas le rendement de l'indice, donc pas la duration de spread. Aucune valeur ne peut être produite sans un chiffre extérieur aux données (E-002).
- `BAMLC0A0CM` : instrument NON ADMISSIBLE — P&L non calculable depuis le dépôt : l'OAS est un spread, et le dépôt ne contient pas le rendement de l'indice, donc pas la duration de spread. Aucune valeur ne peut être produite sans un chiffre extérieur aux données (E-002).

**Vérification tierce (R-032) : NON SATISFAITE pour ce brief.** Le moteur ne dispose d'aucune source extérieure au dépôt. Trois estimateurs **internes** de σ sont publiés côte à côte au §5 ; ce sont des contrôles de cohérence interne, **pas** une vérification tierce, et ils ne sont pas présentés comme telle.

**Ce que ce moteur ne peut pas faire.** Il ne prouve aucune capacité prédictive : la règle de confirmation est une règle de percentile, déclarée et symétrique, pas un modèle validé hors échantillon. Il ne corrige pas la multiplicité : 40 candidats sont évalués et aucune pénalité de sélection n'est appliquée à l'espérance — c'est une limite déclarée, pas un oubli. Il ne voit ni les événements politiques, ni les décisions de banques centrales : le dépôt ne contient que des séries FRED, et toute affirmation de politique monétaire non adossée à `DFF` est refusée (critère 15, faute E-006).

---

*Fin du brief 005. Produit mécaniquement. Ne constitue pas un conseil en investissement.*