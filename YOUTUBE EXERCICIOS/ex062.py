p1 = int(input('Digite o primeiro termo dessa Progressao Aritmetica: '))
razao = int(input('Digite a razao dessa PA: '))
c = 10
cont = 0
while(c>0):
    print(f' {p1} ',end='')
    p1 +=razao
    c -=1
    cont +=1
    if(c==0):
        c = int(input('\nDigite mais quantos termos voce quer nessa PA: '))
print(f'Foram exibidos {cont} termos nessa PA')
        