n = 1
par = 0
impar = 0
while(n!=0):
    n = int(input('Digite um numero: '))
    if(n!=0):
        if(n%2==0):
            par +=1
        else:
            impar +=1
print(f'A quantidade de numero pares digitados pelo usuario foi: {par}')
print(f'A quantidade de numeros impares digitados pelo usuario foi: {impar}')