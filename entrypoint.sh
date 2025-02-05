#!/bin/sh

# Activer l'environnement virtuel
echo "Activation de l'environnement virtuel..."
# shellcheck disable=SC1091
. /app/venv/bin/activate

# Exécuter le script de création du fichier .env
echo "Exécution du script creating_environment_variables.py..."
python /app/creating_environment_variables.py

# Lancer le serveur avec Gunicorn
echo "Démarrage du serveur Django..."
exec gunicorn oc_lettings_site.asgi:application --host 0.0.0.0 --port 8000
