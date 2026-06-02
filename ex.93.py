jogador = {}
jogador['nome'] = str(input('Nome: '))
jogador['partidas'] = int(input('Número de partidas: '))
lista_de_gols = list()
for c in range(0, jogador['partidas']):
    gols = int(input(f'Quantos gols na partida {c}? '))
    lista_de_gols.append(gols)
jogador['gols'] = lista_de_gols[:]
jogador['total'] = sum(lista_de_gols)
print(jogador)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

for i, g in enumerate(jogador['gols']):
    print(f'Na partida {i}, fez {g} gols')

print(f'Foi um total de {jogador['total']} gols')