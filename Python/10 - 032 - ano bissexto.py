# Aula 10 (Condições em Python (if..else))

from datetime import date

anoAtual = date.today().year

ano = int(input('Digite um Ano qualquer ou [0] para o Ano Atual: '))

if ano == 0:
    ano = anoAtual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O Ano {} é Bissexto!'.format(ano))
else:
    print('O Ano {} Não é Bissexto!'.format(ano))
    