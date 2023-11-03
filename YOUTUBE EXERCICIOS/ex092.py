from datetime import datetime
dados = dict()
dados['nome'] = input('Nome: ')
dados['anoNascimento'] = int(input('Digite o ano de nascimento: '))
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if(dados['ctps']) == 0:
    pass
else:
    dados['anoContrato'] = int(input(f'Digite o ano que {dados["nome"]} foi contratado: '))
    dados['salario'] = float(input(f'Digite o salario que {dados["nome"]} recebe: R$ '))
dados['idade'] = datetime.now().year - dados['anoNascimento']
dados['aposentadoria'] = dados['anoContrato'] + 35
del(dados['anoNascimento'])
print('------------------------------------------------------------------------------------')
print(dados.items())
for k,v in dados.items():
    print(f'{k} tem o valor {v}')