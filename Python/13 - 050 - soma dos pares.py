# Aula 13 (Estrutura de Repetição for)

somaP = 0
for c in range(0, 6):
    numero = int(input('Digite um Número: '))
    if numero % 2 == 0:
        somaP += numero
print('A Soma dos Pares é: {}'.format(somaP))
