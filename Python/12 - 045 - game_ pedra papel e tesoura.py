# Aula 12 (Condições em Python (if..elif))

from random import randint
from time import sleep

print(' -=-=-=-=-=-=-=--=-=-=-=-=-=-=- ')
print(' -=- Pedra, Papel e Tesoura -=- ')
print(' -=-=-=-=-=-=-=--=-=-=-=-=-=-=- ')
print(' -=- (1) Pedra              -=- ')
print(' -=- (2) Papel              -=- ')
print(' -=- (3) Tesoura            -=- ')
print(' -=-=-=-=-=-=-=--=-=-=-=-=-=-=- ')

print(' -=- Computador: ', end='')
sleep(2)
computador = randint(1, 3)
print('*')
sleep(1)
jogada = int(input(' -=- Você: '))
print(' -=-=-=-=-=-=-=--=-=-=-=-=-=-=- ')

if computador == 1:
    if jogada == 1:
        print(' -=-    Pedra VS Pedra    -=- '.center(32))
        print(' -=--=- Empatou! -=--=- '.center(32))
    elif jogada == 2:
        print(' -=-    Pedra VS Papel    -=- '.center(32))
        print(' -=--=- Venceu! -=--=- '.center(32))
    elif jogada == 3:
        print(' -=-   Pedra VS Tesoura   -=- '.center(32))
        print(' -=--=- Perdeu! -=--=- '.center(32))
    else:
        print(' -=-  Opção Inválida!  -=- '.center(32))
elif computador == 2:
    if jogada == 1:
        print(' -=-    Papel VS Pedra    -=- '.center(32))
        print(' -=--=- Perdeu! -=--=- '.center(32))
    elif jogada == 2:
        print(' -=-    Papel VS Papel    -=- '.center(32))
        print(' -=--=- Empatou! -=--=- '.center(32))
    elif jogada == 3:
        print(' -=-   Papel VS Tesoura   -=- '.center(32))
        print(' -=--=- Venceu! -=--=- '.center(32))
    else:
        print(' -=- Opção Inválida! -=- '.center(32))
elif computador == 3:
    if jogada == 1:
        print(' -=-   Tesoura VS Pedra   -=- '.center(32))
        print(' -=--=- Venceu! -=--=- '.center(32))
    elif jogada == 2:
        print(' -=-   Tesoura VS Papel   -=- '.center(32))
        print(' -=--=- Perdeu! -=--=- '.center(32))
    elif jogada == 3:
        print(' -=-  Tesoura VS Tesoura  -=- '.center(32))
        print(' -=--=- Empatou! -=--=- '.center(32))
    else:
        print(' -=- Opção Inválida! -=- '.center(32))
print(' -=-=-=-=-=-=-=--=-=-=-=-=-=-=- ')
