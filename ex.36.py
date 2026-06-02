casa = float(input('Valor da casa: R$'))
salario = float(input('Seu salário: R$'))
ano = int(input('Anos de financiamento: '))
meses = 12 * ano
prestacao = casa / meses
minimo = salario * 0.30
print(f'Para pagar a casa de {casa} em {ano}, a prestação será de R${prestacao:.2f}')
if prestacao <= minimo:
    print(f'O empréstimo foi APROVADO!')
else:
    print(f'O empréstimo foi negado!')