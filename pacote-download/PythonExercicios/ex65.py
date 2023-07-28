'''Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
 No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
 O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
continuar = 'S'
cont = 0
soma = 0
media = 0
maior = 0
menor = 0
while continuar == 'S':
    numero = int(input('Digite um número: '))
    continuar = input('Quer continuar? [S/N] ').strip().upper()
    cont = cont + 1
    soma = soma + numero
    if cont == 1:
        menor = numero
        maior = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

media = soma / cont
print('Voce digitou {} numeros e a media foi {}'.format(cont, media))
print('O maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))
