# Aula 18 (Listas (Parte2))

alunos = []
dados = []

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    media = (dados[1] + dados[2]) / 2
    dados.append(media)
    alunos.append(dados[:])
    dados.clear()

    opcao = str(input('Seguir cadastrando? (S/N): ')).upper().strip()[0]
    if opcao == 'N':
        print('Finalizando...')
        break

print('-='*10, ' BOLETIM ', '=-'*10)
for i, aluno in enumerate(alunos):
    print(f'[{i}]: {aluno[0]}: {aluno[3]:.1f}')

opcao2 = 0
while True:
    opcao2 = int(input('Quer ver as notas de qual Aluno? ou (999) para sair. : '))
    if opcao2 == 999 or opcao2 > len(alunos):
        print('Saindo...')
        break
    else:
        print(f'{alunos[opcao2][0]}: {alunos[opcao2][1]} e {alunos[opcao2][2]}')
