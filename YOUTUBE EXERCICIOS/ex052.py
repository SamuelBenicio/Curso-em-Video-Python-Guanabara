n1 = int(input('Digite um numero inteiro: '))
cont = 0
for c in range(1,n1+1):
    if(n1%c==0):
        cont += 1
print(f'O numero foi {n1} foi divisivel {cont} vezes.')
if(cont==2):
    print('O numero é primo')
else:
    print('O numero nao é primo')