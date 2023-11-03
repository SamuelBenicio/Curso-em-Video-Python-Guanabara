from random import randint
print(f'{"Pedra,Papel,Tesoura Jogo":=^40}')
print('[0] PEDRA')
print('[1] PAPEL')
print('[2] TESOURA')
n1 = input('Qual vai ser a sua jogada? ')
n2 = randint(0,2)
0 == 'PEDRA'
1 == 'PAPEL'
2 == 'TESOURA'
if(n1==n2):
    print('Empate')
elif(n1==0 and n2==1):
    print('Computador venceu.')
elif(n1==0 and n2==2):
    print('Voce venceu.')
elif(n1==1 and n2==0):
    print('Voce venceu.')
elif(n1==1 and n2==2):
    print('Computador venceu.')
elif(n1==2 and n2==0):
    print('Computador venceu.')
elif(n1==2 and n2==1):
    print('Voce venceu.')
print(f'{"":=^40}')
print(f'Voce jogou {n1}.')
print(f'O computador jogou {n2}.')
print(f'{"Fim de jogo.":=^60}')