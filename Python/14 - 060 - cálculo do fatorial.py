# Aula 14 (Estrutura de Repetição while)

from math import factorial

numero = int(input('Digite um Número: '))
fatorial = 1

# print(factorial(numero))  com a função factorial

print('{}! = '.format(numero), end='')
while numero != 0:
    print('{} '.format(numero), end='')
    print('X', end=' ') if numero != 1 else print('=', end=' ')
    fatorial *= numero
    numero -= 1
print(fatorial, end=' ')
