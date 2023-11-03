from random import randint
numeros = list()
def sorteia():
    for c in range(5):
        numeros.append(randint(1,20))
    bp=1
    for num in numeros:
        print(num,end=' ')
    print('.Esses foram os numerados sorteados.')
def somaPar(list):
    somap = 0
    for num in numeros:
        if(num%2==0):
            somap+=num
    print(f'Somanda os valores pares de {numeros}, temos {somap}')



            
sorteia()
somaPar(sorteia)

