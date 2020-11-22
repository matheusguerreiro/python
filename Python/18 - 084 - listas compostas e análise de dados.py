# Aula 18 (Listas (Parte 2))

pessoas = []
dadosPessoa = []
pessoasMaisPesadas = []
pessoasMenosPesadas = []

pessoasCadastradas = 0
while True:
    dadosPessoa.append(str(input('Nome: ')))
    dadosPessoa.append(float(input('Peso: ')))
    pessoas.append(dadosPessoa[:])
    if dadosPessoa[1] > 60:
        pessoasMaisPesadas.append(dadosPessoa[:])
    else:
        pessoasMenosPesadas.append(dadosPessoa[:])
    dadosPessoa.clear()
    pessoasCadastradas += 1
    op = int(input('Seguir Cadastrando? (1) Sim (2) Não: '))
    if op == 2:
        print('Finalizando...')
        break
    elif op == 1:
        print('Próximo Cadastro...')
    else:
        print('Opção Errada! Tente Novamente...')
print(f'\nForam Cadastradas {pessoasCadastradas} pessoas')
print('\nLista Completa')
for pessoa in pessoas:
    print(pessoa)
print(f'\nPessoas + Pesadas')
for pessoa in pessoasMaisPesadas:
    print(pessoa)
print(f'\nPessoas - Pesadas')
for pessoa in pessoasMenosPesadas:
    print(pessoa)
