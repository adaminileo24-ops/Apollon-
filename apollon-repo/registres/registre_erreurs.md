# REGISTRE DES ERREURS

**Fichier immuable.** On ajoute, on ne réécrit jamais. Une entrée effacée est une leçon perdue.

**Protocole de lecture — obligatoire :** tout agent consulte ce registre **avant** de produire. C'est le seul mécanisme par lequel une erreur commise dans une session ne se répète pas dans la suivante. Un agent qui ne lit pas ce fichier recommence à zéro.

**Protocole d'écriture :** toute erreur détectée y est inscrite le jour même, avec sa cause racine et la règle qui en découle. Une erreur apparaissant **trois fois** cesse d'être une erreur : elle devient un défaut structurel du mandat, qui doit être réécrit.

---

## Table de suivi

| Réf | Date | Section | Erreur | Gravité | Occurrences | Règle |
|---|---|---|---|---|---|---|
| E-001 | 14/08/2026 | Processus | Brief transmis sans passage Astra | **Critique** | 1 | R-001 |
| E-002 | 14/08/2026 | Macro | Titre d'actualité pris pour une cotation | **Critique** | 1 | R-002 |
| E-003 | 14/08/2026 | Macro | Niveau cité sans contexte historique | Sérieuse | 1 | R-003 |
| E-004 | 14/08/2026 | Macro | Source tronquée à la moitié favorable | **Critique** | 1 | R-004 |
| E-005 | 14/08/2026 | Macro | Variable décisive omise (CPI cœur) | **Critique** | 1 | R-005 |
| E-006 | 14/08/2026 | Macro | Thèse bâtie sur une prémisse non vérifiée | **Critique** | 1 | R-006 |
| E-007 | 14/08/2026 | Macro | Même indicateur utilisé dans deux sens opposés | **Critique** | 1 | R-007 |
| E-008 | 14/08/2026 | Macro | Pari unique présenté comme sept idées | **Critique** | 1 | R-008 |
| E-009 | 14/08/2026 | Macro | Fausse précision — décimales sur un chiffre faux | Modérée | 1 | R-009 |
| E-010 | 14/08/2026 | Macro | Fait institutionnel majeur ignoré | Sérieuse | 1 | R-010 |

---

## E-001 — Brief transmis sans passage Astra

**Fait.** Le brief Macro n° 001 a été transmis à l'opérateur sans contradiction préalable, en violation directe de la règle de séquence écrite deux heures plus tôt. L'opérateur a détecté l'omission en une question.

**Cause racine.** Aucun contrôle bloquant. La règle existait sur le papier ; rien n'empêchait matériellement de la contourner. Une règle sans mécanisme d'application n'est pas une règle, c'est une intention.

**Conséquence.** Le brief comportait sept thèses. Après contradiction : cinq rejetées, deux fragiles, zéro solide.

> **R-001 — Aucune production ne parvient à l'opérateur sans note Astra jointe.** L'absence de note vaut refus de transmission. Le contrôle est structurel : la note Astra fait partie du livrable, pas d'une étape optionnelle qui la précède.

---

## E-002 — Titre d'actualité pris pour une cotation

**Fait.** Le Brent a été porté à « plus de 108 $ » dans la charte fondatrice. Cotation réelle vérifiée : **87,22 $**. Le chiffre provenait d'un titre d'article capté à la pointe du conflit, sans date.

**Cause racine.** Confusion entre un résultat de recherche et une cotation. Un titre décrit un état passé ; une page de cotation décrit l'état présent.

**Conséquence.** La « Tension 1 » de la charte reposait intégralement sur ce chiffre. Diagnostic de régime faux.

> **R-002 — Un prix ne provient jamais d'un titre d'article.** Il provient d'une page de cotation, et la date de la cotation est reportée à côté du chiffre. Un prix sans date est rejeté.

---

## E-003 — Niveau cité sans contexte historique

**Fait.** L'or à 4 377 $ a été décrit comme « proche d'un plus haut ». Il se situe **22 % sous son record de 5 608 $** de janvier 2026.

**Cause racine.** Fenêtre d'observation trop courte. « Plus haut de deux mois » était exact et trompeur simultanément.

> **R-003 — Tout niveau est accompagné de sa distance au record et de sa variation sur un an.** Un prix isolé n'a pas de sens.

---

## E-004 — Source tronquée à la moitié favorable

**Fait.** Le rapport AIE d'août 2026 a été cité pour son déficit d'offre 2026 de 1,27 mb/j. **Le même rapport prévoit un excédent de 4,61 mb/j en 2027**, avec reconstitution des stocks dès mi-2027. Cette moitié a été supprimée.

**Cause racine.** Biais de confirmation opérant à la lecture. La partie du rapport contredisant la thèse en cours de rédaction n'a pas été retenue.

**Gravité particulière.** C'est l'erreur qui ressemble le plus à de la malhonnêteté, même commise sans intention. Elle détruit la valeur de toute citation ultérieure.

> **R-004 — Une source citée est citée dans son intégralité sur le point traité.** Si le document prévoit un déficit puis un excédent, les deux figurent. Citer la moitié favorable d'une source est traité comme une faute grave, pas comme une omission.

---

## E-005 — Variable décisive omise

**Fait.** Le CPI a été présenté à 3,4 % en glissement annuel. Le **CPI cœur est à 2,5 %** (BLS, juillet 2026), l'énergie à −1,5 % sur le mois et +14,7 % sur un an. L'écart de 90 pb est intégralement énergétique.

**Cause racine.** Le chiffre global soutenait la thèse d'une inflation persistante ; le cœur la contredisait. Non recherché.

**Conséquence.** La lecture de la fonction de réaction de la Fed était inversée. Si le pétrole reflue, le global converge vers le cœur en deux trimestres et le problème d'inflation disparaît.

> **R-005 — L'inflation est toujours rapportée en trois chiffres : global, cœur, et contribution énergie.** Jamais le global seul. La série CPILFESL est intégrée au pipeline pour rendre l'omission impossible.

---

## E-006 — Thèse bâtie sur une prémisse non vérifiée

**Fait.** Thèse 6 : « hausse BoJ anticipée en septembre ou octobre, risque non tarifé ». Vérification : **la BoJ a relevé ses taux en juin 2026, de 0,75 % à 1,00 %** — plus haut niveau depuis septembre 1995. Maintien le 31 juillet, 8 voix contre 1, la dissidence demandant 1,25 %.

**Cause racine.** Une spéculation de marché relayée par un article a été traitée comme un fait, sans consultation de la source primaire.

**Aggravation.** Le Nikkei était présenté comme un rallye non corrigé à +58 % sur un an. Il se situe à **−5,9 % de son record de 73 007** atteint en juin 2026 — la correction avait déjà eu lieu.

> **R-006 — Toute affirmation sur une décision de banque centrale est vérifiée à la source primaire ou sur une page de taux directeur.** Jamais depuis un commentaire de marché.

---

## E-007 — Même indicateur utilisé dans deux sens opposés

**Fait.** Thèse 5 : le spread haut rendement à 271 pb est un signal de vente du crédit. Thèse 7 : le spread haut rendement est un indicateur avancé des actions. Les deux ensemble impliquent qu'un spread stable à 271 pb est le signal **le plus haussier** disponible sur les actions — l'inverse de la conclusion défensive retenue.

**Cause racine.** Conclusion écrite avant le raisonnement. Chaque thèse a ensuite été justifiée isolément, sans contrôle de cohérence d'ensemble.

**Gravité particulière.** Cette erreur ne demandait aucune donnée externe pour être détectée. Une relecture de cohérence l'aurait révélée.

> **R-007 — Contrôle de cohérence interne obligatoire avant transmission.** Chaque indicateur ne peut porter qu'un seul sens dans un même document. Les thèses sont relues ensemble, jamais uniquement une par une.

---

## E-008 — Pari unique présenté comme sept idées

**Fait.** Les sept recommandations du brief — longue volatilité, longue énergie, bêta réduit, sous-pondération Japon, sous-pondération haut rendement, or neutre — constituaient **un seul pari sur l'aggravation du risque géopolitique**, réparti sur sept lignes. Aucune corrélation n'était mentionnée.

**Conséquence chiffrée.** Dans le scénario adverse — accord sur Ormuz, probabilité estimée à 40 % — les sept positions perdent simultanément : **−3,3 % à −4,8 % de NAV en six à dix semaines**, et **−8 % à −12 %** en relatif face à un portefeuille 60/40. L'essentiel de la perte porte sur des positions optionnelles qui n'ont aucune capacité de récupération : elles expirent.

> **R-008 — Toute note contenant plus de deux recommandations déclare le facteur commun et la corrélation attendue entre elles.** Si les positions perdent ensemble dans le même scénario, elles constituent une position unique et sont dimensionnées comme telle.

---

## E-009 — Fausse précision

**Fait.** S&P 500 annoncé à « 7 803,01 » avec une variation de « +0,65 % ». Clôture précédente 7 748,50 → le calcul donne 7 798,9. Deux décimales affichées sur un chiffre incohérent avec sa propre variation.

**Cause racine.** Mélange de valeurs intraday et de clôture, et report de la précision affichée par la source sans contrôle.

> **R-009 — Toute valeur d'indice est contrôlée par recalcul depuis la clôture précédente et sa variation.** Précision limitée à ce que la source garantit réellement. La précision typographique ne remplace pas l'exactitude.

---

## E-010 — Fait institutionnel majeur ignoré

**Fait.** **Kevin Warsh a prêté serment comme président de la Réserve fédérale le 22 mai 2026**, et le FOMC l'a désigné à l'unanimité comme son président. Cet élément n'apparaît dans aucun document produit — alors que les trois dissidences hawkish du 29 juillet ont été commentées en détail.

**Cause racine.** Aucune vérification de l'état des institutions. Les données de marché ont été rafraîchies, pas le cadre institutionnel qui les gouverne.

**Portée.** Un changement de présidence de la Fed modifie la fonction de réaction. Commenter les votes du FOMC sans savoir qui le préside est une lacune de fond.

> **R-010 — Fiche institutionnelle vérifiée mensuellement :** dirigeants des banques centrales des dix zones du mandat, composition des comités, calendrier des mandats. Toute analyse de politique monétaire s'y réfère.

---

## Statistiques

| Section | Erreurs | Dont critiques |
|---|---|---|
| Macro | 9 | 6 |
| Processus | 1 | 1 |
| Risque | 0 | 0 |
| Trading | 0 | 0 |
| Quantitative | 0 | 0 |
| Astra | 0 | 0 |

**Lecture au 14/08/2026.** La Section Macro concentre l'intégralité des erreurs, ce qui est attendu — c'est la seule section ayant produit. Le taux d'erreur par production est cependant très élevé : **neuf erreurs sur un seul document, dont six critiques.**

Le mode de défaillance dominant est identifié et unique : **la conclusion précédait le raisonnement.** E-004, E-005, E-007 et E-008 en découlent toutes directement. La sélection des données, la troncature des sources, la contradiction interne et la concentration non déclarée sont quatre symptômes d'une même cause.

C'est ce que le registre est censé révéler, et il l'a révélé dès la première entrée.

---

*Registre ouvert le 14 août 2026. Ne jamais réécrire une entrée existante.*
