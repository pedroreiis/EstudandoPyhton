'''Exercício 5 – Contador

Crie uma classe Aluno que tenha:

Atributo nome

Um atributo de classe total_alunos que conta quantos alunos já foram criados.'''

class Aluno():
  
    total_alunos = 0

    def __init__(self, nome):
        self.nome = nome
        Aluno.total_alunos += 1

    def exibir_info(self):
        print(f"Nome do aluno: {self.nome}")

    @classmethod
    def exibir_total_alunos(cls):
        print(f"Total de alunos criados: {cls.total_alunos}")


# Testando
a1 = Aluno("Ana")
a2 = Aluno("Carlos")
a3 = Aluno("Maria")
a4 = Aluno("Pedro")

a1.exibir_info()
a2.exibir_info()
a3.exibir_info()
a4.exibir_info()

Aluno.exibir_total_alunos() 