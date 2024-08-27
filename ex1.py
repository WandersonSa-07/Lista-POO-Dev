class Pessoa:
    # __init__(): inicia o futuro obejto preenchendo as suas caracteristicas.
    def __init__(self, nome, idade): #Funcao que inicializa o futuro objeto
        self.nome = nome
        self.idade = idade

    #__str__(): imprime as informacoes
    def __str__(self):
        print(self.nome)
        print(self.idade)
        return True
    
    def mostrar_nome(self):
        print("Meu nome eh ", self.nome)

    def mostrar_idade(self):
        print("Eu tenho ",self.idade," anos")

#Instanciando o objeto
pessoa1 = Pessoa("Wanderson", 21)
pessoa1.__str__()
pessoa1.mostrar_idade()
pessoa1.mostrar_nome()
