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

'''Explicação:
Atributo de classe
total_alunos = 0


Esse atributo não pertence a um aluno específico.

Ele pertence à classe Aluno inteira.

Isso significa que todos os objetos compartilham esse valor.

2. Construtor (__init__)
def __init__(self, nome):
    self.nome = nome
    Aluno.total_alunos += 1


Quando criamos um novo aluno (Aluno("Ana")), o Python roda esse código.

self.nome = nome → guarda o nome dentro do objeto.

Aluno.total_alunos += 1 → aumenta em +1 o contador de alunos.

Então, se eu criar 3 alunos, o contador chega em 3.

3. Método normal (exibir_info)
def exibir_info(self):
    print(f"Nome do aluno: {self.nome}")


Esse método é chamado a partir de um objeto específico (a1.exibir_info()).

Ele mostra só o nome daquele aluno.

4. Método de classe (@classmethod)
@classmethod
def exibir_total_alunos(cls):
    print(f"Total de alunos criados: {cls.total_alunos}")


@classmethod cria um método ligado à classe (não a um objeto).

Ele usa cls (classe) no lugar de self (objeto).

Aqui, ele mostra quantos alunos já foram criados no total.

5. Criando e testando
a1 = Aluno("Ana")
a2 = Aluno("Carlos")
a3 = Aluno("Maria")


Cada vez que você cria um aluno, o contador aumenta.

No final, Aluno.exibir_total_alunos() mostra quantos foram criados.

👉 Resumindo:

self → guarda informações de um aluno específico.

total_alunos → guarda informação da classe inteira.

Cada vez que criamos um aluno, o contador sobe.'''