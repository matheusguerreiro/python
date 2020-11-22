# Aula 14 (Estrutura de Repetição while)

from random import randint
from time import sleep

print('-=- Jogo da Adivinhação v2.0 -=-')
print('  -=- (Vez do Computador) -=-')
print('  (1) Computador: ', end='')
sleep(2)
computador = randint(0, 10)
print('*')
print('  -=- (Vez do Jogador)    -=-')
print('  (2) Jogador: ', end='')
jogador = int(input())

palpites = 1
while jogador != computador:
    print('\n        (( ERROU! ))')
    palpites += 1
    sleep(1)
    print('  -=- Tente Novamente...  -=-')
    print('  -=- (Vez do Jogador)    -=-')
    print('  (2) Jogador: ', end='')
    jogador = int(input())

print('\n(( Você ACERTOU na {}ª Jogada! ))'.format(palpites))
