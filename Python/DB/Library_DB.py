import mysql.connector

conex_db = mysql.connector.connect (user = 'root',
                                       password = '123456',
                                       host = 'localhost',)

print('Conexão:', conex_db)
cursor_db = conex_db.cursor()
cursor_db.execute("CREATE DATABASE IF NOT EXISTS db_Livraria")
cursor_db.close()
conex_db.close()
print("Fechou o trem")
