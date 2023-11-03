salario = float(input('Qual o valor do salario que voce recebe? '))
if(salario<=0):
    print('Impossivel de calcular')
elif(salario>1250):
    print(f'O seu salario com o aumento de 10% ficou {salario*1.1:.2f}')
else:
    print(f'O seu salario com o aumento de 15% ficou {salario*1.15:.2f}')
