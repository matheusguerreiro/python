# Aula 08 (Usando Módulos do Python)

from math import sin, cos, tan, radians  # para seno, cosseno e tangente
                                         # é preciso converter o ângulo para radians

angulo = float(input('Digite um Ângulo qualquer: '))

print('Ângulo: {:.2f}'
      '\nSeno: {:.2f}'
      '\nCosseno: {:.2f}'
      '\nTangente: {:.2f}'.format(angulo, sin(radians(angulo)), cos(radians(angulo)), tan(radians(angulo))))
