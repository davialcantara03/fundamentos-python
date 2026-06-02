num = int(input('Quer ver a tabuada de qual valor? '))
while True:
    if num < 0:
        break
    for c in range(1, 11):
        resultado = num * c
        print(f'{num} x {c} = {resultado}')
    num = int(input('Quer ver a tabuada de qual valor? '))

print('Prgrama TABUADA encerrado!')
