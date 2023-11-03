n1 = 0
cont = 0
soma = 0
while(n1!=999):
    n1 = int(input('Digite um numero inteiro: '))
    if(n1==999):
        break
    soma +=n1
    cont +=1
print(f'A quantidade de numeros digitados foi {cont} e a soma entre eles foi {soma}')