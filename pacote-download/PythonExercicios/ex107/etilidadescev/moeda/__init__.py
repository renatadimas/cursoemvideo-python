def metade(num=0, formatado = False):
    res = num/2
    return res if formatado is False else moeda(res)


def dobro(num=0, formatado = False):
    res = 2 * num
    return res if not formatado else moeda(res)


def aumementar(num=0, taxa=0, formatado = False):
    res = num + ((taxa/100) * num)
    return res if formatado is False else moeda(res)


def diminuir(num=0, taxa=0, formatado = False):
    res = num - ((taxa/100) * num)
    return res if formatado is False else moeda(res)


def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:>.2f}'.replace('.',',')


def resumo(num=0, aument=10, diminui=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(num)}')
    print(f'Dobro do preço:  \t{dobro(num, True)}')
    print(f'Metade do preço:  \t{metade(num, True)}')
    print(f'{aument}% de aumento:  \t{aumementar(num,aument,True)}')
    print(f'{diminui}% de redução:  \t{diminuir(num,diminui,True)}')
    print('-' * 30)
