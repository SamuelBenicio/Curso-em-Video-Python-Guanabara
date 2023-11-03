#----------------------------LISTAS COMPOSTAS---------------------------------------------

teste = []
teste.append('Samuel')
teste.append(18)
galera = [] # ou galera = list()
galera.append(teste[:]) #Copia a lista teste uma lista dentro a outra
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
print(galera[0][1]) #Printa a primeira lista dentro da lista galera na posição 1
print(galera[1]) #Printa toda a lista indicada
print('-----------------------------------------------------------------')
pessoas = [['Joao',28],['Gustavo',40],['Paulo',21],['Lucas',68]]
print(pessoas)
print(pessoas[3][1])
print(pessoas[0][1]+pessoas[2][1]) #Faz a soma das idades(Lista 0 na posicao 1 e Lista 1 na posicao 1)
print('--------------------------------------------------------------')
for p in pessoas: #Printa cada elemento dentro de pessoas ou seja cada lista dentro de pessoas
    print(p)
print('--------------------------------------------------------------')
for c in pessoas: #Printa cada elemento dentro de pessoas ou seja cada lista dentro de pessoas
    print(c[0]) #Printa somente os nomes 
print('--------------------------------------------------------------')
for i in pessoas:
    print(i[1]) #Printa somente as idades
print('--------------------------------------------------------------')
for h in pessoas:
    print(f'{h[0]} tem {h[1]} anos de idade')
