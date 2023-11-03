galera = list()
dado = list()
totmai = totmen = 0
for c in range(0,3):
    dado.append(input('Digite o nome: '))
    dado.append(int(input(f'Digite a idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in range(len(galera)):
    if(galera[p][1]>21):
        print(f'{galera[p][0]} tem mais de 21 anos, sua idade é {galera[p][1]}')
        totmai +=1
    else:
        print(f'{galera[p][0]} tem menos de 21 anos')
        totmen +=1
print(f'{totmai} pessoas sao maiores de 21 anos')
print(f'{totmen} pessoas sao menores de 21 anos')

pessoas = [[],[]]
