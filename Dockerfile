# Utiliser une image de base officielle avec Python 3.12.0
FROM python:3.12.0-slim

# Définir le répertoire de travail
WORKDIR /app

# Installer les dépendances système, y compris PostgreSQL et build-essential
RUN apt-get update && \
    apt-get install -y sqlite3 postgresql libpq-dev build-essential && \
    rm -rf /var/lib/apt/lists/*

# Copier le fichier requirements.txt dans le répertoire de travail
COPY requirements.txt /app/

# Installation des dépendances Python
RUN python -m venv venv && \
    /app/venv/bin/pip install --upgrade pip && \
    /app/venv/bin/pip install -r requirements.txt

# Copier le reste de l'application dans le répertoire de travail
COPY . .

# Définir les variables d'environnement
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.settings

# Exposer le port 8000
EXPOSE 8000

# Ajout du répertoire de l'environnement virtuel au PATH pour accéder à gunicorn sans chemin absolu
ENV PATH="/app/venv/bin:$PATH"

# Préparation de la base de données PostgreSQL
RUN /app/venv/bin/python manage.py migrate --settings=oc_lettings_site.settings

# Définir l'environnement par défaut sur "production"
ENV ENVIRONMENT=production

# Afficher la valeur de ENVIRONMENT pour le débogage lors du build
RUN echo "ENVIRONMENT set to: $ENVIRONMENT"

# Collecte des fichiers statiques de l'application
RUN /app/venv/bin/python manage.py collectstatic --noinput --clear --settings=oc_lettings_site.settings

# Vérification de l'installation de Gunicorn (débogage)
RUN /app/venv/bin/gunicorn --version

# Commande par défaut pour exécuter le serveur Django avec Gunicorn
CMD ["sh", "-c", "echo 'ENVIRONMENT at runtime: $ENVIRONMENT' && /app/venv/bin/gunicorn --bind 0.0.0.0:8000 --workers=4 oc_lettings_site.wsgi:application"]
