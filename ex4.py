class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2


    def __str__(self):
        print(self.numero1)
        print(self.numero2)
        return True
    
    def soma(self):
        print(self.numero1 + self.numero2)

    def subtracao(self):
        print(self.numero1 - self.numero2)

    def multiplicacao(self):
        print(self.numero1 * self.numero2)
        
    def divisao(self):
        print(self.numero1 / self.numero2)


operacao = Calculadora(20, 2)
operacao.soma()
operacao.subtracao()
operacao.multiplicacao()
operacao.divisao()