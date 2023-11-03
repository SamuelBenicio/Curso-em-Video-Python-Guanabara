valores = []
numeros = ['primeiro','segundo','terceiro','quarto','quinto']
for c in range(5):
    valores.append(int(input(f'Digite o {numeros[c]} valor para adicionar na lista: ')))
print(f'Voce digitou os valores {valores}')
print(f'O maior valor é {max(valores)} e a posicao {valores.index(max(valores))}')
print(f'O menor valor é {min(valores)} e a posicao {valores.index(min(valores))}')
