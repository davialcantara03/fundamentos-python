from datetime import date
ano = int(input('Digite o ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print(f'Classificação: MIRIM')
elif idade <= 14:
    print(f'Classificação: INFANTIL')
elif idade <= 19:
    print(f'Classificação: JUNIOR')
elif idade <= 25:
    print(f'Classificação: SENIOR')
else:
    print(f'Classificação: MASTER')