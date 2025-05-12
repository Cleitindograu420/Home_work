import mysql.connector

conex = mysql.connector.connect (user = 'root',
                                       password = '123456',
                                       host = 'localhost',
                                       database = 'db_moto')

curs = conex.cursor()

sql = '''CREATE TABLE IF NOT EXISTS tb_Livros(
        titulo varchar(50) not null unique,
        publicadora varchar(40),
        data_publi date not null,
        id_livro integer primary key auto_increment,
        preco decimal (10,2)
        )'''
curs.execute(sql)

#sql = '''INSERT INTO tb_Livros (titulo, publicadora, data_publi, preco)
#        VALUES('Naruto', 'Panini', '1999-9-21', 49.90);'''
#curs.execute(sql)
#conex.commit()

#sql = '''INSERT INTO tb_Livros (titulo, publicadora, data_publi, preco)
#        VALUES('Divina comedia ', '', '1321-1-1', 69.90);'''
#curs.execute(sql)
#conex.commit()

#sql = '''INSERT INTO tb_Livros (titulo, publicadora, data_publi, preco)
#        VALUES('attack on titan', 'Panini', '2007-1-1', 39.50);'''
#curs.execute(sql)
#conex.commit()

#sql = '''INSERT INTO tb_Livros (titulo, publicadora, data_publi, preco)
#        VALUES('harry potter', 'Rocco', '1997-6-26', 76.30);'''
#curs.execute(sql)
#conex.commit()


#sql = '''INSERT INTO tb_Livros (titulo, publicadora, data_publi, preco)
#        VALUES('initial-d', 'Panini', '1983-9-21', 69.90), ('O corvo', '', '1845-1-26', 16.55)'''
#curs.execute(sql)
#conex.commit()



curs.execute("SELECT * FROM tb_Livros")
resultados = curs.fetchall()
print(resultados)

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


valor = input(f"Digite o valor para pesquisar na coluna: ")
coluna = input("Digite qual coluna a pesquisa sera feita: ")


query = f"SELECT * FROM tb_livros WHERE {coluna} LIKE %s"
curs.execute(query, (f"%{valor}%",))

resultados = curs.fetchall()

if resultados:
    for linha in resultados:
        print(linha)
else:
    print("Tabela vazia")

