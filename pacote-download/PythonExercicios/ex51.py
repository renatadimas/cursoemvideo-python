'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.'''
print('='*20)
print('10 PRIMEIRO TERMOS DE UMA PA')
print('='*20)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for c in range(p, p+(10*r), r):
    print(c, end=' ')



