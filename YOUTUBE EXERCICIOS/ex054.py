cont = 0
for c in range(1,8):
    n = int(input('Digite o ano de nascimento: '))
    if(n<=2002):
        cont += 1
print(f'Um total de {cont} pessoa(s) e {c-cont} pessoa(s) não atingiram a maioridade ainda.')