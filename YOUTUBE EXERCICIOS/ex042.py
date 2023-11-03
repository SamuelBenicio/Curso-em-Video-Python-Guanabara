A = float(input('Digite o primeiro segmento: '))
B = float(input('Digite o segundo segmento: '))
C = float(input('Digite o terceiro segmento: '))
if(A+B>C and A+C>B and B+C>A):
    print('Triangulo pode ser formado')
    if(A==B==C):
        print('O triangulo é equilatero (todos os lados iguais)')
    elif(A==B or A==C or B==A or B==C):
        print('O triangulo é isosceles (dois lados iguais)')
    elif(A!=B!=C):
        print('O triangulo é escaleno (todos os lados diferentes)')
else:
    print('Triangulo nao pode ser formado')
