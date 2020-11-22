# Aula 12 (Condições em Python (if..elif))

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 6:
    print('\nNota 1: {:.1f}'
          '\nNota 2: {:.1f}'
          '\n\nMédia: \033[0:31m{:.1f}\033[m'
          '\n\033[1:31mReprovado!\033[m'.format(nota1, nota2, media))
elif media >= 6 and media < 7:
    print('\nNota 1: {:.1f}'
          '\nNota 2: {:.1f}'
          '\n\nMédia: \033[0:33m{:.1f}\033[m'
          '\n\033[1:33mRecuperação!\033[m'.format(nota1, nota2, media))
elif media >= 7 and media <= 10:
    print('\nNota 1: {:.1f}'
          '\nNota 2: {:.1f}'
          '\n\nMédia: \033[0:32m{:.1f}\033[m'
          '\n\033[1:32mAprovado!\033[m'.format(nota1, nota2, media))
else:
    print('\n\033[1:31mErro!\033[m \033[1:33mTente Novamente...\033[m')
