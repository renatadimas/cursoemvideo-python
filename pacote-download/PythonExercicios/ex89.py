'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
 No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
temp = list()
cad = list()
cont = 0
while True:

    temp.append(input('Nome: '))
    n1 = float(input('Nota 1: '))
    temp.append(n1)
    n2 = float(input('Nota 2: '))
    temp.append(n2)
    media = (n1+n2)/2
    temp.append(media)
    resp = input('Quer continuar?[S/N]')
    cad.append(temp[:])
    temp.clear()
    '''if cad[0]:
        maior = cad[0][3]
    if cad[cont][3] > maior:
        maior = cad[cont][3]
    cont = cont + 1'''
    if resp in 'Nn':
        break
print('=-'*30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*30)
'''print(f'A maior média foi {maior}')
crescente = cad[][].sort()'''
for cont in range(0,len(cad)):
    print(f'{cont:<7}', end= '')
    print(f'{cad[cont][0]:^9}', end='')
    print(f'{cad[cont][3]:>6}', end='')
    print()
while True:
    num = int(input('Mostrar a nota de qual aluno? (999 interrompe) '))
    print(f'As notas de {cad[num][0]} são {cad[num][1]} e {cad[num][2]}')
    if num == 999:
        break