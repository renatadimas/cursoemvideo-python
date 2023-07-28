'''Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''
jogo = dict()
lista = list()
jogadores = list()
while True:
    lista.clear()
    jogo.clear()
    jogo['nome'] = str(input('Nome do jogador: '))
    partida = int(input(f'Quantas partidas {jogo["nome"]} jogou? '))
    for c in range(0, partida):
        lista.append(int(input(f'Quantos gols na partida {c}: ')))
    jogo['gols'] = lista[:]
    jogo['total'] = sum(lista)
    while True:
        cont = str(input('Quer continuar?[S/N]? ')).upper()[0]
        if cont in'SN':
            break
        print('Erro! Escreva[S/N]')
    jogadores.append(jogo.copy())
    if cont in 'N':
        break
print('=-'*30)
print(f'{"cod":>4} ', end='')
for k in jogo.keys():
    print(f'{k:<15}', end='')
print()
print('--'*30)
for i,v in enumerate(jogadores):
    print(f'{i:>4} ', end='')
    for t in v.values():
        print(f'{str(t):<15}', end='')
    print()
print('--' * 30)
while True:
    n = int(input('Mostrar os dados de qual jogador?(999 para parar) '))
    if n == 999:
        break
    print(f'---LEVANTAMENTO DO JOGADOR {jogadores[n]["nome"]}')
    for i,v in enumerate(jogadores[n]["gols"]):
        print(f'  No jogo {i} fez {v} gols.')
    print('--' * 30)


