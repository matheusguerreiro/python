def arquivoExiste(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        print('Arquivo Não Encontrado!')
        return False
    else:
        print('Arquivo Encontrado!')
        return True


def arquivoCria(nome):
    try:
        arquivo = open(nome, 'wt+')
        arquivo.close()
    except:
        print('Erro na Criação do Arquivo!')
    else:
        print('Arquivo Criado com Sucesso!')


def arquivoLe(nome):
    try:
        arquivo = open(nome, 'rt')
    except:
        print('Erro na Leitura do Arquivo!')
    else:
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<25}{dado[1]:>20} anos')
    finally:
        arquivo.close()


def cadastrar(arquivo, nome='Desconhecido', idade=0):
    try:
        arq = open(arquivo, 'at')
    except:
        print('Erro ao Abrir Arquivo!')
    else:
        try:
            arq.write(f'{nome};{idade}\n')
        except:
            print('Erro ao Escrever no Arquivo!')
        else:
            print(f'Novo Cadastro realizado com Sucesso!')


