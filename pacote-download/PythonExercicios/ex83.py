'''Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''
parenteses = list()
ex = input(f'Digite a expressão: ')
for caracter in ex:
    if caracter == '(':
        parenteses.append(caracter)
    elif caracter == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
if len(parenteses) == 0:
    print('A sua expressão está correta')
else:
    print('A sua expressão está errada')