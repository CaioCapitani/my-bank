import PySimpleGUI as sg

sg.theme('dark grey 9')

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

## Criação do GUI para input dos dados

layout = [  [sg.Text('Bem vindo ao Banco, por favor selecione o tipo de conta que gostaria de abrir:')],
            [sg.Text('1 - Conta Corrente\n2 - Conta Poupança')],
            [sg.Text('Digite o tipo da conta:', size = (20,1)), sg.InputText()],
            [sg.Text('Digite o seu nome:', size = (20,1)), sg.InputText()],
            [sg.Text('Qual será o deposito inicial:', size = (20,1)), sg.InputText()],
            [sg.Button('Ok',bind_return_key=True), sg.Button('Cancel')] ]

window = sg.Window('Banco', layout, finalize=True)

while True:
    event, values = window.read()
    if event == 'Ok':
        tipo_conta = int(values[0])
        nome = (values[1]).capitalize()
        if nome.isdigit() == True:
            sg.popup_ok("Por favor, digite um nome válido!")
            continue
        quantia = int(values[2])
        break
    elif event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        exit()

window.close()

Conta = criar_conta(tipo_conta, nome, quantia)

def excluir_conta(Conta):
    print("\nConta excluída com sucesso!\n")
    del Conta

while True:

    layout = [  [sg.Text('O que deseja fazer:')],
                [sg.Text('1 - Depositar\n2 - Sacar\n3 - Saldo\n4 - Informaçoes da Conta\n5 - Excluir Conta')],
                [sg.Text('Digite a opção:', size = (15,1)), sg.InputText()],
                [sg.Button('Ok',bind_return_key=True), sg.Button('Cancel')] ]

    window = sg.Window('Bem vindo ao Banco', layout, finalize=True)

    while True:
        event, values = window.read()
        if event == 'Ok':
            opcao = int(values[0])
            break
        elif event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            exit()
            
    window.close()

    if opcao == 1:
        layout = [  [sg.Text('Qual será o valor do depósito:', size = (22,1)), sg.InputText()],
                    [sg.Button('Ok',bind_return_key=True), sg.Button('Cancel')] ]
        
        window = sg.Window('Faça o seu depósito', layout, finalize=True)
        
        while True:
            event, values = window.read()
            if event == 'Ok':
                quantia = int(values[0])
                Conta.depositar(quantia)
                break
            elif event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                break
            
        window.close()
        
    elif opcao == 2:
        layout = [  [sg.Text('Qual será o valor do saque:', size = (22,1)), sg.InputText()],
                    [sg.Button('Ok',bind_return_key=True), sg.Button('Cancel')] ]
        
        window = sg.Window('Faça o seu saque', layout,finalize=True)
        
        while True:
            event, values = window.read()
            if event == 'Ok':
                quantia = int(values[0])
                Conta.sacar(quantia)
                break
            elif event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                break
            
        window.close()
    
    elif opcao == 3:
        layout = [  [sg.Text('Saldo da Conta: R${}'.format(Conta.saldo), size = (22,1)) ],
                    [sg.Button('Ok',bind_return_key=True)] ]
        
        window = sg.Window('Seu Extrato', layout, finalize=True)
        
        while True:
            event, values = window.read()
            if event == 'Ok':
                break
            
        window.close()
        
    elif opcao == 4:
        layout = [  [sg.Text('{}\nSaldo da Conta: R${}\nSaldo mínimo da Conta: R${}\n'.format(Conta, Conta.saldo, Conta.min_saldo), size = (40,3)) ],
                    [sg.Button('Ok',bind_return_key=True)] ]
        
        window = sg.Window('Informaçães da Conta', layout, finalize=True)
        
        while True:
            event, values = window.read()
            if event == 'Ok':
                break
            
        window.close()        
        
    elif opcao == 5:
        layout = [  [sg.Text('Deseja excluir a conta?')],
                    [sg.Button('Sim',bind_return_key=True), sg.Button('Não')] ]
        
        window = sg.Window('Excluir Conta', layout, size=(300,75), element_justification='center', finalize=True)
        
        while True:
            event, values = window.read()
            if event == 'Sim':
                excluir_conta(Conta)
                window.close()
                sg.popup_ok("Conta excluída com sucesso!")
                exit() 
            elif event == 'Não':
                break
                
        window.close()
    