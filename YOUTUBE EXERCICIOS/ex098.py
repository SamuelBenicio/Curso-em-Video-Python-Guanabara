from time import sleep
def linhagrande():
    print('-'*30)
def contador():
    linhagrande()
    print('Contagem de 1 até 10 de 1 em 1')
    for c in range(11):
        print(c , end=' ')
        c+=1
        if(c==11):
            print('FIM!')
        sleep(0.3)
    linhagrande()
    for p in range(6):
        if(p==0):
            print('Contagem de 10 até 0 de 2 em 2')
            a = 10
        print(a , end =' ')
        a -= 2
        if(p==5):
            print('FIM!')
            linhagrande()
        sleep(0.3)
    print('Agora é sua vez de personalizar a contagem!')
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    linhagrande()
    if(passo<0):
        print(f'Contagem de {inicio} até {fim} de {passo*-1} em {passo*-1}')
    elif(passo==0):
        print(f'Contagem de {inicio} até {fim} de {1} em {1}')
    else:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if(inicio<fim):
        if(passo==0):
            passo = 1
        for k in range(fim):
            if(k==0):
                print(inicio,end=' ')
                sleep(0.3)
            elif(k==1):
                k = passo + inicio 
                print(k, end=' ')
                sleep(0.3)
            else:
                k = inicio + (passo*k)
                print(k,end=' ')
                sleep(0.3)
                if(k+passo>fim):
                    print('FIM!')
                    break
    elif(fim<inicio):
        if(passo==0):
            passo= -1
        if(passo<0):
            passo = passo*-1
        for o in range(inicio):
            if(o==0):
                print(inicio,end=' ')
            elif(o==1):
                o = inicio - passo
                print(o,end=' ')
            else:
                o = inicio - (passo*o)
                print(o,end=' ')
                if(o-passo<fim):
                    print('FIM!')
                    break
contador()
bp = 1