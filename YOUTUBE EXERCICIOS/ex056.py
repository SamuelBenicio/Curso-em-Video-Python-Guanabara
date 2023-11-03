mi = 0
somaidade = 0
maior = 0
cont = 0
for c in range(1,5):
    print(f'-----{c} pessoa -----')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')
    somaidade += idade
    if(c==1 and sexo in 'Mm'):
        maior = idade
        nomem = nome
    else:
        if(idade>maior):
            idade = maior
            nomem = nome
    if(sexo in 'Ff'):
        if(idade<20):
            cont += 1
mi = somaidade/4
print(f'A media de idade do grupo é: {mi:.2f}')
print(f'O nome do homem mais velho do grupo é: {nomem}')
print(f'Ao todo são {cont} mulheres com menos de 20 anos no grupo')