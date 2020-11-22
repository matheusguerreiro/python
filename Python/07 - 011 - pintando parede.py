# Aula 07 (Operadores Aritméticos)

larguraP = float(input('Digite a Largura da parede: '))
alturaP = float(input('Digite a Altura da Parede: '))

area = larguraP * alturaP

litrosT = area / 2

print('Largura da Parede: {:.2f}m'
      '\nAltura da Parede: {:.2f}m'
      '\nÁrea da Parede: {:.2f}m²'
      '\nLitros de Tinta para Pintá-la: {:.2f}l'.format(larguraP, alturaP, area, litrosT))
