'''Exercício Python 72: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
           'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
print(numeros)

while True:
    num = int(input('Digite um número entra 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end = '')
print(f'Voce digitou o número {numeros[num]}')
