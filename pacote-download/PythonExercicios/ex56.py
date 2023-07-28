'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo,
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''
soma = 0
maior = 0
nomeMaior = ''
cont = 0
for c in range(1, 5):
    print('-'*5, '{}º PESSOA'.format(c), '-'*5)
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo(M/F): ').upper().strip()
    soma = soma + idade
    if sexo == 'M':
        if c == 1:
            maior = idade
            nomeMaior = nome
        else:
            if idade > maior:
                maior = idade
                nomeMaior = nome
    if sexo == 'F':
        if idade < 20:
            cont = cont +1
print('A média da idade do grupo é {}'.format(soma/4))
print('O nome do homem mais velhor é {}'.format(nomeMaior))
print('Existem {} mulheres com menos de 20 anos'.format(cont))



