maiores = 0
menores = 0
for c in range(1, 8):
    ano_nascimento = int(input('Digite o ano de nascimento: '))
    idade = 2026 - ano_nascimento
    if idade >= 21:
        maiores += 1
    else:
        menores += 1

print(f'Foram {maiores} maiores')
print(f'Foram {menores} menores')