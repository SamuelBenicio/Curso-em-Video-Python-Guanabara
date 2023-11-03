import math
n = float(input('Digite um angulo: '))
rad = (n*3.14)/180
sen = math.sin(rad)
cos = math.cos(rad)
tg = math.tan(rad)
print(f'O valor do angulo {n}, o seno dese angulo é {sen:.2f}, o cosseno é {cos:.2f} e a tangente é {tg:.2f}')
