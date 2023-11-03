A = float(input('Digite o primeiro segmento: '))
B = float(input('Digite o segundo segmento: '))
C = float(input('Digite o terceiro segmento: '))
if(A+B>C and A+C>B and B+C>A):
    print('Triangulo pode ser formado')
else:
    print('Triangulo nao pode ser formado')
