from Entrada_de_Dados_Monetarios_22_112.utilidadesCeV import dado
from Entrada_de_Dados_Monetarios_22_112.utilidadesCeV import moeda

"""valor = float(input('Digite um Valor: R$'))
a = int(input('Aumento %: '))
d = int(input('Redução %: '))

moeda.resumo(valor, a, d)"""

valor = dado.leiaDinheiro('Digite um Valor: R$')
moeda.resumo(valor, 10, 10)
