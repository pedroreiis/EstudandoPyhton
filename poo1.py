# Estudando POO
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
