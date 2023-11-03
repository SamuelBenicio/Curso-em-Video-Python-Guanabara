n1 = int(input('Digite um numero inteiro: '))
div = n1/2
resto = div%2==0
rest = (div+1)%2==0
if(resto or rest):
    print('O numero digitado é par')
else:
    print('O numero digitado é impar')
