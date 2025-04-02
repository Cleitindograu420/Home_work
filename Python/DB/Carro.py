import _sqlite3

database = "Carro.db"
conex = _sqlite3.connect(database)
cursor = conex.cursor()
sql = '''create table if not exists tb_Carro(
        fabricante text , 
        nome text not null, 
        chassi int not null, 
        placa text primary key, 
        ano_fabri int)'''
cursor.execute(sql)

sql = '''INSERT INTO tb_Carro (fabricante, nome, chassi, placa, ano_fabri)
        VALUES('Nissan', '370Z', '123456', 'cpf-2204', 2000);'''
cursor.execute(sql)
conex.commit()

sql = '''INSERT INTO tb_Carro (fabricante, nome, chassi, placa, ano_fabri)
        VALUES('Volvo', '850', '654321', 'cfc-3306', 1980);'''
cursor.execute(sql)
conex.commit()

sql = '''INSERT INTO tb_Carro (fabricante, nome, chassi, placa, ano_fabri)
        VALUES('Nissan', 'GT-R R33', '615234', 'jek-6969', 2010);'''
cursor.execute(sql)
conex.commit()

sql = '''INSERT INTO tb_Carro (fabricante, nome, chassi, placa, ano_fabri)
        VALUES('Pegeot', '250', '694202', 'kct-4079', 1990);'''
cursor.execute(sql)
conex.commit()



while True:
        
        op = int(input(f" 1 - Ver a tabela toda \n 2 - Inserir carro novo na tabela \n 3 - Limpar tabela \n 4- Finalizar \n Escolha uma opção: "))
        if op == 1:
                sql = "SELECT * FROM tb_Carro"
                cursor.execute(sql)
                l_reg = cursor.fetchall()
                print(l_reg)

        elif op == 2:
                fabricante = str(input("Digite a fabricante do carro: "))
                nome = str(input("Digite o nome do carro: "))
                chassi = int(input("Digite o chassi do carro: "))
                placa = str(input("Digite a placa do carro: "))
                ano_fabri = int(input("Digite o ano de fabricação do carro: "))
                sql = '''INSERT INTO tb_Carro (fabricante, nome, chassi, placa, ano_fabri)
                        VALUES('{}', '{}', '{}', '{}', '{}');'''.format(fabricante, nome, chassi, placa, ano_fabri)
                cursor.execute(sql)
                conex.commit()
        
        elif op == 3:
                sql = '''DELETE FROM tb_Carro'''
                cursor.execute(sql)
                conex.commit()

        elif op == 4:
                break

        else:
                print("Opção invalida")
