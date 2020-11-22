# Aula 20 (Funções (Parte 1))

def maior(* n):     # * para receber x parametros
    c = maior = 0
    if len(n) == 0:
        print(f'Não foi passado nenhum valor.')
    else:
        print('Analisando os Valores')
        print(n)
        for c in range(0, len(n)):
            if c == 0:
                maior = n[c]
            elif n[c] > maior:
                maior = n[c]
        print(f'Foram analisados {len(n)} valores, onde desses valores o {maior} é o maior.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()