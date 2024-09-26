class Ponto():
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x
    
    def set_x(self):
        self.x = float(input("Digite o valor de X: "))

    def get_y(self):
        return self.y
    
    def set_y(self):
        self.y = float(input("Digite o valor de Y: "))

    def get_all(self):
        print(f"O valor de X é:{(self.x)}")
        print(f"O valor de Y é:{(self.y)}")

plano1 = Ponto(10,5)
plano2 = Ponto(2,3)
plano3 = Ponto(3)
plano4 = Ponto(y=5)

while True:
    print("="*90)
    #otp_plano = int(input("Selecione um plano: "))
    opt = int(input('''Selecione uma opção:
[1] - Mostrar X e Y
[2] - Alterar X ou Y
'''))
    
    if opt == 1:
        plano1.get_all()
    
    if opt == 2:
        eixo_raw = str(input("X ou Y: "))
        eixo = eixo_raw.lower()
        
        if eixo == "x":
            plano1.set_x()
        
        if eixo == "y":
            plano1.set_y()

