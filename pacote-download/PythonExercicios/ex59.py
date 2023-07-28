'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
opcao = 0
maior = 0
while opcao != 5:
    print(' \n[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa \n====================')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        print('O resultado de {} + {} é {}'.format(a, b, a+b))
        sleep(4)
    elif opcao == 2:
        print('O resultado de {} * {} é {}'.format(a, b, a * b))
        sleep(4)
    elif opcao == 3:
        if a > b:
           maior = a
        else:
            maior = b
        print('Entre {} e {} o maior é {}'.format(a, b, maior))
        sleep(4)
    elif opcao == 4:
        a = float(input('Digite o primeiro número: '))
        b = float(input('Digite o segundo número: '))
        sleep(4)
    else:
        print('Opção invalida. Tente novamente!')
print('=-='*10)
print('Finalizando')
sleep(4)
print('Fim do programa')


