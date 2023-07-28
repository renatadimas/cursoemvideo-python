num = int(input('Digite um número para calcular o seu fatorial: '))
c = num
produto = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    produto = produto * c
    c = c - 1
print('{}'.format(produto))
