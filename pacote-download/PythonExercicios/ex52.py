'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''
n = int(input('Escreva um número '))
cont = 0
for c in range(1,n+1):
    if n % c == 0:
        cont = cont + 1
print('O numero {} foi divisível {} vezes'.format(n,cont))
if cont == 2:
    print('O numero {} é primo'.format(n))
else:
    print('O numero {} não é primo'.format(n))