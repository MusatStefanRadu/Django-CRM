import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Radoi2004!',
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE daza_de_bata_django")

print("All Done!")