#Passo 1: Entrada de dados
galera= list()
dado = list()
mai = men = 0
while(True):
    dado.append(input('Nome: '))
    dado.append(float(input('Peso: ')))
    if(len(galera)==0):
        mai = dado[1]
        men = dado[1]
    else:
        if(dado[1]>mai):
            mai = dado[1]
        if(dado[1]<men):
            men = dado[1]
    galera.append(dado[:])
    dado.clear()
    resposta = input('Quer continuar? [S/N] ')
    while(resposta not in 'SsNn'):
        resposta = input('Quer continuar? [S/N] ')
    if(resposta in 'Nn' ):
        break


print('--------------------------------------------------')
#Passo 2:Quantas pessoas foram cadastradas
print(f'Ao todo foram cadastradas {len(galera)} pessoas.')
#Passo 3:Pessoas mais pesadas e mais leves
print(f'O maior peso foi de {mai:.2f}Kg. Peso de ',end='')
for p in galera:
    if(p[1]==mai):
        print(f'[{p[0]}] ',end='')
print()
print(f'O menor peso foi de {men:.2f}Kg. Peso de ',end='')
for c in galera:
    if(c[1]==men):
        print(f'[{c[0]}]',end='')
print()
