c = 0
total = 0
mais_barato = ' '
menor_preço = None
while True:
    produto = input('Digite o nome do produto: ')
    preço = float(input('Digite o preço do produto: R$ '))
    escolha = input('Quer continuar? [S/N]').upper()
    total += preço
    if preço > 1000.00:
        c += 1
    if menor_preço is None or preço < menor_preço:
        menor_preço = preço
        mais_barato = produto
    if escolha == 'N':
        break

print(f'O total da compra foi de R${total}')
print(f'Temos {c} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {mais_barato} e custa R${menor_preço}')