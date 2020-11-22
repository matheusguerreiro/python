# Aula 09 (Manipulando Texto)

numero = int(input('Digite um Número entre 0 e 9999: '))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print('Seu Número: {}'
      '\nUnidade: {}'
      '\nDezena: {}'
      '\nCentena: {}'
      '\nMilhar: {}'.format(numero, unidade, dezena, centena, milhar))
