vel = float(input('Digite a velocidade do carro: '))
if(vel>80):
    print('Voce foi multado por ultrapassar o limite de velocidade de 80km/h')
    multa = vel - 80
    print(f'O valor a ser pago pela multa é {7*multa}')
else:
    print('Voce nao ultrapassou o limite de velocidade')
