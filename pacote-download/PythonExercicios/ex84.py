'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''
temp = list()
princ = list()
maior = menor = 0
while True:
    temp.append(input('Nome: '))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    sn = input('Quer continuar?[S/N] ').strip().upper()
    if sn in 'Nn':
        break
print(f'A listagem é {princ}')
print(f'Existem {len(princ)} pessoas no cadastro')
print(f'O maior peso é {maior}. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso é {menor}. Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]} ', end='')
print()
'''for p in princ:
    print(p[0])
for p in princ:
    print(p[1])
print(princ[0])
print(princ[0][0])
print(princ[1][0])'''