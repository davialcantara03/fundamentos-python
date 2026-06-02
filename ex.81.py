números = list()
while True:
    n = int(input('Digite um valor: '))
    números.append(n)
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'Você digitou {len(números)} elementos')
números.sort(reverse = True)
print(f'Os valores em ordem decrescente são {números}')
if 5 in números:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista.')
print('-=' * 30)
