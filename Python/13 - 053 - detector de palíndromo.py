# Aula 13 (Estrutura de Repetição for)

frase = str(input('Digite uma frase: ')).lower().strip()
print(frase)

fraseEmPalavras = frase.split()
print(fraseEmPalavras)

fraseTudoJunto = ''.join(fraseEmPalavras)
print(fraseTudoJunto)

'''fraseInversa = ''
                        # OU fraseInversa = fraseTudoJunto[::-1]
for letra in range(len(fraseTudoJunto) - 1, -1, -1):
    fraseInversa += fraseTudoJunto[letra]'''

fraseInversa = fraseTudoJunto[::-1]

print(fraseInversa)

if fraseTudoJunto == fraseInversa:
    print('A Frase: {}'
          '\nÉ um Palíndromo!'.format(frase))
else:
    print('Não é um Palíndromo!')
