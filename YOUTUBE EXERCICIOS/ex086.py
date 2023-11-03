from random import random
def mostrar(matriz):
    for linha in matriz:
        print(linha)
matriz = ([None]*3)
for c in range(len(matriz)):
    matriz[c] = [None]*3
    for j in range(len(matriz[c])):
        matriz[c][j] = int(input('Digite numero inteiro: '))
mostrar(matriz)

