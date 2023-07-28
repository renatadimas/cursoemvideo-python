'''Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''
valores = list()
maior = menor = 0
for cont in range(0, 5):
    valores.append(int(input('Digite um valor na posição {}: '.format(cont))))
    if cont == 0:
        maior = valores[0]
        menor = valores[0]
    else:
        if valores[cont] >= maior:
            maior = valores[cont]
        if valores[cont] <= menor:
            menor = valores[cont]

print(f'Os valores digitados foram {valores}')
print(f'O maior valor digitado é {maior} na posição', end=' ')
for c, v in enumerate(valores):
    if v == maior:
        print(f'{c}...', end= ' ')
print(f'\nO menor valor digitado é {menor} na posição', end=' ')
for c, v in enumerate(valores):
    if v == menor:
        print(f'{c}...', end= ' ')
#print(f'O maior valor digitado é {max(valores)} na posição {valores.index(max(valores))}')
#print(f'O menor valor digitado é {min(valores)} na posição {valores.index(min(valores))}')