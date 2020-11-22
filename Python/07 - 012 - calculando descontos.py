# Aula 07 (Operadores Aritméticos)

preco = float(input('Digite o Valor do produto: R$'))

print('Preço: R${:.2f}'
      '\nPreço com 5% de desconto: R${:.2f}'.format(preco, (preco - ((preco * 5) / 100))))
