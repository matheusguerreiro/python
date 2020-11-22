# Aula 10 (Condições em Python (if..else))

segmento1 = int(input('Digite o primeiro segmento: '))
segmento2 = int(input('Digite o segundo segmento: '))
segmento3 = int(input('Digite o terceiro segmento: '))

if segmento1 < segmento2 + segmento3 and segmento2 < segmento3 + segmento1 and segmento3 < segmento1 + segmento2:
    print('Esses segmentos formam um Triângulo.')
else:
    print('Esses segmentos Não formam um Triângulo.')
