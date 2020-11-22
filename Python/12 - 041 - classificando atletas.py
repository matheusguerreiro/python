# Aula 12 (Condições em Python (if..elif))

from datetime import datetime

anoN = int(input('Digite o ano de nascimento: '))
anoA = datetime.today().year

idade = anoA - anoN

if idade <= 9:
    print('Idade: {} anos'
          '\nCategoria: Mirim'.format(idade))
elif idade <= 14:
    print('Idade: {} anos'
          '\nCategoria: Infantil'.format(idade))
elif idade <= 19:
    print('Idade: {} anos'
          '\nCategoria: Júnior'.format(idade))
elif idade <= 25:
    print('Idade: {} anos'
          '\nCategoria: Sênior'.format(idade))
else:
    print('Idade: {} anos'
          '\nCategoria: Master'.format(idade))
