nome = input('Digite o seu nome completo: ').strip()
print(f'O meu nome em maiúsculas é {nome.upper()}')
print(f'O meu nome em minúsculas é {nome.lower()}')
print(f"Seu nome tem ao todo {len(nome) - nome.count(' ')} letras")