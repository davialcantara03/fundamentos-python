s = 0
c = 0
num = int(input('Digite um número: '))
s += num
c += 1
while num != 999:
    num = int(input('Digite um número: '))
    if num != 999:
        s += num
        c += 1

print(f'O programa contou com {c} números e a soma total foi de {s}')