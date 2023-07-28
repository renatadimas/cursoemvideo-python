'''Exercício Python 73: Crie uma tupla preenchida com os 20
primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.'''
times = ('Botafogo', 'Fortaleza','Palmeiras', 'Internacional',
         'Fluminense', 'Cruzeiro', 'Grêmio', 'São Paulo', 'Vasco', 'Atlético-MG', 'Santos',
         'Bragantino', 'Flamengo', 'Athletico-PR', 'Goiás', 'Corinthians', 'Cuiabá',
         'Coritiba', 'Bahia', 'América-MG')
print('-'*30)
print(f'Todos os times do Brasileirão {times}')
print('-'*30)
print(f'Os cinco primeiros {times[:5]}')
print('-'*30)
print(f'Os ultimos quatro colocados {times[-4:]}')
print('-'*30)
print(f'Times em ordem alfabética {sorted(times)}')
print('-'*30)
print(f'O Flamengo se encontra na posição {times.index("Flamengo")+1}')
