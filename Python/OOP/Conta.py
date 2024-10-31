class Conta():
    def __init__(self,nome,saldo=0.0):
        self.nome = nome
        self.saldo = saldo
    
    def get_nome(self):
        return self.nome
    
    def set_nome(self):
        self.nome = str(input("Digite o novo nome: "))

    def get_saldo(self):
        return self.saldo
    
    def set_saldo(self):
        self.saldo = float(input("Digite o novo saldo: "))

    def get_all(self):
        print(f"O nome da conta é {self.nome}, e o saldo é de R${self.saldo}")

class PF():
    def __init__(self,nome,saldo=0,CPF="000.000.000-00",genero=" "):
        super.__init__(nome,saldo)
        self.CPF = CPF
        self.genero = genero

    def get_genero(self):
        return self.genero
    
    def set_genero(self):
        self.genero = str(input("Digite o novo CPF"))

    def get_CPF(self):
        return self.CPF
    
    def set_CPF(self):
        self.CPF = str(input("Digite o novo CPF"))


class PJ():
    def __init__(self,nome,saldo = 0, CNPJ = "00.000.000/0001-00", modalidade = " "):
        super.__init__(nome,saldo)
        self.CNPJ = CNPJ
        self.modalidade = modalidade

    def get_modalidade(self):
        return self.modalidade
    
    def set_modalidade(self):
        self.modalidade = str(input("Digite o novo CPF"))

    def get_CNPJ(self):
        return self.CNPJ
    
    def set_CNPJ(self):
        self.CNPJ = str(input("Digite o novo CNPJ"))
    
    def deposito (self):
        self.saldo + float(input("Digite o valor do deposito: "))
    
    def saque (self):
        self.saldo - float(input("Digite o valor: "))


if __name__ == "__main__":
    c1 = Conta("Rafael", 45000.99)