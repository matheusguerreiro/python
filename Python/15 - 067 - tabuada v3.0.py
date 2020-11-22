# Aula 15 (Interrompendo Repetições while)

c = 0
while True:
    numero = int(input('Digite um Número: '))
    if numero < 0:
        break
    for c in range(0, 11, 1):
        print('{} X {} = {}'.format(numero, c, numero*c))
print('Fim')