from Transformando_Modulos_em_Pacotes_22_111.utilidadesCeV import moeda

valor = float(input('Digite um Valor: R$'))
a = int(input('Aumento %: '))
d = int(input('Redução %: '))

moeda.resumo(valor, a, d)
