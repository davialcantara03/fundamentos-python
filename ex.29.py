velocidade = int(input('Qual a velocidade do carro? '))
if velocidade > 80:
    print(f'MULTADO! Você excedeu o limite de 80km/h')
    multa = (velocidade - 80) * 7
    print(f'O valor da multa foi R${multa:.2f}')
else:
    print(f'Tenha um bom dia e dirija com cuidado!')
