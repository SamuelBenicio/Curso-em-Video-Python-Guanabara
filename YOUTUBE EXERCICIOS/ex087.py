soma3 = par = maior2 = 0
def mostrar(matriz):
    for linha in matriz:
        print(linha)
matriz = ([None]*3)
for c in range(len(matriz)):
    matriz[c] = [None]*3
    for j in range(len(matriz[c])):
        matriz[c][j] = int(input('Digite numero inteiro: '))
        if(matriz[c][j]%2==0):
            par +=matriz[c][j]

for k in range(3):
    soma3 += matriz[k][2]
for o in range(3):
    maior2 = matriz[2][0]
    if(matriz[2][o]>maior2):
        maior2 = matriz[2][o]
print('----------------------------------------------------------------')
mostrar(matriz)
print(f'A soma de todos os valores pares digitados é: {par}')
print(f'A soma de todos os valores da terceira coluna é: {soma3}')
print(f'O maior valor da segunda linha é: {maior2}')

