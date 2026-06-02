preço = float(input('Qual é o preço desse produto?R$'))
novo = preço - (preço * 15 / 100)
print(f'O produto que custava {preço:.2f} agora custa {novo:.2f}.')
