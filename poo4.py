'''Exercício 4: Herança

Crie uma classe Animal com o método falar() que apenas imprime "Som de animal".
Depois crie as classes Cachorro e Gato, que herdam de Animal, mas sobrescrevem o método falar():

Cachorro deve dizer "Au Au"

Gato deve dizer "Miau"'''
class Animal:
    def falar(self):
        print("Som de animal")


class Cachorro(Animal):
    def falar(self):
        print("Au Au")


class Gato(Animal):
    def falar(self):
        print("Miau")

a = Animal()
c = Cachorro()
g = Gato()

a.falar()  
c.falar()  
g.falar() 

'''Explicação:
. Classe mãe (Animal)
class Animal:
    def falar(self):
        print("Som de animal")


Essa é a classe base.

Todo animal pode "falar" (emitir som).

Aqui deixamos um comportamento genérico.

2. Classes filhas (Cachorro e Gato)
class Cachorro(Animal):
    def falar(self):
        print("Au Au")

class Gato(Animal):
    def falar(self):
        print("Miau")


As duas herdam de Animal.

Mas elas reescrevem (override) o método falar() para ter seu próprio comportamento.

Isso é chamado de polimorfismo → mesma função, mas resultado diferente dependendo do objeto.

3. Criando objetos
a = Animal()
c = Cachorro()
g = Gato()


Criamos um objeto de cada classe.

4. Chamando os métodos
a.falar()  # Som de animal
c.falar()  # Au Au
g.falar()  # Miau


Mesmo método (falar()), mas cada classe tem um resultado diferente.

👉 Resumindo

Herança: Cachorro e Gato herdaram de Animal.

Sobrescrita: eles mudaram o comportamento do método falar().

Polimorfismo: o mesmo nome de método (falar) funciona de formas diferentes dependendo do objeto.'''