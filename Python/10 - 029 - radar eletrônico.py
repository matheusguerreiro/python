# Aula 10 (Condições em Python (if..else))

velocidade = int(input('Digite a Velocidade atual: '))

if velocidade <= 80:
    print('\nVocê está viajando a {}km/h, tenha uma boa viagem.'.format(velocidade))
else:
    multa = (velocidade - 80) * 7
    print('\nVocê está viajando a {}km/h e ultrapassou a velocidade permitida!'
          '\nSerá multado em R${:.2f} pelo excesso de velocidade.'.format(velocidade, multa))
