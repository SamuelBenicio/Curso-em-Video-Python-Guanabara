s = 0
cont = 0
for c in range(1,7):
    n = int(input(f'Digite o {c} numero: '))
    if(n%2==0):
        s += n
        cont += 1
    else:
        print('O progama faz a soma somente dos numero pares.')
print(f'A soma dos numeros pares({cont}) é {s}')