'''Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas
de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''
print('='*20)
print('BANCO CEV')
print('='*20)
while True:
    valor = int(input('Qual valor você quer sacar? R$'))
    if valor / 50 >= 1:
        quant50 = valor // 50
        print(f'Total de {quant50} células de 50 reais')
        if valor % 50 == 0:
            break
        valor = valor % 50
    if valor / 20 >= 1:
        quant20 = valor // 20
        print(f'Total de {quant20} células de 20 reais')
        if valor % 50 == 0:
            break
        valor = valor % 20
    if valor / 10 >= 1:
        quant10 = valor // 10
        print(f'Total de {quant10} células de 10 reais')
        if valor % 50 == 0:
            break
        valor = valor % 10
    if valor / 1 >= 1:
        quant1 = valor // 1
        print(f'Total de {quant1} células de 1 reais')
        break





