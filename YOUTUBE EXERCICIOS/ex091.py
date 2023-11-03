from random import randint
bp =1
from time import sleep

jogadores = dict()
jogtot = list()
for c in range(4):
    jogadores['numero'] = randint(1,6)
    jogtot.append(jogadores.copy())
    if(c==0):
        print('Valores sorteados:')
    print(f'    O jogador{c+1} tirou {jogtot[c]["numero"]}')
    sleep(0.8)
    if(c==3):
        print('Ranking dos jogadores: ')
for item in sorted(jogadores, key = jogadores.get):
    print (jogadores[item])