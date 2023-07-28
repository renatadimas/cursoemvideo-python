a = float(input('Digite o primeiro valor '))
b = float(input('Digite o segundo valor '))
c = float(input('Digite o terceiro valor '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor número é {}'.format(menor))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior numero é {}'.format(maior))


