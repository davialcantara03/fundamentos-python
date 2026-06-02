num = (int(input('Digite um número: ')), 
       int(input('Digite outro: ')), 
       int(input('Digite mais um: ')), 
       int(input('Digite o último: ')))
cont_pares = 0
print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}° posição')
else:
    print('O valor 3 não foi digitado')

print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        cont_pares += 1
        print(f'{n} ', end='')
