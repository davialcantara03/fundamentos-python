valores = []
lista_par = []
lista_impar = []
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'A lista completa é {valores}')
for n in valores:
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)

print(f'Você digitou {len(lista_par)} números pares: {lista_par}')
print(f'Você digitou {len(lista_impar)} números ímpares: {lista_impar}')