# Étape 1 : Installation des dépendances de construction
FROM python:3.10-alpine AS builder

# Installation des bibliothèques PostgreSQL
RUN apk add --no-cache postgresql-libs

# Installation des dépendances de construction temporaires et d'outils
RUN apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev

# Étape 2 : Installation des dépendances Python
FROM builder AS python-dependencies

# Création du répertoire /app dans le conteneur
RUN mkdir /app

# Définition du répertoire de travail comme /app
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

# Configuration des variables d'environnement pour Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Configuration des variables d'environnement spécifiques à l'application
ENV SENTRY_DSN $SENTRY_DSN
ENV PORT 8080

# Copie du contenu local dans le répertoire /app du conteneur
COPY . /app/

# Copie des dépendances Python de l'étape python-dependencies
COPY --from=python-dependencies /app/venv /app/venv

# Collecte des fichiers statiques de l'application
RUN /app/venv/bin/python manage.py collectstatic --noinput --settings=oc_lettings_site.settings

# Création d'un dump de la base de données dans data.json
RUN /app/venv/bin/python manage.py dumpdata -o data.json

# Commande par défaut pour exécuter le serveur Django
CMD /app/venv/bin/python manage.py runserver 0.0.0.0:$PORT
