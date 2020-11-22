# Aula 21 (Funções (Parte 2))

def ajuda(c):
    help(c)

def titulo(mensagem, cor=0):
    tamanho = len(mensagem)
    print(f'-'*tamanho)
    print(mensagem)
    print(f'-'*tamanho)

comando = ''
while True:
    titulo('Sistema de Ajuda PyHelp')
    comando = str(input('Função ou Biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
