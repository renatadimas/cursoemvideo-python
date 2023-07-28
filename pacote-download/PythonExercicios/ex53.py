'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''
frase = input('Digite uma frase: ').strip().upper()
frase2 = frase.replace(' ', '')
'''inverso = frase2[::-1]
print('O inverso de {} é {}'.format(frase2, inverso))
if frase2 == inverso:
    print('A frase digitada é um palíndromo:')
else:
    print('A frase digitada não é um palíndromo:')'''
inverso =''
for letra in range(len(frase2)-1, -1, -1):
    inverso = inverso + frase2[letra]
print('O inverso de {} é {}'.format(frase2, inverso))
if frase2 == inverso:
    print('A frase digitada é um palíndromo:')
else:
    print('A frase digitada não é um palíndromo:')