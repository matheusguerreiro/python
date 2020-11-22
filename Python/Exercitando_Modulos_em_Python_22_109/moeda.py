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

