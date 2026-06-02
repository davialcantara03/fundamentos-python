import random
from time import sleep
computador = random.randint(0, 5)
jogador = int(input('Em que número eu pensei? '))
if jogador == computador:
    print(f'Parabéns, você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {jogador}')
