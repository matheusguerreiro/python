# Aula 19 (Dicionários)

from datetime import date

trabalhador = {}
trabalhador['Nome'] = str(input('Nome: '))
anoN = int(input('Ano de Nascimento: '))
idade = date.today().year - anoN
trabalhador['Idade'] = idade
trabalhador['CTPS'] = int(input('Nº carteira de Trabalho: '))
if trabalhador['CTPS'] != 0:
    trabalhador['Ano de Contratação'] = int(input('Ano de Contratação: '))
    trabalhador['Salario'] = float(input('Salário: R$'))
    trabalhador['Aposentadoria'] = trabalhador['Idade'] + (trabalhador['Ano de Contratação'] + 35) - date.today().year
    print(f"\nNome: {trabalhador['Nome']}\n"
          f"Idade: {trabalhador['Idade']}\n"
          f"CTPS: {trabalhador['CTPS']}\n"
          f"Ano de Contratação: {trabalhador['Ano de Contratação']}\n"
          f"Salário: R${trabalhador['Salario']:.2f}\n"
          f"Idade quando se Aposentar: {trabalhador['Aposentadoria']}")
else:
    print(f"\nNome: {trabalhador['Nome']}\n"
          f"Idade: {trabalhador['Idade']}\n")
