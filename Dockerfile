# Étape 1 : Installation des dépendances de construction
FROM python:3.10-alpine AS builder

# Installation des bibliothèques PostgreSQL et autres dépendances nécessaires à la construction
RUN apk add --no-cache postgresql-libs gcc musl-dev postgresql-dev

# Étape 2 : Installation des dépendances Python
FROM builder AS python-dependencies

# Création du répertoire /app dans le conteneur
WORKDIR /app

# Copie du fichier requirements.txt dans le répertoire /app/
COPY requirements.txt /app/

# Création d'un environnement virtuel
RUN python -m venv venv

# Mise à jour de pip dans l'environnement virtuel
RUN /app/venv/bin/pip install --upgrade pip

# Installation des dépendances Python depuis requirements.txt
RUN /app/venv/bin/pip install -r requirements.txt

# Étape 3 : Construction de l'image finale
FROM python:3.10-alpine

# Configuration du répertoire de travail
WORKDIR /app

# Variables d'environnement pour Python et l'application
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV SENTRY_DSN $SENTRY_DSN
ENV PORT 8080

# Copie du contenu local dans le répertoire /app du conteneur
COPY . /app/

# Copie des dépendances Python de l'étape python-dependencies
COPY --from=python-dependencies /app/venv /app/venv

# Collecte des fichiers statiques de l'application
RUN /app/venv/bin/python manage.py collectstatic --noinput --settings=oc_lettings_site.settings

# Préparation de la base de données PostgreSQL
# 1. Migration des modèles
RUN /app/venv/bin/python manage.py migrate --settings=oc_lettings_site.settings

# Vérification de l'installation de Gunicorn
RUN /app/venv/bin/gunicorn --version

# Commande par défaut pour exécuter le serveur Django avec Gunicorn
CMD ["/app/venv/bin/gunicorn", "--bind", "0.0.0.0:$PORT", "--workers=4", "oc_lettings_site.wsgi:application"]
