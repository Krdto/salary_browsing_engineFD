# Application de Recherche de Salaires

Cette application fournit une interface pour rechercher les salaires annuels moyens et les bonus pour divers intitulés de postes dans différents pays. L'application utilise un fichier Excel pour le stockage des données et offre des fonctionnalités de recherche et de visualisation des salaires via une interface web simple.

## Table des Matières

1. [Installation](#installation)
2. [Utilisation](#utilisation)
3. [Fonctionnalités](#fonctionnalités)
4. [Points de terminaison de l'API](#points-de-terminaison-de-lapi)
5. [Structure des fichiers](#structure-des-fichiers)

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

## Structure des fichiers

- `src/app.py` : Script principal de l'application.
- `templates/index.html` : Modèle HTML pour l'interface web.
- `static/` : Fichiers statiques (images, feuilles de style CSS, JavaScript).
