dias = float(input('Informe a quantidade de dias que o carro foi alugado: '))
km = float(input('Informe a quantidade de km rodados pelo carro: '))
total = (60*dias)+(0.15*km)
print(f'O valor total a ser pago é R${total}')