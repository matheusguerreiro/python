# Aula 09 (Manipulando Texto)

frase = str(input('Digite uma Frase: ')).strip().upper()

print('Quantidade de Letras A: {}'.format(frase.count('A')))
print('Primeira Apariçao: {}'.format(frase.find('A')))
print('Última Aparição: {}'.format(frase.rfind('A')))
