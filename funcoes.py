import inquirer
from rich.console import Console
from rich.text import Text
from rich.align import Align

def Cadastrar(contas_bancarias,saldos,extratos):
    entrar=[inquirer.Text('nome', message="Digite seu nome"),
           inquirer.Text('cpf',message="Digite seu cpf"),inquirer.Password('senha', message= "Digite sua senha")]
    
    saldos.append(0)
    extratos.append([])
    
    

    cadastro=inquirer.prompt(entrar)
    cadastro=list(cadastro.values())
    contas_bancarias.append(cadastro)

    indice=contas_bancarias.index(cadastro)

    return indice
    

def Login(contas_bancarias):
    entrar=[inquirer.Text('nome', message="Digite seu nome"),
           inquirer.Text('cpf',message="Digite seu cpf"),inquirer.Password('senha', message= "Digite sua senha")]
    
    login=inquirer.prompt(entrar)
    login=list(login.values())
    
    while login not in contas_bancarias:
        print("Usuário não encontrado, ou senha incorreta")
        entrar=[inquirer.Text('nome', message="Digite seu nome"),
           inquirer.Text('cpf',message="Digite seu cpf"),inquirer.Password('senha', message= "Digite sua senha")]
    
        login=inquirer.prompt(entrar)
        login=list(login.values())
    

    indice=contas_bancarias.index(login)

    return indice


def Sacar(saldos,indice,extratos):

    sacar=int(input("Escolha o valor para sacar: "))
    
    continuar=True
    while continuar :

        if sacar> saldos[indice]:
            print(f"Saldo insuficiente, seu saldo é: {saldos[indice]}")
            resposta=input("Deseja colocar outro valor?: ").upper()

            if resposta== "SIM":
                sacar=int(input("Escolha o valor para sacar: "))
            else:
                print("Operação cancelada.")
                return f"Saldo atual: {saldos[indice]}"

        else:
            continuar=False



    saldos[indice]-=sacar
    extratos[indice].append(f"Saque de R${sacar:.2f}")
    

    print(f"OPERAÇÃO FINALIZADA\nNovo saldo:{saldos[indice]}")


def Consultar_Extrato (extratos,indice):
    if extratos[indice] is not None:

        for element in extratos[indice]:
            print(element)
    

def Deposito (saldos,indice,extrato):
    deposito=int(input("Quanto você deseja depositar? "))

    while deposito<0:
        deposito=int(input("Número inválido, digite novamente (ou 0 para sair)"))

    if deposito == 0:
        print("OPERAÇÃO CANCELADA")
    else:
        saldos[indice]+=deposito
        extrato[indice].append(f"Depósito de R${deposito}")
        print(f"OPERÇÃO FINALIZADA\nSeu novo saldo é {saldos[indice]}")

def Transferencia(saldos,indice,extratos):
    
    transferir=int(input("Escolha o valor para sacar: "))
    
    continuar=True
    while continuar :

        if transferir> saldos[indice]:
            print(f"Saldo insuficiente, seu saldo é: {saldos[indice]}")
            resposta=input("Deseja colocar outro valor?: ").upper()

            if resposta== "SIM":
                sacar=int(input("Escolha o valor para transferir: "))
            else:
                print("Operação cancelada.")
                return f"Saldo atual: {saldos[indice]}"

        else:
            continuar=False



    saldos[indice]-=transferir
    extratos[indice].append(f"transferencia de R${transferir:.2f}")
    

    print(f"OPERAÇÃO FINALIZADA\nNovo saldo:{saldos[indice]}")

    return 0

def Menu (indice,contas_bancarias,saldos,extratos):
    
        continuar=True
        while continuar:

            perguntas = [
                inquirer.List(
                    'escolha',
                    message= (f"Bem vindo(a) {contas_bancarias[indice][0]}.O seu saldo é {saldos[indice]}. O que deseja realizar?"),
                    choices=['Sacar', 'Depositar', 'Ver extrato', 'Transferencia',"Sair"]
                )
            ]

            resposta = inquirer.prompt(perguntas)


            if resposta['escolha'] == "Sacar":

                Sacar(saldos,indice,extratos)

            elif resposta['escolha']== "Sair":
                continuar=False

            elif resposta['escolha'] == "Depositar":

                Deposito(saldos,indice,extratos)

            elif resposta['escolha'] == "Ver extrato":

                Consultar_Extrato(extratos,indice)

            else:
                Transferencia(saldos,indice,extratos)








def LOGO():
    console = Console()

    # Sua logo ASCII
    logo_ascii = r"""
      ____                          _   _            _                   _ 
    | __ )  __ _ _ __   ___ ___   | \ | | __ _  ___(_) ___  _ __   __ _| |
    |  _ \ / _` | '_ \ / __/ _ \  |  \| |/ _` |/ __| |/ _ \| '_ \ / _` | |
    | |_) | (_| | | | | (_| (_) | | |\  | (_| | (__| | (_) | | | | (_| | |
    |____/ \__,_|_| |_|\___\___/  |_| \_|\__,_|\___|_|\___/|_| |_|\__,_|_|
                                                                       
    """

    # Criar objeto Text para colorir
    texto_colorido = Text()
    cores = ["white", "magenta"]  # cores alternadas

    for i, linha in enumerate(logo_ascii.splitlines()):
        cor = cores[i % len(cores)]  # alterna cores por linha
        texto_colorido.append(linha + "\n", style=f"bold {cor}")

    # Exibir no terminal
    console.print(Align.center(texto_colorido))
    texto="[bold magenta]Bem-vindo ao Sistema Bancário![/bold magenta]"
    console.print(Align.center(texto))