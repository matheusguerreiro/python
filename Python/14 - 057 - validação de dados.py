# Aula 14 (Estrutura de Repetição while)

sexo = str(input('Digite seu Sexo: [M/F]: ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Digite seu Sexo: [M/F]: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
