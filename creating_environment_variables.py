"""Créer un modèle de fichier .env pour OC_lettings_site
   avec une clé secrète générée aléatoirement
"""
from django.core.management.utils import get_random_secret_key

# Liste des noms de variables d'environnement
env_variable_names = [
    'DJANGO_SECRET_KEY',
    'SENTRY_DSN',
    'HEROKU_APP_NAME',
    'DEBUG',
]

# Générer la clé secrète aléatoire
secret_key = get_random_secret_key()

# Ouvrir le fichier .env en mode écriture
with open(".env", "w") as f:
    # Écrire les noms des variables d'environnement avec leurs valeurs
    f.write(f"DJANGO_SECRET_KEY={secret_key}\n")
    for env_var in env_variable_names[1:]:
        f.write(f"{env_var}=\n")

# Afficher un message indiquant que le modèle de fichier .env a été créé
print("\n.env file created!")
