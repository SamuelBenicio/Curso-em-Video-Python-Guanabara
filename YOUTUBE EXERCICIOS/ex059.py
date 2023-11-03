print(f'{"Bem-Vindo":=^40}')
print('[1] Soma.')
print('[2] Multiplicação.')
print('[3] Maior Valor digitado.')
print('[4] Para digitar novos valores.')
print('[5] Para sair do progama.')
n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite outro numero inteiro: '))
n3 = 0
maior = 0
while(n3!=5):
    n3 = int(input('Digite o numero da operação a ser realizada: '))
    while(n3>5):
        n3 = int(input('Digite um numero valido para realizar a operação:'))
    if(n3==1):
        print(f'O valor da soma entre os numeros {n1} + {n2} é: {n1+n2}')
    if(n3==2):
        print(f'O valor da multiplicação entre os numeros {n1} * {n2} é: {n1*n2}')
    if(n3==3):
        if(n1>n2):
            maior = n1
        else:
            maior = n2
        print(f'O maior valor digitado é: {maior}')
    if(n3==4):
        print(f'{"=":=^40}')
        print('[1] Soma.')
        print('[2] Multiplicação.')
        print('[3] Maior Valor digitado.')
        print('[4] Para digitar novos valores.')
        print('[5] Para sair do progama.')
        n1 = int(input('Digite um numero inteiro: '))
        n2 = int(input('Digite outro numero inteiro: '))