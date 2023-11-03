av3 = 0
nome = input('Digite o nome completo do aluno:')
av1 = float(input('Digite a nota que o aluno {} tirou na av1:'.format(nome)))
av2 = float(input('Digite a nota que o aluno {} tirou na av2:'.format(nome)))
s = float((av1+av2)/2)
if(s<4):
    print('Infelizmente voce foi reprovado nessa cadeira {} ,sua média foi: {} '.format(nome , s ))
    
if (s>=4) :
    av3 = float(input('Digite a nota que o aluno {} tirou na av3:'.format(nome)))
    avf = float(((s)+(av3))/2)
    if(avf<=5):
        print('Infelizmente voce foi reprovado nessa cadeira {} ,sua média foi: {}'.format(nome , s ))
    else :
        print('Parabens!!Voce foi aprovado nessa cadeira {} , sua média foi {} , boa sorte no proximo semestre!'.format(nome , s ))
    
else :
    (av3<5),print('Reprovado')





