'''Exercício 1: Classe Básica

Crie uma classe chamada Carro com os atributos:

marca

modelo

ano

E um método chamado exibir_info() que mostre os dados do carro.
RESPOSTA: '''
class Carro():
    def __init__(self, marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_info(self):
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Ano: {self.ano}')

carro1 = Carro('Ford', 'Fiesta', '2015')
carro1.exibir_info()

'''explicação:
1. Criando a classe
class Carro:


Aqui definimos uma classe chamada Carro.

Uma classe é como um molde ou planta de construção para criar objetos (no caso, carros).

2. Construtor (__init__)
def __init__(self, marca, modelo, ano):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano


Esse método é chamado automaticamente quando você cria um carro novo.

self → representa o próprio objeto que será criado.

marca, modelo e ano → são as informações que você passa quando cria o carro.

self.marca = marca → guarda a marca dentro do objeto.

Exemplo:

carro1 = Carro("Toyota", "Corolla", 2020)


Aqui:

marca = "Toyota"

modelo = "Corolla"

ano = 2020

E essas infos ficam armazenadas em carro1.

3. Método para mostrar informações
def exibir_info(self):
    print(f"Marca: {self.marca}")
    print(f"Modelo: {self.modelo}")
    print(f"Ano: {self.ano}")


Esse método só serve para exibir os dados do carro.

Quando você chama carro1.exibir_info(), ele pega os atributos salvos no objeto e imprime.

4. Criando objetos
carro1 = Carro("Toyota", "Corolla", 2020)
carro2 = Carro("Honda", "Civic", 2022)


Aqui criamos dois carros diferentes usando o mesmo molde.

Cada um guarda suas próprias informações.

5. Chamando o método
carro1.exibir_info()


Resultado:

Marca: Toyota
Modelo: Corolla
Ano: 2020


👉 Resumindo:

Classe = molde

Objeto = carro criado a partir do molde

Atributos (marca, modelo, ano) = características

Método (exibir_info) = ações que o carro pode executar'''