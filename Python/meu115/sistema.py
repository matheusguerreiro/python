from meu115.biblioteca.interface import *
from meu115.biblioteca.arquivo import *
from time import sleep

arquivo = 'pessoas.txt'
if not arquivoExiste(arquivo):
    arquivoCria(arquivo)

cabecalho('SISTEMA DE ARQUIVOS')
print(linha())
while True:
    op = menu(['Ver Pessoas Cadastradas', 'Cadastrar Pessoas', 'Sair'])
    if op == 1:
        cabecalho('Pessoas Cadastradas')
        arquivoLe(arquivo)
    elif op == 2:
        cabecalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arquivo, nome, idade)
    elif op == 3:
        print('Saindo...')
        break
    else:
        print('\033[0;31mOpção Inválida! Digite uma opção válida...\033[m')
        sleep(2)
