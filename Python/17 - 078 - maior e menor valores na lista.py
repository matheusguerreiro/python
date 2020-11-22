# Aula 17 (Listas (Parte 1))

numeros = []

maior = menor = 0
for c in range(0, 5):
    numeros.append(int(input('Digite um Número: ')))
    if c == 0:
        maior = numeros[0]
        menor = numeros[0]
    else:
        if numeros[c] > maior:
            maior = numeros[c]
        if numeros[c] < menor:
            menor = numeros[c]

print(f'Sua Lista é: {numeros}')
print(f'O Maior é: {maior} na posição: ', end='')
for indice, valor in enumerate(numeros):
    if valor == maior:
        print(f'{indice}', end=' ')
print(f'\nO Menor é: {menor} na posição: ', end='')
for indice, valor in enumerate(numeros):
    if valor == menor:
        print(f'{indice}', end=' ')
