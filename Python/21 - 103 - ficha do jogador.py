# Aula 21 (Funções (Parte 2))

def ficha(n='Desconhecido', gs=0):
    print(f'O Jogador {n} fez {gs} gol(s) no Campeonato.')


print('Dados do Jogador')
nome = str(input('Nome: '))
gols = str(input('Gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gs=gols)
else:
    ficha(nome, gols)
