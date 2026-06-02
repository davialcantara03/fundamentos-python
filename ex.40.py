n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1 + n2) / 2
print(f'Tirando {n1} e {n2}, a média do aluno é {media}')
if media >= 7:
    print(f'APROVADO!')
elif media >= 5 and media <= 6.9:
    print(f'RECUPERAÇÃO!')
else:
    print(f'REPROVADO!')
