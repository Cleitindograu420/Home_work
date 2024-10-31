from abc import ABC, abstractmethod

class Carro(ABC):
    preço = 100

    @classmethod
    def get_preço(cls):
        return cls.preço
    @classmethod
    
    def set_preço(cls):
        cls.preço = float(input("Digite o valor do carro: "))
    
    def __init__(self,modelo):
        self.modelo = modelo
    
    def get_modelo(self):
        return self.modelo
    
    def set_modelo(self):
        self.modelo = str(input("Digite o modelo do carro: "))

    @abstractmethod
    def preço_diario(self):
        pass

class Economico(Carro):
    def __init__(self, modelo,km_l):
        super().__init__(modelo)
        self.km_l = km_l

    def preço_diario(self):
        val_diario = Carro.get_preço() * 1.5
        return val_diario
    
    def get_km_l(self):
        return self.km_l
    
    def set_km_l(self):
        self.km_l = float(input("DIgite quantos KM/L o carro faz: "))


if __name__ == "__main__":
    #c1 = Carro("Mazda")
    c2 = Economico("E36",9.7)
    c3 = Economico("HB20",14,9)

    #print(c1.get_modelo())
    print(c2.get_km_l())
    print(c3.get_km_l())


