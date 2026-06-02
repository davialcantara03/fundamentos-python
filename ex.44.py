preço = float(input('Digite o preço do produto: R$ '))
print('1 - À vista dinheiro')
print('2 - Em até 2x no cartão')
print('3 - Cartão parcelado 3x ou mais')
print('4 - Á vista cartão')
condicao = input('Qual a forma de pagamento que você vai utilizar?')
if condicao == '1':
    desconto = preço * 0.10
    valor_total = preço - desconto
    print(f'O valor do produto com desconto é R$ {valor_total:.2f}')
elif condicao == '4':
    valor_total = preço - (preço * 0.05)
    print(f'À vista no cartão: R$ {valor_total:.2f}')
elif condicao == '2':
    valor_total = preço
    parcela = valor_total / 2
    print(f'Em 2x de R$ {parcela:.2f} sem juros. Total: R$ {valor_total:.2f}')
elif condicao == '3':
    valor_total = preço + (preço * 0.20)
    totparc = int(input('Quantas parcelas? '))
    parcela = valor_total / totparc
    print(f'Em {totparc}x de R$ {parcela:.2f} com juros. Total: R$ {valor_total:.2f}')