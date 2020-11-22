# Aula 19 (Dicionários)

aluno = {}

aluno['nome'] = str(input('Nome do Aluno(a): '))
aluno['media'] = float(input(f'Média do Aluno(a) {aluno["nome"]}: '))

if aluno['media'] >= 7 and aluno['media'] <= 10:
    aluno['situacao'] = str('Aprovado')
    print('\033[0:32m')
elif aluno['media'] >= 6 and aluno['media'] < 7:
    aluno['situacao'] = str('Recuperação')
    print('\033[0:33m')
elif aluno['media'] >= 0 and aluno['media'] < 6:
    aluno['situacao'] = str('Reprovado')
    print('\033[0:31m')
else:
    print('Opção Errada!')
    print('\033[0:31m')

for chave, valor in aluno.items():
    print(f'{chave}: {valor}')
