# Aula 22 (Módulos e Pacotes)

from Exercitando_Modulos_em_Python_22_107 import moeda

valor = float(input('Digite um Valor: R$'))

print(f'O Dobro de {valor} é {moeda.dobro(valor)}')
print(f'A Metade de {valor} é {moeda.metade(valor)}')
a = int(input('Aumentar %: '))
print(f'O valor {valor} com mais {a}% de aumento é: {moeda.aumentar(valor, a)}')
d = int(input('Diminuir %: '))
print(f'O valor {valor} com menos {d}% é: {moeda.diminuir(valor, d)}')
