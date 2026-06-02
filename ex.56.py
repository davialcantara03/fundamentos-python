soma_idade = 0
media_idade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for c in range(1, 5):
    nome = input('Digite o seu nome: ')
    idade = int(input('Digite a sua idade: '))
    sexo = input('[M/F]: ')
    soma_idade += idade
    if sexo == 'M' and idade > maioridadehomem:
        nomevelho = nome
        maioridadehomem = idade
    if sexo == 'F' and idade < 20:
        totmulher20 += 1

media = soma_idade / 4
print(f'A média de idade do grupo é de {media} anos')
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')