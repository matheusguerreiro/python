# Aula 12 (Condições em Python (if..elif))

lado1 = float(input('Lado 1: '))
lado2 = float(input('Lado 2: '))
lado3 = float(input('Lado 3: '))

if lado1 < (lado2 + lado3) and lado2 < (lado3 + lado1) and lado3 < (lado1 + lado2):
    print('\033[0:33mEssas medidas formam um Triângulo!\033[m')
    if lado1 == lado2 == lado3:
        print('\033[0:32mEquilátero!\033[m')
    elif lado1 != lado2 != lado3 != lado1:
        print('\033[0:32mEscaleno!\033[m')
    else:
        print('\033[0:32mIsósceles!\033[m')
else:
    print('\033[0:31mEssas medidas Não formam um Triângulo!\033[m')
