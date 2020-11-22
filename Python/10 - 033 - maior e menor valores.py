# Aula 10 (Condições em Python (if..else))

numero1 = int(input('Digite um Número: '))
numero2 = int(input('Digite outro Número: '))
numero3 = int(input('Digite mais um Número: '))

menor = numero1

if numero2 < numero1 and numero2 < numero3:
    menor = numero2

if numero3 < numero1 and numero3 < numero2:
    menor = numero3

maior = numero1

if numero2 > numero1 and numero2 > numero3:
    maior = numero2

if numero3 > numero1 and numero3 > numero2:
    maior = numero3

print('O menor é: {}'
      '\nO Maior é: {}'.format(menor, maior))
