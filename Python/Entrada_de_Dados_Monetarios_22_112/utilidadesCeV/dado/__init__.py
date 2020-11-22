def leiaDinheiro(msg):
    valido = False
    while valido is False:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mErro! Digite um Valor Numérico!\033[m')
        else:
            valido = True
            return float(entrada)
