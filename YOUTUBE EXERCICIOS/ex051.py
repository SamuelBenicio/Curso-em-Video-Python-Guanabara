print(f'{"Progressao Aritmetica":=^40}')
n1 = int(input('Digite o primeiro termo dessa Progessao Aritmetica: '))
n2 = int(input('Digite a razao da Progessao Aritmetica: '))
decimo =  n1 + (11-1) * n2
for c in range(n1,decimo,n2):
    print(c)
    