# FEUILLE DE ROUTE — PROFESSIONNALISATION

## De la structure au fonds réellement opérationnel

**Date :** 14 août 2026
**Objet :** ce qui sépare concrètement votre dispositif actuel d'un fonds professionnel, et l'ordre dans lequel combler l'écart.

---

# PARTIE I — VOTRE AVANTAGE RÉEL

Avant l'outillage, une question de stratégie qui détermine tout le reste.

**Vous ne battrez pas Goldman Sachs sur l'analyse.** Ils ont des centaines d'analystes, des données alternatives, des flux d'ordres clients, des équipes sur place. Chercher à les surpasser sur leur terrain est une impasse.

**Mais vous disposez de six avantages structurels qu'aucun fonds institutionnel ne possède**, et c'est là que réside la totalité de votre edge exploitable :

| Votre avantage | La contrainte institutionnelle correspondante |
|---|---|
| **Aucun rachat de clients** | Un fonds subit des retraits au pire moment et devient vendeur forcé au creux |
| **Aucun indice de référence** | Un gérant qui sous-performe son indice deux trimestres perd son poste — il achète donc ce que tout le monde achète |
| **Le droit d'être 100 % liquide** | Un fonds actions doit rester investi, même quand il n'y a rien à faire |
| **Aucune contrainte de capacité** | Les positions trop petites pour eux vous sont accessibles |
| **Aucun risque de carrière** | Vous pouvez avoir tort et seul, ce qui est la seule manière d'avoir raison et seul |
| **Un horizon illimité** | Ils sont jugés au trimestre. Vous êtes jugé quand vous le décidez |

**Conséquence directe sur la conception du fonds.** Vos stratégies doivent exploiter ces avantages, pas les gaspiller :

- **Arbitrage d'horizon** — acheter ce que les institutions doivent vendre pour des raisons non fondamentales : fin de trimestre, sortie d'indice, dégradation de notation, ventes fiscales de décembre
- **Patience de l'attente** — la capacité à ne rien faire pendant six mois est un actif, pas une défaillance
- **Concentration assumée** — huit positions comprises valent mieux que soixante suivies de loin
- **Événements sous le radar** — situations spéciales trop petites pour intéresser un fonds de plusieurs milliards

Toute stratégie qui vous met en concurrence frontale avec des institutions mieux équipées est à écarter par principe. Le trading intraday appartient à cette catégorie.

---

# PARTIE II — LES CINQ ÉCARTS TECHNIQUES

## Écart 1 — Le biais du survivant

**Le plus grave, et le plus invisible.** Les données gratuites ne contiennent que les sociétés encore cotées aujourd'hui. Enron, Lehman, Wirecard, Nortel ont disparu des bases. Toute stratégie testée sur ces données achète mécaniquement des entreprises dont vous savez déjà qu'elles ont survécu.

Effet mesuré : **surestimation de 1 à 4 points de rendement annuel.** C'est la raison numéro un pour laquelle un backtest amateur donne 18 % par an et le compte réel −3 %.

**Correctif :** base de données sans biais du survivant, incluant les radiations. Norgate Data ou équivalent, environ 70 $ par mois. Il n'existe pas de version gratuite crédible.

## Écart 2 — Les données point-in-time

Les résultats publiés sont révisés. Le PIB, l'emploi, les bénéfices sont corrigés des mois plus tard. Une base actuelle vous donne le chiffre **révisé** — que personne ne connaissait à l'époque.

Tester une stratégie macro sur des données révisées revient à parier en connaissant le résultat. C'est la forme de tricherie la plus courante et la plus involontaire.

**Correctif :** ALFRED, la base point-in-time de la Fed de Saint-Louis — **gratuite**. Pour les fondamentaux d'entreprise, il faut payer.

## Écart 3 — Les coûts de transaction

Un backtest exécute au prix moyen. La réalité facture : écart achat-vente, impact de marché, commissions, coût d'emprunt sur les ventes à découvert, financement des positions à effet de levier.

Ordre de grandeur : une stratégie à rotation quotidienne perd **2 à 5 % par an** en frottement. Un edge brut de 4 % devient une perte nette.

**Correctif :** intégrer un modèle de coûts dès la conception. Règle simple et sévère — une stratégie qui ne survit pas à un coût de 15 points de base par aller-retour est rejetée sans discussion.

## Écart 4 — La décomposition factorielle

**L'écart le plus discriminant entre amateur et professionnel.**

Vous croyez avoir trouvé un edge. Dans neuf cas sur dix, il s'agit d'une exposition déguisée à un facteur connu : marché, taille, valeur, momentum, qualité, faible volatilité. Vous ne gagnez pas d'alpha — vous prenez un risque factoriel rémunéré, accessible pour 0,15 % par an via un ETF.

**Correctif :** régresser systématiquement tout rendement de stratégie contre Fama-French à cinq facteurs augmenté du momentum. Ce qui reste — l'ordonnée à l'origine, l'alpha — est votre contribution réelle. Le reste est du bêta que vous payez cher.

Les données de facteurs sont **gratuites** sur la bibliothèque de Kenneth French. Aucune excuse pour ne pas le faire.

## Écart 5 — Le Sharpe honnête

Un ratio de Sharpe obtenu après avoir testé deux cents variantes n'est pas un ratio de Sharpe : c'est le maximum d'un échantillon de bruit.

**Correctifs — et c'est précisément le domaine de votre Générale De Prado :**

- **Deflated Sharpe Ratio** — corrige du nombre d'essais effectués
- **Probability of Backtest Overfitting** — probabilité que la stratégie soit un artefact
- **Longueur minimale de track record** — durée nécessaire pour distinguer compétence et chance

Règle opérationnelle : **le nombre de configurations testées est consigné avant de commencer.** Sans ce compte, aucune correction n'est possible et tout résultat est ininterprétable.

---

# PARTIE III — HUIT AJOUTS QUI ÉLÈVENT LE DISPOSITIF

## 1. Le classificateur de régime — conditionner au lieu de moyenner

La mauvaise question : *« cette stratégie fonctionne-t-elle ? »*
La bonne question : *« dans quel régime fonctionne-t-elle, et sommes-nous dans ce régime ? »*

Une stratégie momentum est excellente en marché de tendance et destructrice en marché sans direction. Sa performance moyenne toutes périodes confondues ne veut rien dire.

**Construction — quatre axes, huit à douze régimes :**

| Axe | Mesure | Seuils |
|---|---|---|
| Volatilité | VIX | < 15 / 15–25 / > 25 |
| Courbe | Pente 2s10s | Inversée / plate / pentue |
| Tendance | S&P vs MM200 | Au-dessus / en dessous |
| Crédit | Spread haut rendement | Resserrement / élargissement |

Chaque stratégie porte une carte de performance par régime. On ne déploie que dans les régimes favorables.

*Application immédiate — régime actuel : VIX 14,6 (bas), courbe +48 pb (pentue), S&P au-dessus de sa MM200. Régime « expansion complaisante ». Le momentum y fonctionne ; le retour à la moyenne y échoue.*

## 2. Le fichier des morts

Registre de toutes les stratégies testées et **rejetées**, avec la raison du rejet.

Personne ne tient ce fichier, et tout le monde retombe donc sur les mêmes impasses tous les huit mois. Il vaut avec le temps plus cher que le registre des stratégies retenues : il rétrécit continuellement l'espace de recherche.

## 3. Le pré-mortem écrit — avant l'entrée

Avant toute position significative, Astra rédige le récit suivant :

> *« Nous sommes trois mois plus tard. Cette position a perdu 20 %. Voici précisément ce qui s'est passé. »*

Écrit **avant** l'entrée, jamais après. La recherche en psychologie de la décision est constante sur ce point : la projection dans un échec déjà advenu révèle des risques que l'analyse prospective classique ne fait jamais apparaître.

## 4. Le registre d'espérance

Chaque position porte une espérance mathématique annoncée à l'entrée. Chaque clôture inscrit le résultat réalisé.

Au bout de trente positions, la comparaison entre espérance annoncée et espérance réalisée dit tout — et notamment la seule chose qui compte : **votre processus a-t-il un avantage, ou avez-vous eu de la chance ?**

C'est le score de calibration transposé à l'argent.

## 5. Le dimensionnement ajusté de la liquidité

La volatilité seule ne suffit pas. Une position doit également respecter un plafond de participation au volume quotidien moyen — au-delà, vous ne pouvez plus sortir au prix affiché.

Règle : **jamais plus de 1 % du volume quotidien moyen sur vingt séances.** Cette contrainte est peu mordante à votre taille, mais l'inscrire maintenant évite d'avoir à y penser plus tard.

## 6. Le moniteur de corrélation

Mesure quotidienne : corrélation moyenne entre toutes les paires de positions du portefeuille.

Tant qu'elle reste sous 0,3, la diversification est réelle. Au-dessus de 0,6, vous détenez une seule position répartie sur plusieurs lignes. C'est l'indicateur qui prévient avant que le portefeuille ne se révèle beaucoup moins diversifié qu'il n'en avait l'air.

## 7. La lettre mensuelle à l'investisseur

Rédigez chaque mois une lettre à un investisseur imaginaire, expliquant vos décisions et vos résultats.

Le dispositif paraît artificiel. Il est d'une efficacité redoutable : il est presque impossible d'écrire *« j'ai perdu 8 % ce mois-ci »* sans confronter honnêtement la raison. La lettre est le plus puissant instrument anti-complaisance disponible, et il est gratuit.

## 8. La politique de couverture permanente

Plutôt que de décider au cas par cas, fixez une règle conditionnée au régime :

| VIX | Politique de couverture |
|---|---|
| < 15 | Achat systématique de protection — elle est bon marché |
| 15–25 | Couverture opportuniste |
| > 25 | Aucun achat de protection — trop chère. Vente de volatilité envisageable |

*Le VIX est à 14,64. La règle s'applique **aujourd'hui**.* Acheter la protection quand elle est chère, c'est-à-dire après le choc, est l'erreur la plus universelle du métier.

---

# PARTIE IV — INFRASTRUCTURE DE DONNÉES

## 4.1 Constat technique

| Source | Statut depuis le conteneur cloud | Testé |
|---|---|---|
| yfinance / Yahoo | **Bloqué** | ✗ |
| Stooq, CoinGecko, FRED, FMP | **Bloqués** | ✗ |
| Pages de cotation via recherche web | **Fonctionne** | ✓ |
| OpenBB, TWS Interactive Brokers | Nécessite l'exécution sur votre Mac | — |

Les cotations du tableau de bord proviennent de la dernière ligne. C'est suffisant pour la macro, le régime et le swing. Ce n'est pas suffisant pour la Section Quantitative.

## 4.2 Stack recommandée, par ordre de rapport valeur/coût

| Priorité | Source | Coût | Ce que cela débloque |
|---|---|---|---|
| **1** | **FRED + ALFRED** (clé gratuite) | 0 € | Toute la macro, en version point-in-time |
| **2** | **API Interactive Brokers** (vous l'avez) | 0 € | Prix temps réel, chaînes d'options, exécution |
| **3** | **Bibliothèque Kenneth French** | 0 € | Décomposition factorielle — indispensable |
| **4** | **OpenBB** (installé) | 0 € | Agrégation, fondamentaux |
| **5** | Norgate Data | ~70 $/mois | Historique actions sans biais du survivant |
| **6** | Polygon ou Databento | 30–200 $/mois | Données tick, historique d'options |

**Les quatre premières lignes sont gratuites et déjà en votre possession.** Elles couvrent l'essentiel de ce qui manque. C'est le chantier prioritaire, avant toute autre chose.

---

# PARTIE V — ORDRE D'EXÉCUTION

| Phase | Durée | Contenu | Critère de passage |
|---|---|---|---|
| **1. Données** | 1–2 sem. | FRED, IBKR, French. Un script consolidé produisant un instantané de marché reproductible | Le script tourne sans intervention |
| **2. Macro seule** | 2 sem. | Brief quotidien uniquement. Rien d'autre | 10 briefs consécutifs que vous lisez réellement |
| **3. Risque** | 1 sem. | Classificateur de régime, VaR, moniteur de corrélation | Rapport de risque quotidien produit |
| **4. Astra** | 1 sem. | Contradiction, pré-mortem, score de calibration | 5 contradictions ayant modifié une conclusion |
| **5. Trading** | 2 sem. | Swing uniquement. Papier. Registre d'espérance | 10 idées passant le seuil des six critères |
| **6. Quantitative** | 4 sem. | Tests avec Deflated Sharpe et décomposition factorielle | 1 stratégie survivant à la correction |
| **7. Capital réel** | — | Après 3 mois de suivi virtuel complet | Score de calibration mesuré et acceptable |

**La phase 1 conditionne tout.** Sans données, les phases 3 et 6 produisent une simulation de travail — le résultat le plus dangereux qui soit, parce qu'il en a toutes les apparences.

---

# PARTIE VI — CE QUI TUE LES FONDS

Par fréquence décroissante, d'après l'historique du métier :

1. **Le levier appliqué à une position juste au mauvais moment.** LTCM avait raison sur ses convergences. Ils ont fait faillite avant qu'elles ne se réalisent.
2. **La concentration non intentionnelle.** Vingt positions différentes exposées au même facteur.
3. **Le renforcement sur thèse invalidée.** Confondre conviction et entêtement.
4. **Le surapprentissage.** La stratégie fonctionnait parfaitement — dans le passé, sur lequel elle avait été optimisée.
5. **L'illusion de liquidité.** Sortable en temps normal, impossible à vendre le jour où c'est nécessaire.
6. **La dérive de mandat.** Le fonds macro qui se met à faire du capital-risque parce que la macro ne payait plus.
7. **Le sur-trading.** Mille décisions à espérance légèrement négative après frais.

Votre cadre de risque traite les points 1 à 3 et 7. Le point 4 relève de De Prado. Le point 5 exige la contrainte de liquidité. **Le point 6 est le vôtre** — aucun agent ne peut vous empêcher de changer de mandat.

---

# PARTIE VII — L'ÉVALUATION HONNÊTE

**Ce que ce dispositif peut réellement atteindre :** un processus discipliné, traçable, avec un cadre de risque appliqué mécaniquement et une mesure honnête de sa propre qualité. C'est déjà supérieur à la pratique de la grande majorité des investisseurs particuliers, dont la faiblesse n'est pas l'intelligence mais l'absence de processus.

**Ce que ce dispositif ne fera pas :** produire du rendement par sa seule existence. La structure ne crée pas d'alpha. Elle empêche de le détruire — ce qui est différent, et suffisant pour justifier de la construire.

**Le risque principal, et il n'est pas technique :** un organigramme élégant procure un sentiment de maîtrise que les résultats ne confirment pas nécessairement. Onze entités, vingt sous-sections, une hiérarchie ordonnée — tout cela produit la sensation de diriger un fonds. La sensation n'est pas le fonds.

Ce qui distinguera votre dispositif d'un jeu de rôle sophistiqué tient en trois points, et trois seulement :

1. **Le score de calibration existe et est mesuré** — sinon vous ne saurez jamais si le système fonctionne
2. **Le veto de Risque est respecté quand il est contrariant** — il ne sera testé que le jour où il vous empêchera de prendre la position dont vous êtes le plus certain
3. **La phase 1 est terminée avant les autres** — sinon tout le reste est décoratif

---

*Feuille de route — 14 août 2026*
*Ne constitue pas un conseil en investissement.*
