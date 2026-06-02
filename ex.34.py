salario = float(input('Digite salario do funcionário: R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)

else:
    novo = salario + (salario * 15 / 100)
print(f'O salario recebido era: R${salario} e agora passa a receber: R${novo}')