![Static Badge](static/badges/build-with-python.svg)   
![Static Badge](static/badges/build-with-django.svg)   
![Static Badge](static/badges/build-with-bootstrap.svg)   
![Static Badge](static/badges/build-with-docker.svg)   

![Static Badge](static/badges/use-sqlite.svg)   
![Static Badge](static/badges/use-sentry.svg)   
![Static Badge](static/badges/use-heroku.svg)   
![Static Badge](static/badges/use-github-actions.svg)   
![Static Badge](static/badges/use-read-the-docs.svg)   

[![Documentation Status](https://readthedocs.org/projects/python-oc-lettings/badge/?version=latest)](https://python-oc-lettings.readthedocs.io/fr/latest/?badge=latest) ➔ [Read the Docs](https://python-oc-lettings.readthedocs.io/fr/latest/)

[![Django CI/CD Master](https://github.com/Bubhux/Projet-Python-OC-Lettings-FR/actions/workflows/ci_cd_branch_master.yml/badge.svg?branch=master)](https://github.com/Bubhux/Projet-Python-OC-Lettings-FR/actions/workflows/ci_cd_branch_master.yml) ➔ [Workflow GitHub Actions](https://github.com/Bubhux/Python-OC-Lettings-FR/actions/runs/6032226608)

<div id="top"></div>

## Menu   
1. **[Informations générales](#informations-générales)**   
2. **[Documentation Read the Docs](#documentation)**   
3. **[Fonctionnalitées](#fonctionnalitées)**   
4. **[Interface d'administration Django](#interface-administration-django)**   
5. **[Liste pré-requis](#liste-pre-requis)**   
6. **[Tests et couverture de code](#tests-et-couverture-de-code)**   
7. **[Création environnement](#creation-environnement)**   
8. **[Activation environnement](#activation-environnement)**   
9. **[Installation des librairies et dépendances](#installation-librairies)**   
10. **[Installation des variables d'environnement](#installation-environnement)**   
11. **[Exécution de l'application](#execution-application)**   
12. **[Image avec Docker](#docker-image)**   
13. **[Rapport avec flake8](#rapport-flake8)**   
14. **[Informations importantes sur les différents fichiers et dossiers](#informations-importantes)**   
15. **[Auteur et contact](#auteur-contact)**   


<div id="informations-générales"></div>

### Projet Orange County Lettings   


- L'objectif de ce projet est de mettre à l'échelle une application **Django** en utilisant une architecture modulaire.   

- Plusieurs domaines du site **OC Lettings** ont été améliorés à partir du projet forker et cloner à l'adresse suivante ➔ [Python-OC-Lettings-FR](https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR)   
- L'objectif de ce projet est de mettre à l'échelle une application **Django** en utilisant une architecture modulaire   

Plusieurs domaines du site **OC Lettings** ont été améliorés.   
À partir du projet forker et cloner à l'adresse suivante : ➔ [Python-OC-Lettings-FR](https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR)   

--------------------------------------------------------------------------------------------------------------------------------

__Réduction de la dette technique__   

   - Remplacer les templates de manière cohérente dans les nouvelles applications.   
   - Correction des erreurs de linting.   
   - Correction de la pluralisation des noms de modèles dans le site d'administration.   


__Amélioration de l'architecture modulaire__   

   - Créer 2 applications ``lettings``, ``profiles`` pour séparer les fonctionnalités de l'application.   
   - remplir les nouvelles tables avec les données déjà présentes dans la base de données en utilisant les fichiers de migration **Django**.   
   - Remplir les nouvelles tables avec les données déjà présentes dans la base de données en utilisant les fichiers de migration **Django**.   
   - Convertir ``oc_lettings_site`` en projet **Django**.   
   - Développer une suite de tests.   


__Ajout d'un pipeline CI/CD avec [GitHub Actions](https://github.com) et déploiement sur [Heroku](https://www.heroku.com)__   

   - *Compilation* : exécuter le linting et la suite de tests.
   - *Conteneurisation* : construire et push une image du site avec [Docker](https://www.docker.com).   
   - *Déploiement* : exécuter le déploiement de l'application avec **Heroku**.   
   - **Compilation :** exécuter le linting et la suite de tests.
   - **Conteneurisation :** construire et push une image du site avec [Docker](https://www.docker.com).   
   - **Déploiement :** exécuter le déploiement de l'application avec **Heroku**.   


>_**Note :** Monitoring de l'application et suivi des erreurs via [Sentry](https://sentry.io/welcome/)._   

--------------------------------------------------------------------------------------------------------------------------------


<div id="documentation"></div>
<a href="#top" style="float: right;">Retour en haut 🡅</a>

### Documentation Read the Docs   

Bienvenue dans notre documentation complète disponible sur **Read the Docs / Sphinx**.   
- Vous trouverez toutes les informations essentielles pour comprendre et travailler avec notre projet.   

- La documentation est disponible à l'adresse suivante ➔ [Read the Docs](https://python-oc-lettings.readthedocs.io/fr/latest/)   
>**Note : N'hésitez pas à explorer les différents chapitres ci-dessous.**   
  &nbsp;   

1. **Description du Projet :** Découvrez notre démarche d'amélioration de l'architecture modulaire.   
    - Amélioration de l’architecture Modulaire   

2. **Installation :** Apprenez comment installer notre application sur votre environnement de développement.   
    - Récupération et installation du projet   

3. **Guide de Démarrage Rapide :** Obtenez rapidement votre application en marche.   
    - Prépartion de l’environnement   

4. **Technologies et Langages :** Explorez les technologies et langages utilisés dans le projet.   
    - Les technologies et les langages utilisés   

5. **Structure de la Base de Données et Modèles de Données :** Comprenez la structure de la base de données.   
    - Structure de la base de données   
    - Modèles de données   

6. **Interfaces de Programmation :** Découvrez les API exposées par l'application.   
    - Interface de programmation   

7. **Guide d'Utilisation :** Apprenez comment utiliser notre application avec des cas d'utilisation.   
    - Introdcution   

8. **Procédures de Déploiement et de Gestion :** Suivez les étapes pour déployer et gérer l'application.   
    - Déploiement et gestion   

  >_**Note :** N'hésitez pas à explorer les différents chapitres ci-dessus._   

--------------------------------------------------------------------------------------------------------------------------------

<div id="fonctionnalitées"></div>
<a href="#top" style="float: right;">Retour en haut 🡅</a>

### Fonctionnalitées   

- Opérations **CRUD** par le site d'administration de **Django**.   
- Navigation au travers des end points de l'API.   

>**Note : Testé sous Windows 10 - Python 3.12.0 - Django 3.2.20**   
>_**Note :** Testé sous **Window**s 7 - **Python** 3.7.2 - **Django** 3.2.20_   

--------------------------------------------------------------------------------------------------------------------------------

<div id="interface-administration-django"></div>
<a href="#top" style="float: right;">Retour en haut 🡅</a>

### Interface d'administration Django   

- L'interface d'administration **Django** est disponible et fonctionnelle.   
  
Identifiant : **admin** | Mot de passe : **Abc1234!**   
➔ http://127.0.0.1:8000/admin/   

--------------------------------------------------------------------------------------------------------------------------------

<div id="liste-pre-requis"></div>
<a href="#top" style="float: right;">Retour en haut 🡅</a>

### Liste pré-requis   

- Compte **GitHub** avec accès en lecture à ce repository   
- **Git CLI**   
- **SQLite3 CLI**   
- Interpréteur **Python**, version 3.6 ou supérieure   

Programme élaboré avec les logiciels suivants:   
- **Python** v3.12.0 choisissez la version adaptée à votre ordinateur et système. **Python** est disponible à l'adresse suivante ➔ https://www.python.org/downloads/   
- **Git** CLI   
- **SQLite3** CLI   
- Interpréteur **Python**, version 3.6 ou supérieure   

Programme élaboré avec les logiciels suivants:   
- **Python** v3.7.2 choisissez la version adaptée à votre ordinateur et système.   
- **Python** est disponible à l'adresse suivante ➔ https://www.python.org/downloads/   
- **Django** 3.2.20   
- **Bootstrap** 5.3.1   
- **Docker Toolbox** v.19.03.1   
- **Sentry**   
- **Heroku CLI**   
- **SqLite Tools**   
- **GitHub Actions**   
- **Visual Studio Code** 1.70.2   
- **Windows** 7 professionnel SP1   
- **Heroku** CLI   
- **SqLite** Tools   
- **GitHub Actions**   
- **Visual Studio Code** 1.70.2   
- **Windows** 7 professionnel SP1   
  &nbsp;   

- Les scripts **Python** s'exécutent depuis un terminal.   
- Pour ouvrir un terminal sur **Windows**, pressez la touche ``windows + r`` et entrez ``cmd``.   
- Sur **Mac**, pressez la touche ``command + espace`` et entrez ``terminal``.   
- Sur **Linux**, vous pouvez ouviri un terminal en pressant les touches ``Ctrl + Alt + T``.   

--------------------------------------------------------------------------------------------------------------------------------

<div id="tests-et-couverture-de-code"></div>
<a href="#top" style="float: right;">Retour en haut 🡅</a>

### Tests et couverture de code   

- Exécution des tests de plusieurs manières pour garantir la qualité du code.   

##### Exécution de Pytest   

- Pour exécuter des tests à l'aide de **Pytest**, utilisez la commande suivante :   

```bash
$ pytest
```
```bash
lettings/tests.py::TestLettingsApp::test_address_model PASSED                                [  7%]
lettings/tests.py::TestLettingsApp::test_letting_detail_url PASSED                           [ 15%]
lettings/tests.py::TestLettingsApp::test_letting_detail_view PASSED                          [ 23%]
lettings/tests.py::TestLettingsApp::test_letting_model PASSED                                [ 30%]
lettings/tests.py::TestLettingsApp::test_lettings_index_url PASSED                           [ 38%]
lettings/tests.py::TestLettingsApp::test_lettings_index_view PASSED                          [ 46%]
profiles/tests.py::TestProfilesApp::test_profile_detail_url PASSED                           [ 53%]
profiles/tests.py::TestProfilesApp::test_profile_detail_view PASSED                          [ 61%]
profiles/tests.py::TestProfilesApp::test_profile_model PASSED                                [ 69%]
profiles/tests.py::TestProfilesApp::test_profiles_index_url PASSED                           [ 76%]
profiles/tests.py::TestProfilesApp::test_profiles_index_view PASSED                          [ 84%]
profiles/tests.py::TestProfilesApp::test_user_model PASSED                                   [ 92%]
oc_lettings_site/tests.py::test_dummy PASSED                                                 [100%]

================================== 13 passed in 5.79s =============================================
``` 

#### Exécution des tests Django   

- Utilisation des tests **Django**, créer dans les fichiers tests.py des applications ``lettings`` et ``profiles``   
- Utilisation des tests **Django**, créer dans les fichiers tests.py des applications **``lettings``** et **``profiles``**   

```bash
$ python manage.py test
```

Renvoie :   

```bash
Ran 12 tests in 2.981s                            
                                                  
OK                                                
Destroying test database for alias 'default'...   
```
#### Exécution des tests Coverage   

- Utilisation de **Coverage** pour mesurer la couverture de code.   
- Cette commande exécute vos tests en utilisant **Coverage** pour collecter les informations de couverture.   
- Cette commande exécute vos tests en utilisant coverage pour collecter les informations de couverture.   

```bash
$ coverage run manage.py test
```

- Cela affichera un rapport de couverture indiquant le pourcentage de code couvert par vos tests.   
- Vous verrez également les lignes de code qui ont été exécutées (couvertes) ou non exécutées (non couvertes).   

```bash
$ coverage report
```

>_**Renvoie :** **84%** de couverture de code_

```bash
$ coverage html
```
- Cela générera un dossier ``htmlcov`` dans lequel vous pouvez ouvrir le fichier ``index.html`` pour visualiser un rapport interactif de la couverture de code dans votre navigateur.   

--------------------------------------------------------------------------------------------------------------------------------

<div id="creation-environnement"></div>
<a href="#top" style="float: right;">Retour en haut 🡅</a>

### Création de l'environnement virtuel   

- Installer une version de **Python** compatible pour votre ordinateur.   
- Une fois installer ouvrer le cmd (terminal) placer vous dans le dossier principal (dossier racine).   
- Une fois installer ouvrer **le cmd (terminal)** placer vous dans le dossier principal **(dossier racine)**.   

Taper dans votre terminal :   

```bash
$ python -m venv venv
```
Un répertoire appelé ``venv`` doit être créé.   

--------------------------------------------------------------------------------------------------------------------------------

<div id="activation-environnement"></div>
<a href="#top" style="float: right;">Retour en haut 🡅</a>

### Activation de l'environnement virtuel   

- Placez-vous avec le terminal dans le dossier principale **(dossier racine)**.   

Pour activer l'environnement virtuel créé, il vous suffit de taper dans votre terminal :   
>_**Note :** Pour activer l'environnement virtuel créé, il vous suffit de taper dans votre terminal :_   

```bash
$ venv\Scripts\activate.bat
```
- Ce qui ajoutera à chaque ligne de commande de votre terminal ``(venv)`` :   
**Pour désactiver l'environnement virtuel, il suffit de taper dans votre terminal :**   
>_**Note :** Pour désactiver l'environnement virtuel, il suffit de taper dans votre terminal :_   

```bash
$ deactivate
```
--------------------------------------------------------------------------------------------------------------------------------

<div id="installation-librairies"></div>
<a href="#top" style="float: right;">Retour en haut 🡅</a>

### Installation des librairies et dépendances   

##### 1. Installer les librairies   

- Le programme utilise plusieurs librairies externes et modules de **Python**, qui sont répertoriés dans le fichier ``requirements.txt``.   
- Placez-vous dans le dossier où se trouve le fichier requirements.txt avec le terminal, l'environnement virtuel doit être activé.   
- Placez-vous dans le dossier où se trouve le fichier ``requirements.txt`` avec le terminal, l'environnement virtuel doit être activé.   
- Pour faire fonctionner le programme, il vous faudra installer les librairies requises.   
- À l'aide du fichiers ``requirements.txt`` mis à disposition.   

Taper dans votre terminal la commande :   

```bash
$ pip install -r requirements.txt
```

##### 2. Installer les dépendances   

  - Dans un terminal exécuter la commande suivante dans le répertoire du projet.   
  - Cela installera toutes les dépendances spécifiées dans le fichier ``package.json`` ➔ ([package.json](package.json)).   

```bash   
$ npm install
```   

--------------------------------------------------------------------------------------------------------------------------------

<div id="installation-environnement"></div>
<a href="#top" style="float: right;">Retour en haut 🡅</a>

### Installation des variables d'environnement   

- Pour utiliser l'application, il faut configurer l'environnement de l'application **OC Lettings** et générer une clé secrète aléatoire pour la configuration de **Django**.   
- De plus, il est nécessaire d'inclure des noms de variables d'environnement préconfigurées.   

##### Configuration de l'environnement :   

- Créer un modèle de fichier ``.env`` pour **oc_lettings_site**
  avec une clé secrète générée aléatoirement et des variables d'environnement préconfigurées.

- Utiliser le script ``creating_environment_variables.py`` ➔ ([creating_environment_variables.py](creating_environment_variables.py))   
  pour génèrer un fichier ``.env`` qui peut être utilisé pour configurer l'environnement de l'application **oc_lettings_site**   

- Il génère une clé secrète aléatoire pour la configuration de **Django** et inclut également des noms de variables d'environnement préconfigurés tels que :

```bash
'DJANGO_SECRET_KEY'
'SENTRY_DSN'
'HEROKU_APP_NAME'
'DEBUG'
```

##### Création du fichier ``.env`` :   

À la racine du dossier principal **OC Lettings**, créer le fichier ``.env``   
Taper dans votre terminal :   

```bash
$ python creating_environment_variables.py
```

Il est essentiel de configurer l'environnement de l'application.
- Générez une clé secrète aléatoire pour la configuration de **Django** et incluez des noms de variables d'environnement préconfigurées.   

Utilisez le fichier ``.env``, voici un exemple d'un fichier ``.env`` une fois configuré avec les paramètres :   


```bash   
DJANGO_SECRET_KEY=sxkxd_*2rncaz^sg7u5igt3nd&4zl9@s=l5s=n_27k*7z05ktg
SENTRY_DSN=https://2714498e0009ae5e7e5df869ade74b8e@o4505744838623343.ingest.sentry.io/4505744878142551
HEROKU_APP_NAME=oc-lettings-apps
DEBUG=0
```   

##### Configuration du fichier ``.env`` :   

Une fois le fichier ``.env`` créé, ouvrez-le avec un éditeur de texte.   
- Remplissez les champs avec les valeurs appropriées pour chaque variable d'environnement.   
- Ces étapes garantissent une configuration correcte de l'environnement nécessaire au bon fonctionnement de l'application **OC Lettingss**.   

>_**Note :** La clé **SENTRY_DSN** doit être récupérée dans les paramètres de votre compte **Sentry**._   

>_**Note :** Le fichier **.env** généré doit être configuré avec des valeurs appropriées pour chaque variable d'environnement avant utilisation._   

--------------------------------------------------------------------------------------------------------------------------------
<div id="execution-application"></div>
<a href="#top" style="float: right;">Retour en haut 🡅</a>

### Exécution de l'application   

##### Utilisation   

1. Lancement du serveur **Django**.   
- Placez-vous avec le terminal dans le dossier principal.   
- Activer l'environnement virtuel et ensuite lancer le serveur **Django**.   

Taper dans votre terminal la commande :   

```bash
$ python manage.py runserver
```

2. Lancement de l'application dans le navigateur de votre choix.   
Se rendre à l'adresse ➔ http://127.0.0.1:8000/   

**Navigateur**   
>**Note : Les tests ont était fait sur Firefox et Google Chrome.**   

--------------------------------------------------------------------------------------------------------------------------------

<div id="docker-image"></div>
<a href="#top" style="float: right;">Retour en haut 🡅</a>

### Image Docker   

- Une image **Docker** est disponible pour ce projet.   

- Récupérer l'image sur **Docker Hub** ➔ [Image Docker](https://hub.docker.com/r/bubhux/bubhux-oc-image-build/tags)   

```bash   
$ docker pull bubhux/bubhux-oc-image-build:latest
```   

- Lancer l'image en local

```bash   
$ docker run -p 8080:8080 bubhux/bubhux-oc-image-build:latest
$ docker run -it bubhux/bubhux-oc-image-build:latest /bin/sh
```   

- Accéder au dossier du container

```bash   
$ docker run -it bubhux/bubhux-oc-image-build:latest /bin/sh
$ docker exec -it [ID_DU_CONTENEUR] sh
```   

- Retourner dans les logs du conteneur en temps réel

```bash   
$ docker logs -f <ID_OR_NAME>
  ```   

##### Activation de Sentry dans le conteneur en local   

```bash
$ docker exec -it [ID_DU_CONTENEUR] sh
```

```bash
$ pip install django
```

- Ouvrir et visualiser un fichier

```bash
$ - > cat .env
```

- Vérifie la présence d'un fichier

```bash
$ which .env
```

- Exécuter un script **Python** à l'intérieur du conteneur

```bash
$ python creating_environment_variables.py
```

- Editer un fichier

```bash
vi .env
```

- Une fois que l'éditeur **Vi** est ouvert avec votre fichier, appuyez sur ``i`` pour entrer en mode édition **(insertion)**.

- Collez l'URL que vous souhaitez copier à partir du presse-papiers dans l'éditeur **Vi**.

- Pour coller dans **Vi**, faites un clic droit ou utilisez ``Ctrl + v``.

- Après avoir collé le contenu, appuyez sur ``Esc`` pour quitter le mode d'insertion.

- Enregistrez vos modifications en tapant ``:wq`` et appuyez sur Enter.
Se rendre à l'adresse. ➔ http://127.0.0.1:8000/   
 
>_**Note navigateur :** Les tests ont était fait sur **Firefox** et **Google Chrome**._   

--------------------------------------------------------------------------------------------------------------------------------

<div id="rapport-flake8"></div>
<a href="#top" style="float: right;">Retour en haut 🡅</a>

### Rapport avec flake8   

Tapez dans votre terminal la commande :   

```bash
$ flake8
```
- Ne renvoie aucune erreur.   

--------------------------------------------------------------------------------------------------------------------------------

<div id="informations-importantes"></div>
<a href="#top" style="float: right;">Retour en haut 🡅</a>

### Informations importantes sur les différents fichiers et dossiers   

**Le dossier lettings**   
  - Le dossier est une apps **Django** qui contient :   
  - Un dossier ``migrations`` contenant les fichiers de configuration pour la base de données ➔ ([migrations](lettings/migrations))   
  - Á la racine du dossier ``lettings`` les fichiers tels que views.py, tests.py ➔ ([lettings](lettings))   

**Le dossier oc_lettings_site**   
  - Le dossier est une apps **Django** qui contient :   
  - Un dossier ``migrations`` contenant les fichiers de configuration pour la base de données ➔ ([migrations](oc_lettings_site/migrations))   
  - Á la racine du dossier ``oc_lettings_site`` les fichiers tels que settings.py ➔ ([oc_lettings_site](oc_lettings_site))   

**Le dossier profiles**   
  - Le dossier est une apps **Django** qui contient :   
  - Un dossier ``migrations`` contenant les fichiers de configuration pour la base de données ➔ ([migrations](profiles/migrations))   
  - Á la racine du dossier ``profiles`` les fichiers tels que views.py, tests.py ➔ ([profiles](profiles))   

**Le dossier ``lettings``**   
  - Le dossier est une apps **Django** qui contient :   
  - Un dossier ``migrations`` contenant les fichiers de configuration pour la base de données. ➔ ([migrations](lettings/migrations))   
  - Á la racine du dossier ``lettings`` les fichiers tels que views.py, tests.py. ➔ ([lettings](lettings))   

**Le dossier ``oc_lettings_site``**   
  - Le dossier est une apps **Django** qui contient :   
  - Un dossier ``migrations`` contenant les fichiers de configuration pour la base de données. ➔ ([migrations](oc_lettings_site/migrations))   
  - Á la racine du dossier ``oc_lettings_site`` les fichiers tels que settings.py. ➔ ([oc_lettings_site](oc_lettings_site))   

**Le dossier ``profiles``**   
  - Le dossier est une apps **Django** qui contient :   
  - Un dossier ``migrations`` contenant les fichiers de configuration pour la base de données. ➔ ([migrations](profiles/migrations))   
  - Á la racine du dossier ``profiles`` les fichiers tels que views.py, tests.py. ➔ ([profiles](profiles))   

**Le dossier ``.github``**   
  - Le dossier contient le fichier ``ci_cd_branch_master.yml`` ([.github](.github/workflows))   

**Le dossier ``doc``**   
  - Le dossir contient toute la configuration de ``Read the Docs`` et de ``Sphinx`` ([doc](doc))   

**Le dossier ``static``**   
- Dossier qui contient qui contient les images svg des badges et les dossiers nécessaire à ```Bootstrap```.   

--------------------------------------------------------------------------------------------------------------------------------

<div id="auteur-contact"></div>
<a href="#top" style="float: right;">Retour en haut 🡅</a>

### Auteur et contact   

Pour toute information supplémentaire, vous pouvez me contacter.   
**Bubhux :** bubhuxpaindepice@gmail.com   
