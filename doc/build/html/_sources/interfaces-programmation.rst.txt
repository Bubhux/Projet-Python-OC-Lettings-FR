*******************************************
Description des interfaces de programmation
*******************************************

Interface de programmation
++++++++++++++++++++++++++

.. |python-logo| image:: _static/python-logo-only.svg
   :alt: Python Logo
   :width: 20px

.. |github-logo| image:: _static/github.svg
   :alt: GitHub Logo
   :width: 20px

.. |github-actions-logo| image:: _static/githubactions.svg
   :alt: GitHub Actions Logo
   :width: 20px

.. |heroku-logo| image:: _static/heroku.svg
   :alt: Heroku Logo
   :width: 20px

.. |sentry-logo| image:: _static/sentry.svg
   :alt: Sentry Logo
   :width: 20px

.. |docker-logo| image:: _static/docker.svg
   :alt: Docker Logo
   :width: 20px

Ce projet Django repose sur un ensemble d'interfaces de programmation (API) bien définies qui facilitent la gestion, la collaboration et le déploiement de l'application. Ces API sont au cœur de notre stack technologique et garantissent un fonctionnement harmonieux de bout en bout.


Python |python-logo|
====================

1. Fichier Python
-----------------

1. **API Python :** Python est le langage de programmation principal de ce projet. Il expose des API internes qui permettent à notre code Django de s'interfacer avec différentes parties de l'application. Ces API Python sont structurées de manière à simplifier le développement, la maintenance et l'extensibilité de l'application.

- Importation du modèle Profile personnalisé :

    .. code-block:: python

        from .models import Profile

        def profile(request, username):
        """
        Affiche le profil de l'utilisateur avec le nom d'utilisateur donné.
        Si le profil n'existe pas, affiche une page personnaliséé error 500.
        """
        if Profile.objects.filter(user__username=username):
            profile = Profile.objects.get(user__username=username)
            context = {'profile': profile}
            return render(request, 'profiles/profile.html', context)
        else:
            return render(
                request,
                'oc_lettings_site/error_template.html', {'error_code': 500}, status=500
            )


GitHub |github-logo|
====================

2. **GitHub API :** GitHub est la plateforme de gestion de code source sur laquelle notre projet est hébergé. L'API GitHub est utilisée pour automatiser la gestion du code, notamment la création de demandes de fusion (pull requests), la gestion des problèmes (issues), et le suivi des modifications de code. Elle permet également de déclencher des actions d'intégration continue.

- Création d'une demande de fusion (pull request) via l'API GitHub en utilisant Git Bash:


Ce document vous guidera à travers un flux de travail de base en utilisant Git Bash pour gérer vos projets Git localement et sur GitHub.

1. Ouvrez Git Bash
-------------------
Si Git Bash n'est pas déjà installé, téléchargez-le depuis le site officiel de Git (https://git-scm.com/).

2. Naviguez vers le répertoire de votre référentiel local
---------------------------------------------------------
Utilisez la commande `cd` pour accéder au répertoire de votre projet :

.. code-block:: bash

    $ cd chemin/vers/votre/referentiel

Assurez-vous d'être dans le répertoire racine de votre référentiel.

3. Vérifiez l'état actuel de votre référentiel
----------------------------------------------
Utilisez `git status` pour voir les modifications en attente :

.. code-block:: bash

    $ git status

Cela affichera les fichiers modifiés, non suivis, etc.

4. Ajoutez les fichiers que vous souhaitez inclure dans votre prochaine validation
----------------------------------------------------------------------------------
Utilisez `git add` pour ajouter les fichiers :

.. code-block:: bash

    $ git add nom_du_fichier

Vous pouvez également ajouter tous les fichiers modifiés en utilisant :

.. code-block:: bash

    $ git add .

5. Validez vos modifications avec un message de commit significatif
-------------------------------------------------------------------
Utilisez `git commit` pour créer un commit :

.. code-block:: bash

    $ git commit -m "Ajout de nouvelles fonctionnalités"

Assurez-vous que le message de commit décrit clairement les modifications apportées.

6. Pousser vos modifications vers le référentiel distant
--------------------------------------------------------
Utilisez `git push` pour pousser vers le référentiel distant (remplacez `development` par le nom de votre branche) :

.. code-block:: bash

    $ git push origin development

Par exemple, pour pousser vers la branche `development` :

.. code-block:: bash

    $ git push origin main

7. Effectuer le merge
---------------------
Pour effectuer le merge de la branche `development` vers la branche `master`, suivez ces étapes sur GitHub :
   - Allez dans votre demande de fusion (pull request).
   - Cliquez sur "Merge Pull Request".
   - Sélectionnez "Create a merge commit" ou "Squash and merge" selon votre préférence.
   - Cliquez sur "Confirm Merge" pour effectuer le merge.

Ceci est un exemple de flux de travail Git de base en utilisant Git Bash pour effectuer des modifications locales, valider et pousser ces modifications vers un référentiel distant, ainsi que pour créer une demande de fusion sur GitHub.

.. note::
    L'étape 7 permet d'effectuer le merge vers la branche **master**. Le processus de demande de fusion peut varier selon votre flux de travail et votre plateforme d'hébergement de code.

8. Créez une demande de fusion (pull request) sur GitHub (si nécessaire)
------------------------------------------------------------------------
- Allez sur la page de votre référentiel GitHub.
- Cliquez sur "New Pull Request".
- Sélectionnez la branche que vous souhaitez fusionner dans le menu déroulant.
- Cliquez sur "Create Pull Request".
- Donnez un titre et une description significatifs.
- Cliquez sur "Create Pull Request" pour ouvrir la demande de fusion.

.. note::
    Attendez la révision et la fusion de votre demande de fusion par les collaborateurs.

Ceci est un exemple de flux de travail Git de base en utilisant Git Bash pour effectuer des modifications locales, valider et pousser ces modifications vers un référentiel distant. Le processus de demande de fusion peut varier selon votre flux de travail et votre plateforme d'hébergement de code.


GitHub Actions |github-actions-logo|
====================================

1. Fichier yaml
---------------

3. **GitHub Actions :** GitHub Actions fournit une API pour la configuration et l'automatisation des flux de travail d'intégration continue (CI) et de déploiement continu (CD). Ces actions automatisées sont essentielles pour garantir que chaque modification du code est testée, construite et déployée de manière cohérente.

- Fichier de configuration yaml pour GitHub Actions qui déclenche le workflow à chaque `push` ou `pull request` sur la branche master :

.. code-block:: yaml

   name: Django CI/CD Master

    on:
    push:
        branches:
        - master
    pull_request:
        branches:
        - master

    jobs:
    build_and_test:
        runs-on: ubuntu-latest
        strategy:
        matrix:
            python-version: ["3.7"]

        steps:
        - name: Checkout code
            uses: actions/checkout@v3

        - name: Set up Python ${{ matrix.python-version }}
            uses: actions/setup-python@v3
            with:
            python-version: ${{ matrix.python-version }}

        - name: Install Dependencies
            run: |
            python -m pip install --upgrade pip
            pip install -r requirements.txt
        - name: Run linting
            run: flake8

        - name: Run tests with pytest
            env:
            SECRET_KEY: ${{ secrets.DJANGO_SECRET_KEY }}
            DEBUG: 0
            run: pytest

        - name: Run Django tests
            run: python manage.py test

        - name: Run tests with coverage
            run: |
            coverage run --omit=*/tests.py manage.py test
        - name: Check test coverage
            run: coverage report --fail-under=80

    build_and_push_to_dockerhub:
        needs: build_and_test
        runs-on: ubuntu-latest

        steps:
        - name: Checkout repository
            uses: actions/checkout@v3

        - name: Set up Docker Buildx
            uses: docker/setup-buildx-action@v2

        - name: Log into Docker Hub
            uses: docker/login-action@v2
            with:
            username: ${{ secrets.DOCKER_USERNAME }}
            password: ${{ secrets.DOCKER_PASSWORD }}

        - name: Build and push Docker image
            run: |
            docker buildx build --load --file Dockerfile --tag bubhux/bubhux-oc-image-build:${{ github.sha }} --tag bubhux/bubhux-oc-image-build:latest .
            docker push bubhux/bubhux-oc-image-build:${{ github.sha }}
            docker push bubhux/bubhux-oc-image-build:latest

        - name: Set IMAGE_ID environment variable
            run: |
            IMAGE_ID=$(docker inspect --format='{{.Id}}' bubhux/bubhux-oc-image-build:${{ github.sha }})
            echo "IMAGE_ID=$IMAGE_ID" >> $GITHUB_ENV

        - name: Tag Docker image with commit hash
            run: |
            docker tag bubhux/bubhux-oc-image-build:${{ github.sha }} bubhux/bubhux-oc-image-build:commit-${{ github.sha }}

    deploy_to_heroku:
        needs: build_and_push_to_dockerhub
        runs-on: ubuntu-latest

        steps:
        - name: Checkout code
            uses: actions/checkout@v3

        - name: Install Heroku CLI
            run: curl https://cli-assets.heroku.com/install.sh | sh

        - name: Purge Heroku cache
            run: |
            heroku plugins:install heroku-repo
            heroku repo:purge_cache -a ${{ secrets.HEROKU_APP_NAME }}

        - name: Log in to Heroku Container Registry
            run: heroku container:login
            env:
            HEROKU_API_KEY: ${{ secrets.HEROKU_API_KEY }}

        - name: Push to Heroku Container Registry
            run: heroku container:push -a ${{ secrets.HEROKU_APP_NAME }} web

        - name: Deploy to Heroku
            run: |
            HEROKU_DEBUG=1 heroku container:release -a ${{ secrets.HEROKU_APP_NAME }} web

.. note::
    Pour voir le flux de travail GitHub Actions correspondant. `Cliquez ici : workflow GitHub Actions <https://github.com/Bubhux/Python-OC-Lettings-FR/actions/runs/6032226608>`_

Docker |docker-logo| 
====================

1. Fichier Dockerfile
---------------------

4. **Docker API :** Docker est utilisé pour la conteneurisation de notre application. Bien que la plupart de nos interactions avec Docker se fassent via la ligne de commande, l'API Docker permet une gestion programmatique des conteneurs. Elle joue un rôle crucial dans la création, la mise à l'échelle et la gestion des conteneurs pour nos services.

- Configutation et construction de l'image en local :

    .. code-block:: docker

        # Étape 1 : Installation des dépendances de construction
        # Utilisation de l'image Python 3.7.2 basée sur Alpine Linux
        FROM python:3.7.2-alpine AS builder

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
        FROM python:3.7.2-alpine

        # Configuration du répertoire de travail
        WORKDIR /app

        # Configuration des variables d'environnement pour Python
        ENV PYTHONDONTWRITEBYTECODE 1
        ENV PYTHONUNBUFFERED 1

        # Configuration des variables d'environnement spécifiques à l'application
        ENV SENTRY_DSN $SENTRY_DSN
        ENV HEROKU_APP_NAME $HEROKU_APP_NAME
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

- Création de l'image du projet et de son lancement sur le serveur local en ligne de commande Docker :

    .. code-block:: bash

        # Connexion au démon Docker
        $ docker login

        # Téléchargement de l'image Docker depuis un registre (par exemple, Docker Hub)
        $ docker pull bubhux/bubhux-oc-image-build:latest

        # Création et exécution d'un conteneur à partir de l'image
        $ docker run -it -p 8080:8080 bubhux/bubhux-oc-image-build:latest

        # Accéder au dossier du container 
        docker run -it bubhux/bubhux-oc-image-build:latest /bin/sh

        # Pour lister les conteneurs en cours d'exécution
        $ docker ps

        # Pour arrêter le conteneur par son nom
        $ docker stop nom_conteneur

        # OU pour arrêter le conteneur par son ID (remplacez 'id_conteneur' par l'ID réel)
        $ docker stop id_conteneur

        # Pour supprimer le conteneur (après l'arrêt)
        $ docker rm nom_conteneur

        # OU pour supprimer le conteneur par son ID (après l'arrêt)
        $ docker rm id_conteneur


Sentry |sentry-logo|
====================

1. Intégration de Sentry
------------------------

5. **Sentry API :** Sentry est notre plateforme de gestion d'erreurs en temps réel. Son API nous permet de surveiller activement les erreurs et les exceptions dans notre application, ce qui facilite la détection et la correction rapides des problèmes. Les rapports d'erreurs envoyés via cette API sont précieux pour le débogage.

- Intégration de Sentry dans l'application Django pour capturer les erreurs :

    .. code-block:: python

        import sentry_sdk

        from sentry_sdk.integrations.django import DjangoIntegration

        # Initialisation de Sentry
        sentry_sdk.init(
            dsn=SENTRY_DSN,
            integrations=[
                DjangoIntegration(
                    transaction_style='url',
                    middleware_spans=True,
                    signals_spans=False,
                    cache_spans=False,
                ),
            ],
            traces_sample_rate=1.0,
            send_default_pii=True
        )


Heroku |heroku-logo|
====================

1. Heroku CLI
-------------

6. **Heroku API :** Heroku est notre plateforme d'hébergement cloud pour l'application. L'API Heroku est utilisée pour gérer les ressources de l'application, notamment le scaling automatique, le déploiement continu et la surveillance des performances.

- Connexion à Heroku CLI et affichage de la liste des applications associées à votre compte :

    .. code-block:: bash

        # Connexion à Heroku
        $ heroku login

        # Vous serez redirigé vers une page web pour vous authentifier.
        # Une fois authentifié, vous serez connecté à Heroku via la CLI.

        # Affichage de la liste des applications associées à votre compte
        $ heroku apps

        # Utilisation de la commande 'heroku info' pour obtenir des informations sur l'application actuelle (en option)
        $ heroku info

        # Connexion au registre de conteneurs Heroku
        $ heroku container:login

        # Pousser votre conteneur local vers Heroku
        $ heroku container:push web

        # Libération (déploiement) du conteneur sur Heroku
        $ heroku container:release web

        # Si vous avez également des modifications dans votre dépôt Git local,
        # vous pouvez les pousser vers le dépôt Heroku (branche master)
        $ git push heroku master
