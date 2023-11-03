while(True):
    n1 = int(input('Digite um numero positivo para fazer a tabuada: '))
    if(n1<0):
        break
    for c in range(1,11):
        print(f'{n1} x {c} = {n1*c}')
