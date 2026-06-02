a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
#se b é menor que a e b é menor que C, o menor é B
if b < a and b < c:
    menor = b
#se c é menor que a e c é menor que B, o menor é c
if c < a and c < b:
    menor = c
maior = a
#Se B é maior que A e B é maior que C, o maior é B
if b > a and b > c:
    maior = b
#Se C é maior que B e C é maior que A, o maior é C
if c > a and c > b:
    maior = c
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')