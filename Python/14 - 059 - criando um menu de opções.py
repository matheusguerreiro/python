# Aula 14 (Estrutura de Repetição while)

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

opcao = 0
while opcao != 5:
    print('''\n  - MENU -     
    1 - somar
    2 - multiplicar
    3 - maior
    4 - novos valores
    5 - sair''')

    opcao = int(input('Opção: '))

    if opcao == 1:
        soma = valor1 + valor2
        print('A Soma é: {}'.format(soma))
    elif opcao == 2:
        multiplicacao = valor1 * valor2
        print('A Multiplicação é: {}'.format(multiplicacao))
    elif opcao == 3:
        if valor1 > valor2:
            maior = valor1
            print('O Maior é: {}'.format(maior))
        else:
            maior = valor2
            print('O Maior é: {}'.format(maior))
    elif opcao == 4:
        valor1 = int(input('Novo valor 1: '))
        valor2 = int(input('Novo valor 2: '))
    elif opcao == 5:
        print('Saindo...')
    else:
        print('Opção Inválida!'
              '\nTente novamente...')
