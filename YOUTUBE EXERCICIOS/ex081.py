valores = []
cont = 0
while(True):
    valores.append(int(input('Digite um valor inteiro: ')))
    cont +=1
    r = input('Quer continuar? [S/N] ')
    while(r not in 'SsNn'):
        r = input('Quer continuar? [S/N] ')
    if(r in 'Nn'):
        break
print(f'{cont} numeros foram digitados')
print(f'A lista na ordem digitada: {valores}')
valores.sort(reverse=True)
print(f'A lista em ordem decrescente fica: {valores}')
if(valores.count(5)):
    print(f'O valor 5 está na lista e posicao dele é {valores.index(5)}')
else:
    print(f'O valor 5 nao esta na lista')