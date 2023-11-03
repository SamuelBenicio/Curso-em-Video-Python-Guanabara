n1 = int(input('Digite o seu ano de nascimento: '))
if(n1>2005):
    print(f'Voce ainda tem que se alistar no futuro,voce é muito novo, daqui há {n1-2005} anos voce podera se alistar')
elif(n1==2005):
    print(f'Voce tem que se alistar esse ano.')
else:
    print(f'Voce ja passou do alistamento, voce esta atrasado {(2005-n1)} ano(s) do alistamento militar obrigatorio para maiores de 18 anos')