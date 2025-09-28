'''Exercício 3: Construtor

Crie uma classe Pessoa que receba nome e idade no construtor (__init__)
E um método que diga se a pessoa é maior de idade ou não.'''

class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def verificar_idade(self):
        if self.idade >= 18:
            print(f'{self.nome} é maior de idade.')
        else:
            print(f'{self.nome} é menor de idade.')

pessoa1 = Pessoa('Pedro', 23)
pessoa1.verificar_idade()
pessoa2 = Pessoa('Lucas', 6)
pessoa2.verificar_idade()
pessoa3 = Pessoa('Maria', 19)
pessoa3.verificar_idade()