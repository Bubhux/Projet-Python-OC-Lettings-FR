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

# Collecter les fichiers statiques
RUN /app/venv/bin/python manage.py collectstatic --noinput

# Lancer le serveur Django
CMD ["/app/venv/bin/gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]
