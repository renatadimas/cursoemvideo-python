'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint
computador = randint(0, 10)
print('Sou o seu computador \nAcabei de pensar em um número entre 0 e 10 \nSerá que voce consegue adivinhar qual foi?')
acertou = False
cont = 0
while not acertou:
    pessoa = int(input('Qual é o seu palpite '))
    if pessoa == computador:
        acertou = True
    else:
        if pessoa < computador:
            print('Mais.. Tente mais uma vez. ')
        else:
            print('Menos.. Tente mais uma vez. ')
    cont = cont + 1
print('Você acertou! Foram necessários {} palpites'.format(cont))
