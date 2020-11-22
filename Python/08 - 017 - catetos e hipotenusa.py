# Aula 08 (Usando Módulos do Python)

from math import hypot

opostoC = float(input('Digite o cateto Oposto: '))
adjacenteC = float(input('Digite o cateto Adjacente: '))

print('Cateto Oposto: {}'
      '\nCateto Adjacente: {}'
      '\nHipotenusa: {:.2f}'.format(opostoC, adjacenteC, hypot(opostoC, adjacenteC)))

# OU

hipotenusa = ((opostoC ** 2) + (adjacenteC ** 2)) ** (1/2)

print('Hipotenusa: {:.2f}'.format(hipotenusa))
