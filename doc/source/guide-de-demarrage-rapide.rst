.. _guide-de-demarrage-rapide:

*************************
Guide de démarrage rapide
*************************

.. |github-logo| image:: _static/github.svg
   :alt: GitHub Logo
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

Pour démarrer le projet, les prérequis suivants sont nécessaires :

- Un compte GitHub |github-logo| (https://github.com/)
- Un compte Docker |docker-logo| (https://www.docker.com/)
- Un compte Sentry |sentry-logo| (https://sentry.io/)
- Un compte Heroku |heroku-logo| (https://www.heroku.com/)


Prépartion de l'environnement
=============================

Ce guide vous explique les étapes pour créer et configurer l'environnement nécessaire à l'exécution du programme. Suivez ces instructions pour une mise en place rapide.

1. Création de l'Environnement Virtuel
--------------------------------------

Pour démarrer, suivez ces étapes :

1. Installer une version de Python compatible avec votre ordinateur. (https://www.python.org/downloads/)
2. Ouvrez le terminal (ou invite de commande) et placez-vous dans le dossier principal (dossier racine) du projet.

3. Tapez la commande suivante dans votre terminal pour créer un environnement virtuel nommé "venv" :

.. code-block:: bash

   $ python -m venv venv

Un répertoire appelé "venv" sera créé dans le dossier.

2. Activation de l'Environnement Virtuel
----------------------------------------

Pour activer l'environnement virtuel créé, suivez ces étapes :

1. Assurez-vous d'être dans le dossier principal (dossier racine) du projet avec le terminal.

2. Tapez la commande suivante pour activer l'environnement virtuel :

.. code-block:: bash

   $ venv\Scripts\activate.bat

Cela ajoutera le préfixe "venv" à chaque ligne de commande dans votre terminal.

Pour désactiver l'environnement virtuel, utilisez cette commande :

.. code-block:: bash

   $ deactivate

4. Installation des Librairies
------------------------------

1. Assurez-vous d'être dans le dossier où se trouve le fichier "requirements.txt" avec l'environnement virtuel activé.

2. Pour installer les librairies requises, utilisez la commande suivante :

.. code-block:: bash

   $ pip install -r requirements.txt

5. Exécution de l'Application
-----------------------------

Utilisez ces étapes pour exécuter l'application :

1. Lancez le serveur :

   - Assurez-vous d'être dans le dossier principal du projet avec l'environnement virtuel activé.
   - Utilisez la commande suivante :

     .. code-block:: bash

        $ python manage.py runserver

2. Accédez à l'application dans le navigateur de votre choix :

   - Ouvrez votre navigateur web.
   - Rendez-vous à l'adresse : http://127.0.0.1:8000/

Commencez dès maintenant à utiliser l'application et à explorer ses fonctionnalités passionnantes !
