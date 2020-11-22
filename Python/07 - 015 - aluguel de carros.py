# Aula 07 (Operadores Aritméticos)

kmP = float(input('Quantidade de km percorridos: '))
dias = int(input('Quantidade de dias alugado: '))

preco = (kmP * 0.15) + (dias * 60)

print('Quilometros Percorridos: {:.2f}'
      '\nDias Alugado: {}'
      '\nPreço a Pagar: R${:.2f}'.format(kmP, dias, preco))
