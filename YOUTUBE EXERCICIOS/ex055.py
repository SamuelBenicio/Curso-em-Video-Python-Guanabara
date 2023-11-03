maior = 0
menor = 0
for c in range (1,6):
    peso = float(input('Digite o peso da pessoa: '))
    if(c==1):
        maior = c
        menor = c
    else:
        if(peso>maior):
            peso = maior
        if(peso<menor):
            peso = menor
        