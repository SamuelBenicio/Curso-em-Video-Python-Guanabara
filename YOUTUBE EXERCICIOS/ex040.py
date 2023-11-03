n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1+n2)/2
if(media<5):
    print(f'Infelizmente voce foi reprovado, a sua media foi {media:.2f}')
elif(5<=media<=6.9):
    print(f'Voce está na recuperaçao, sua media foi {media:.2f}')
else:
    print(f'Voce foi aprovado parabens, sua media foi {media:.2f}')
