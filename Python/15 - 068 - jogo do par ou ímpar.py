# Aula 15 (Interrompendo Repetições while)

from random import randint

vitoriasJ = 0
while True:
    jogador = int(input('Escolha:  (1) Par  -  (2) Ímpar  : '))
    if jogador == 1:
        computador = 2
        jogadorJ = int(input('Jogada: '))
        computadorJ = randint(0, 10)
        resultado = jogadorJ + computadorJ
        if resultado % 2 == 0:
            print('Jogador Venceu!')
            vitoriasJ += 1
        else:
            print('\nComputador Venceu! Jogo Encerrado.')
            print('Número de Vitórias: {}'.format(vitoriasJ))
            break
    elif jogador == 2:
        computador = 1
        jogadorJ = int(input('Jogada: '))
        computadorJ = randint(0, 10)
        resultado = jogadorJ + computadorJ
        if resultado % 2 != 0:
            print('Jogador Venceu!')
            vitoriasJ += 1
        else:
            print('\nComputador Venceu! Jogo Encerrado...')
            print('Número de Vitórias: {}'.format(vitoriasJ))
            break
    else:
        print('Opção Errada! Tente novamente...')
