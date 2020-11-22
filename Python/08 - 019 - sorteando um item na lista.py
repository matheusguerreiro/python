# Aula 08 (Usando Módulos do Python)

from random import choice  # import random

nome1 = str(input('Primeiro Aluno: '))
nome2 = str(input('Segundo Aluno: '))
nome3 = str(input('Terceiro Aluno: '))
nome4 = str(input('Quarto Aluno: '))

lista = [nome1, nome2, nome3, nome4]

escolhido = choice(lista)

print('O aluno escolhido foi: {}'.format(escolhido))
