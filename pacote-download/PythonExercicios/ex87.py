'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''
matriz = [[0,0,0],[0,0,0],[0,0,0]]
somap = somac = maior = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para {l}x{c}: '))
        if matriz[l][c] % 2 ==0:
            somap = somap + matriz[l][c]
        if c == 2:
            somac = somac + matriz[l][c]
        if l == 1:
            maior = matriz[1][0]
            if matriz[l][c] > maior:
                maior = matriz[l][c]
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}:^5]', end='')
    print()
print(f'A soma de todos os valores pares digitados é {somap}')
print(f'A soma de todos os valores da terceira coluna é {somac}')
print(f'O maior valor digitado na segunda linha é {maior}')