dados = dict()

dados['nome'] = input('Digite o nome do jogador: ')
dados['partidas'] = int(input(f'Digite o numero de partidas que {dados["nome"]} jogou: '))
for c in range(dados['partidas']):
    dados['gols'] = int(input(f'Digite quantos gols {dados["nome"]} fez na partida {c+1}: '))
    
print('----------------------------------------------------------------------------------------')
print(dados.items())