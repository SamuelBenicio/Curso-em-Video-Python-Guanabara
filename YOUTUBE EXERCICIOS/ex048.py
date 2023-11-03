s = 0
cont = 0
for c in range(1,500,2):
    if(c%3==0):
        s += c
        cont += 1
print(f'A soma de todos os numeros impares({cont}) entre 0 e 500 é {s}')