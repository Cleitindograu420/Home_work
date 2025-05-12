import mysql.connector

conex = mysql.connector.connect (user = 'root',
                                       password = '123456',
                                       host = 'localhost',
                                       database = 'db_moto')

curs = conex.cursor()

sql = '''CREATE TABLE IF NOT EXISTS tb_Moto(
        fabricante VARCHAR(20) , 
        nome VARCHAR(30) not null, 
        chassi int not null, 
        placa VARCHAR(7) primary key, 
        ano_fabri int,
        preço decimal (10, 2))'''
curs.execute(sql)

sql = '''INSERT INTO tb_Moto (fabricante, nome, chassi, placa, ano_fabri , preço)
        VALUES('Suzuki', 'GSX', '123456', 'cpf2204', 2008, 20000.90);'''
curs.execute(sql)
conex.commit()

sql = '''INSERT INTO tb_Moto (fabricante, nome, chassi, placa, ano_fabri , preço)
        VALUES('Yamaha', 'XJ6', '654321', 'joj2469', 2020, 10000.90);'''
curs.execute(sql)
conex.commit()

sql = '''INSERT INTO tb_Moto (fabricante, nome, chassi, placa, ano_fabri , preço)
        VALUES('Kawasaki', 'Ninja', '162534', 'lol6666', 1984, 30000.90);'''
curs.execute(sql)
conex.commit()

curs.execute("SELECT * FROM tb_Moto")

resultados = curs.fetchall()


if len(resultados) == 0:
    print("Tabela vazia.")

else:

    print("\nResultado na Horizontal:")
    for linha in resultados:
        print("\t".join(str(valor) for valor in linha))


    print("\nResultado na Vertical:")
    for linha in resultados:
        for i, valor in enumerate(linha):
            print(f"Coluna {i + 1}: {valor}")
        print("-" * 20)

curs.close()
conex.close()