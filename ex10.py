import abc

class FormaGeometrica(abc.ABC):
    @abc.abstractmethod
    def calcularArea(self, figura):
        print("A area do ", figura, ": ", self.base * self.altura,"\n")
    
class Quadrado(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(sel):
        return super().calcularArea("quadrado")
    
class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcularArea(self):
        print("Area do circulo: ", 3.14159265359 * ((self.raio)**2),"\n")
    
if __name__=='__main__':
    quadradro = Quadrado(2,2)
    circulo = Circulo(3)
    quadradro.calcularArea()
    circulo.calcularArea()
