# Aula 20 (Funções (Parte 1))

from random import randint

def sorteia(l):
    for c in range(0, 5):
        numeros.append(randint(0, 10))
    print(f'Os Números sorteados foram: {numeros}')

def somaPar(l):
    sP = 0
    for v in l:
        if v % 2 == 0:
            sP += v
    print(f'A Soma dos Números pares é: {sP}')


numeros = []

sorteia(numeros)
somaPar(numeros)
