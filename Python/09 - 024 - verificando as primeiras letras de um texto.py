# Aula 09 (Manipulando Texto)

cidade = str(input('Em que Cidade você nasceu? ')).strip().upper()

cidadeS = cidade.split()

print('Sua Cidade começa com Santo? {}'.format(cidadeS[0] == 'SANTO'))

# OU

print(cidade[:5].upper() == 'SANTO')
