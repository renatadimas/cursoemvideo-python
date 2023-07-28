numero = int(input('Digite um número inteiro: '))
print('[1] Converter para BINÁRIO')
print('[2] Converter para OCTAL')
print('[3] Converter para HEXADECIMAL')
escolha = int(input('Escolha uma das bases de conversão:'))
print('Sua opção {}'.format(escolha))
if escolha == 1:
    '''resultado = format(numero, 'b')'''
    print('{} convertido para BINARIO é {}'.format(numero, bin(numero)[2:]))
elif escolha == 2:
    '''resultado = format(numero, 'o')'''
    print('{} convertido para OCTAL é {}'.format(numero, oct(numero)[2:]))
elif escolha == 3:
    '''resultado = format(numero, 'x')'''
    print('{} convertido para HEXADECIMAL é {}'.format(numero, hex(numero)[2:]))
else:
    'Opção invalida'
