peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
print(f'O imc dessa pessoa é de {imc:.2f}')
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc <= 25:
    print('Peso ideal')
elif 26 <= imc <= 30:
    print('Sobrepeso')
else:
    print('Obesidade')