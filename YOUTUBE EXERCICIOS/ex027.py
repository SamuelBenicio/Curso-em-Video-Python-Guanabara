nome = input('Digite o seu nome completo: ')
nomed = nome.split()
print(f'O primeiro nome da pessoa é: {nomed[0]}')
print(f'O ultimo nome da pessoa é: {nomed[len(nomed)-1]}')