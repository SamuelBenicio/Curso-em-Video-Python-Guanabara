from random import randint
n = (randint(1,100) , randint(1,100) , randint(1,100) , randint(1,100) , randint(1,100))
print(f'Os valores sorteados foram: ',end='')
for p in n:
    print(f' {p} ',end='')
print(f'\nO maior valor sorteado é {max(n)}')
print(f'O menor valor sorteado é {min(n)}')
