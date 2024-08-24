class Carro:
    def __init__(self,ano,marca,cor,potencia):
        self.ano = ano
        self.marca = marca
        self.cor = cor
        self.potencia = potencia
    
    def get_ano(self):
        return self.ano
    
    def set_ano(self):
        self.ano = int(input("Digite o ano do carro: "))
    
    def get_marca(self):
        return self.marca
    
    def set_marca(self):
        self.marca = str(input("Digite a marca do carro: "))
    
    def get_cor(self):
        return self.cor
    
    def set_cor(self):
        self.cor = str(input("Digite a cor do carro: "))
    
    def get_potencia(self):
        return self.potencia
    
    def set_potencia(self):
        self.potencia = str(input("Digite quantos cavalos de potencia tem o carro: "))
    
    def get_all(self):
        return self.ano, self.marca, self.cor, self.potencia

GTR_R33 = Carro(1995,"Nissan","Prata",485)
Stratos_HF = Carro(1973,"Lancia","Azul",280)
Volvo_850 = Carro(1991,"Volvo","Preto",225)

#todos os set's
print(GTR_R33.set_ano())
print(GTR_R33.set_marca())
print(GTR_R33.set_cor())
print(GTR_R33.set_potencia())

#todos os get's
print(GTR_R33.get_ano())
print(GTR_R33.get_marca())
print(GTR_R33.get_cor())
print(GTR_R33.get_potencia())
print(GTR_R33.get_all())