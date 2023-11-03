dados = dict() # ou dados={}
dados = {'nome':'Samuel','idade':18}
print(dados['nome'])
print(dados['idade'])
dados['sexo']='M' #Adiciona a chave sexo ao dicionarios
print(dados['sexo']) 
print(dados)
print('-------------------------------Deletei o elemento idade-----------------------------------------------------------------------------')
del dados['idade'] #Exclui a chave idade do dicionario
print(dados)
print('---------------------------------------------------------------------------')
filme={'título':'Oppenheimer',
'nota':8.5,
'critíca':'Bom filme mas longo',
'diretor':'Cristopher Nolan,',
'ano':'2023'
}
print(filme.values()) #Printa somente os elementos por exemplo oppenheimer
print(filme.keys()) #Printa somente as chaves por exemplo titulo
print(filme.items()) #Printa tudo que esta dentro do dicionario

for k,v in filme.items():
    print(f'O {k} é {v}')