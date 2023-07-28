'''Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date
atual = date.today().year
print(atual)
cont = 0
cont2 = 0
for c in range(1, 8):
    ano = int(input('Qual o ano de nascimento da {}º pessoa '.format(c)))
    if atual - ano >= 21:
        cont = cont + 1
    else:
        cont2 = cont2 + 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(cont))
print('Ao todo tivemos {} pessoas menores de idade'.format(cont2))
