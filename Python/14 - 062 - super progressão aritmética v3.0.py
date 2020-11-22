# Aula 14 (Estrutura de Repetição while)

pT = int(input('Primeiro Termo: '))
ra = int(input('Razão: '))

t = pT
q = 10
ct = 0

op = 1
while op != 0:
    c = 1
    ct += q
    while c <= q:
        print('{} -> '.format(t), end='')
        t += ra
        c += 1
    print('Pause')
    op = int(input('Quer ver mais quantos termos? '))
    q = op
print('Fim, você viu {} termos.'.format(ct))