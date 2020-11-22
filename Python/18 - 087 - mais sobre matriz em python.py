# Aula 18 (Listas (Parte 2))

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

somaPares = soma3C = maiorV2 = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a posição [{linha}:{coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            somaPares += matriz[linha][coluna]
        if coluna == 2:
            soma3C += matriz[linha][2]
        if linha == 1 and coluna == 0:
            maiorV2 = matriz[1][coluna]
        else:
            if matriz[1][coluna] > maiorV2:
                maiorV2 = matriz[1][coluna]
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^3}]', end='')
    print()
print(f'Soma de todos os valores Pares: {somaPares}'
      f'\nSoma valores 3ª coluna: {soma3C}'
      f'\nMaior valor da 2ª linha: {maiorV2}')
