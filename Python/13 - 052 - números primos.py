# Aula 13 (Estrutura de Repetição for)

numero = int(input('Digite um Número: '))

totalDivisiveis = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[0:32m', end='')
        totalDivisiveis += 1
    else:
        print('\033[0:31m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO Número {} foi divisivel {} vezes!'.format(numero, totalDivisiveis))
if totalDivisiveis == 2:
    print('\033[0:33m{} é Primo!\033[m'.format(numero))

# Um Número só é Primo quando for divisível por 1 e por ele mesmo!