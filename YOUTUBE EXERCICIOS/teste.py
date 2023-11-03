galera = list()
dado = list()
for c in range(0,3):  #Entrada de dados
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:   #Leitura dos dados
    if(p[1]>=21):
        print(f'{p[0]} é maior de idade.')
    else:
        print(f'{p[0]} é menor de idade.')
print(f'Ao todo foram cadastradas {len(galera)} pessoas')  #Fim do cadastro com total de pessoas cadastradas