nome = input('Digite seu nome completo: ')
print(f'O nome com todas as letras maisculas fica: {nome.upper()}')
print(f'O nome com todas as letras minusculas fica: {nome.lower()}')
espaço0 = nome.replace(' ', '')
print(f'A quantidade de letras que tem no nome é: {len(espaço0)}')
nomed = nome.split()
print(f'A quantidade de letras que tem no primeiro nome é: {len(nomed[0])}')

