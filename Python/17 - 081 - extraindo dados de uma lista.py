# Aula 17 (Listas (Parte 1))

valores = []

while True:
    valor = int(input('Digite um Valor ou -1 para Finalizar: '))
    if valor < 0:
        print('\nFinalizando...')
        break
    else:
        valores.append(valor)
print(f'Foram digitados {len(valores)} números')
valores.sort(reverse=True)
print(f'Lista ordenada de forma decrescente: {valores}')
if 5 in valores:
    valores.reverse()
    print(f'O valor 5 foi digitado e está na {valores.index(5)} posição.')
else:
    print('Valor 5 não encontrado na lista.')
