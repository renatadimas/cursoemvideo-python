'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''
valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = input('Quer continuar?[S/N] ').strip().upper()[0]
    if resp == 'N':
        break
valores.sort(reverse=True)
print(f'Foram digitados {len(valores)} números')
print(f'A lista de valores, ordenada de forma decrescente {valores}')
if 5 in valores:
    print('O valor 5 foi digitado')
else:
    print('O valor 5 não foi digitado')
