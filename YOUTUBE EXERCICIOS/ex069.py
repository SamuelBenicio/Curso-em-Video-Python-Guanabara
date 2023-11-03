cont18 = homem = contm20 = 0
while(True):
    print(f'{"":=^40}')
    idade = int(input('Digite a idade da pessoa: '))
    sexo = ' '
    while(sexo not in 'MF'):
        sexo = input('Digite o sexo da pessoa (M/F): ').strip().upper()
    print(f'{"":=^40}')
    if(idade>18):
        cont18 +=1
    if(sexo=='M'):
        homem +=1
    if(sexo=='M'):
        if(idade<20):
            contm20 +=1
    continua = ' '
    while(continua not in 'SN'):
        continua = input('Voce quer continuar a rodar o progama?(S/N)  '.upper())
    if(continua=='N'):
        break
print(f'A quantidade de pessoas cadastradas com mais de 18 anos é {cont18}, a quantidade de homens cadastrados é {homem} e')
print(f' a quantidade de mulheres com menos de 20 anos é {contm20}.')
