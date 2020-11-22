# Aula 20 (Funções (Parte 1))

def escreva(f):
    t = len(f) + 10
    print('-'*t)
    print(f'{f}'.center(t))
    print('-'*t)


print('Digite sua frase')
frase = str(input('Frase: '))
escreva(frase)
