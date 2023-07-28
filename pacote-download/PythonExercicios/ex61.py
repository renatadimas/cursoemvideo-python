'''Exercício Python 61: Refaça o DESAFIO 51,
lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.'''
print('='*20)
print('10 PRIMEIRO TERMOS DE UMA PA')
print('='*20)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 0
n = p
while c < 10:
    print('{} --> '.format(n), end='')
    n = n + r
    c = c + 1
print('FIM')

