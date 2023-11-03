n1 = int(input('Digite o primeiro valor inteiro: '))
n2 = int(input('Digite o segundo valor inteiro: '))
n3 = int(input('Digite o terceiro valor inteiro: '))
n4 = int(input('Digite o quarto valor inteiro: '))
numeros = (n1,n2,n3,n4)
print(f'O numero 9 apareceu {numeros.count(9)} vezes na tupla')
if(3 in numeros):
    print(f'O numero 3 foi digitado pela primeira vez na posiçao {numeros.index(3)+1}')
else:
    print(f'O numero 3 nao foi digitado')
print(f'Os valores pares digitados foram ',end='')
for n in numeros:
    if(n%2==0):
        print(n,end=' ')
