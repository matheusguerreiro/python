# Aula 21 (Funções (Parte 2))

from math import factorial

def fatorial(n, v):
    '''
    :param n: numero para se calcular o fatorial
    :param v: visualizar o calculo ou não
    :return: não
    '''
    f = 1
    if v == False:
        print(f'O Fatorial de {n} é: {factorial(n)}')
    else:
        print(f'{n}! = ', end='')
        for c in range(n, 0, -1):
            print(c, end=' X ') if c > 1 else print(c, end=' = ')
            f *= c
        print(f, end='')


print('Vamos Calcular o Fatorial')
numero = int(input('Fatorial de: '))
calculo = False
while True:
    oc = str(input('Mostrar Cálculo? (1) Sim  (2) Não : ')).strip()[0]
    if oc in '12':
        break
    else:
        print('Digite apenas 1 ou 2.')
if oc == '1':
    calculo = True

fatorial(numero, calculo)