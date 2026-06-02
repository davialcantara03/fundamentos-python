segmento_1 = int(input('Primeiro segmento: '))
segmento_2 = int(input('Segundo segmento: '))
segmento_3 = int(input('Terceiro segmento: '))
if segmento_1 < segmento_2 + segmento_3 and segmento_3 < segmento_1 + segmento_2 and segmento_2 < segmento_1 + segmento_3:
    if segmento_1 == segmento_2 == segmento_3:
        print('EQUILÁTERO')
    elif segmento_1 == segmento_2 or segmento_1 == segmento_3 or segmento_2 == segmento_3:
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('Esses lados não formam um triângulo!')