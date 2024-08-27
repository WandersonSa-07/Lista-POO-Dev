class Motor:
    def __init__(self):
        self.estado_peca = "bom"
        self.ligado = "Desligado"

    def __str__(self):
        print(self.estado_peca)
        print(self.ligado)

class Carro:
    def __init__(self, modelo, placa):
        self.modelo = modelo
        self.placa = placa
        self.motor = Motor()

    def __str__(self):
        print(self.modelo)
        print(self.placa)
        print(format(self.motor.estado_peca))
        print(format(self.motor.ligado))
        return True

    def darPartida(self):
        self.ligado = "Ligado"  #Posso acessar tanto usando "self.motor.ligado" quanto usando "self.ligado"
        print("O motor está ", self.ligado)

    def desligar(self):
        self.motor.ligado = "Desligado"   #Posso acessar tanto usando "self.motor.ligado" quanto usando "self.ligado
        print("O motor está ", self.motor.ligado)

    def estadoMotor(self, estado):
        self.estado_peca = estado
        print("As peças do motor se encontram ", self.estado_peca)

carro = Carro("Go", "123-ABC")
carro.__str__()
carro.darPartida()
carro.estadoMotor("bem")
carro.__str__()
carro.desligar()