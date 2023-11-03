from random import randint
n1 = randint(0,10)
n2 = int(input('Digite um numero inteiro entre 0 a 10: '))
cont = 1
while(n1!=n2):
    n2 = int(input('Digite um numero inteiro entre 0 a 10: '))
    cont +=1
print(f'Voce acertou o numero pensado pelo computador({n1}) em {cont} tentativas.')