from datetime import date
ano = input(int('Digite seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano
print(f'Quem nasceu em {ano} tem {idade} anos em {ano_atual}')
if idade < 18:
    ano_alistamento = ano + 18
    print(f'Você tem que se alistar em {ano_alistamento} ')
    falta = 18 - idade
    print(f'Você ainda vai se alistar em {falta} anos')
elif idade == 18:
    ano_alistamento = ano + 18
    print(f'Você precisa se alistar imediatamente em {ano_alistamento} ')
    print(f'Você PRECISA se alistar imediatamente')
else:
    ano_alistamento = ano + 18
    passou = idade - 18
    print(f'Você já deveria ter se alistado há {passou} anos')
    print(f'Você se alistou em {ano_alistamento} ')