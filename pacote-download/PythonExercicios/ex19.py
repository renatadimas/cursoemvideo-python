from random import choice
a = input('Digite o primeiro nome ')
b = input('Digite o segundo nome ')
c = input('Digite o terceiro nome ')
d = input('Digite o quarto nome ')
lista = [a,b,c,d]
print('O aluno escolhido foi {}'.format(choice(lista)))