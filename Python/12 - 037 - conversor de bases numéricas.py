# Aula 12 (Condições em Python (if..elif))

numero = int(input('Digite um Número: '))

print('Opções...'
      '\n(1) Binário'
      '\n(2) Octal'
      '\n(3) Hexadecimal')
opcao = int(input('Opção: '))

if opcao == 1:
    print('{} em Binário é: {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} em Octal é: {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} em Hexadecimal é: {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção Inválida!')
