class Aluno():
    def __init__(self, matricula):
        self.matricula = matricula
        self.nome = None
        self.noa = None

    def inserir_nome(self, nome):
        self.nome = nome

    def inserir_nota(self, nota):
        if nota >= 0 or nota <= 10:
            self.nota = nota
        else:
            print("Valor invalido")

class Escola():
    def __init__(self):
       self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_alunos(self):
        for cadaAluno in self.alunos:
            print(cadaAluno.nome)
        

if __name__=='__main__':
    minha_escola = Escola()
    a1 = Aluno(123)
    a1.inserir_nome("João")
    a1.inserir_nota(6)
    a2 = Aluno(456)
    a2.inserir_nome("Wanderson")
    a2.inserir_nota(9)
    a3 = Aluno(789)
    a3.inserir_nome("Kaue")
    a3.inserir_nota(7)
    minha_escola.adicionar_aluno(a1)
    minha_escola.adicionar_aluno(a2)
    minha_escola.adicionar_aluno(a3)
    minha_escola.listar_alunos()
