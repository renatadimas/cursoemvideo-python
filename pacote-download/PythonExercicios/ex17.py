import math
a = float(input('Comprimento do cateto oposto '))
b = float(input('Comprimento do cateto adjacente '))
h = math.hypot(a,b)
print('A hipotenusa vai medir {:.2f} '.format(h))