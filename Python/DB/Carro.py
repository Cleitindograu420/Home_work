import _sqlite3

database = "Carro.db"
conex = _sqlite3.connect(database)
cursor = conex.cursor()

sql = '''create table tb_Carro(
        fabricante primary key, 
        nome text not null, 
        chassi int not null, 
        placa text, 
        ano_fabri text)'''

sql = '''INSERT INTO tb_Carro
        VALUES('Volvo', '850', '9753', 'kuka', '1990')'''

sql = "SELECT * FROM tb_Carro"
regi = cursor.fetchall()
cursor.execute(sql)
