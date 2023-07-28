'''Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da
digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''
def leiaInt(msg):
    while True:
        try:
            m = int(input(msg))
        except(ValueError, TypeError):
            print('ERRO! Por favor digite um número inteiro válido')
            continue
        except(KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário')
            return 0
        else:
           return m


def leiaFloat(msg):
    while True:
        try:
            m = float(input(msg))
        except(ValueError, TypeError):
            print('ERRO! Por favor digite um número real válido')
            continue
        except(KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário')
            return 0
        else:
            return m


n1 = leiaInt('Digite um numero inteiro: ')
n2 = leiaFloat('Digite um numero real: ')
print(f'Voce acabou de digitar o número {n1} e {n2}')
