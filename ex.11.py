larg = float(input('Qual é a largura da parede?'))
alt = float(input('Qual é a altura da parede?'))
area = larg * alt
tinta = area / 2
print(f'Sua parede tem a dimensão de {larg}x{alt} e sua área é de {area:.2f}m². ')
print(f'Pra pintar essa parede será preciso {tinta:.2f}l de tinta')