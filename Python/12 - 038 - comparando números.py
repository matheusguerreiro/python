# Aula 12 (Condições em Python (if..elif))

numero1 = int(input('Número 1: '))
numero2 = int(input('Número 2: '))

if numero1 > numero2:
    print('O número \033[0:32m{}\033[m é Maior!'.format(numero1))
elif numero2 > numero1:
    print('O número \033[0:32m{}\033[m é Maior!'.format(numero2))
else:
    print('\033[0:33mNão tem Maior!\033[m'
          '\n\033[0:31mOs Dois são Iguais.\033[m')
