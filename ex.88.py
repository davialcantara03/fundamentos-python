from random import randint
from time import sleep
lista = list()
jogos_completos = list()
quant = int(input('Quantos jogos você quer que eu sorteie? '))
total = 1
while total <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos_completos.append(lista[:])
    lista.clear()
    total += 1

print(f'-=' * 3, f' SORTEANDO {quant} jogos ', '-=' * 3)
for i, l in enumerate(jogos_completos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)