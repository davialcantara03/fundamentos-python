time = list()
jogador = {}
lista_de_gols = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    
    lista_de_gols.clear()
    for c in range(0, tot):
        lista_de_gols.append(int(input(f'   Quantos gols na partida {c + 1}? ')))
    
    jogador['gols'] = lista_de_gols[:]
    jogador['total'] = sum(lista_de_gols)
    time.append(jogador.copy())
    
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)

for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogador com código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca] ["nome"]}: ')
        for i, g in enumerate(time[busca] ['gols']):
            print(f'    No jogo {i+1} fez {g} gols')
    print('-=' * 30)
print('<<< VOLTE SEMPRE! >>>')