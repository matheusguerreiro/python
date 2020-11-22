# Funções

def aumentar(v=0, p=0, f=False):
    r = v + (v * p / 100)
    return r if f is False else moeda(r)


def diminuir(v=0, p=0, f=False):
    r = v - (v * p / 100)
    return r if f is False else moeda(r)


def dobro(v=0, f=False):
    r = v * 2
    return r if f is False else moeda(r)


def metade(v=0, f=False):
    r = v / 2
    return r if f is False else moeda(r)


def moeda(v=0, moeda='R$'):
    return f'{moeda}{v:.2f}'.replace('.', ',')      # replace para substituir os . por ,


def resumo(v=0, a=0, d=0):
    print(f'\nPreço analisado: {moeda(v)}\n'
            f'Dobro: {dobro(v, True)}\n'
            f'Metade: {metade(v, True)}\n'
            f'Com {a}% de aumento: {aumentar(v, a, True)}\n'
            f'Com {d}% de redução: {diminuir(v, d, True)}')

