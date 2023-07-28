'''Exercício Python 100: Faça um programa que tenha uma lista chamada números e
duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números
 e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.'''
from random import randint
numeros = list()


def sorteia():
    for n in range(0,5):
        numeros.append(randint(1,10))
    print(f'Sorteando 5 valores da lista:', end='')
    for p in numeros:
        print(f'{p} ', end='')
def somaPar(lst):
    soma = 0
    for p in lst:
        if p % 2 == 0:
            soma = soma + p
    print()
    print(f'Somando os valores pares de {lst}, temos {soma}')


sorteia()
somaPar(numeros)
