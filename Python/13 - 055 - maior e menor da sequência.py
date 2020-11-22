# Aula 13 (Estrutura de Repetição for)

maior = menor = 0
for c in range(0, 5):
    peso = float(input('Digite seu Peso: '))
    if c == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('Das 5 pessoas:'
      '\nO maior peso é: {:.1f}Kg'
      '\nO menor peso é: {:.1f}Kg'.format(maior, menor))
