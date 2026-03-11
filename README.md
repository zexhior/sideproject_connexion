# Projet Python ETL

## Prérequis

- Python 3.10+ (recommandé)

## Installation

1. Créer un environnement virtuel :
   - Linux/macOS : `python -m venv .venv`
   - Windows : `py -m venv .venv`
2. Activer l'environnement virtuel :
   - Linux/macOS : `source .venv/bin/activate`
   - Windows : `.venv\\Scripts\\activate`
3. Installer les dépendances :
   - `pip install -r requirements.txt`

## Exécution

- `python src/main.py`

## Journalisation de connexion BDD

- À chaque démarrage de l'application, une entrée est ajoutée dans la table `database_connection_log`.
- Champs enregistrés :
  - `source` (par défaut: `application`)
  - `connected_at` (date/heure de connexion)
