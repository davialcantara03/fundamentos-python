n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
print('[1] somar')
print('[2] multiplicar')
print('[3] maior')
print('[4] novos números')
print('[5] sair do programa')
escolha = int(input('Qual é a sua escolha? '))
while escolha != 5:
    if escolha == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}')
    elif escolha == 2:
        print(f'A multiplicação entre {n1} e {n2} é {n1 * n2}')
    elif escolha == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2} o maior número é {n1}')
        elif n1 < n2:
            print(f'Entre {n1} e {n2} o maior número é {n2}')
    elif escolha == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair do programa')
    escolha = int(input('Qual é a sua escolha?'))
print('Programa finalizado')