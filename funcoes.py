import inquirer

def Cadastrar(contas_bancarias,saldos):
    entrar=[inquirer.Text('nome', message="Digite seu nome"),
           inquirer.Text('cpf',message="Digite seu cpf"),inquirer.Password('senha', message= "Digite sua senha")]
    
    saldos.append(0)
    
    
    
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


def Sacar(saldo):
    return 0

def Consultar_Extrato (saldo):
    return 0

def Deposito (saldo):
    return 0

def Transferencia(saldo):
    return 0

def Consultar_saldo(saldo):
    return 0

def Menu (indice,contas_bancarias):
    
        continuar=True
        while continuar:

            perguntas = [
                inquirer.List(
                    'escolha',
                    message= (f"Bem vindo(a) {contas_bancarias[indice][0]}. O que deseja realizar?"),
                    choices=['Sacar', 'Depositar', 'Ver extrato', 'Transferencia',"Sair"]
                )
            ]

            resposta = inquirer.prompt(perguntas)


            if resposta['escolha'] == "Sacar":
                sacar=1 #teste,ignorem essa linha
                #teste

            elif resposta['escolha']== "Sair":
                continuar=False