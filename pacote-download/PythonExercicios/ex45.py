from random import choice
print('Suas opções')
print('''[0] PEDRA
[1] PAPEL
[2] TESOURA''')
n = int(input('Qual é a sua jogada? '))
print('JO')
print('KE')
print('POO!')
lista = ['PEDRA', 'PAPEL', 'TESOURA']
escolha = choice(lista)
print('-='*10)
print('Computador jogou {}'.format(escolha))
if n == 0:
    nome = 'PEDRA'
elif n == 1:
    nome = 'PAPEL'
elif n == 2:
    nome = 'TESOURA'
else:
    nome = 'Numero invalido'
print('Jogador jogou {}'.format(nome))
print('-='*10)
if n == 0 and escolha == 'TESOURA':
    print('Jogador vence')
elif n == 0 and escolha == 'PAPEL':
    print('Computador venceu')
elif n == 1 and escolha == 'PEDRA':
    print('Jogador vence')
elif n == 1 and escolha == 'TESOURA':
    print('Computador venceu')
elif n == 2 and escolha == 'PAPEL':
    print('Jogador vence')
elif n == 2 and escolha == 'PEDRA':
    print('Computador venceu')
else:
    print('Empate, jogue novamente')