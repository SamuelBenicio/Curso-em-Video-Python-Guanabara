city = input('Em qual cidade voce mora: ')
cityd = city.split()
res = 'Santo' in cityd[0]
print(f'O nome da cidade começa com santo? {res}')
