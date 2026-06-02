cont = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    num = int(input('Digite um valor entre 0 e 20: '))
    if num >= 0 and num <= 20:
        break
    else:
        print('Número inválido. Tente novamente!')
print(f'Você digitou o número {cont[num]}')