# Aula 14 (Estrutura de Repetição while)

qT = int(input('Quantos termos para a sequência de fibonacci? '))

pT = 0
sT = 1
print('{} -> {} -> '.format(pT, sT), end='')

c = 3
while c <= qT:
    tT = pT + sT
    print('{} -> '.format(tT), end='')
    pT = sT
    sT = tT
    c += 1
print('FIM')
