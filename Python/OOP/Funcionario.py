class Funcionario:
    def __init__(self,nome, salario = 0):
        self.nome = nome
        self.salario = salario

    def get_nome(self):
        return self.nome
    
    def set_nome(self):
        self.nome = str(input("Digite o novo nome: "))
    
    def get_salario(self):
        return self.salario
    
    def set_salario(self):
        self.salario = int(input("Digite o novo valor do salario: "))

    def show_all(self):
        print(f"Nome do Funcionario {self.get_nome}")
        print(f"Salario do Funcionario {self.get_salario}")

class Gerente(Funcionario):
    def __init__(self,nome,salario,n_func = 1):
        super().__init__(nome, salario)
        self.n_func = n_func
        
    def get_n_func(self):
        return self.n_func
    
    def set_n_func(self):
        self.n_func = int(input("Digite a nova quantidade de funcionarios: "))

    
    def show_all(self):
        print(f"Nome do Gerente {self.get_nome}")
        print(f"Salario do Gerente {self.get_salario}")
        print(f"Salario do Gerente {self.get_n_func}")


if __name__ == '__main__':
    func1 = Funcionario("Rafael", 35000)
    func2 = Funcionario("Mateus", 17000)
    func3 = Funcionario("Lorena")
    gere1 = Gerente("Lucão",5000,20)

    print(gere1.get_nome())