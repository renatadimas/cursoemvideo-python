'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''
print('-'*20)
print('LOJA SUPER BARATÃO')
print('-'*20)
total = 0
contador = 0
mais = 0
while True:
    contador = contador + 1
    nome = input('Nome do produto: ')
    preco = float(input('Preço:R$'))
    total = total + preco
    if contador == 1 or preco < menorp:
        menor = nome
        menorp = preco
    if preco > 1000:
        mais = mais + 1
    cont = ' '
    while cont not in 'SN':
        cont = input('Quer continuar?[S/N] ').strip().upper()[0]
    if cont == 'N':
        break
print(f'O total da compra foi {total}')
print(f'Temos {mais} produto custando mais de 1000 reais')
print(f'O produto mais barato foi {menor} custando {menorp} reais')

