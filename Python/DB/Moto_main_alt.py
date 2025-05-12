import mysql.connector

conex = mysql.connector.connect (user = 'root',
                                       password = '123456',
                                       host = 'localhost',
                                       database = 'db_Moto')

cursor = conex.cursor()

sql = '''CREATE TABLE IF NOT EXISTS tb_Moto(
        id_moto INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        fabricante VARCHAR(20), 
        nome VARCHAR(30) NOT NULL, 
        chassi INT NOT NULL UNIQUE, 
        placa VARCHAR(7), 
        ano_fabri DATE,
        preço DECIMAL (10, 2))'''
cursor.execute(sql)
conex.commit()

#sql = '''INSERT INTO  tb_Moto (fabricante, nome, chassi, placa, ano_fabri , preço)
#        VALUES('Suzuki', 'GSX', '123456', 'cpf2204', 2008, 20000.90);'''
#cursor.execute(sql)
#conex.commit()

#sql = '''INSERT INTO tb_Moto (fabricante, nome, chassi, placa, ano_fabri , preço)
#        VALUES('Yamaha', 'XJ6', '654321', 'joj2469', 2020, 10000.90),
#            ('Kawasaki', 'Ninja', '162534', 'lol6666', 1984, 30000.90);'''
#cursor.execute(sql)
#conex.commit()


cursor.execute("SELECT * FROM tb_Moto")
resultados = cursor.fetchall()

while True:

    op = int(input(
        f" 1 - Ver a tabela toda \n 2 - Inserir moto nova na tabela \n 3 - Limpar tabela \n 4- Deletar uma moto \n 5 - Finalizar \n Escolha uma opção: "))

    if op == 1:
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

    elif op == 2:
        fabricante = str(input("Digite a fabricante da Moto: "))
        nome = str(input("Digite o nome da Moto: "))
        chassi = int(input("Digite o chassi da Moto: "))
        placa = str(input("Digite a placa da Moto: "))
        ano_fabri = str(input("Digite o ano de fabricação da Moto: "))
        preço = str(input("Digite o valor da Moto: "))
        sql = '''INSERT INTO tb_Moto (fabricante, nome, chassi, placa, ano_fabri, preço)
                        VALUES('{}', '{}', '{}', '{}', '{}', '{}');'''.format(fabricante, nome, chassi, placa, ano_fabri, preço)
        cursor.execute(sql)
        conex.commit()
        cursor.close()
        conex.close()

    elif op == 3:
        sql = '''DELETE FROM tb_Moto;'''
        cursor.execute(sql)
        conex.commit()
        cursor.close()
        conex.close()


    elif op == 4:
        c_moto = input("Digite o chassi da moto que deseja excluir: ")
        sql = f'''DELETE FROM tb_Moto WHERE chassi = '{c_moto}' ;'''
        cursor.execute(sql)
        conex.commit()
        cursor.close()
        conex.close()

    elif op == 5:
        break

    else:
        print("Opção invalida")
