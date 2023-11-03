casa = float(input('Qual o valor da casa: R$'))
salario = float(input('Qual o salario do comprador: R$'))
anos = int(input('Em quantos anos ele vai pagar a casa: '))
prestacao = casa / (anos*12)
minimo = salario*0.3
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos, a prestação será de R${prestacao:.2f}')
if(prestacao <= minimo):
    print('Emprestimo aprovado')
else:
    print('Emprestimo reprovado')