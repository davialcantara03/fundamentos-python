from random import randint
c = 0
while True:
    jogador = int(input('Digite um valor: '))
    escolha = input('Par ou ímpar?').lower()
    computador = randint(0, 10)
    total = jogador + computador
    print(f'Você jogou {jogador} e o computador {computador}')
    if total % 2 == 0:
        resultado = 'par' 
    elif total % 2 != 0:
        resultado = 'impar'
    if resultado == escolha:
        print(f'Você ganhou! Eu pensei em {computador} e você em {jogador}. Total deu {total} e é {resultado}')
        c += 1
    else:
        print(f'Eu venci! Pensei em {computador} e você em {jogador}. Total deu {total} e é {resultado}')
        break
print(f'GAME OVER. Você venceu {c} vezes')
