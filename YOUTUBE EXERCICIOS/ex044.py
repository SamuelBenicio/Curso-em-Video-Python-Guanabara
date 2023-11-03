print(f'{"Lojas Benicio":=^40}')
n1 = float(input('Preço das compras: R$'))
print('[1] á vista dinheiro/cheque')
print('[2] á vista no cartão')
print('[3] parcelado 2 vezes no cartao')
print('[4] parcelado 3 vezes ou mais no cartao')
n2 = int(input('Digite o numero da forma de pagamento: '))
while(n2>=5):
    print('[1] á vista dinheiro/cheque')
    print('[2] á vista no cartão')
    print('[3] parcelado 2 vezes no cartao')
    print('[4] parcelado 3 vezes ou mais no cartao')
    n2 = int(input('Digite o numero da forma de pagamento: '))
    if(n2==1 or n2==2 or n2==3 or n2==4):
        break
if(n2==1):
    print(f'O valor da compra a vista no dinheiro/cheque fica: R${n1*0.9:.2f}')
elif(n2==2):
    print(f'O valor da compra a vista no cartao fica: R${n1*0.95:.2f}')
elif(n2==3):
    print(f'O valor da compra parcelada 2 vezes no cartao fica: R${n1:.2f}')
elif(n2==4):
    print(f'O valor da compra parcelada 3 vezes ou mais no cartao fica: R${n1*1.2:.2f}')

