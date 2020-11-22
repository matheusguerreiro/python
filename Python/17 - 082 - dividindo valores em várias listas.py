# Aula 17 (Listas (Parte 1))

numeros = []

while True:
    numero = int(input('Digite um Número ou -1 para Finalizar: '))
    if numero < 0:
        break
    else:
        numeros.append(numero)
print(numeros)

numerosPares = []
numerosImpares = []

for n in numeros:
    if n % 2 == 0:
        numerosPares.append(n)
    else:
        numerosImpares.append(n)

print(f'\nLista: {numeros}'
      f'\nLista 2: {numerosPares}'
      f'\nLista 3: {numerosImpares}')
