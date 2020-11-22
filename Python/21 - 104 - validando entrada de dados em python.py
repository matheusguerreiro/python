# Aula 21 (Funções (Parte 2))

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[1;31mErro! Digite um número inteiro.\033[m')
        if ok == True:
            break
    return valor


print('Validação de Dados')
numero = leiaInt('Digite um Número: ')
print(f'\033[1;32mVocê acabou de digitar o número {numero}.\033[m')