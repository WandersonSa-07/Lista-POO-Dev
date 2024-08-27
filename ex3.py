class Produto:
    #Construtor
    def __init__(self, nome, preco, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    def __str__(self):
        print(self.nome)
        print(self.preco)
        print(self.quantidade_estoque)
        return True
    

produto1 = Produto("Caneta", 10.00, 100)
produto2 = Produto("Lapis", 2.00, 200)
produto3 = Produto("Borracha", 3.00, 50)

produto1.__str__()
produto2.__str__()
produto3.__str__()
