class Animal:
    def __init__(self, filoChordata): # é o filo de animais com coluna vertebral: aves, mamíferos, répteis, anfíbios, peixes
        self.filoChordata = filoChordata

    def __str__(self):
        print(self.filoChordata)
        return True
    
    def emitirSom(self, som):
        print(som)


class Cachorro(Animal):
    def __init__(self, filoChordata):
        super().__init__(filoChordata)

    def __str__(self):
        return super().__str__()
    
    def emitirSom(self):
        print("Au! Au! Au!")

class Gato(Animal):
    def __init__(self, filoChordata):
        super().__init__(filoChordata)

    def __str__(self):
        return super().__str__()
    
    def emitirSom(self):
        print("MIAU!")


cachorro = Cachorro("Mamifero")
gato = Gato("Mamifero")

cachorro.emitirSom()
gato.emitirSom()
