# Aula 14 (Estrutura de Repetição while)

op = 'S'
media = 0
maior = menor = 0
quantidade = 0
while op == 'S':
    numero = int(input('Digite um Número: '))
    if quantidade == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    quantidade += 1
    media += numero
    op = str(input('Quer Continuar a digitar valores? [S/N]: ')).strip().upper()[0]
print('\nVocê digitou {} números'
      '\nA média é {:.2f}'
      '\nO Maior é {}'
      '\nO Menor é {}'.format(quantidade, media/quantidade, maior, menor))
