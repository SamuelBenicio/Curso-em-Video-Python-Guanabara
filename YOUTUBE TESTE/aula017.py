'LISTAS' #Listas sao mutaveis
lanche = ['hambuguer','pudim']
print(lanche[1])
                              #ADICIONANDO ELEMENTOS NA TUPLA
lanche[1] = 'sushi' #Mutei a lista, nao da para adicionar elementos dessa forma
print(lanche[1])
lanche.append('cookie') #Adiciona um elemento na lista,apenas um de cada vez
print(lanche)
lanche.insert(0,'cachorro quente') #Adiciona um elemento na lista na posição que for indicada lanche.inset(#posição,#elemento a ser inserido)
print(lanche)

                                    #APAGANDO ELEMENTOS NA TUPLA
del lanche[3] #Apaga o elemento indicado da lista - del lanche[#Posição do elemento a ser apagado]
print(lanche)
lanche.pop(1) #Apaga o elemento indicado da lista - lanche.pop(#Posição do elemento a ser apagado) ou lanche.pop()#Apaga sempre o ultimo elemento da lista
print(lanche)
lanche.remove('sushi') #Apaga o nome do elemento indicado da lista - lanche.remove('#Nome do elemento')
print(lanche)
if('hamburguer' in lanche): #Se hamburguer estiver em lanche, remover hamburguer 
    lanche.remove('hamburguer')


'''n1,n2 = map(int,input().split(' '))
valores = list(range(n1,n2+1,2)) #Cria uma lista valores com os numeros de n1 até n2+1 ordenada de forma crescente,pulando de 2 em 2
print(valores)'''
numeros = list(range(4,11)) #Cria uma lista com numeros de 4 até 10
                        #ORGANIZANDO A LISTA EM ORDENS
nums = [8,2,5,4,15,100,22,2]
nums.sort() #Os numeros da lista organizados em ordem crescente
print(nums) 
nums.sort(reverse=True) #Os numeros da lista em ordem decrescente
print(nums)
print(len(nums)) #Indica a quantidade de elementos que tem na lista

