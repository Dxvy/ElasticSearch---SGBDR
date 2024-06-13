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
