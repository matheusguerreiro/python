# Aula 14 (Estrutura de Repetição while)

numero = somaN = numerosD = 0
while numero != 999:
    numero = int(input('Digite um Número ou 999 para parar: '))
    numerosD += 1
    somaN += numero
print('Você digitou {} números e a soma deles é {}.'.format(numerosD - 1, somaN - 999))
