# Aula 19 (Dicionários)

from random import randint

jogador = {}
gols = []
jogadores = []

while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input('Nome do Jogador: ')).strip().title()
    qPartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, qPartidas):
        print(f'Gols na {c+1}ª partida: ', end='')
        gols.append(randint(0, 3))
        print(gols[c])
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)

    jogadores.append(jogador.copy())

    while True:
        opcao = str(input('\nQuer seguir cadastrando? [S|N]: ')).strip().upper()[0]
        if opcao in 'SN':
            break
        print('Erro! Digite apenas S ou N.')
    if opcao == 'N':
        print('Saindo...')
        break
    print()

print()
print('-'*80)
print(f'{"Aproveitamento dos Jogadores":^80}')
print('-'*80)
print(f'{"COD":^10}{"NOME":^20}{"GOLS":^40}{"TOTAL":^10}')
print('-'*80)
for c in range(0, len(jogadores)):
    print(f'{c:^10}{jogadores[c]["nome"]:^20}{str(jogadores[c]["gols"]):^40}{jogadores[c]["total"]:^10}')
print('-'*80)

while True:
    opcao2 = str(input('[1] Ver detalhes Individuais - [2] Finalizar : '))
    if opcao2 == '1':
        print()
        print(f'-'*15)
        print(f'{"COD":^5}{"NOME":^10}')
        print(f'-'*15)
        for c in range(0, len(jogadores)):
            print(f'{c:^5}{jogadores[c]["nome"]:^10}')
        print(f'-'*15)
        while True:
            cod = int(input('COD: '))
            if cod >= 0 and cod <= len(jogadores)-1:
                print()
                print('-'*24)
                print(f'Jogador {jogadores[cod]["nome"]}')
                print('-' * 24)
                for c in range(0, len(jogadores[cod]['gols'])):
                    print(f'Fez {jogadores[cod]["gols"][c]} gols na {c+1}ª partida')
                print(f'Total de Gols: {jogadores[cod]["total"]} gols')
                print('-' * 24)
                break
            else:
                print('Erro! Digite um COD válido.')
    elif opcao2 == '2':
        print('Finalizando...')
        break
    else:
        print('Erro! Digite apenas 1 ou 2.')
