n2 = int(input('Digite o ano de nascimento do atleta: '))
n1 = 2023-n2
if(1<=n1<=9):
    print('A categoria do atleta é a Mirim')
elif(10<=n1<=14):
    print('A categoria do atleta é a Infantil')
elif(15<=n1<=19):
    print('A categoria do atleta é a Junior')
elif(n1==20):
    print('A categoria do atleta é a Senior')
elif(n1>20):
    print('A categoria do atleta é a Master')