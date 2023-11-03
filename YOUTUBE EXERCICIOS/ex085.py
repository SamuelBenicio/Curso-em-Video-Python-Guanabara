numeros = [[],[]]
for c in range(1,8):
    n1 = 1
    if(n1%2==0):
        numeros[0].append(n1)
    else:
        numeros[1].append(n1)

numeros[0].sort()
numeros[1].sort()
print(f'Os numeros pares em ordem crescente : {numeros[0]}')
print('----------')
print(f'Os numeros IMpares em ordem crescente : {numeros[1]}')