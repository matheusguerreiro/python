# Aula 16 (Tuplas)

produtos = ('Caderno', 15.00,
            'Canetas', 5.00,
            'Lapiseira', 11.00,
            'Estojo', 7.00,
            'Mochila', 35.00)

for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<30}', end='')
    else:
        print(f'R${produtos[c]:>5.2f}')