import inquirer
import funcoes

perguntas = [
    inquirer.List(
        'escolha',
        message= "Faça o login (se não, faça o cadastro)",
        choices=['Sacar', 'Depositar', 'Ver extrato', 'Transferencia']
    )
]

resposta = inquirer.prompt(perguntas)


if resposta == "Sacar":
    sacar=1 #teste,ignorem essa linha