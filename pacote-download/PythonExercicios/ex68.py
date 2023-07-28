'''Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
from random import randint
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
cont = 0
while True:
    n = int(input('Digite um valor: '))
    pi = ' '
    while pi not in 'PI':
        pi = input('Par ou impar(P/I): ').strip().upper()[0]
    comp = randint(0, 11)
    result = n+comp
    print('-'*20)
    print(f'Você jogou {n} e o computador {comp}. Total de {result} ', end='')
    print(f'DEU PAR' if result % 2 == 0 else 'DEU IMPAR')
    print('-' * 20)
    if pi in 'P':
        if result % 2 == 0:
            print('Você venceu')
            cont = cont + 1
        else:
            print('Você perdeu')
            break
    elif pi in 'I':
        if result % 2 == 0:
            print('Você perdeu')
            break
        else:
            print('Você venceu')
            cont = cont + 1
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {cont} vezes')
