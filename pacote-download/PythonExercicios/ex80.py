'''Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
 já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''
valores = list()
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > valores[len(valores)-1]:
        valores.append(n)
        print('Adicionado no final da lista')
    else:
        for s in range(0, len(valores)):
            if n < valores[s]:
                valores.insert(s, n)
                print(f'Adicionado na posição {s}')
                break
print(f'Os valores digitados em oride crescente: {valores}')