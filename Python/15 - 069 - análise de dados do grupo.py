# Aula 15 (Interrompendo Repetições while)

pessoasM18 = homensC = mulheresm20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M|F]: ')).upper().strip()[0]
    if idade > 18:
        pessoasM18 += 1
    if sexo == 'M':
        homensC += 1
    if sexo == 'F' and idade < 20:
        mulheresm20 += 1
    op = str(input('Digite N para parar o cadastro: ')).upper().strip()[0]
    if op == 'N':
        break
print('\nPessoas com mais de 18 anos: {}'
      '\nHomens cadastrados: {}'
      '\nMulheres com menos de 20 anos: {}'.format(pessoasM18, homensC, mulheresm20))
