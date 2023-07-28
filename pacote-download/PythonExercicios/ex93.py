'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
jogo = dict()
lista = list()
jogo['nome'] = str(input('Nome do jogador: '))
partida = int(input(f'Quantas partidas {jogo["nome"]} jogou? '))
for c in range(0, partida):
    lista.append(int(input(f'Quantos gols na partida {c}: ')))
jogo['gols'] = lista[:]
jogo['total'] = sum(lista)
print('=-'*30)
print(jogo)
print('=-'*30)
for k,v in jogo.items():
    print(f'O campo {k} tem valor de {v}')
print('=-'*30)
print(f'O jogador {jogo["nome"]} jogou {partida} partidas')
for i,v in enumerate(lista):
    print(f'Na partida {i}, fez {v} gols')
print(f'Foi um total de {jogo["total"]} gols')
