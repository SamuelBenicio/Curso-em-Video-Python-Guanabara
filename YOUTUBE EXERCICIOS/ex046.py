import time
#ADICIONAL
x = time.localtime()
print(f'Hoje é dia {x[2]}, do mes {x[1]} e sao exatamente {x[3]} horas e {x[4]} minutos')
#FIM ADICIONAL

for c in range(1,11):
    print(c)
    time.sleep(1)
print('Os fogos foram lançados!')