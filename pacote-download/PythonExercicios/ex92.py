'''Exercício Python 092: Crie um programa que leia nome, ano de nascimento e
carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também
o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import date
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
ano = date.today().year
dados['idade'] = ano - nasc
dados['ctps'] = int(input('Carteira de trabalho(0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano da contratação: '))
    dados['salário'] = float(input('Salários: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - date.today().year)
for k,v in dados.items():
    print(f'{k} tem valor {v}')
