# Aula 16 (Tuplas)

numeros = (int(input('N1: ')), int(input('N2: ')), int(input('N3: ')), int(input('N4: ')))

print(f'Quantidade de 9: {numeros.count(9)}')
if 3 in numeros:
    print(f'Posição primeiro 3: {numeros.index(3)}')
else:
    print(f'Número 3 não foi digitado')
print('Números pares: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(f'{n}', end=' ')
