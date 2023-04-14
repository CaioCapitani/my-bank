class Conta:
    def __init__(self, nome, saldo, min_saldo):
        self.nome = nome
        self.saldo = saldo
        self.min_saldo = min_saldo

    def depositar(self, quantia):
        self.saldo += quantia

    def sacar(self, quantia):
        if self.saldo - quantia >= self.min_saldo:
            self.saldo -= quantia
        else:
            print("Desculpa, sem fundos suficientes!")

    def extrato(self):
        print("Saldo da Conta: R${}".format(self.saldo))

class Corrente(Conta):
    def __init__(self, nome, saldo):
        super().__init__(nome, saldo, min_saldo = -1000)

    def __str__(self):
        return "Conta Corrente de {}".format(self.nome)
    
class Poupanca(Conta):
    def __init__(self, nome, saldo):
        super().__init__(nome, saldo, min_saldo = 0)
        
    def __str__(self):
        return "Conta Poupança de {}".format(self.nome)
    
## Criação das contas por input

def criar_conta(tipo_conta, nome, quantia):
    if tipo_conta == 1: 
        print("\nConta Corrente criada com sucesso!")
        return Corrente(nome, quantia)
    elif tipo_conta == 2:
        print("\nConta Poupança criada com sucesso!\n") 
        return Poupanca(nome, quantia)
    else:
        print("\nPor favor, digite um valor válido!")

print("\nBem vindo ao Banco, por favor selecione o tipo de conta que gostaria de abrir:\n")
print("1 - Conta Corrente\n2 - Conta Poupança")

tipo_conta = int(input("\nDigite o tipo da conta: ").strip())

nome = input("\nCerto, qual o seu nome: ").capitalize()

## Checa em um loop se o valor do deposito inserido foi um número e não uma string

while True:
    
    quantia = input("\nQual será o deposito inicial: ") 

    try:
        quantia = int(quantia)
        break
    except ValueError:
        print("Por favor, digite um valor em número!\n")

Conta = criar_conta(tipo_conta, nome, quantia)

def excluir_conta(Conta):
    print("\nConta excluída com sucesso!\n")
    del Conta
    
print ("\nO que deseja fazer:\n1 - Depositar\n2 - Sacar\n3 - Saldo\n4 - Informaçoes da Conta\n5 - Excluir Conta")

while True:
    opcao = int(input("Digite a opção: ").strip())
    if opcao == 1:
        quantia = int(input("Qual será o valor do deposito: ").strip())
        Conta.depositar(quantia)
    elif opcao == 2:
        quantia = int(input("Qual será o valor do saque: ").strip())
        Conta.sacar(quantia)
    elif opcao == 3:
        Conta.extrato()
    elif opcao == 4:
        print(Conta)
    elif opcao == 5:
        excluir_conta(Conta)
        break
    else:
        print("Por favor, digite um valor válido!")

    