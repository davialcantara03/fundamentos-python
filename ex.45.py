j1 = input(f'Digite sua escolha:')
j2 = input(f'Digite sua escolha:')
if j1 == j2:
    print(f'O resultado foi: EMPATE!')
elif (j1 == 'pedra' and j2 == 'tesoura') or (j1 == 'tesoura' and j2 == 'papel') or (j1 == 'papel' and j2 == 'pedra'):
    print('Jogador 1 venceu!')
else:
    print(f'Jogador 2 venceu!')