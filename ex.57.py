sexo = input('Digite o seu sexo: ').strip().upper()[0]
while sexo not in 'MF':
    print('Dados incorretos. Tente novamente!')
    sexo = input('Digite o seu sexo: ').strip().upper()[0]
    
print(f'Sexo {sexo} registrado com sucesso!')
    