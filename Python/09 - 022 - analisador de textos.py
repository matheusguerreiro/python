# Aula 09 (Manipulando Texto)

nome = str(input('Digite seu nome Completo: ')).strip()

print('Todo em MAIÚSCULAS: {}'
      '\nTodo em minúsculas: {}'.format(nome.upper(), nome.lower()))
print('Quantidade de Letras: {}'.format(len(nome) - nome.count(' ')))
print('Quantidade de Letras do Primeiro nome: {}'.format(nome.find(' ')))
