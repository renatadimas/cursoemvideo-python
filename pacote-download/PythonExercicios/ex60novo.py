num = int(input('Digite um número para calcular o seu fatorial: '))
fatorial = 1
for c in range(num, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else " = ", end='')
    fatorial = fatorial * c
print(fatorial)
