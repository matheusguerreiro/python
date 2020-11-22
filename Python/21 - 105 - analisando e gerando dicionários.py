# Aula 21 (Funções (Parte 2))

def notas(*notas, situacao=False):
    '''
    :param notas: as notas dos alunos
    :param situacao: se vai mostrar ou não a situação da turma
    :return: retorna o dicionário com todas as informações
    '''
    ret = {}
    ret['total'] = len(notas)
    ret['maior'] = max(notas)
    ret['menor'] = min(notas)
    ret['media'] = sum(notas) / len(notas)
    if situacao == True:
        if 7 <= ret['media'] <= 10:
            ret['situação'] = 'BOA'
        elif 6 <= ret['media'] < 7:
            ret['situação'] = 'RAZOÁVEL'
        else:
            ret['situação'] = 'RUIM'
    return ret


retorno = notas(7.2, 4.4, 9.6, 5, 7, situacao=True)
print(retorno)
help(notas)
