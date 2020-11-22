# Aula 06 (Tipos Primitivos e Saída de Dados)

algo = input('Digite Algo pelo Teclado: ')

print('O Tipo Primitivo é: {}'
      '\nSó tem Espaços: {}'
      '\nÉ um Número: {}'
      '\nÉ Alfabético: {}'
      '\nÉ Alfanumérico: {}'
      '\nEstá em MAIÚSCULAS: {}'
      '\nEstá em minúsculas: {}'
      '\nEstá Captalizada: {}'.format(type(algo), algo.isspace(), algo.isnumeric(), algo.isalpha(), algo.isalnum(),
                                      algo.isupper(), algo.islower(), algo.istitle()))
