# Aula 07 (Operadores Aritméticos)

grausC = float(input('Digite a Temperatura em ºC: '))

grausF = ((grausC * 9) / 5) + 32
grausK = grausC + 273.15

print('Temperatura em ºC = {:.1f}'
      '\nTemperatura em ºF = {:.1f}'
      '\nTemperatura em ºK = {:.1f}'.format(grausC, grausF, grausK))
