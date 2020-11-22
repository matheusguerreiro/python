from Tratamento_de_Erros_e_Excecoes_23_115.lib.interface import *
from Tratamento_de_Erros_e_Excecoes_23_115.lib.arquivo import *

arquivo = 'cursoemvideo.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Pessoas', 'Sair'])
    if resposta == 1:
        # Ler Arquivo
        lerArquivo(arquivo)
    elif resposta == 2:
        cabecalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        print('Saindo...')
        break
    else:
        print('\033[0;31mOpção Inválida!\033[m')
