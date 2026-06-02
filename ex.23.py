num = int(input('Informe um número: '))
Unidade = num // 1 % 10
Dezena = num // 10 % 10
Centena = num // 100 % 10
Milhar = num // 1000 % 10
print(f'Analisando o número...')
print(f'Unidade: {Unidade}')
print(f'Dezena: {Dezena}')
print(f'Centena: {Centena}')
print(f'Milhar: {Milhar}')
