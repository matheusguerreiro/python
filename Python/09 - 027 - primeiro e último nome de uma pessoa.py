# Aula 09 (Manipulando Texto)

nome = str(input('Digite seu nome Completo: ')).strip().title()

nomeS = nome.split()

print('Seu Primeiro nome é: {}'.format(nomeS[0]))
print('Seu Último nome é: {}'.format(nomeS[len(nomeS)-1]))
