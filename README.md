# ElasticSearch---SGBDR

### Partie 1: Installation et Configuration du SGBDR & peuplement des données

#### Étapes détaillées avec lignes de code :

1. **Choix de l'Environnement :**
   - Vous pouvez opter pour une configuration sur un serveur unique ou des conteneurs Docker. (ici nous partirons sur l'emploi de Docker)

2. **Installation du SGBDR :**
   - Pour installer MariaDB via Docker, exécutez la commande suivante :
     ```bash
     docker run --name mon_serveur_mariadb -e MYSQL_ROOT_PASSWORD=monmotdepasse -d mariadb
     ```

3. **Création de données fictives :**
   - Utilisez un outil de génération de données fictives comme Faker en Python. Voici un exemple de code pour générer des données fictives en Python avec Faker :
     ```python
     from faker import Faker
     import mysql.connector

     fake = Faker()

     # Connectez-vous à votre base de données MariaDB
     db = mysql.connector.connect(
         host="localhost",
         user="root",
         password="monmotdepasse",
         database="votre_base_de_donnees"
     )
     cursor = db.cursor()

     # Générez des données fictives et insérez-les dans votre base de données
     for _ in range(10):  # Exemple pour insérer 10 enregistrements
         nom = fake.name()
         adresse = fake.address()
         cursor.execute("INSERT INTO table (nom, adresse) VALUES (%s, %s)", (nom, adresse))

     db.commit()
     ```

4. **Validation :**
   - Utilisez un client SQL comme MySQL Workbench pour requêter les données depuis votre base de données MariaDB.


### Partie 2: Synchronisation des données du SGBDR avec ElasticSearch

#### Étapes détaillées avec lignes de code :

1. **Choix de l'Environnement :**
   - Vous pouvez décider de configurer le service Logstash sur un serveur unique ou via des conteneurs Docker.

2. **Installation de Logstash :**
   - Pour installer Logstash via Docker, utilisez la commande suivante :
     ```bash
     docker run -d --name mon_logstash docker.elastic.co/logstash/logstash:7.15.1
     ```

3. **Configuration de pipeline de données :**
   - Créez un fichier de configuration Logstash pour définir une récupération de données depuis le SGBDR et leur envoi vers ElasticSearch. Voici un exemple de configuration Logstash :
     ```conf
     input {
       jdbc {
         jdbc_connection_string => "jdbc:mysql://localhost:3306/votre_base_de_donnees"
         jdbc_user => "root"
         jdbc_password => "monmotdepasse"
         jdbc_driver_library => "/path/to/mysql-connector-java.jar"
         jdbc_driver_class => "com.mysql.cj.jdbc.Driver"
         statement => "SELECT * FROM table"
       }
     }

     output {
       elasticsearch {
         hosts => ["localhost:9200"]
         index => "nom_de_l_index"
       }
     }
     ```

4. **Validation :**
   - Assurez-vous que les données peuvent être requêtées depuis ElasticSearch en utilisant des requêtes de recherche Elasticsearch.
