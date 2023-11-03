from random import randint
pc = 0
soma = cont = n1 = jogadas = 0
while(True):
    while(n1!=1 and n1!=2):
        n1 = int(input('Voce quer ser par(1) ou impar(2): '))
        jogadas +=1
    if(jogadas>1):
        n1 = int(input('Voce quer ser par(1) ou impar(2): '))
    n2 = int(input('Digite o seu numero a ser jogado: '))
    pc = randint(1,100)
    soma = n2 + pc
    jogadas +=1
    if(n1==1):
        if(soma%2==0):
            print(f'Voce venceu.Jogue novamente, o numero jogado pelo computador foi {pc}')
            cont +=1
        elif(soma%2!=0):
            print(f'Voce perdeu o seu numero de vitorias consecutivas foi {cont}, o numero jogado pelo computador foi {pc}')
            break
    if(n1==2):
        if(soma%2!=0):
            print(f'Voce venceu.Jogue novamente, o numero jogado pelo computador foi {pc}')
            cont +=1
        elif(soma%2==0):
            print(f'Voce perdeu o seu numero de vitorias consecutivas foi {cont}, o numero jogado pelo computador foi {pc}')
            break