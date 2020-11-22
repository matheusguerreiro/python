# Aula 10 (Condições em Python (if..else))

from random import randint
from time import sleep

print('-'*50)
print(' JOGO da Adivinhação v.1.0'.center(50))
print('-'*50)
print('(1) - Computador  X  (2) - Você'.center(50))
print('-'*50)
sleep(2)
print('Vamos Começar...'.center(50))
sleep(2)
print('-'*50)
print('Player (1) - Computador'.center(50))
sleep(2)
print('Vou pensar em um Número de 0 a 5...')
numeroC = randint(0, 5)
sleep(2)
print('Pensando...')
sleep(4)
print('Pronto! Em que Número eu pensei? ')
sleep(1)
print('-'*50)
print('Player (2) - Você'.center(50))
tentativa = int(input('Tente Adivinhar: '))

if tentativa == numeroC:
    print('-' * 50)
    print('Parabéns! Você me venceu nessa.')
    print('-' * 50)
else:
    print('-' * 50)
    print('Hahaha... Eu pensei no número {} e não no {}.'
          '\nEu Venci.'.format(numeroC, tentativa))
    print('-' * 50)
