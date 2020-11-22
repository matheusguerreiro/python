# Aula 07 (Operadores Aritméticos)

seudinheiro = float(input('Quanto dinheiro você tem? R$'))

dolar = 5.41
euro = 6.37

print('Você tem: R${:.2f}'
      '\nPode Comprar'
      '\n${:.2f} | \u20ac{:.2f}'.format(seudinheiro, (seudinheiro / dolar), (seudinheiro / euro)))
