expressao = input('Digite a expressao: ')
if(expressao.count('(') == expressao.count(')')):
    print(f'A expressao está valida.')
else:
    print(f'A expressao esta invalida.')