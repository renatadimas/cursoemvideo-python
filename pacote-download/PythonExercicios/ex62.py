'''Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.'''
print('='*20)
print('10 PRIMEIRO TERMOS DE UMA PA')
print('='*20)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
total = p
novos = 10
cont = 1
numero = 0
while novos != 0:
    numero = numero + novos
    while cont <= numero:
        print('{} ---> '.format(total), end='')
        total = total + r
        cont = cont + 1
    print('PAUSE')
    novos = int(input('Quantos termos voce quer mostrar a mais? '))
print('Progressão finalizada com {} termo mostrados'.format(numero))


