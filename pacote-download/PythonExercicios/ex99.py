''''Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''


def maior(*num):
    print('Analisando os valores passados...')
    for v in num:
        print(f'{v} ', end='')
    print(f'Foram informados {len(num)} valores ao todo.')
    m = max(num)
    print(f'O maior valor informado foi o {m}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
