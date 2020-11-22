# Aula 17 (Listas (Parte 1))

expressao = str(input('Digite a Expressão Numérica: ')).strip().lower()
print(expressao)

lista = []

for simbolo in expressao:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Expressão Válida!')
else:
    print('Expressão Inválida!')
