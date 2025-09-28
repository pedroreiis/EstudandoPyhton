'''Exercício 2: Métodos Simples

Crie uma classe ContaBancaria com:

Atributo saldo

Métodos depositar(valor) e sacar(valor)

Um método exibir_saldo()
RESPOSTA: '''
class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"✅ Depósito de R${valor} realizado com sucesso.")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"✅ Saque de R${valor} realizado com sucesso.")
        else:
            print("❌ Saldo insuficiente!")

    def exibir_saldo(self):
        print(f"💰 Saldo atual: R${self.saldo}")


# Programa principal
conta = ContaBancaria()

while True:
    print("\n--- Menu ---")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver saldo")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Digite o valor para depositar: R$"))
        conta.depositar(valor)
    elif opcao == "2":
        valor = float(input("Digite o valor para sacar: R$"))
        conta.sacar(valor)
    elif opcao == "3":
        conta.exibir_saldo()
    elif opcao == "4":
        print("✅ Encerrando o programa...")
        break
    else:
        print("❌ Opção inválida, tente novamente.")

'''Explicação:
1. Criando a classe
class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo


Criamos uma classe chamada ContaBancaria.

O __init__ é o construtor, ou seja, o que acontece quando criamos uma conta nova.

O parâmetro saldo=0 significa que, se você não passar nada, a conta começa com saldo zero.

Exemplo:

conta = ContaBancaria()       # começa com saldo 0
conta2 = ContaBancaria(100)   # começa com saldo 100

2. Métodos da conta
def depositar(self, valor):
    self.saldo += valor
    print(f"✅ Depósito de R${valor} realizado com sucesso.")


Esse método soma o valor ao saldo.

self.saldo += valor → é o mesmo que self.saldo = self.saldo + valor.

def sacar(self, valor):
    if valor <= self.saldo:
        self.saldo -= valor
        print(f"✅ Saque de R${valor} realizado com sucesso.")
    else:
        print("❌ Saldo insuficiente!")


Aqui verificamos se tem dinheiro suficiente antes de sacar.

Se tiver, o saldo diminui.

Se não tiver, mostra a mensagem de erro.

def exibir_saldo(self):
    print(f"💰 Saldo atual: R${self.saldo}")


Só mostra o saldo atual formatado.

3. Programa principal (menu interativo)
while True:
    print("\n--- Menu ---")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver saldo")
    print("4 - Sair")


Criamos um loop infinito (while True), ou seja, o programa fica rodando até você mandar parar.

O menu mostra as opções.

opcao = input("Escolha uma opção: ")


Aqui o usuário digita a opção.

Dependendo do valor, vai para o if/elif.

4. As escolhas

Se escolher 1, pede um valor e chama depositar.

Se escolher 2, pede um valor e chama sacar.

Se escolher 3, chama exibir_saldo.

Se escolher 4, dá break → sai do loop e encerra.

Se digitar algo inválido, aparece a mensagem de erro.

👉 Resumindo:

A classe ContaBancaria é o modelo da conta (atributos + métodos).

O while True é o caixa eletrônico rodando, recebendo comandos do usuário.'''