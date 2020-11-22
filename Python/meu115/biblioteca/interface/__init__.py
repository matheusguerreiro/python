def linha(tamanho=50):
    return f'-' * tamanho


def cabecalho(cabecalho):
    print(linha())
    print(f'{cabecalho.center(50)}')
    print(linha())


def menu(lista):
    cabecalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    op = leiaInt('Opção: ')
    print(linha())
    return op


def leiaInt(mensagem):
    while True:
        try:
            n = int(input(mensagem))
        except (ValueError, TypeError):
            print(f'\033[0;31mErro! Digite um Número Inteiro.\033[m')
            continue
        else:
            return n

