class Jogo:
    def __init__(self,dev,tamanho,valor,ano):
        self.dev = dev
        self.tamanho = tamanho
        self.valor = valor
        self.ano = ano
    
    def get_dev(self):
        return self.dev
    
    def set_dev(self):
        self.dev = int(input("Digite a desenvolvedora do jogo: "))


    def get_tamanho(self):
        return self.tamanho
    
    def set_tamanho(self):
        self.tamanho = str(input("Digite o tamanho do jogo em GB: "))


    def get_valor(self):
        return self.valor
    
    def set_valor(self):
        self.valor = str(input("Digite o valor do jogo: "))
    

    def get_ano(self):
        return self.ano
    
    def set_ano(self):
        self.ano = str(input("Digite o ano de publicação do jogo: "))
    
    
    def get_all(self):
        return self.dev, self.tamanho, self.valor, self.ano

#Tamanho em GB
Call_of_duty = Jogo("Activision" , 13.5 , 49.99 , 2003)
Team_Fortres_2 = Jogo("Valve" , 13.8 , 00.00 , 2007)
Couter_Strike = Jogo("Valve" , 0.304 , 00.00 , 2000)


#todos os set's
print(Call_of_duty.set_dev())
print(Call_of_duty.set_tamanho())
print(Call_of_duty.set_valor())
print(Call_of_duty.set_ano())

#todos os get's
print(Call_of_duty.get_dev())
print(Call_of_duty.get_tamanho())
print(Call_of_duty.get_valor())
print(Call_of_duty.get_ano())
print(Call_of_duty.get_all())