frase = input('Digite uma frase: ').strip().upper()
print(f'A letra A aparece {frase.count("A")} vezes')
print(f'A posição em que a letra A aparece primeiro é: {frase.find("A") + 1} ')
print(f'A posição em que a letra A aparece por último é {frase.rfind("A") + 1 } ')