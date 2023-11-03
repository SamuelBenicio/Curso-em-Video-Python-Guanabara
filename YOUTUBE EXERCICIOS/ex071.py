print('=' * 30)
n1 = int(input('Informe o valor a ser sacado: '))
total = n1
totced = 0
ced = 50
while(True):
    if(total>=ced):
        total -= ced
        totced +=1
    else:
        if(totced>0):
            print(f'Total de {totced} cédulas de {ced}')
        if(ced==50):
            ced = 20
        elif(ced==20):
            ced = 10
        elif(ced==10):
            ced = 1
        totced = 0
        if(total==0):
            break
        
