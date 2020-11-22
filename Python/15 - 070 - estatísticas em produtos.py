# Aula 15 (Interrompendo Repetições while)

total = pM1000 = c = 0
precoMB = 0
nomeMB = ''
while True:
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço do Produto: R$'))
    if c == 0:
        precoMB = preco
        nomeMB = nome
    else:
        if preco < precoMB:
            precoMB = preco
            nomeMB = nome
    total += preco
    if preco > 1000:
        pM1000 += 1
    c += 1
    op = str(input('Quer continuar comprando? [S|N]: ')).strip().upper()[0]
    if op == 'N':
        break
print('A) Total: R${:.2f}'
      '\nB) + 1000: {}'
      '\nC) Nome mais Barato: {}'.format(total, pM1000, nomeMB))
