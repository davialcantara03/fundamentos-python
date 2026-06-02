# Importa o random
import random
# Faz a variável do computador e manda ele escolher entre 0 a 10
computador = random.randint (0, 10)
# Printa com as frases do jogo
print('Acabei de pensar em um número entre 0 e 10')
print('Você consegue adivinhar qual é?')
# Pede o palpite do jogador
palpite = int(input('Qual o seu palpite? '))
tentativas = 1
# Faz o while, if e else
while palpite != computador:
    if computador > palpite:
        print('Mais... Tente novamente!')
    else:
        #Pede o input do palpite
        print('Menos... Tente novamente!')
    palpite = int(input('Qual é o seu palpite? '))
    tentativas += 1

print(f'Você acertou com {tentativas} tentativas. Parabéns!')