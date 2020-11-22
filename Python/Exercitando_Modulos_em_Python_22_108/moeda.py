# Funções

def aumentar(v=0, p=0):
    r = v + (v * p / 100)
    return r


def diminuir(v=0, p=0):
    r = v - (v * p / 100)
    return r


def dobro(v=0):
    r = v * 2
    return r


def metade(v=0):
    r = v / 2
    return r


def moeda(v=0, moeda='R$'):
    return f'{moeda}{v:.2f}'.replace('.', ',')      # replace para substituir os . por ,

