dias = int(input('Quantos dias ficaram?'))
km = float(input('Quantos km foram rodados?'))
total = (dias * 60) + (km * 0.15)
print(f'O total de dinheiro gasto foi R${total:.2f}')