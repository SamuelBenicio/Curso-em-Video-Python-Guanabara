dist = float(input('Digite a distancia da viagem em km: '))
if(dist<=200):
    print(f'O valor da passagem é: {dist*0.5}R$')
else:
    print(f'O valor da passagem é: {dist*0.45}R$')