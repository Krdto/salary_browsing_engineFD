# Application de Recherche de Salaires

Cette application fournit une interface pour rechercher les salaires annuels moyens et les bonus pour divers intitulés de postes dans différents pays. L'application utilise un fichier Excel pour le stockage des données et offre des fonctionnalités de recherche et de visualisation des salaires via une interface web simple.

## Table des Matières

1. [Installation](#installation)
2. [Dépendances](#dépendances)
3. [Utilisation](#utilisation)
4. [Fonctionnalités](#fonctionnalités)
5. [Points de terminaison de l'API](#points-de-terminaison-de-lapi)

## Installation

Pour installer et exécuter cette application, suivez ces étapes :

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/Krdto/salary_browsing_engineFD.git
   ```
2. Accédez au répertoire du projet :
   ```bash
   cd salary_browsing_engineFD
   ```
3. Installez les dépendances requises :
   ```bash
   pip install -r requirements.txt
   ```
4. Démarrez le serveur Flask :
   ```bash
   python app.py
   ```

## Dépendances

L'application nécessite les packages Python suivants :

- alabaster==0.7.16
- Babel==2.15.0
- beautifulsoup4==4.12.3
- blinker==1.8.2
- certifi==2024.7.4
- charset-normalizer==3.3.2
- click==8.1.7
- colorama==0.4.6
- CurrencyConverter==0.17.25
- docutils==0.21.2
- Flask==3.0.3
- furo==2024.5.6
- idna==3.7
- imagesize==1.4.1
- itsdangerous==2.2.0
- Jinja2==3.1.4
- MarkupSafe==2.1.5
- numpy==2.0.0
- packaging==24.1
- pandas==2.2.2
- Pygments==2.18.0
- python-dateutil==2.9.0.post0
- pytz==2024.1
- rapidfuzz==3.9.4
- requests==2.32.3
- six==1.16.0
- snowballstemmer==2.2.0
- soupsieve==2.5
- Sphinx==7.3.7
- sphinx-basic-ng==1.0.0b2
- sphinxcontrib-applehelp==1.0.8
- sphinxcontrib-devhelp==1.0.6
- sphinxcontrib-htmlhelp==2.0.5
- sphinxcontrib-jsmath==1.0.1
- sphinxcontrib-qthelp==1.0.7
- sphinxcontrib-serializinghtml==1.1.10
- thefuzz==0.22.1
- tzdata==2024.1
- urllib3==2.2.2
- Werkzeug==3.0.3

## Utilisation

Pour utiliser l'application :

1. **Charger les données** : Assurez-vous que le fichier Excel `Conso 2024.xlsx` se trouve dans le répertoire racine.
2. **Exécuter le serveur** : Démarrez le serveur Flask en utilisant la commande fournie dans les étapes d'installation.
3. **Accéder à l'interface web** : Ouvrez un navigateur web et allez à [http://localhost:5000](http://localhost:5000).

## Fonctionnalités

- **Fonction de recherche** : Les utilisateurs peuvent saisir un intitulé de poste pour rechercher des salaires moyens.
- **Nettoyage des données** : Nettoie et filtre automatiquement les données du fichier Excel.
- **Interface interactive** : Interface conviviale avec des résultats de recherche en temps réel.
- **Gestion des erreurs** : Gestion complète des erreurs et journalisation.

## Points de terminaison de l'API

- `GET /`: Route principale qui rend la page d'accueil.
- `POST /search`: Accepte un intitulé de poste et renvoie des données JSON avec des intitulés de postes corrigés et les salaires associés.
