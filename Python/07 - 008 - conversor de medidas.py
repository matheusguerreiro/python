# Aula 07 (Operadores Aritméticos)

medida = int(input('Digite uma Medida em metros: '))

print('mm: {}'
      '\ncm: {}'
      '\ndm: {}'
      '\nm: {}'
      '\ndam: {}'
      '\nhm: {}'
      '\nkm: {}'.format((medida * 1000), (medida * 100), (medida * 10), medida,
                        (medida / 10), (medida / 100), (medida / 1000)))
