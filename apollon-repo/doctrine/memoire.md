# SYSTÈME DE MÉMOIRE — COMMENT L'ÉQUIPE APPREND DE SES ERREURS

**Date :** 14 août 2026
**Objet :** le mécanisme concret par lequel une erreur commise aujourd'hui ne se répète pas dans six mois.

---

# PARTIE I — LE PROBLÈME, ÉNONCÉ SANS DÉTOUR

Je n'ai **aucune mémoire** entre les sessions. Chaque nouvelle session démarre sans le moindre souvenir de la précédente. Ce n'est pas une limitation contournable par une astuce de configuration : c'est le fonctionnement du modèle.

Il n'existe pas non plus d'apprentissage. Un document que vous me donnez ne modifie rien en moi. Aucun entraînement, aucune pondération ajustée, aucune trace persistante.

**Conséquence directe :** sans dispositif externe, l'équipe répète indéfiniment les mêmes fautes. Les neuf erreurs du 14 août reviendraient le 15, le 16, et tous les jours suivants.

**Ce qui fonctionne réellement :** la mémoire n'est pas dans le modèle, elle est **dans des fichiers que le modèle lit avant de travailler**. La distinction n'est pas théorique — elle détermine toute l'architecture.

Fonctionnellement, le résultat est équivalent à de la mémoire. À une condition, et une seule : **les fichiers doivent être lus au début de chaque session.** Un registre que personne ne consulte est un fichier mort.

---

# PARTIE II — L'ARCHITECTURE À TROIS ÉTAGES

| Étage | Emplacement | Contenu | Durée de vie |
|---|---|---|---|
| **1. Mémoire vive** | Session en cours | Raisonnement, calculs intermédiaires | Meurt avec la session |
| **2. Mémoire de travail** | **Projet Claude** | Charte, doctrine, registre des erreurs, calibration, journal | Permanente, accessible partout |
| **3. Mémoire longue** | **Vault Obsidian + `data/history/`** | Bibliothèque, notes de lecture, séries de prix accumulées | Permanente, vous appartient |

## La règle d'arbitrage — une seule question

> **Un agent en a-t-il besoin pour travailler à 2h du matin, alors que votre Mac est éteint ?**
>
> Oui → **Projet**. Non → **Obsidian**.

Cette règle n'est pas cosmétique. L'accès à votre Mac passe par le pont de l'application de bureau, qui exige qu'elle soit ouverte et connectée. Le cycle de 2h du matin s'exécutera pendant que votre machine dort. **Un agent dont la doctrine réside uniquement dans Obsidian se réveillera sans accès à sa propre doctrine.**

---

# PARTIE III — LES QUATRE FICHIERS QUI CONSTITUENT LA MÉMOIRE

## 1. Le registre des erreurs — `registre-erreurs.md`

**Le fichier le plus important du dispositif.**

Chaque erreur y est inscrite avec quatre éléments obligatoires :

- le **fait**, formulé sans atténuation
- la **cause racine** — jamais « inattention », toujours le mécanisme précis
- la **conséquence**, chiffrée quand elle peut l'être
- la **règle** qui en découle, numérotée et exécutable

Le fichier est **immuable** : on ajoute, on ne réécrit jamais. Une erreur reformulée après coup pour paraître moins grave est une leçon détruite.

**Ce que le registre a déjà produit, dès sa première entrée.** Dix erreurs consignées le 14 août, dont six critiques. Et surtout, un mode de défaillance unique identifié : **la conclusion précédait le raisonnement.** Les erreurs E-004 (source tronquée), E-005 (variable omise), E-007 (contradiction interne) et E-008 (pari unique déguisé) ne sont pas quatre problèmes différents — ce sont quatre symptômes d'une même cause.

Aucune de ces quatre erreurs n'aurait été détectée sans le registre. C'est exactement ce qu'il est censé faire.

**La règle des trois occurrences :** une erreur qui réapparaît trois fois cesse d'être une erreur. Elle devient un **défaut structurel du mandat**, et c'est le mandat qui doit être réécrit — pas l'agent qui doit faire attention.

## 2. Le registre de calibration — `registre-calibration.csv`

**Le seul dispositif qui transforme « les agents s'améliorent » en fait vérifiable.**

Chaque affirmation prospective y est inscrite avec une probabilité chiffrée et une date d'échéance. À l'échéance, le résultat est constaté et le score de Brier calculé.

Neuf prédictions sont déjà ouvertes. La première est déjà instructive : **C-003 a dû être marquée `REFORMULÉ`** parce que sa formulation initiale reposait sur un fait faux — la BoJ avait déjà monté ses taux. Une prédiction fondée sur une prémisse erronée n'est pas une prédiction fausse : c'est une prédiction **vide**, et elle doit être distinguée des autres pour ne pas polluer la mesure.

Ce que la mesure révélera dans trois mois, et que rien d'autre ne peut révéler :

- une section **surconfiante** — annonce 80 %, réalise 55 %
- une section qui **n'engage rien** — n'annonce jamais hors de la plage 45–55 %, donc n'apporte aucune information
- une section **compétente sur un domaine et mauvaise sur un autre**, ce qui permet de resserrer son mandat au lieu de la supprimer

**Une contrainte non négociable : le registre ne vaut rien rétroactivement.** Une prédiction inscrite après coup n'est pas une prédiction. Il fallait commencer dès la première production — c'est fait.

## 3. Les fiches de doctrine — `doctrines/<section>.md`

Une fiche par section. Elle contient :

- les **règles** issues du registre des erreurs, applicables à cette section
- les **principes opérationnels** extraits des ouvrages, formulés comme des règles et non comme des résumés
- les **seuils chiffrés** et critères de décision
- les **conditions d'invalidation** — quand la méthode cesse de fonctionner

**Le point critique sur les livres que vous voulez me transmettre :** ne versez jamais un ouvrage brut dans la base. Un PDF de 400 pages produit des extraits décousus et coûte cher à chaque consultation. Un agent ne peut pas appliquer un livre — il peut appliquer une règle.

Le traitement correct : le livre est archivé dans Obsidian comme source de vérification ; sa **fiche de doctrine** de trois à six pages vit dans le Projet. C'est la fiche que l'agent consulte.

## 4. L'historique de données — `data/history/`

La mémoire quantitative, produite par le pipeline. Chaque exécution **fusionne** les nouvelles observations dans les fichiers existants, sans jamais écraser.

C'est ce qui rend possible, au bout de quelques mois : les calculs de VaR et de Sortino sur données réelles, le classificateur de régime avec profondeur historique, les post-mortem chiffrés, et les tests de la Section Quantitative.

`regime_log.csv` accumule une ligne par jour. Après six mois, vous pourrez conditionner n'importe quelle stratégie au régime observé — l'ajout n° 1 de la feuille de route.

---

# PARTIE IV — LE PROTOCOLE, EN QUATRE TEMPS

## Ouverture de session — obligatoire

Tout agent, avant de produire quoi que ce soit :

1. lit le **registre des erreurs** — au minimum les règles R-001 à R-010
2. lit la **fiche de doctrine** de sa section
3. vérifie les **prédictions arrivant à échéance** dans le registre de calibration

Sans cette lecture, l'agent recommence à zéro et le dispositif ne sert à rien.

## Production

- toute affirmation prospective porte une **probabilité chiffrée** et est inscrite au registre de calibration
- tout chiffre porte sa **source et sa date**
- le **contrôle de cohérence interne** est exécuté avant transmission — règle R-007

## Contradiction

Astra attaque. Toute erreur qu'elle détecte est inscrite au registre **le jour même**, avant toute autre suite.

## Clôture — mensuelle

- résolution des prédictions échues, calcul du score de Brier par section
- consolidation des erreurs récurrentes en règles
- réécriture du mandat de toute section dont une erreur atteint trois occurrences
- révision des fiches de doctrine

---

# PARTIE V — CE QUE CE SYSTÈME NE FAIT PAS

**Il ne rend pas le modèle plus intelligent.** Les mêmes capacités, les mêmes angles morts. Ce qui change, c'est que les angles morts sont **documentés**, donc contournables.

**Il ne fonctionne pas tout seul.** Un registre que personne ne lit est un fichier mort. Le dispositif repose entièrement sur la discipline de lecture en ouverture de session. C'est le point de rupture le plus probable de tout le système.

**Il ne remplace pas votre jugement.** Le registre enregistre les erreurs identifiées. Celles que personne ne remarque n'y figurent jamais — et ce sont statistiquement les plus coûteuses.

**Il est asymétrique par construction.** Il capte les erreurs de commission — ce qui a été fait et s'est révélé faux. Il ne capte pas les erreurs d'omission : les opportunités non vues, les positions non prises. C'est une limite structurelle, à garder à l'esprit lors de la lecture des statistiques.

---

# PARTIE VI — ÉTAT AU 14 AOÛT 2026

| Composant | État | Emplacement |
|---|---|---|
| Registre des erreurs | **Actif — 10 entrées, 6 critiques** | Projet |
| Registre de calibration | **Actif — 9 prédictions ouvertes** | Projet |
| Charte fondatrice | Active, corrigée après vérification | Projet |
| Doctrine d'équipe | Active | Projet |
| Feuille de route | Active | Projet |
| Note Astra n° 001 | Archivée | Projet |
| Pipeline de données | **Livré, en attente de clé FRED** | Mac |
| Historique de données | **Vide — première exécution requise** | Mac |
| Fiches de doctrine | **Non créées** | — |
| Vault Obsidian | **Non créé** | — |

**Les deux actions qui débloquent le reste :**

1. Obtenir la clé FRED et lancer `python3 apollon_data.py --history 10 --factors`. L'historique commence à s'accumuler le jour où vous le lancez, jamais avant.
2. Transmettre le premier ouvrage, que je transformerai en fiche de doctrine — ce qui fixera le format pour tous les suivants.

---

*Ne constitue pas un conseil en investissement.*
