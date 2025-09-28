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

'''Explicação:
Definição da classe
class Pessoa:


Criamos a classe Pessoa.

Essa classe é o molde para criar várias pessoas (objetos).

2. O construtor __init__
def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade


__init__ é chamado quando criamos uma nova pessoa.

nome e idade são recebidos como parâmetros.

self.nome = nome → guarda o nome dentro do objeto.

self.idade = idade → guarda a idade dentro do objeto.

Exemplo:

p1 = Pessoa("Ana", 17)


Aqui: self.nome = "Ana" e self.idade = 17.

3. Método verificar_idade
def verificar_idade(self):
    if self.idade >= 18:
        print(f"{self.nome} é maior de idade.")
    else:
        print(f"{self.nome} é menor de idade.")


Esse método pega a idade da pessoa (self.idade).

Se for 18 ou mais, imprime que é maior de idade.

Caso contrário, diz que é menor de idade.

4. Criando objetos
p1 = Pessoa("Ana", 17)
p2 = Pessoa("Carlos", 21)


Criamos duas pessoas diferentes:

p1 → nome: "Ana", idade: 17

p2 → nome: "Carlos", idade: 21

5. Chamando o método
p1.verificar_idade()  # "Ana é menor de idade."
p2.verificar_idade()  # "Carlos é maior de idade."


Cada objeto usa suas próprias informações.

👉 Resumindo:

Classe = molde da pessoa

Atributos = nome e idade

Método = verificar se é maior ou menor de idade

Objetos = cada pessoa criada com a classe'''