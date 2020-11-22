# Aula 15 (Interrompendo Repetições while)

soma = quantidade = 0
while True:
    numero = int(input('Digite um Número ou 999 para finalizar: '))
    if numero == 999:
        break
    quantidade += 1
    soma += numero
print('Você digitou {} números e a soma deles é {}.'.format(quantidade, soma))
