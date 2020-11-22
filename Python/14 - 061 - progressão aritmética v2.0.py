# Aula 14 (Estrutura de Repetição while)

primeiroT = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))

decimoT = primeiroT + (10 - 1) * razao

pa = primeiroT
while pa != (decimoT + razao):
    print('PA: ', end='') if pa == primeiroT else print('-> ', end='')
    print(pa, end=' ')
    pa += razao
print('-> Acabou!')

# OU

termo = primeiroT
c = 1
while c <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    c += 1
print('FIM')