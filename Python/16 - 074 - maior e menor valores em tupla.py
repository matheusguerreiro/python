# Aula 16 (Tuplas)

from random import randint

numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10),
           randint(0, 10), randint(0, 10))

print('Os Números sorteados foram: ', end='')
for n in numeros:
    print(n, end=' ')

print(f'\nO Maior é: {max(numeros)}'
      f'\nO Menor é: {min(numeros)}')
