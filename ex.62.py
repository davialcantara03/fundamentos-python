termo = int(input('Digite o seu primeiro termo: '))
razao = int(input('Digite a sua razão: '))
t = 1
total = 0
mais = 10 
while mais != 0:
    total = total + mais
    while t <= total:
        t += 1
        print(f'{termo}')
        termo += razao
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados!')