r = float(input('Quantidad de km rodados '))
d = int(input('Quantidade de dias de aluguel do carro '))
t = (d*60) + (0.15*r)
print('Valor cobrado é de {:.2f} reais'.format(t))