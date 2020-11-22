# Aula 13 (Estrutura de Repetição for)

nomeHMVelho = ''
media = mulheresm20 = idadeHMVelho = 0
for c in range(0, 4):
    nome = str(input('Nome da {}ª pessoa: '.format(c + 1))).strip()
    idade = int(input('Idade da {}ª pessoa: '.format(c + 1)))
    sexo = str(input('Sexo da {}ª pessoa: [M|F]: '.format(c + 1))).strip().upper()[0]

    if c == 0 and sexo == 'M':
        nomeHMVelho = nome
        idadeHMVelho = idade
    elif sexo == 'M' and idade > idadeHMVelho:
        idadeHMVelho = idade
        nomeHMVelho = nome

    if sexo == 'F' and idade < 20:
        mulheresm20 += 1

    media += idade
print('\nDas 4 pessoas analisadas:'
      '\nA Média de Idade é: {:.1f}'
      '\nO Nome do Homem mais velho é: {}'
      '\n{} mulheres tem menos de 20 anos'.format(media / 4, nomeHMVelho, mulheresm20))
