ano = int(input('Digite um ano: '))
resto = ano%4==0
if((ano%4==0 and ano%100!= 0) or ano%400==0):
    print('Bissexto')
else:
    print('Nao bissexto')

bp=1