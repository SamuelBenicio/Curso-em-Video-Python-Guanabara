cont = 0
soma = 0
while(True):
    n1 = int(input('Digite um numero (999 para parar o progama): '))
    if(n1==999):
        break
    soma +=n1
    cont +=1
print(f'A soma dos {cont} foi {soma}')