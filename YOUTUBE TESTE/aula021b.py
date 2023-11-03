def funcao(n2):
    global n1 #Torna o n1 de dentro da funcao para funcionar globalmente
    n1 = 8 #Escopo local
    n2 += 4
    n3 = 2
    print(f'N1 dentro vale {n1}')
    print(f'N2 dentro vale {n2}')
    print(f'N3 dentro vale {n3}')

n1 = 5 #Escopo global
n1 +=1 #Somou +3 ao escopo global
#n1 local e n1 global sao duas variaveis diferentes,
#n1 local só pode ser usada dentro da funcao que foi definida,logo
#n1 global pode ser usada no programa todo

funcao(n1) 
print(f'N1 global vale {n1}')