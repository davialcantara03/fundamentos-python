times = ('Palmeiras', 'Flamengo', 'São Paulo', 'Fluminense', 'Bahia', 'Athletico-PR',
        'Coritiba', 'Atlético-MG', 'Bragantino', 'Vitória', 'Botafogo', 'Grêmio', 'Vasco',
        'Internacional', 'Santos', 'Cruzeiro', 'Corinthians', 'Remo', 'Chapecoense', 'Mirassol')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são: {times[:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'A ordem alfabética dos times é {sorted(times)}')
print('-=' * 15)
print(f'A Chapecoense está em {times.index("Chapecoense") + 1}º lugar')
print('-=' * 15)