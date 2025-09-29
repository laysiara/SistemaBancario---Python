import inquirer
import funcoes

contas_bancarias=[['iaralays','11407','123'],['ana','78654','567']]
saldos=[3000,10000]

continuaçao=True
while continuaçao:
    
    entrar= [
        inquirer.List(
            'entrada',
            message= "Banco Nacional",
            choices=['Login', 'Cadastro','Sair']
        )
    ]

    forma=inquirer.prompt(entrar)

    if forma['entrada']== "Login":

        
        indice=funcoes.Login(contas_bancarias)

        funcoes.Menu(indice,contas_bancarias)
        
    elif forma['entrada']=="Cadastro":

        indice=funcoes.Cadastrar(contas_bancarias,saldos)
        funcoes.Menu(indice,contas_bancarias)
        
        
    elif forma['entrada']=="Sair":
        continuaçao=False
        
    print(contas_bancarias,saldos)
    