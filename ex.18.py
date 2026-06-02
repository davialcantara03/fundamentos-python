import math
angulo = float(input('Digite o valor do angulo: '))
radiano = math.radians(angulo)
seno = math.sin(radiano)
coseno = math.cos(radiano)
tangente = math.tan(radiano)
print(f'O valor de seno é igual a {seno:.2f}')
print(f'O valor de coseno é igual a {coseno:.2f}')
print(f'O valor da tangente é igual a {tangente:.2f}')