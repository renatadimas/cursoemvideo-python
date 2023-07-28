palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR'
            'MERCADO', 'PROGRAMADOR', 'FUTURO')
for cont in range(0,len(palavras)):
    print(f'\nNa palavra {palavras[cont]} temos', end = ' ')
    if 'A' in palavras[cont]:
        print('a', end=' ')
    if 'E' in palavras[cont]:
        print('e', end=' ')
    if 'I' in palavras[cont]:
        print('i', end=' ')
    if 'O' in palavras[cont]:
        print('o', end=' ')
    if 'U' in palavras[cont]:
        print('u', end=' ')

