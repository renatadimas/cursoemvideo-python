dist = float(input('Qual a distância da sua viagem '))
print('VocÇe está prestes a começar uma viagem de {} km')
if dist <= 200:
    preco = 0.50*dist
else:
    preco = 0.45*dist
print('E o preço da sua passagem será de {} reais'.format(preco))
