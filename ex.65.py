resposta = 's'
s = c = maior = menor = 0
while resposta == 's':
    num = int(input('Digite um número: '))
    c += 1
    s += num
    if c == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resposta = input('Deseja continuar? [S/N] ').strip().lower()

media = s / c
print(f'A soma mostrou {c} números e a média total é {media:.2f}')
print(f'O número maior é {maior} e o número menor é {menor}')