def contador(i,f,p):
    #Inicio da doc string para ajudar o usuario a utilizar a função -> help(contador)
    """
    --> Faz uma contagem e mostra na tela.
    :param i: início da contagem 
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    #Fim da doc string -> help(funcao)
    c = i
    while(c<=f):
        print(f'{c}',end=' ')
        c +=p
    print('FIM!')
def somar(a=0,b=0,c=0):  #a,b e c sao parametros opcional, é possivel utilizar essa funcao com apenas dois parametros
    #Doc string
    """
    Funcao para realizar a soma 3 de variaveis no maximo,
    podendo realizar a soma de 2 ou 3
    recebe numeros inteiros ou até mesmo numeros float
    a,b e c sao parametros opcionais ,logo a funcao funciona sem nenhum parametro
    """
    s = a+b+c
    print(f'A soma vale {s}')
somar(8,4)
