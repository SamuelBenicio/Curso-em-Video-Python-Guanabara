aluno = dict()
for c in range(1):
    aluno['Nome'] = input('Nome: ')
    aluno['Media'] = float(input(f'Média de {aluno["Nome"]}: '))
    if(aluno['Media']>=7.0):
        aluno['Situacao'] = 'Aprovado'
    else:
        aluno['Situacao'] = 'Reprovado'
for k,v in aluno.items():
    print(f'{k} é igual a {v}')