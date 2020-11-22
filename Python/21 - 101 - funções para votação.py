# Aula 21 (Funções (Parte 2))

def voto(an):
    from datetime import date
    aa = date.today().year
    i = aa - an
    if i < 16:
        return f'Com idade {i} o voto é: NEGADO'
    elif i >= 16 and i < 18:
        return f'Com idade {i} o voto é: OPCIONAL'
    elif i >= 18 and i < 65:
        return f'Com idade {i} o voto é: OBRIGATÓRIO'
    else:
        return f'Com idade {i} o voto é: OPCIONAL'


anoNascimento = int(input('Ano de Nascimento: '))
print(voto(anoNascimento))
