'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''
conti = conth = contm = 0
print('-'*20)
print('CADASTRE UMA PESSOA')
print('-'*20)
while True:
    i = int(input('Idade: '))
    s = ' '
    while s not in 'MF':
        s = input('Sexo [M/F]: ').strip().upper()[0]
    print('-' * 20)
    if i > 18:
        conti = conti + 1
    if s == 'M':
        conth = conth + 1
    if s in 'F':
        if i < 20:
            contm = contm + 1
    q = ' '
    while q not in 'SN':
        q = input('Quer continuar [S/N]: ').strip().upper()[0]
    print('-' * 20)
    if q in 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {conti}')
print(f'Ao todo temos {conth} homens cadastrados')
print(f'Ao todo temos {contm} mulher com menos de 20 anos')
