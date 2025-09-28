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
