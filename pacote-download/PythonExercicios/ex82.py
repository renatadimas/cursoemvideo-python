'''Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''
numeros = list()
contador = 0
pares = list()
impares = list()
while True:
    numeros.append(int(input('Digite um número: ')))
    if numeros[contador] % 2 == 0:
        pares.append(numeros[contador])
    else:
        impares.append(numeros[contador])
    contador = contador + 1
    resp = input('Deseja continuar?[S/N] ')
    if resp in 'Nn':
        break
print(f'Todos os valores digitados:{numeros}')
print(f'Os valores pares digitados:{pares}')
print(f'Os valores impares digitados {impares}')