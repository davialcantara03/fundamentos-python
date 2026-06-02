from random import choice
j1 = input('Digite sua escolha: ').lower().strip()
computador = choice(['pedra', 'papel', 'tesoura'])
if j1 == computador:
    print(f'O resultado foi: EMPATE!')
elif (j1 == 'pedra' and computador == 'tesoura') or (j1 == 'tesoura' and computador == 'papel') or (j1 == 'papel' and computador == 'pedra'):
    print('Você me venceu. Parabéns!')
else:
    print(f'EU VENCI! Pensei em {computador} e isso vence {j1}')