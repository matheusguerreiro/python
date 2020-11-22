# Aula 15 (Interrompendo Repetições while)

valorDoSaque = int(input('Valor do Saque: R$'))

total = valorDoSaque

cedula = 50
totalCedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totalCedula += 1
    else:
        print(f'{totalCedula} notas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedula = 0
        if total == 0:
            break
