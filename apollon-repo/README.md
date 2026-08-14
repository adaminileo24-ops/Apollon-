# APOLLON — Data center et mémoire du fonds

Ce dépôt **est** la mémoire de l'équipe. Il tourne 24h/24, indépendamment de votre Mac.

---

## Pourquoi ce dépôt existe

Le modèle n'a aucune mémoire entre les sessions et n'apprend rien de façon permanente. La mémoire ne peut donc pas être *dans* l'agent : elle doit être dans des fichiers qu'il lit avant de travailler.

Restait à trouver **où** les mettre. Trois contraintes se combinaient mal :

| Contrainte | Conséquence |
|---|---|
| Le conteneur cloud n'atteint aucune API financière | Testé : Yahoo, Stooq, CoinGecko, FRED, FMP — tous bloqués |
| Le Mac n'est pas allumé la nuit | Le cycle de 2h du matin n'a accès à rien de local |
| Les cycles programmés démarrent des sessions neuves | Aucun état conservé d'une exécution à l'autre |

**GitHub résout les trois simultanément.** Accessible depuis le conteneur cloud — vérifié par clone réel. Toujours en ligne. Et git rend l'historique immuable par construction : on ne peut pas réécrire discrètement un registre d'erreurs sans que le commit le montre.

C'est exactement la propriété qu'on demande à un registre d'erreurs.

---

## Architecture

```
   GitHub Actions                    Ce dépôt                    Session Claude
   (cron 2×/jour)                    (mémoire)                   (à toute heure)
        │                                │                             │
        │  collecte FRED + facteurs      │                             │
        ├───────────────────────────────►│                             │
        │  commit + push                 │                             │
        │                                │◄────────────────────────────┤
        │                                │   git clone au démarrage    │
        │                                │   lit registres + données   │
        │                                │                             │
        │                                │◄────────────────────────────┤
        │                                │   écrit brief, erreurs      │
                                         │
   Mac (optionnel)                       │
        │  IBKR temps réel, analyses     │
        └───────────────────────────────►┘
```

**Le Mac devient facultatif.** GitHub Actions exécute la collecte sur les serveurs GitHub, avec un accès réseau complet. Votre machine peut rester éteinte une semaine : les données continuent d'arriver.

---

## Installation — 10 minutes, une seule fois

### 1. Créer le dépôt

Sur github.com : **New repository** → nom `apollon` → **Private** → Create.

### 2. Pousser ce contenu

```bash
cd ~/Documents/"Section Macro"/apollon
git init
git add .
git commit -m "Apollon — initialisation de la mémoire"
git branch -M main
git remote add origin https://github.com/VOTRE_USER/apollon.git
git push -u origin main
```

### 3. Déclarer la clé FRED en secret

Dépôt → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**

- Name : `FRED_API_KEY`
- Secret : votre clé, obtenue gratuitement sur https://fredaccount.stlouisfed.org/apikeys

### 4. Autoriser les Actions à écrire

Dépôt → **Settings** → **Actions** → **General** → **Workflow permissions** → cocher **Read and write permissions** → Save.

### 5. Premier lancement

Onglet **Actions** → *Apollon — collecte quotidienne* → **Run workflow**.

Deux minutes plus tard, `data/` contient l'instantané, dix ans d'historique sur 23 séries, et les facteurs Fama-French.

### 6. Me donner l'accès en lecture

Créez un **fine-grained personal access token** :
github.com → Settings → Developer settings → Personal access tokens → Fine-grained tokens

- Repository access : **Only select repositories** → `apollon` uniquement
- Permissions : Contents → **Read and write** (lecture seule si vous préférez committer vous-même)
- Expiration : 90 jours

Transmettez-le moi en session. Je clonerai avec :

```bash
git clone https://<token>@github.com/VOTRE_USER/apollon.git
```

**Sur la sécurité :** ce jeton n'ouvre qu'un seul dépôt privé, sans accès à votre compte ni à vos autres projets. Il est révocable en un clic depuis la même page, et expire seul. Ne réutilisez jamais un jeton classique à portée large.

---

## Arborescence

```
apollon/
├── .github/workflows/
│   └── apollon.yml           le data center — cron 2×/jour
├── doctrine/
│   ├── charte_fonds.md       mandat, cadre de risque, calendrier
│   ├── doctrine_equipe.md    hiérarchie, sections, sous-sections
│   ├── professionnalisation.md   écarts techniques et feuille de route
│   └── memoire.md            protocole de mémoire
├── registres/
│   ├── registre_erreurs.md   IMMUABLE — 10 entrées, 6 critiques
│   └── registre_calibration.csv   9 prédictions ouvertes
├── briefs/                   briefs quotidiens et notes Astra
├── pipeline/
│   └── apollon_data.py       collecte, régime, archivage
└── data/
    ├── snapshot_AAAA-MM-JJ.md    instantané lisible
    ├── regime_log.csv            journal du régime, 1 ligne par exécution
    ├── fama_french_5_daily.csv   facteurs
    └── history/                  23 séries, jamais écrasées
```

---

## Le protocole d'ouverture de session

**À me dire au début de chaque session, ou à inscrire dans le prompt des tâches programmées :**

> Clone le dépôt apollon, lis `registres/registre_erreurs.md` et `registres/registre_calibration.csv`, puis travaille.

C'est la seule étape qui fait vivre le dispositif. Un registre que personne ne lit est un fichier mort — c'est le point de rupture le plus probable de tout le système.

---

## Ce que git apporte que rien d'autre n'apporte

**L'immuabilité vérifiable.** Le registre des erreurs doit être un fichier qu'on n'a pas le droit de réécrire. Avec git, ce n'est plus une règle de discipline mais une propriété technique : toute modification d'une entrée existante apparaît dans le diff du commit.

```bash
git log --follow -p registres/registre_erreurs.md
```

Cette commande montre l'intégralité de l'évolution du registre. Une entrée adoucie après coup y est visible. **C'est le seul dispositif du système qui ne repose pas sur la bonne foi.**

---

## Étape suivante — le Mac reprend sa place

Une fois le dépôt en marche, votre Mac sert à ce que GitHub ne peut pas faire :

- **Interactive Brokers** — prix temps réel, chaînes d'options, données intraday. TWS doit tourner localement.
- **Analyses lourdes** — backtests, décomposition factorielle sur l'historique accumulé.
- **Obsidian** — bibliothèque, notes de lecture, graphe de connaissances.

Le Mac pousse ses résultats vers le même dépôt. Le data center reste GitHub.

---

## Coût

| Poste | Coût |
|---|---|
| Dépôt privé GitHub | 0 € |
| GitHub Actions (privé) | 2 000 min/mois offertes — ce workflow en consomme ~120 |
| Données FRED | 0 € |
| Facteurs Fama-French | 0 € |
| **Total** | **0 €** |

Un VPS à 5 €/mois ne deviendra nécessaire que le jour où vous voudrez une collecte IBKR en continu, hors des créneaux du cron.

---

*Document de recherche. Ne constitue pas un conseil en investissement.*
