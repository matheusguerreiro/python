# Aula 23 (Tratamento de Erros e Exceções)

def leiaInt(mensagem):
    while True:
        try:
            n = int(input(mensagem))
        except (ValueError, TypeError):
            print(f'\033[0;31mErro! Digite um Número Inteiro.\033[m')
            continue
        else:
            return n


def leiaFloat(mensagem):
    while True:
        try:
            v = float(input(mensagem))
        except (ValueError, TypeError):
            print(f'\033[0;31mErro! Digite um Valor Real.\033[m')
            continue
        else:
            return v


numero = leiaInt('Digite um Número: ')
valor = leiaFloat('Digite um Valor: R$')
print(f'\033[0;32mSeu Número é {numero} e seu Valor é {valor:.1f}\033[m')
