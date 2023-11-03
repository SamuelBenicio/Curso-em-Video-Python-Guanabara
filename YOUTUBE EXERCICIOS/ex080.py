numeros = []

for c in range(5):
    n = int(input('Digite um valor: '))
    if(c==0 or n>numeros[-1]):
        numeros.append(n)
    else:
        pos = 0
        while(pos<len(numeros)):
            if(n<=numeros[pos]):
                numeros.insert(pos,n)
                break
            pos+=1
print(f'Os valores em ordem crescente foram {numeros}')


'''   valores = [] 
for c in range(5):
    valores.append(int(input('Digite um valor: ')))        #COM SORT
valores.sort()
print(f'Os valores em ordem crescente foram {valores}')  '''