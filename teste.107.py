import moeda
num = float(input('Digite o preço: R$ '))
print(f'A metade de {num} é {moeda.metade(num)}')
print(f'O dobro de {num} é {moeda.dobro(num)}')
print(f'Aumentando 10%, temos R$ {moeda.aumentar(num, 10):.2f}')
print(f'Diminuindo 10%, temos R$ {moeda.diminuir(num, 10):.2f}')