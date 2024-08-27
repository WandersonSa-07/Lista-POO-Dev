
class ContaBancaria: 
    def __init__(self, saldo):
        self.__saldo = saldo #Para tornar como privado é preciso colocar 2 "_", ficando: sel.__atributo = atributo

    def __str__(self):
        print(self.saldo)
        return True
    
    def depositar(self,valor):
        self.__saldo = self.__saldo + valor
        
    def sacar(self,valor):
        self.__saldo = self.__saldo - valor

    def consultarSaldo(self):
        print("Seu saldo: ", self.__saldo)

cliente = ContaBancaria(600)
cliente.consultarSaldo()
cliente.depositar(100)
cliente.consultarSaldo()
cliente.sacar(50)
cliente.consultarSaldo()
