num = int(input('Digite um número: '))
primo = True
for c in range (2, num):
    if num % c == 0:
        primo = False
if primo:
    print('O número é primo')
else:
    print('O número não é primo')