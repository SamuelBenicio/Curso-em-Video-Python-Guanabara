dados = dict()
dadostot = list()
cont = media =0
while(True):
    dados['nome'] = input('Nome: ')
    dados['sexo'] = input('Sexo: [M/F] ')
    dados['idade'] = int(input('Idade: '))
    contin = input('Quer continuar? [S/N] ')
    dadostot.append(dados.copy())
    while(contin not in 'SsNn'):
        contin = input('Quer continuar? [S/N] ')
    if(contin in 'Nn'):
        break
print('------------------------------------------------------------------------------')
print(f'- O grupo tem {len(dadostot)} pessoas')
for c in  range(len(dadostot)):
    media += dadostot[c]['idade']
media = media/len(dadostot)
print(f'- A média de idade é de {media:.2f} anos')
for k in range(len(dadostot)):
    if(dadostot[k]['sexo'] in 'Ff'):
        print(f'- As mulheres cadastradas foram:',end=' ')
        print(f'{dadostot[k]["nome"]}')
for p in range(len(dadostot)):
    if(dadostot[p]['idade']) > media:
        print('- Lista das pessoas que estão acima da média de idade:')
        print()
        print(f'{dadostot[p]}')
print('---------ENCERRADO------')
