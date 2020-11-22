# Aula 19 (Dicionários)

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}

jogoRanking = []

for chave, valor in jogo.items():
    print(f'{chave} tirou {valor}')
    sleep(1)

jogoRanking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print()
for indice, valor in enumerate(jogoRanking):
    print(f'{indice+1} lugar: {valor[0]} com {valor[1]}')
    sleep(1)
