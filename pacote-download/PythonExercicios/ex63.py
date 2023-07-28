'''Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre
na tela os N primeiros elementos de uma Sequência de Fibonacci.Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8'''
print('=-'*10)
print('Sequencia de Fibronatti')
print('=-'*10)
termos = int(input('Quantos termos voce quer? '))
cont = 1
ultimo = 1
penultimo = 1
numero = 1
while cont <= termos:
     if cont == 1:
          print('0 --> ', end='')
          cont = cont + 1
     elif cont == 2:
          print('1 --> ', end='')
          cont = cont + 1
     else:
          print('{} --> '.format(numero), end = '')
          numero = ultimo + penultimo
          penultimo = ultimo
          ultimo = numero
          cont = cont + 1
print('FIM')
'''a1 = 1
a2 = 1
a3 = a2 + a1 = 1 + 1 = 2
a4 = a3 + a2 = 2 + 1 = 3
a5 = a4 + a3 = 3 + 2 = 5
a6 = a5 + a4 = 5 + 3 = 8
a7 = a6 + a5 = 8 + 5 = 13
a8 = a7 + a6 = 13 + 8 = 21
a9 = a8 + a7 = 21 + 13 = 34'''

