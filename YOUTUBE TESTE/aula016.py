'TUPLAS'
from random import randint
lanche = ('Hambuguer','Suco','Pizza','Pudim')
print(lanche) #Printa todos os elementos da tupla
print(lanche[0]) #A tupla começa no 0
print(lanche[1])
print(lanche[2])
print(lanche[3])
print(lanche[1:3]) #Vai printar o elemento 1 e 2, pois o python exclui o ultimo.
print(len(lanche)) #Quantos elementos tem na tupla
for c in lanche:
    print(c) #Ira printar todos os elementos da tupla um de cada vez
for cont in range(0, len(lanche)): #Contador dos elementos do lanche
    #print(cont)
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print(sorted(lanche)) #Coloca os elementos em ordem

a = (2,5,4)
b = (5,8,1,2)
c = a + b #Junta os elementos da tupla
print(len(c)) #Quantidade de elementos na tupla C
print(c.count(5))  #Conta os numeros 5 na tupla C
print(c)
print(c.index(4)) #Mostra a posicao do elemento, se tiver mais de um elemento igual irá aparecer o primeiro
print(f'O maior valor da tupla c é {max(c)}') #Printa o maior valor da tupla selecionada
print(f'O menor valor da tupla c é {min(c)}') #Printa o menor valor da tupla selecionada

pessoa = ('Samuel',18,'M',67.4)
print(pessoa)
del(pessoa) #Apaga a tupla
pessoa = ('Ian',18,'M',80)
print(pessoa)

n = (randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100)) #Cria uma tupla com valores aleatorios
print(n)