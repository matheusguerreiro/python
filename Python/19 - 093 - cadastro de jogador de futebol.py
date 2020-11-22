# Aula 19 (Dicionários)

from time import sleep

jogador = {}
gols = []

jogador['Nome'] = str(input('Nome do Jogador: '))
totalGols = 0
quantidadePartidas = int(input('Quantas partidas ele Jogou? '))
for c in range(0, quantidadePartidas):
    gols.append(int(input(f'Gols da {c+1}ª partida: ')))
jogador['Gols'] = gols[:]
jogador['Total de Gols'] = sum(jogador['Gols'])

print(f'\n{jogador}')
sleep(1)

print()
for chave, valor in jogador.items():
    print(f"O campo {chave} tem o valor {valor}")
sleep(1)

print(f"\nO Jogador {jogador['Nome']} jogou {len(jogador['Gols'])} partidas.")
for item, valor in enumerate(jogador['Gols']):
    print(f'Na partida {item+1} fez {valor} gols')
print(f"Foi um total de {jogador['Total de Gols']} gols.")
