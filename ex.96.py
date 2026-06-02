def area(largura, comprimento):
    total_area = largura * comprimento
    print(f'A área de um terreno de {largura}x{comprimento} é de {total_area}m².')

# Programa Principal
print(' Controle de Terrenos ')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)