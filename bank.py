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

    def declaracao(self):
        print("Saldo da Conta: R${}".format(self.saldo))

class Corrente(Conta):
    def __init__(self, nome, saldo):
        super().__init__(nome, saldo, min_saldo = -1000)

    def __str__(self):
        return "Conta Corrente de {}: Saldo R${}".format(self.nome, self.saldo)
    
class Poupanca(Conta):
    def __init__(self, nome, saldo):
        super().__init__(nome, saldo, min_saldo = 0)
        
    def __str__(self):
        return "Conta Poupança de {}: Saldo R${}".format(self.nome, self.saldo)