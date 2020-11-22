# Aula 20 (Funções (Parte 1))

def area(l, c):
    a = l * c
    print(f'A Área é: {a:.2f}m²')


largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))

area(largura, comprimento)
