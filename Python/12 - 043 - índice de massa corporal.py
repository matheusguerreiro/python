# Aula 12 (Condições em Python (if..elif))

altura = float(input('Digite sua Altura: '))
peso = float(input('Digite seu Peso: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Seu IMC é: \033[0:31m{:.1f}'
          '\nAbaixo do Peso!\033[m'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é: \033[0:32m{:.1f}'
          '\nPeso Ideal!\033[m'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é: \033[0:33m{:.1f}'
          '\nSobrepeso!\033[m'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC é: \033[0:31m{:.1f}'
          '\nObesidade!\033[m'.format(imc))
else:
    print('Seu IMC é: \033[0:31m{:.1f}'
          '\nObesidade Mórbida!\033[m'.format(imc))
