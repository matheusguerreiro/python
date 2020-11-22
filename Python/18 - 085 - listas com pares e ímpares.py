# Aula 18 (Listas (Parte 2))

valores = [[], []]
valor = 0

for c in range(1, 8):
    valor = int(input(f'Digite o {c}º Valor: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)
print(f'\nOs Valores digitados foram: {valores}')
valores[0].sort()
print(f'São Pares: {valores[0]}')
valores[1].sort()
print(f'São Ímpares: {valores[1]}')
