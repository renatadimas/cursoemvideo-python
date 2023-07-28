'''Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
 No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
compras = ('Caderno', 15,
           'Lápis', 2.50,
           'Borracha', 5,
           'Estojo', 15,
           'Caneta', 4.20,
           'Régua', 3.30,
           'Agenda', 40.50,
           'Caldendário', 15.60)
for cont in range(0, len(compras)):
    if cont % 2 == 0:
        print(f'{compras[cont]:.<30}', end = ' ')
    else:
        print(f'R${compras[cont]:>6.2f}')
print('-' * 40)