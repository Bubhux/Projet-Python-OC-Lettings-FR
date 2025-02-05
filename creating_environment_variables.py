"""
Créer un modèle de fichier .env pour oc_lettings_site
avec une clé secrète générée aléatoirement et des variables d'environnement préconfigurées.

Ce script génère un fichier .env qui peut être utilisé pour configurer
l'environnement de l'application oc_lettings_site.
Il génère une clé secrète aléatoire pour la configuration de Django
et inclut également des noms de variables d'environnement
préconfigurés tels que :

    - 'ENVIRONMENT'
    - 'DJANGO_SECRET_KEY'
    - 'SENTRY_DSN'
    - 'HEROKU_APP_NAME'
    - 'RAILWAY_APP_NAME'
    - 'RAILWAY_TOKEN'
    - 'RAILWAY_SERVICE_ID'
    - 'RAILWAY_PROJECT_ID'
    - 'DATABASE_URL'
    - 'DEBUG': '0'

Le fichier .env généré doit être configuré avec des valeurs appropriées
pour chaque variable d'environnement avant utilisation.

Exemple d'utilisation :

    1. Exécutez ce script pour générer un fichier .env.
    2. Configurez les valeurs des variables d'environnement
       dans le fichier .env généré.
    3. Utilisez le fichier .env pour configurer
       l'environnement de votre application oc_lettings_site.

.. note::
    Remarque :
    Le fichier .env généré ne doit pas être partagé publiquement
    car il contient des informations sensibles.

"""

from django.core.management.utils import get_random_secret_key

# Liste des noms de variables d'environnement et de leurs valeurs par défaut
env_variables = {
    'ENVIRONMENT': 'development',
    'DJANGO_SECRET_KEY': get_random_secret_key(),
    'SENTRY_DSN': '',
    'HEROKU_APP_NAME': 'oc-lettings-apps',
    'RAILWAY_APP_NAME': 'oc-lettings-apps',
    'RAILWAY_TOKEN': '',
    'RAILWAY_SERVICE_ID': '',
    'RAILWAY_PROJECT_ID': '',
    'DATABASE_URL': '',
    'DEBUG': '0'
}

# Génére le fichier .env
with open(".env", "w") as f:
    for key, value in env_variables.items():
        f.write(f"{key}={value}\n")

# Affiche un message indiquant que le fichier .env a été créé
print("\n.env file created with the following variables:")
for key in env_variables.keys():
    print(f" - {key}")
