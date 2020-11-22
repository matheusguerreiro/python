# Aula 07 (Operadores Aritméticos)

salario = float(input('Digite seu Salário: R$'))

salario15 = salario + ((salario * 15) / 100)

print('Salário Atual: R${:.2f}'
      '\nSalário com 15% de Aumento: R${:.2f}'.format(salario, salario15))
