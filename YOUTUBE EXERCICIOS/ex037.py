n1 = int(input('Digite um numero inteiro: '))
pergunta = int(input(f'O numero digitado foi {n1}, agora escolha para qual base esse numero vai ser convertido 1-base binaria, 2-base octal e 3-base hexadecimal: '))
if(pergunta==1):
    print(f'O numero na bae binaria fica: {bin(n1)}')
elif(pergunta==2):
    print(f'O numero na base octal fica: {oct(n1)}')
else:
    print(f'O numero na base hexadecimal fica: {hex(n1)}')