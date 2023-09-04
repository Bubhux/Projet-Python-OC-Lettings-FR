********************************************************
Procédures de déploiement et de gestion de l'application
********************************************************

Déploiement et gestion
++++++++++++++++++++++

.. |heroku-logo| image:: _static/heroku.svg
   :alt: Heroku Logo
   :width: 20px


config de Heroku |heroku-logo|
=====================================
La plateforme d'hébergement utilisé pour le déploiement de l'application est Heroku.

1. Paramétrer Heroku
--------------------

- Après la création de votre compte Heroku. (https://www.heroku.com/)

.. important::
   - Vous pourrez récupérer la clé `HEROKU_API_KEY` en allant dans `Account settings` ensuite dans le menu `Account` ou se trouve **API Key**.

2. Créer une appplication sur Heroku
------------------------------------

- Pour créer une application rendez-vous sur le `Dashboard`, cliquer sur **`New`** et **`Create new app`**.
- Une fois, votre application créée, rentrée dans celle-ci, se rendre dans le menu `Deploy` comme montré sur la capture d'écran et connectez-vous à votre compte `GitHub`.
- Et connecter votre `repository`.

.. raw:: html

   <a href="_static/heroku-config-1.png" target="_blank">
       <img src="_static/heroku-config-1.png" alt="Heroku Screenshot" style="max-width: 100%; border: 1px solid #ccc;">
   </a>


Lancer un premier déploiement sur Heroku |heroku-logo|
======================================================

1. Exécutez un premier déploiement
----------------------------------

.. important::
   - Pour effectuer un premier déploiement, il faut lancer un push sur la branche `master` de `GitHub` ce qui aura pour effet de lancer le workflow sur `GitHub Actions`.

- Une fois que le workflow a passé toutes les étapes avec succés. 
- Retourner sur `Heroku` dans votre apllication allez dans le menu `Deploy` comme montré sur la capture d'écran.
- Dans la partie `Manual deploy` choisissez la branche `master` et cliquer sur **`Deploy Branch`**.

.. raw:: html

   <a href="_static/heroku-config-2.png" target="_blank">
       <img src="_static/heroku-config-2.png" alt="Heroku Screenshot" style="max-width: 100%; border: 1px solid #ccc;">
   </a>

.. note::
   - Après que le build soit finis vous pourrez accéder à l'application en cliquant sur **Open app**.


Lancer un deuxième déploiement Heroku |heroku-logo|
===================================================

1. Créer un pipeline pour l'application
---------------------------------------

Pour déployer une nouvelle version de l'application, vous devez créer un pipeline.

.. important::
   - Pour effectuer un deuxième déploiement et déployer une nouvelle version de l'application, il faut lancer un push sur la branche `master` de `GitHub` ce qui aura pour effet de lancer le workflow sur `GitHub Actions`.

- Retourner sur `Heroku` dans votre application allez dans le menu `Deploy`.
- Selectionner `Choose a pipeline` et `Create a new pipeline`.
- Une fois le pipeline créé rendez-vous dans la partie `Settings` et connecter votre `GitHub` et choisissez votre dépôt.

2. Créer un Review apps
-----------------------

- Activez **Enable Review Apps** et cliquer **New app** sélectionnez `Choose a branch to deploy` et la branche `master`, cliquer sur **Create**.

.. raw:: html

   <a href="_static/heroku-config-3.png" target="_blank">
       <img src="_static/heroku-config-3.png" alt="Heroku Screenshot" style="max-width: 100%; border: 1px solid #ccc;">
   </a>

- Une fois le build terminer allez dans l'étape `Staging` cliquer sur **Create new app**.
- Toujours dans l'étape `Staging` après la création de la `new app` cliquer sur le menu déroulant à côté de `Open app` et choisissez `Deploy a branch`, sélectionnez la branche `master` et cliquer sur **Deploy**

.. note::
   - Une fois ces étapes effectuées, dans le menu déroulant, vous pourrez choisir de bouger l'application `Move to development` ou `Move to production`

.. raw:: html

   <a href="_static/heroku-config-4.png" target="_blank">
       <img src="_static/heroku-config-4.png" alt="Heroku Screenshot" style="max-width: 100%; border: 1px solid #ccc;">
   </a>


Activez Sentry pour le monitoring sur Heroku
============================================

1. Activez Sentry dans Heroku
-----------------------------

.. important::
   - Pour que le monitoring avec `Sentry` soit fonctionnelle il faudra rentrer celle-ci dans `Heroku`.
   - Rendez-vous dans l'application principal la partie `Settings` allez dans `Config Vars` et saisissez votre clé `SENTRY_DSN`.

   .. raw:: html

      <a href="_static/heroku-config-5.png" target="_blank">
         <img src="_static/heroku-config-5.png" alt="Heroku Screenshot" style="max-width: 100%; border: 1px solid #ccc;">
      </a>

.. important::
   - Rendez-vous dans le pipeline dans la partie `Settings` allez dans `Review app config vars` et saisissez votre clé `SENTRY_DSN`.

   .. raw:: html

      <a href="_static/heroku-config-6.png" target="_blank">
         <img src="_static/heroku-config-6.png" alt="Heroku Screenshot" style="max-width: 100%; border: 1px solid #ccc;">
      </a>
