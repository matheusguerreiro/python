# Aula 20 (Funções (Parte 1))

from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    if i < f:
        c = i
        while c <= f:
            print(f'{c} ', end='')
            sleep(0.5)
            c += p
        print('Fim')
    else:
        c = i
        while c >= f:
            print(f'{c} ', end='')
            sleep(0.5)
            c -= p
        print('Fim')


contador(1, 10, 1)
contador(10, 0, 2)
print('Sua vez de personalizar a Contagem')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
