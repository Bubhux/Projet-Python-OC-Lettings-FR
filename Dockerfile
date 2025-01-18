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

# Mise à jour de pip
RUN pip install --upgrade pip

# Installation des dépendances Python depuis requirements.txt
RUN pip install -r requirements.txt

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
COPY --from=python-dependencies /app /app

# Installation globale de Gunicorn
RUN pip install gunicorn

# Collecte des fichiers statiques de l'application
RUN python manage.py collectstatic --noinput --settings=oc_lettings_site.settings

# Création d'un dump de la base de données dans data.json
RUN python manage.py dumpdata -o data.json

# Vérification de l'installation de Gunicorn
RUN gunicorn --version

# Commande par défaut pour exécuter le serveur Django avec Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "oc_lettings_site.wsgi:application"]
