# Aula 18 (Listas (Parte 2))

from random import randint
from time import sleep

palpites = []
dados = []

numeroP = int(input('Vamos gerar quantos jogos? '))

for c in range(0, numeroP):
    for c2 in range(0, 6):
        d = randint(1, 60)
        if d not in dados:
            dados.append(d)
    dados.sort()
    palpites.append(dados[:])
    dados.clear()

print('\nSegue os palpites...')
for palpite in palpites:
    print(f'{palpite}')
    sleep(1)
