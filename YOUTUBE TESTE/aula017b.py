nums = [2,2,20,8,10,3]
nums.remove(2) #Remove o primeiro elemento,caso tenha mais de um na lista
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)
for v in valores: #Mostra todos os elementos da lista um de cada vez
    print(f'{v}...')
numeros = []
for cont in range(0,5): #Adiciona 5 valores na lista, um de cada vez
    numeros.append(int(input('Digite um valor: '))) #Adiciona 5 valores na lista, um de cada vez
for i,n in enumerate(numeros): #Mostra a posicao do elemento na lista e o propio elemento
    print(f'Na posicao {i} encontrei o valor {n}!')

a = [2,3,4,7]
b = a[:] #Copia a lista 'a' e posso muta ela depois
print(f'Lista A: {a}')
print(f'Lista B: {b}')
b[2] = 8 #Modifica um elemento da lista que eu clonei anteriormente
print(f'Lista A: {a}')
print(f'Lista B: {b}')