n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
if(n1>n2):
    print(f'O primeiro numero {n1} é maior que o segundo numero {n2}')
elif(n2>n1):
    print(f'O segundo numero {n2} é maior que o primeiro numero {n1}')
else:
    print('Os dois numeros sao iguais')