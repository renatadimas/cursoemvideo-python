'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média'''
cadastro = dict()
lista = list()
soma = 0
while True:
    cadastro.clear()
    cadastro['nome'] = str(input('Nome: '))
    while True:
        cadastro['sexo'] = str(input('Sexo[M/F]: ')).upper()[0]
        if cadastro['sexo'] in 'MF':
            break
        print('Erro! Por favor, digite M ou F.')
    cadastro['idade'] = int(input('Idade: '))
    soma = soma + cadastro['idade']
    while True:
        cont = str(input('Quer continuar?[S/N] ')).upper()[0]
        if cont in 'SN':
            break
        print('Erro! Por favor, digite S ou N.')
    lista.append(cadastro.copy())
    if cont in 'Nn':
        break
print(lista)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas')
media = soma/len(lista)
print(f'B) A média de idade é {media:.2f} anos')
print(f'C)As mulheres cadastradas foram: ', end='')
for p in lista:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end='')
print()
print('D)Lista das pessoas que estão acima da média')
for p in lista:
    if p['idade'] > media:
        for k,v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')



