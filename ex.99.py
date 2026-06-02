from time import sleep
def maior(* num):
    print('-=' * 20)
    print('Analisando os valores passados...')
    for v in num:
        print(f'{v} ', end='', flush=True)
        sleep(0.5)
    tam = len(num)
    print(f'\nForam informados {tam} valores ao todo.')
    if tam > 0:
        maior_v = max(num)
    else:
        maior_v = 0
    print(f'O maior valor informado foi {maior_v}')

# Programa principal:
maior(2, 9, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()