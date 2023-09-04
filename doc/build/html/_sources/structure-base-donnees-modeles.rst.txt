Description de la structure de la base de données et des modèles de données
***************************************************************************

.. |sqlite-logo| image:: _static/sqlite-logo-rectangle.svg
   :alt: SqLite Logo
   :width: 80px

.. |python-logo| image:: _static/python-logo-only.svg
   :alt: Python Logo
   :width: 20px

Structure de la base de données |sqlite-logo|
=============================================

Dans le cadre de ce projet Django, nous avons opté pour l'utilisation de la base de données SQLite3. SQLite3 est un système de gestion de base de données relationnelles léger, efficace et performant. Il est idéal pour les petites et moyennes applications web.

L'avantage d'SQLite3 réside dans sa facilité d'utilisation et sa portabilité. Il est intégré directement dans Django, ce qui signifie que vous n'avez pas besoin d'installer un système de gestion de base de données externe. Vous pouvez accéder à votre base de données SQLite3 de deux manières principales :

1. **Via la ligne de commande SQLite3 CLI :** Vous pouvez utiliser l'outil en ligne de commande SQLite3 CLI pour interagir directement avec la base de données, exécuter des requêtes SQL, et examiner les données. Pour utiliser cet outil, assurez-vous d'avoir SQLite3 installé sur votre système, puis exécutez la commande `sqlite3 chemin_vers_la_base_de_données` pour ouvrir la base de données.

2. **Via l'interface d'administration de Django :** Django fournit une interface d'administration conviviale qui permet de gérer facilement les données de l'application. Vous pouvez accéder à cette interface en démarrant le serveur de développement Django et en vous rendant sur la page d'administration dans votre navigateur web a l'adresse (http://127.0.0.1:8000/admin/). À partir de là, vous pouvez ajouter, modifier ou supprimer des données, et effectuer diverses opérations de gestion de la base de données.

.. note::
   - En résumé, la structure de la base de données de notre projet repose sur SQLite3, offrant ainsi une solution légère, performante et pratique pour le stockage et la gestion des données de l'application.

1. Utilisation de SQLite3
-------------------------

.. code-block:: shell

   (venv) C:\Users\Bubhux\Desktop\OP projet 13\Orange-County-Lettings\Python-OC-Lettings-FR>sqlite3
   SQLite version 3.42.0 2023-05-16 12:36:15
   Enter ".help" for usage hints.

2. Ouverture de la base de données
----------------------------------

Pour ouvrir une base de données existante, utilisez la commande suivante :

.. code-block:: shell

   .open oc-lettings-site.sqlite3

3. Liste des tables
-------------------

Pour afficher la liste des tables dans la base de données, utilisez la commande :

.. code-block:: shell

   .tables

4. Informations sur la table "profiles_profile"
-----------------------------------------------

Pour afficher les informations sur les colonnes de la table "profiles_profile", utilisez la commande suivante :

.. code-block:: shell

   pragma table_info(profiles_profile);

5. Exemple de requête
---------------------

Pour effectuer une requête sur la table "profiles_profile" pour sélectionner les utilisateurs dont la ville favorite commence par "B", utilisez la commande suivante :

.. code-block:: shell

   SELECT user_id, favorite_city FROM profiles_profile WHERE favorite_city LIKE 'B%';

6. Quitter SQLite3
------------------

Pour quitter SQLite3, utilisez la commande suivante :

.. code-block:: shell

   .quit


Modèles de données |python-logo|
================================

1. Modèles de données Python
----------------------------

Les modèles de données sont essentiels pour la définition de la structure de la base de données et la gestion des informations de l'application. Dans notre projet, nous utilisons le langage de programmation Python pour créer ces modèles.

Les modèles Django représentent les différentes entités et relations au sein de l'application. Chaque modèle est associé à une table de base de données, et les champs du modèle correspondent aux colonnes de la table. Ces modèles permettent de définir comment les données seront stockées et manipulées.

Par exemple, voici un modèle de classe de notre projet :

.. code-block:: python

   from django.db import models

   class Letting(models.Model):
      """
      Représente une location avec un titre et une adresse associée.
      """
      title = models.CharField(max_length=256)
      address = models.OneToOneField(Address, on_delete=models.CASCADE)

      def __str__(self):
         """
         Renvoie une représentation lisible par l'humain de la location.
         """

         # Méthode logger_debug pour enregistrer des messages de débogage.
         logger.debug("Location convertie en chaîne : %s, Adresse : %s", self.title, self.address)
         return self.title

Dans cet exemple, nous avons un modèle de données appelé **Letting** avec des champs tels que **title** et **address**.

Les relations entre les modèles, telles que les clés étrangères et les clés primaires, sont également définies dans les modèles Django, ce qui garantit la cohérence et l'intégrité des données.

L'utilisation du langage Python pour la définition des modèles facilite la création et la gestion de la base de données. Vous pouvez définir des modèles de manière intuitive en utilisant des classes Python, ce qui rend le code plus lisible et maintenable.

.. note::
   En résumé, la base de données SQLite3 associée aux modèles Django forme le socle de données de l'application, permettant de stocker et de récupérer efficacement les informations nécessaires au bon fonctionnement de l'application web.
