# Aula 13 (Estrutura de Repetição for)

from datetime import date

anoA = date.today().year

maiores = menores = 0
for c in range(0, 7):
    anoN = int(input('Digite o Ano de Nascimento desse vivente: '))
    idade = anoA - anoN
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print('Das 7 pessoas:'
      '\n{} são de Maioridade e {} são de Menoridade.'.format(maiores, menores))
