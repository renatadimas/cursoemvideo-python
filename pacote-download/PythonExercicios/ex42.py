print('-='*20)
print('ANALISADOR DE TRIANGULOS')
print('-='*20)
a = float(input('Primeiro segmento '))
b = float(input('Segundo segmento '))
c = float(input('Terceiro segmento '))
if (a + b) > c and (b + c) > a and (a + c) > b:
    print('Os segmentos acima PODEM formar um triangulo ', end='')
    if a == b == c:
        print('EQUILATERO')
    elif a != b != c != a:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('Os segmentos acima NAO PODEM formar um triangulo')