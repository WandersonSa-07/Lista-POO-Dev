# 1. Crie uma classe chamada conta bancaria com metodo calcular rendimento,em seguida crie subclasses: Conta-corrente, Conta-poupança e conta investimento. Cada uma implementando sua propria versão do metodo calcular rendimento. Levando em consideração de diferentes taxas de investimento, Crie uma lista contendo diferentes contas e calcula e calcule cada uma usando polimorfismo.
# A partir do código abaixo crie uma classe conta bancaria com atributos privados, saldo e titular. Implemente método para depositar e sacar garantido que o saldo nao ficara indicativo. 

from abc import ABC

       
class Conta_Banc(ABC):

    def __init__(self, saldo, titular):
        self._saldo = saldo
        self._titular = titular

    def calcularRend(self,temp_Meses):
        return ((1+self.tx_rend)**temp_Meses)*self.saldo

       
class Conta_Cor(Conta_Banc):
        def __init__(self,saldo):
            super().__init__(saldo)
            self.tx_rend = 0

class Conta_Poup(Conta_Banc):
        def __init__(self,saldo):
            super().__init__(saldo)
            self.tx_rend = 0.01

class Conta_Invest(Conta_Banc):
        def __init__(self,saldo):
            super().__init__(saldo)
            self.tx_rend = 0.02
   

def __main__():
    c1 = Conta_Cor(2000)
    c2 = Conta_Poup(2000)
    c3 = Conta_Invest(2000)

    lista_contas = [c1,c2,c3]
    for x in lista_contas:
        print(x.calcularRend(3))
if __name__ == '__main__':
    __main__()