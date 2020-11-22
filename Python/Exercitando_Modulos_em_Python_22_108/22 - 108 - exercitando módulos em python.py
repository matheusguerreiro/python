# Aula 22 (Módulos e Pacotes)

#107
from Exercitando_Modulos_em_Python_22_108 import moeda

valor = float(input('Digite um Valor: R$'))

print(f'O Dobro de {valor} é {moeda.dobro(valor)}')
print(f'A Metade de {valor} é {moeda.metade(valor)}')
a = int(input('Aumentar %: '))
print(f'O valor {valor} com mais {a}% de aumento é: {moeda.aumentar(valor, a)}')
d = int(input('Diminuir %: '))
print(f'O valor {valor} com menos {d}% de desconto é: {moeda.diminuir(valor, d)}')

#108
print(f'\nO Dobro de {moeda.moeda(valor)} é: {moeda.moeda(moeda.dobro(valor))}')
print(f'A Metade de {moeda.moeda(valor)} é: {moeda.moeda(moeda.metade(valor))}')
print(f'O valor {moeda.moeda(valor)} com mais {a}% de aumento é: {moeda.moeda(moeda.aumentar(valor, a))}')
print(f'O valor {moeda.moeda(valor)} com menos {d}% de desconto é: {moeda.moeda(moeda.diminuir(valor, d))}')
