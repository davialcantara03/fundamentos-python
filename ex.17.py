import math
cateto_oposto = float(input('Digite um cateto oposto: '))
cateto_adjacente = float(input('Digite um cateto adjacente: '))
hi = math.hypot(cateto_oposto, cateto_adjacente)
print(f'A hipotenusa é igual a {hi:.2f}')
