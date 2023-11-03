from random import randint
n1 = randint(0,5)
n2 = int(input('Digite um numero: '))
if(n1==n2):
    print('Parabens!!Voce acertou o mesmo numero que o computador pensou!Voce venceu!')
else:
    print('Nao foi dessa vez!!Tente novamente! Voce perdeu!')