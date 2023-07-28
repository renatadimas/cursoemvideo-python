def fatoria(num):
    f = 1
    for c in range(1, num+1):
        f = f * c
    return f


numero = int(input('Digite um número: '))
fat = fatoria(numero)
print(f"O fatorial de {numero} é {fat}")