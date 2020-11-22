# Aula 16 (Tuplas)

palavras = ('Computador', 'Windows', 'Linux', 'Acer', 'Dell', 'Monitor', 'Smartphone')

print(palavras)

for c in range(0, len(palavras)):
    print(f'\n{palavras[c]}', end=': ')
    for l in palavras[c]:
        if l in 'aeiouAEIOU':
            print(l, end=' ')
