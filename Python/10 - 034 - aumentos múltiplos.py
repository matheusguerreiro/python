# Aula 10 (Condições em Python (if..else))

salario = float(input('Digite o Salario atual: R$'))

if salario > 1250:
    print('Seu novo Salário é: {:.2f}'.format(salario + (salario * 10 / 100)))
else:
    print(('Seu novo Salário é: {:.2f}'.format(salario + (salario * 15 / 100))))
