from random import randint
from time import sleep
print('-=--'*20)
print('Vou pensar em um número entre 0 e 5 tente adivinhar...')
print('-=--'*20)
jogador = int(input('Em qual número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
computador = randint(0, 5)
if jogador == computador:
    print('Você ganhou, pensamos no némero {}'.format(jogador))
else:
    print('Você errou, pensei no numero {} e não no número {}'.format(computador, jogador))

