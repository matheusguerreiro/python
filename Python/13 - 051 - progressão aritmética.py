# Aula 13 (Estrutura de Repetição for)

primeiroT = int(input('Primeiro Termo da PA: '))
razao = int(input('Razão: '))

decimoT = primeiroT + (10 - 1) * razao

for c in range(primeiroT, decimoT + razao, razao):
    print('{} ->'.format(c), end=' ')
print('Acabou!')

# Fórmula para calcular o x termo de uma PA: termoX = primeiroT + (X - 1) * razão