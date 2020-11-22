# Aula 19 (Dicionários)

pessoa = {}
pessoas = []
pessoasMulheres = []
pessoasAMedia = []

somaIdade = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).strip()
    while True:
        pessoa['sexo'] = str(input('Sexo: [M|F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    somaIdade += pessoa['idade']
    pessoas.append(pessoa.copy())
    if pessoa['sexo'] == 'F':
        pessoasMulheres.append(pessoa.copy())
    while True:
        opcao = str(input('Quer Continuar? [S|N]: ')).strip().upper()[0]
        if opcao in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if opcao == 'N':
        break
print(f"\nA) Ao todo temos {len(pessoas)} pessoas cadastradas.")
mediaIdade = somaIdade / len(pessoas)
print(f"B) A média de idade é {mediaIdade:.2f} anos.")
print(f"C) As mulheres cadastradas foram ", end='')
for c in range(0, len(pessoasMulheres)):
    if c < len(pessoasMulheres) - 1:
        print(pessoasMulheres[c]['nome'], end=', ')
    else:
        print(pessoasMulheres[c]['nome'], end='.')
print(f"\nD) As pessoas acima da média foram ", end='')
for c in range(0, len(pessoas)):
    if pessoas[c]['idade'] > mediaIdade:
        pessoasAMedia.append(pessoas[c].copy())         # sempre .copy() para copiar dicionários
    if c < len(pessoas) - 1 and pessoas[c]['idade'] > mediaIdade:
        print(pessoas[c]['nome'], end=', ')
    elif c == len(pessoas) - 1 and pessoas[c]['idade'] > mediaIdade:
        print(pessoas[c]['nome'], end='.')
