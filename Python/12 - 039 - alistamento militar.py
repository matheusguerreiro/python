# Aula 12 (Condições em Python (if..elif))

from datetime import datetime

anoN = int(input('Digite seu ano de nascimento: '))
anoA = datetime.today().year

idade = anoA - anoN

if idade < 18:
    print('Você tem \033[0:32m{} anos\033[m, falta \033[0:32m{} anos\033[m para se alistar.'
          '\nSeu alistamento será em \033[0:32m{}\033[m.'.format(idade, (18 - idade), (anoN + 18)))
elif idade == 18:
    print('Você tem \033[0:33m18 anos\033[m, \033[0:33m{}\033[m é o ano do alistamento!'.format(anoA))
else:
    print('Você tem \033[0:31m{} anos\033[m, já passou \033[0:31m{} anos\033[m do seu alistamento.'
          '\nSeu alistamento foi em \033[0:31m{}\033[m.'.format(idade, (idade - 18), (anoN + 18)))
