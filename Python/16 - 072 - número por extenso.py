# Aula 16 (Tuplas)

numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')

while True:
    n = int(input('\nDigite um Número entre 0 e 20: '))
    if n > 20 or n < 0:
        print('Número Inválido... Adios!')
        break
    else:
        print('Você digitou o Número: {}'.format(numeros[n]))
