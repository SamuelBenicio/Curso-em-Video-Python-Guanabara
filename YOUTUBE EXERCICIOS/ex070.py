soma = barato = cont1000 = maisbarato = cont = nomeb =0
while(True):
    nome = input('Nome do produto: ')
    preço = float(input('Preço do produto: '))
    soma +=preço
    cont +=1
    if(preço>1000):
        cont1000 +=1
    if(cont==1):
        barato = preço
    else:
        if(preço<barato):
            barato = preço
            nomeb = nome
    n = ' '
    while(n not in 'SN'):
        n = input('Voce quer continuar com o progama [S/N]? ').upper()
    if(n=='N'):
        break
print(f'{"":=^40}')
print(f'O valor total gasto na compra foi R${soma:.2f}, {cont1000} produtos custam mais que 1000 reais e {nomeb} foi o produto mais barato com')
print(f' o valor de R${barato:.2f}. ')
print(f'{"Fim.":=^40}')