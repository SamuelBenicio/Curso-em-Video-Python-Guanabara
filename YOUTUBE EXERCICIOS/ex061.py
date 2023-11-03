n1 = int(input('Digite o primeiro termo de uma dessa Progressao Aritmetica: '))
n2= int(input('Digite a Razão dessa Progessao Aritmetica: '))
n3= 0
while(n3<10):
    pa = n1 + (11-1) * n2
    print(pa)
    n1 = n1+n2
    n3 +=1