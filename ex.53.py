frase = input('Digite a frase: ').strip().upper().replace(' ','')
inverso = ''
for letra in range(len(frase) - 1, -1, -1):
    inverso += frase[letra]

print(f'O inverso de {frase} é {inverso}')

if inverso == frase:
    print('TEMOS UM PALÍNDROMO!')

else:
    print('Não é palíndromo!')