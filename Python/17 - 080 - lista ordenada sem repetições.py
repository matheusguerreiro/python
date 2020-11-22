# Aula 17 (Listas (Parte 1))

valores = []

for c in range(0, 5):
    valor = int(input('Digite um Valor: '))
    if c == 0 or valor > valores[-1]:
        valores.append(valor)
    else:
        posicao = 0
        while posicao < len(valores):
            if valor <= valores[posicao]:
                valores.insert(posicao, valor)
                break
            posicao += 1
print(valores)
