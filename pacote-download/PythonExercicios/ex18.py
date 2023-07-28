import math
a = float(input('Digite o ângulo que você deseja '))
print('O angulo de {} tem o seno de {:.2f}'.format(a, math.sin(math.radians(a))))
print('O angulo de {} tem o coseno de {:.2f}'.format(a, math.cos(math.radians(a))))
print('O angulo de {} tem a tangente de {:.2f}'.format(a, math.tan(math.radians(a))))
