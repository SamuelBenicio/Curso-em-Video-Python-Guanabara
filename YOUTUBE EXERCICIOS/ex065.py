n1 = 0
media = 0
cont = 0
soma = 0
maior = 0
menor = 0
while(True):
    n1 = int(input('Digite um numero inteiro: '))
    soma += n1
    cont += 1
    media = soma/cont
    perg = input('Quer continuar?[S/N]: ').upper()
    if(cont==1):
        maior = menor = n1
    else:
        if(n1>maior):
            maior = n1
        if(n1<menor):
            menor = n1
    if(perg=='S'):
        continue
    elif(perg=='N'):
        break
print(f'Voce digitou {cont} numeros e a media entre eles foi {media:.2f} ')
print(f'O maior valor foi {maior} e o menor valor foi {menor} ')

