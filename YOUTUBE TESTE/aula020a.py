def mensagem(msg): #Funcao para mostrar uma mensagem organizada
    print('-'* 30)
    print(msg)
    print('-'* 30)
def soma(a,b): #Funcao para somar
    print(a+b)
def contador(* num): #Funcao para mostrar a quantidade de numero que foram inseridos
    tam = len(num)
    print(f'Recebi os valores {num} e sao ao todos {tam} numeros')
def dobra(lista): #Dobra os valores de uma lista
    pos = 0
    while pos<len(lista):
        lista[pos] *= 2
        pos+=1
bp=1
def somatudo(*valores): #Soma todos os valores digitados
    s = 0
    for num in valores:
        s +=num
    print(f'Somando os valores {valores} temos o resultado {s}')


mensagem('Supermercado Guanabara')
soma (4,8)
contador(5,10,20,25)
valores = [6,5,10,15,20]
dobra(valores)
print(valores)
somatudo(8,10,40)
somatudo(5,2)