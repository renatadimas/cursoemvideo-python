'''
Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
'''
from time import sleep
c = {'sem cor': '\033[m',
        'vermelho': '\033[0;30;41m',
        'verde': '\033[0;30;42m',
        'amarelo': '\033[0;30;43m',
        'azul': '\033[0;30;44m',
        'roxo': '\033[0;30;45m',
        'branco': '\033[7;30m'
       }


def ajuda(a):
    titulo(f"Acessando o manual do comando {nome}", 'azul')
    print(c['roxo'],end='')
    help(a)
    print(c['roxo'],end='')
    sleep(2)


def titulo(msg, cor='sem cor'):
    tam = len(msg) + 4
    print(c[cor],end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(c['sem cor'], end='')
    sleep(1)

while True:
    titulo('Sistema de ajuda PyHELP','verde')
    nome = str(input('Função ou biblioteca> '))
    sleep(0.5)
    if nome.upper() == 'FIM':
        break
    else:
        ajuda(nome)
titulo('ATÉ LOGO','vermelho')