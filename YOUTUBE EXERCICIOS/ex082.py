valores = []
par = []
impar = []
while(True):
    n = int(input('Digite um valor: '))
    if(n%2==0):
        par.append(n)
    else:
        impar.append(n)
    valores.append(n)
    r = input('Quer continuar? [S/N] ')
    while(r not in 'SsNn'):
        r = int(input('Quer continuar? [S/N]'))
    if(r in 'Nn'):
        break
print(f'Os valores digitados foram {valores}')
print(f'Os valores pares digitados foram {par}')
print(f'Os valores impares digitados foram {impar}')