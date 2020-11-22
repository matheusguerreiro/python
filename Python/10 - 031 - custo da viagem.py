# Aula 10 (Condições em Python (if..else))

distancia = int(input('Digite a distância em km: '))

if distancia <= 200:
    preco = distancia * 0.50
    print('Sua viagem tem distância de {}km, o preço é: R${:.2f}'.format(distancia, preco))
else:
    preco = distancia * 0.45
    print('Sua viagem tem distância de {}km, o preço é: R${:.2f}'.format(distancia, preco))

# OU

preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('Sua viagem tem distância de {}km, o preço é: R${:.2f}'.format(distancia, preco))
