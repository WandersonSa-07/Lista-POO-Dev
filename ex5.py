class Veiculo:
    def __init__(self, marca, modelo, placa):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa

    def __str__(self):
        print(self.marca)
        print(self.modelo)
        print(self.placa)
        return True
    
class Carro(Veiculo):
    def __init__(self, marca, modelo, placa, portas):
        super().__init__(marca, modelo, placa)
        self.portas = portas

    def __str__(self):
        super().__str__()
        print(self.portas)
        return True

    def darPartida(self):
        print("Carro ligado")

carro = Carro("GO", "HB20", "ABC", 4)
carro.__str__()
carro.darPartida()