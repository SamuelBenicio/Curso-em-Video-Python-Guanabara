numeros = []
while(True):
    n1 = int(input('Digite um valor inteiro : '))
    if(n1 in numeros):
        print(f'Numero repetido.Numero nao adicionado')
    else:
        numeros.append(n1)
    cont = input('Quer continuar? [S/N] ')
    while(cont not in 'SsNn'):
        cont = input('Quer continuar? [S/N] ')
    if(cont in 'Nn'):
        break
numeros.sort()
print(f'Os valores digitados foram: {numeros}')