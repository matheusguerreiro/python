# Aula 17 (Listas (Parte 1))

valores = []

while True:
    valor = int(input('Digite um Valor ou -1 para Finalizar: '))
    if valor == -1:
        break
    else:
        if valor not in valores:
            valores.append(valor)
valores.sort()
print(valores)
