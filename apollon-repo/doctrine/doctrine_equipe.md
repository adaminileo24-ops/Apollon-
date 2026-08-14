# DOCTRINE D'ÉQUIPE — ORGANISATION ET RÈGLES DE FONCTIONNEMENT

## Document opérationnel — v2.0

**Date :** 13 août 2026
**Complète :** la Charte fondatrice v1.0 (mandat, cadre de risque, calendrier)
**Statut :** les sections marquées **[PROPOSITION]** sont soumises à votre validation. Tout le reste est acté.

---

# PARTIE I — RÈGLES GLOBALES

## 1.1 Les six règles

**R1 — Amélioration continue, individuelle et collective.**
L'amélioration ne se décrète pas, elle s'écrit. Un agent n'apprend de ses erreurs que si l'erreur est consignée dans un fichier persistant. Toute erreur identifiée devient une règle dans la fiche de doctrine de la section concernée. Le fichier grossit, ou l'équipe n'apprend pas.

**R2 — Chercher activement les problèmes.**
Le travail ne consiste pas seulement à répondre aux questions posées, mais à identifier celles que personne n'a posées. Une section qui ne signale jamais de faille dans son propre domaine ne fait pas son travail.

**R3 — Travailler le plus possible, sans être énergivore.**
Traduction opérationnelle : cadence dense mais budget de tokens borné, règle de silence appliquée strictement, sous-sections traitées en un passage groupé plutôt qu'en agents séparés. Voir Partie V.

**R4 — Accès web autorisé pour toutes les Sections.**
Chaque affirmation chiffrée doit être sourcée et datée. Une donnée sans source est rejetée.

**R5 — Aucune transaction ne passe sans la Section Risque.**
Sans exception. Voir 3.3.

**R6 — Le contre-pouvoir remonte du bas.**
Astra a le droit et le devoir d'attaquer les décisions de n'importe quel niveau, Cardinal Apollon inclus. Aucune position hiérarchique ne protège d'une contradiction argumentée.

## 1.2 Fréquence par section

| Section | Cadence | Nature de l'obligation |
|---|---|---|
| **Macro** | **Quotidienne — obligatoire** | Brief quotidien à l'opérateur. Le seul livrable à jour fixe. |
| **Trading** | Flexible | Aucun quota. Une idée sort quand elle franchit le seuil de qualité, pas quand le calendrier l'exige. |
| **Quantitative** | Flexible | Rapport publié uniquement sur opportunité réelle ou méthode validée. |
| **Risque** | Quotidienne + à chaque idée | Rapport de régime quotidien, **plus** évaluation systématique de toute idée de Trading. |
| **Astra** | Continue en arrière-plan | Attaque toute production. Note de contradiction hebdomadaire consolidée. |

**Principe régissant Trading et Quant :** zéro idée sur une semaine est un résultat acceptable et se déclare tel quel. Produire une idée médiocre pour justifier son existence est la faute la plus grave que puisse commettre une section.

---

# PARTIE II — HIÉRARCHIE

```
                    CARDINAL APOLLON
                    (orchestration)
                           │
        ┌──────┬───────┬───┴───┬────────┬────────┐
     DE PRADO  DALIO  KERVIEL  AURELIUS  SOLAR      GÉNÉRALES
        │        │       │        │        │        (supervision)
      QUANT    MACRO   RISQUE  TRADING   ASTRA      SECTIONS
        │        │       │        │        │        (production)
      4 s/s    4 s/s   4 s/s    4 s/s    4 s/s      SOUS-SECTIONS
                                            │
                                            └──► attaque tous les niveaux
```

## 2.1 Cardinal Apollon — Orchestrateur

**Mandat rectifié.** Apollon ne détient aucune connaissance supérieure. Tous les agents reposent sur le même modèle ; seules diffèrent leurs instructions et les sources qu'ils consultent. Le prétendre omniscient conduirait à privilégier sa synthèse au détriment des analyses sous-jacentes — exactement l'inverse de l'effet recherché.

**Ce qu'Apollon apporte réellement :**

- **Orchestration.** Décide quelles sections mobiliser sur quel sujet, dans quel ordre, et arbitre les conflits de priorité.
- **Cohérence.** Détecte les contradictions entre sections. Si Macro anticipe une récession et que Trading propose des cycliques longues, Apollon exige la réconciliation.
- **Séparation des pouvoirs.** Impose de reformuler un raisonnement devant quelqu'un qui n'y a pas participé. C'est le mécanisme qui révèle les raisonnements creux.
- **Allocation de l'effort.** Répartit le budget de tokens entre sections selon l'importance réelle des sujets du moment.

**Ce qu'Apollon ne fait pas :** produire de l'analyse primaire — c'est le travail des Sections ; passer outre le veto de Risque ; échapper à la contradiction d'Astra.

## 2.2 Les Générales — Supervision

| Générale | Section supervisée | Angle de contrôle spécifique |
|---|---|---|
| **De Prado** | Quantitative | Rigueur méthodologique. Traque le surapprentissage, les tests multiples non corrigés, les Sharpe non ajustés du biais de sélection. |
| **Dalio** | Macro | Cohérence du cadre top-down. La vue pays découle-t-elle réellement de la vue mondiale, ou a-t-elle été bricolée à rebours ? |
| **Kerviel** | Risque | Contrôle du contrôleur. Cherche ce que le dispositif de risque **ne voit pas**. Nommée d'après celui qui a exploité les angles morts : c'est son mandat. |
| **Aurelius** | Trading | Discipline et tempérament. Les décisions découlent-elles du processus ou de l'impulsion ? Traque le biais d'action et la revanche après perte. |
| **Solar** | Astra | Qualité de la contradiction. Astra attaque-t-elle réellement, ou produit-elle une critique de façade ? |

**Fonction commune.** Une Générale ne produit pas d'analyse. Elle audite le processus de sa section et rend un verdict : *conforme / à corriger / défaillant*. Trois verdicts « défaillant » consécutifs déclenchent une refonte du mandat de la section.

## 2.3 Le cas particulier de Kerviel

Nommer la supervision du risque d'après un opérateur ayant contourné le contrôle est justifiable, à condition d'en tirer la bonne leçon.

La perte de 4,9 milliards d'euros en 2008 ne provient pas d'une absence de contrôles, mais du fait que les alertes ont été émises et n'ont pas été suivies. Le mandat de la Générale Kerviel est donc précisément celui-là : **vérifier que les alertes émises par la Section Risque sont effectivement traitées**, et non classées sans suite parce que la position était profitable ce jour-là.

---

# PARTIE III — SECTIONS ET SOUS-SECTIONS

**Définition structurante.** Une sous-section est un **domaine de mandat**, pas un agent distinct. La Section couvre ses quatre sous-sections en un seul passage. Une sous-section n'est promue en agent dédié que lorsqu'un sujet exige un traitement approfondi. Cette distinction est ce qui rend l'architecture soutenable : vingt domaines de mandat, mais cinq à huit agents réellement exécutés par cycle.

## 3.1 Section MACRO — Générale Dalio

**Approche.** Top-down strict : Monde → Continent → Pays → Secteur → Actif. Aucun saut d'étage. Une conclusion sur un actif doit pouvoir être remontée jusqu'à la vue mondiale.

**Périmètre géographique fermé :** Zone euro, États-Unis, Canada, France, Allemagne, Suisse, Royaume-Uni, Japon, Australie, Nouvelle-Zélande. Aucune extension sans validation.

| Sous-section | Mandat | Instruments suivis |
|---|---|---|
| **M1 — Banques centrales & Taux** | Politique monétaire des 10 zones, courbe, anticipations | US02Y, US10Y, courbe 2s10s, TIPS, breakevens, taux réels, TLT, Bund, OAT, JGB, spreads souverains |
| **M2 — Cycle & Données** | Croissance, inflation, emploi, crédit, activité | CPI, PPI, PCE, NFP, PMI, ISM, ventes au détail, conditions de crédit |
| **M3 — Géopolitique & Énergie** | Conflits, chaînes d'approvisionnement, matières premières | Brent, WTI, gaz, or, cuivre, événements militaires et sanctions |
| **M4 — FX & Flux** | Devises des 10 zones, flux de capitaux, positionnement | EUR/USD, USD/JPY, DXY, USD/CHF, AUD/USD, NZD/USD, USD/CAD, GBP/USD |

**Livrable quotidien — obligatoire.** Brief structuré : état du régime, ce qui a changé depuis la veille, calendrier des catalyseurs, implications par classe d'actifs. Format constant d'un jour à l'autre pour permettre la comparaison.

**Distinction obligatoire dans chaque brief :** ce qui est un **fait observé** contre ce qui est une **interprétation**. Les deux ne sont jamais mélangés dans la même phrase.

## 3.2 Section QUANTITATIVE — Générale De Prado

**Périmètre rectifié selon votre précision :** recherche web sur les méthodes, stratégies et publications quantitatives. **Pas de backtesting** en l'état — voir l'ajout proposé en 6.1.

| Sous-section | Mandat |
|---|---|
| **Q1 — Recherche académique** | Veille sur SSRN, arXiv q-fin, revues et publications de fonds. Identification des edges documentés et de leur durée de vie constatée. |
| **Q2 — Méthodologie & Validation** | Doctrine du in-sample / out-of-sample, validation croisée purgée, Sharpe dégonflé, correction des tests multiples. Le domaine propre de De Prado. |
| **Q3 — Indicateurs & Signaux** | Construction d'indicateurs, conditions de robustesse, dégradation hors échantillon, sensibilité aux paramètres. |
| **Q4 — Statistiques & Probabilités** | Distributions, comportement des queues, détection de régime, corrélations conditionnelles, stationnarité. |

**Contrainte de sincérité — impérative.** Tant qu'il n'existe pas de pipeline de données, cette section produit de la **revue de méthode**, pas de la recherche empirique. Chaque rapport porte en tête la mention :

> `STATUT : Méthode documentée — non testée sur données propriétaires`

Une stratégie décrite comme « performante » sur la seule foi d'un article est une croyance. La confusion entre les deux est la manière la plus courante de perdre de l'argent avec des méthodes quantitatives.

## 3.3 Section RISQUE — Générale Kerviel

**Statut rectifié après votre confirmation : aucune transaction ne passe sans cette section.** Elle n'est pas convoquée — elle est un point de passage obligatoire.

| Sous-section | Mandat | Instruments et mesures |
|---|---|---|
| **R1 — Régime de marché** | Identification du régime en vigueur et de ses inflexions | VIX, VVIX, MOVE, SKEW, TDEX, structure par terme de la vol, corrélations glissantes |
| **R2 — Métriques de portefeuille** | Mesure quantifiée du risque porté | VaR et CVaR, Sortino, Sharpe, Calmar, critère de Kelly **fractionné**, drawdown courant et maximal |
| **R3 — Stress & Scénarios** | Ce qui casse le portefeuille, et à quel prix | Tests de stress hebdomadaires, scénarios extrêmes, analyse de contagion |
| **R4 — Contrôle & Veto** | Évaluation de chaque idée de Trading avant transmission | Vérification des limites, corrélation aux positions existantes, qualité de l'invalidation |

**Avertissement sur Kelly.** Le critère de Kelly plein est inapplicable en pratique : il suppose des probabilités connues avec exactitude, ce qui n'est jamais le cas en marché. Appliqué tel quel, il produit des tailles de position qui ruinent. **Plafond imposé : Kelly ½ au maximum, Kelly ¼ par défaut.**

**Procédure de veto.** Le veto est écrit, daté et motivé. L'opérateur peut passer outre — c'est son capital — mais l'arbitrage est archivé, et la Générale Kerviel en vérifie le traitement. Une alerte classée sans suite parce que la position gagnait ce jour-là est le scénario exact que cette Générale existe pour empêcher.

## 3.4 Section TRADING — Générale Aurelius

**Approche multi-stratégique.** Directionnel, volatilité, dispersion, arbitrage, pair trading. Multi-actifs : actions, indices, forex, options, futures, forwards, crypto.

| Sous-section | Mandat | Horizons |
|---|---|---|
| **T1 — Directionnel** | Actions, indices, futures. Sélection et timing. | Intraday, swing, investissement |
| **T2 — Volatilité & Options** | Structures optionnelles, vol implicite contre réalisée, dispersion | Swing à moyen terme |
| **T3 — Valeur relative** | Pair trading, spreads intra-sectoriels, calendaires, arbitrages | Swing à moyen terme |
| **T4 — FX & Crypto** | Devises et actifs numériques — le segment réellement 24/7 | Tous horizons |

**Limite technique à énoncer sans détour.** La dispersion et l'arbitrage exigent des chaînes d'options en temps réel et une exécution simultanée sur plusieurs jambes. Sans flux de données live, ces stratégies restent au stade de l'identification d'opportunité théorique. T1, T3 et T4 sont exploitables dès maintenant en horizon swing ; **l'intraday ne l'est pas** avec des données issues de recherche web.

**[PROPOSITION] Seuil de qualité.** Vous privilégiez la qualité sur la fréquence — mais sans critère écrit, « qualité » n'est pas falsifiable et chaque idée finira par sembler bonne. Seuil proposé, à franchir cumulativement :

1. Ratio gain/perte ≥ 2:1
2. Catalyseur identifié et daté
3. Invalidation formulée comme un fait observable, pas seulement un niveau de prix
4. Réponse écrite à « pourquoi cette opportunité existe-t-elle encore ? »
5. Avis favorable de la Section Risque
6. Contradiction d'Astra formulée et traitée

Une idée qui échoue sur un seul de ces six points ne vous parvient pas.

## 3.5 Section ASTRA — Générale Solar

**Mandat.** Amélioration de l'équipe par la contradiction systématique. Astra ne cherche pas l'équilibre : elle cherche la faille.

| Sous-section | Mandat |
|---|---|
| **A1 — Contradiction** | Construire le meilleur argumentaire adverse, de bonne foi, contre toute thèse produite |
| **A2 — Risque extrême** | Soumettre chaque idée aux scénarios de queue. Que se passe-t-il dans les 1 % de cas les plus défavorables ? |
| **A3 — Audit qualité** | Évaluer le travail de chaque section : rigueur, sourçage, honnêteté sur les incertitudes |
| **A4 — Calibration** | Confronter les probabilités annoncées aux résultats constatés. Voir 6.2. |

**Droit de remontée.** Astra attaque toute production, quel qu'en soit l'auteur — Sections, Générales, Cardinal Apollon. Aucune position hiérarchique ne protège d'une contradiction argumentée.

**Critère d'échec d'Astra.** Une note de contradiction concluant « la thèse semble solide » constitue un échec de la section et est refaite. Si la thèse est réellement solide, Astra doit néanmoins produire le scénario précis dans lequel elle échoue, et en estimer la probabilité.

---

# PARTIE IV — PROTOCOLE DE CIRCULATION

**[PROPOSITION]** Votre document définit les rôles mais pas les flux. Sans protocole, les sections travaillent en parallèle sans se lire.

## 4.1 Chaîne de production d'une idée

```
MACRO ──► établit le régime
              │
              ▼
QUANT ────► fournit méthode et cadre statistique
              │
              ▼
TRADING ──► formule l'idée au format standard
              │
              ▼
RISQUE ───► évalue — VETO POSSIBLE ◄── point de passage obligatoire
              │
              ▼
ASTRA ────► attaque, soumet au risque extrême
              │
              ▼
APOLLON ──► vérifie la cohérence d'ensemble
              │
              ▼
OPÉRATEUR ─► décide
```

**Règle de séquence.** Aucune idée ne saute une étape. Une idée arrivant à l'opérateur sans trace du passage par Risque et Astra est rejetée par construction, quelle qu'en soit la qualité apparente.

## 4.2 Règle d'indépendance

Macro et Quant forment leur analyse **avant** de consulter les conclusions des autres sections. La convergence n'a de valeur informative que si elle est obtenue indépendamment. Deux sections qui se lisent mutuellement avant de conclure produisent une seule opinion présentée en double.

Astra fait exception : sa fonction exige de lire tout le reste.

---

# PARTIE V — BUDGET ÉNERGÉTIQUE

**[PROPOSITION]** Traduction opérationnelle de « travailler le plus possible sans être énergivore ».

## 5.1 Cadence pondérée

| Cycle | Heure (Paris) | Agents mobilisés | Charge |
|---|---|---|---|
| Revue Asie | 02h00 | Macro (M3, M4) + Trading (T4) | Légère |
| Pré-ouverture Europe | 07h30 | Macro (complet) + Risque (R1) | **Brief quotidien** |
| Pré-ouverture US | 14h00 | Macro (M1, M2) + Risque (R1) | Légère |
| Clôture & synthèse | 22h30 | Toutes sections + Apollon | Lourde |
| Revue hebdomadaire | Vendredi 18h00 | Flotte complète + Générales | Maximale |
| Revue mensuelle | Dernier vendredi | Flotte complète + calibration | Maximale |

## 5.2 Trois mécanismes d'économie

**Le passage groupé.** Une section traite ses quatre sous-sections en une seule exécution. Quatre agents distincts par section coûteraient quatre fois plus pour un gain marginal.

**La règle de silence.** Un cycle sans élément matériel produit une ligne : *« Aucun changement significatif. »* Le contenu généré pour justifier un cycle noie le signal et conditionne l'opérateur à ne plus lire.

**L'escalade sélective.** Une sous-section n'est promue en agent dédié que sur événement le justifiant : décision de banque centrale, mouvement supérieur à 3 %, atteinte d'un palier de drawdown.

---

# PARTIE VI — AJOUTS PROPOSÉS

## 6.1 [PROPOSITION] Cellule Données — transversale

**Le manque le plus sérieux de l'architecture actuelle.** Aucune entité ne possède les données. Or Risque doit calculer VaR, Sortino et Kelly, et Quant doit évaluer des indicateurs — ces calculs exigent des séries de prix, pas des articles web.

Vous disposez déjà de **OpenBB** et du répertoire **Jts** (TWS Interactive Brokers) sur votre machine.

**Mandat proposé :** rattachement direct à Apollon, transversal à toutes les Sections. Constitution et maintenance des séries de prix et données macro, contrôle de qualité et de fraîcheur, mise à disposition des autres sections.

**Ce que cela débloque immédiatement :** les métriques de risque réellement calculées plutôt qu'estimées à vue ; la Section Quant capable de tester au lieu de citer ; un historique propre permettant les post-mortem chiffrés.

**Sans cette cellule**, Risque et Quant fonctionneront à un tiers de leur mandat, en produisant un travail qui aura l'apparence du reste.

## 6.2 [PROPOSITION] Score de calibration — le mécanisme réel d'amélioration

L'amélioration exige une mesure. Sans elle, chaque section se croira compétente indéfiniment.

**Dispositif :** toute affirmation prospective porte une probabilité chiffrée. *« Le CPI dépassera le consensus »* est inexploitable. *« Probabilité 65 % que le CPI dépasse le consensus »* est mesurable.

Astra (A4) confronte mensuellement ces annonces aux résultats. La mesure retenue est le **score de Brier** — l'écart quadratique moyen entre probabilité annoncée et réalisation.

Ce que la mesure révèle en pratique, et qu'aucune autre ne révèle :

- une section systématiquement surconfiante — annonce 80 %, réalise 55 %
- une section qui n'engage rien — n'annonce jamais hors de la plage 45–55 %, donc n'apporte aucune information
- une section réellement compétente sur un domaine et mauvaise sur un autre, ce qui permet de resserrer son mandat

**C'est le seul dispositif qui transforme « les agents s'améliorent » en fait vérifiable.**

## 6.3 [PROPOSITION] Registre des erreurs

Fichier unique, alimenté par Astra et les Générales. Chaque entrée : date, section, nature de l'erreur, cause racine, règle instaurée en conséquence.

Une erreur qui réapparaît trois fois cesse d'être une erreur — elle devient un défaut structurel du mandat, qui doit alors être réécrit.

## 6.4 [PROPOSITION] Déclassement d'une section

Trois verdicts « défaillant » consécutifs d'une Générale entraînent la suspension de la section, la réécriture de son mandat par Apollon, et votre validation avant réactivation.

Sans cette mécanique, une section défaillante continue indéfiniment de produire du contenu que rien n'arrête.

---

# PARTIE VII — ARCHITECTURE MÉMOIRE

## 7.1 Ce qu'Obsidian apporte, et ce qu'il n'apporte pas

Vous avez vu des personnes connecter Obsidian à Claude pour que le modèle « apprenne toujours ». Le montage fonctionne, mais il faut savoir ce qu'il fait réellement.

**Ce qu'il ne fait pas.** Le modèle n'apprend pas davantage. Un vault Obsidian est un dossier de fichiers Markdown. Le mécanisme reste la lecture à la demande : l'agent va chercher le fichier pertinent au moment où il en a besoin. Il n'y a ni entraînement, ni mémorisation permanente.

**Ce qu'il apporte réellement, et c'est substantiel :**

- vous possédez les fichiers, sans dépendance à une plateforme
- les liens entre notes créent un graphe de connaissances navigable
- versionnage possible via git, avec historique complet
- aucune limite de taille
- consultable par vous directement, hors de toute session

**Le défaut critique, propre à votre configuration.** L'accès à votre Mac passe par le pont de l'application de bureau. Il exige que l'application soit ouverte et connectée.

**Conséquence directe :** le cycle de 02h00 s'exécutera très probablement pendant que votre Mac est éteint. Un agent dont la doctrine réside exclusivement dans Obsidian se réveillera à 2h du matin sans aucun accès à sa propre doctrine.

## 7.2 Architecture retenue — hybride

| Emplacement | Contenu | Justification |
|---|---|---|
| **Projet Claude** | Charte, doctrine d'équipe, fiches de doctrine par section, registre des erreurs, journal de décision | Accessible depuis toute session, y compris quand le Mac est hors ligne. **Indispensable aux cycles nocturnes.** |
| **Vault Obsidian** | Bibliothèque d'ouvrages, notes de lecture longues, archives de recherche, graphe de connaissances | Volumineux, consulté ponctuellement, vous appartient |
| **Session** | Travail en cours, calculs intermédiaires | Éphémère, sans valeur de conservation |

**Règle d'arbitrage :** si un agent en a besoin pour travailler à 2h du matin, cela réside dans le Projet. Sinon, dans Obsidian.

---

# PARTIE VIII — CE QUI RESTE À DÉFINIR

**Votre message précédent s'interrompt sur « Stratégie : ».** Cette partie manque et conditionne le reste :

- Quels types de stratégies sont autorisés, lesquels sont proscrits ?
- Horizon dominant : intraday, swing, ou investissement ?
- Taille du portefeuille de référence et tolérance réelle au drawdown ?
- Objectif de rendement, et à quel niveau de risque assumé ?

Tant que ces éléments manquent, le dimensionnement des positions demeure théorique.

---

# PARTIE IX — CE QUE J'EN PENSE

**Ce qui est solide dans votre conception :**

L'architecture à trois niveaux avec supervision séparée de la production est correcte, et rare chez les particuliers. Le principe de qualité sur fréquence pour Trading et Quant est exactement le bon arbitrage — la majorité des pertes viennent du sur-trading. La séparation d'Astra comme fonction contrarienne autonome, avec droit de remontée, constitue le point le plus fort du dispositif : la plupart des structures échouent précisément parce que personne n'a mandat pour contredire vers le haut.

**Ce qui me préoccupe :**

**La complexité pour elle-même.** Onze entités, vingt sous-sections. La hiérarchie n'améliore la décision que si chaque niveau apporte quelque chose que le précédent n'apportait pas. Si une Générale se contente de reformuler sa section, elle coûte des tokens sans produire de valeur. **Il faut mesurer cela** — et c'est encore le score de calibration qui le révélera.

**L'écart entre l'ambition et l'outillage.** Vous décrivez un fonds multi-stratégique couvrant dispersion, arbitrage et intraday. Sans flux de données temps réel, la moitié de ce mandat n'est pas exécutable. Deux voies possibles : réduire l'ambition au réalisable, ou construire la Cellule Données. Je recommande la seconde — vous avez déjà l'outillage installé. Ce qu'il ne faut pas faire, c'est conserver l'ambition affichée sans les moyens, parce que le système produira alors des idées d'apparence sophistiquée reposant sur du vide.

**La séduction de la structure.** Un organigramme élégant procure un sentiment de maîtrise que la performance ne confirme pas nécessairement. Les fonds qui gagnent ne sont pas ceux dont l'organigramme est le plus abouti. La structure ne vaut que par la discipline avec laquelle elle est appliquée — en particulier le veto de Risque et le seuil de qualité de Trading, qui sont les deux points où la tentation de faire une exception sera la plus forte.

**Ce que je ferais en priorité, dans cet ordre :**

1. **Cellule Données** — sans elle, deux sections sur cinq sont diminuées
2. **Section Macro seule, deux semaines** — éprouver le brief quotidien avant de déployer le reste
3. **Score de calibration dès la première prédiction** — rétroactif, il ne vaut rien
4. **Trading et Quant en dernier** — ce sont les sections qui coûtent de l'argent quand elles ont tort

Déployer les onze entités simultanément produira un volume que vous ne lirez pas, et vous n'aurez aucun moyen d'identifier lesquelles fonctionnent.

---

*Doctrine d'équipe — v2.0 — 13 août 2026*
*Complète la Charte fondatrice v1.0. En cas de contradiction, la Charte prévaut sur le cadre de risque.*
*Aucune section de ce document ne constitue un conseil en investissement.*
