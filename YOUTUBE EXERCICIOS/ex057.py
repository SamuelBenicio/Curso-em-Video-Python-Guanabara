sexo = input('Digite o sexo da pessoa [M/F]: ').upper()
while(sexo not in 'MF'):
    sexo = input('Digite o sexo da pessoa novamente [M/F]: ').upper()
print('Fim.')