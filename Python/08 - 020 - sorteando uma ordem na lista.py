# Aula 08 (Usando Módulos do Python)

from random import shuffle

nome1 = str(input('Digite o Primeiro nome: '))
nome2 = str(input('Digite o Segundo nome: '))
nome3 = str(input('Digite o Terceiro nome: '))
nome4 = str(input('Digite o Quarto nome: '))

lista = [nome1, nome2, nome3, nome4]
shuffle(lista)

print('A ordem de apresentação será: {}'.format(lista))
