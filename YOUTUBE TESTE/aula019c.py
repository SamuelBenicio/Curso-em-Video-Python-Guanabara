estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy())
#print(brasil)
'''for c in range(3):
    print(brasil[c]['uf']) #printa somente as unidades federativas'''
for estado in brasil:
    for k,v in estado.items():
        print(f'O campo {k} tem valor {v}')