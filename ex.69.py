count_idade = 0
count_homens = 0
count_mulheres = 0
while True:
    idade = int(input('Digite a sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').strip().upper()[0]
    if sexo == 'M':
        count_homens += 1
    if idade > 18:
        count_idade += 1
    if sexo == 'F' and idade < 20:
        count_mulheres += 1
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N]').strip().upper()[0]    
    if resp == 'N':
        break
print(f'A quantidade de mulheres com menos de 20 anos foi {count_mulheres}')
print(f'A quantidade de homens cadastrados foi {count_homens}')
print(f'A quantidade de pessoas cadastradas com mais de 18 anos foi de {count_idade}')
print('FIM DO PROGRAMA')