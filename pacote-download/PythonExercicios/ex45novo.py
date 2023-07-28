from random import randint
from time import sleep
print('Suas opções')
print('[0] PEDRA')
print('[1] PAPEL')
print('[2] TESOURA')
jogador = int(input('Qual é a sua jogada? '))
lista = ['PEDRA', 'PAPEL', 'TESOURA']
comp = randint(0, 2)
print('-='*10)
print('Computador jogou {}'.format(lista[comp]))
print('Jogador jogou {}'.format(lista[jogador]))
print('-='*10)
print('JO')
sleep(1)
print('KE')
sleep(1)
print('POO!')
sleep(1)
if jogador != 0 or jogador != 1 or jogador != 2:
    print('Numero digitado invalido')
elif comp == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador ganhou')
    elif jogador == 2:
        print('Computador ganhou')
    else:
        print('Numero digitado invalido')
elif comp == 1:
    if jogador == 0:
        print('Computador ganhou')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador ganhou')
    else:
        print('Numero digitado invalido')
elif comp == 2:
    if jogador == 0:
        print('Jogador ganhou')
    elif jogador == 1:
        print('Computador ganhou')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Numero digitado invalido')

