fatorial = 1
num = int(input('Digite o valor para calcular seu fatorial: '))
copia = num
while num > 1:
    fatorial *= num
    num = num -1
    print(f'{num}', end=' x ')

print(f'O fatorial de {copia} é {fatorial}')