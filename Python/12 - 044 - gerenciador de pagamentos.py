# Aula 12 (Condições em Python (if..elif))

produtoP = float(input('Valor do Produto: R$'))

print("""Condições
1 - à vista dinheiro/cheque: 10% de desconto
2 - à vista no cartão: 5% de desconto
3 - em até 2X no cartão: preço normal
4 - 3X ou mais no cartão: 20% de juros""")

opcao = int(input('Opção: '))

if opcao == 1:
    print('\033[0:32m10% de desconto!\033[m'
          '\nDe \033[0:33mR${:.2f}\033[m você vai pagar \033[0:32mR${:.2f}\033[m'.format(produtoP, produtoP - (produtoP * 10 / 100)))
elif opcao == 2:
    print('\033[0:32m5% de desconto!\033[m'
          '\nDe \033[0:33mR${:.2f}\033[m você vai pagar \033[0:32mR${:.2f}\033[m'.format(produtoP, produtoP - (produtoP * 5 / 100)))
elif opcao == 3:
    print('\033[0:33mpreço normal!\033[m'
          '\nVocê vai pagar \033[0:33mR${:.2f}\033[m'.format(produtoP))
elif opcao == 4:
    print('\033[0:31m20% de juros!\033[m'
          '\nDe \033[0:33mR${:.2f}\033[m você vai pagar \033[0:31mR${:.2f}\033[m'.format(produtoP, produtoP + (produtoP * 20 / 100)))
else:
    print('\033[0:31mOpção Inválida!\033[m')
