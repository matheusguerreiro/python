# Aula 12 (Condições em Python (if..elif))

valorC = float(input('Digite o Valor da Casa: R$'))
salario = float(input('Salário do Comprador: R$'))
anos = int(input('Em quantos Anos vai pagar? '))

prestacao = valorC / (anos * 12)
salario30 = salario * 30 / 100

if prestacao > salario30:
    print('Empréstimo Negado.'
          '\nA prestação de R${:.2f} é mais alta que 30% do salário do comprador. R${:.2f}'.format(prestacao, salario30))
else:
    print('Parabéns! Empréstimo Aprovado.'
          '\nPrestação: R${:.2f}'
          '\nAnos: {}'.format(prestacao, anos))
