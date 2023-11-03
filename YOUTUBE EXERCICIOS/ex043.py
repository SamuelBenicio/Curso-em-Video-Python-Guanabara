p1 = float(input('Digite o peso da pessoa: '))
h1 = float(input('Digite a altura da pessoa: '))
imc = p1/(h1**2)
if(imc<18.5):
    print(f'A pessoa esta abaixo de peso, seu IMC é {imc:.1f}')
elif(18.5<=imc<=25):
    print(f'A pessoa esta no peso ideal, seu IMC é {imc:.1f}')
elif(25<=imc<=30):
    print(f'A pessoa esta com sobrepeso, seu IMC é {imc:.1f}')
elif(30<=imc<=40):
    print(f'A pessoa esta com obesidade, seu IMC é {imc:.1f}')
elif(imc>40):
    print(f'A pessoa esta com obesidade morbidade, seu IMC é {imc:.1f}')