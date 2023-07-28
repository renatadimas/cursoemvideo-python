'''Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''
from time import sleep


def contador(i,f,p):
    print('='*35)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i > f and p > 0:
        p = -p
    if i < f and p < 0:
        p = -p
    if f > 0:
        for c in range(i, f+1, p):
            print(f'{c} ', end='')
            sleep(0.3)
        print('FIM')
    else:
        for c in range(i, f-1, p):
            print(f'{c} ', end='')
            sleep(0.3)
        print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)
print('='*35)
print('Agora é a sua vez de personalizar a contagem')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)