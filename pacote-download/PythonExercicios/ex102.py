'''Exercício Python 102: Crie um programa que tenha uma função fatorial()
 que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show,
que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''
def fatorial(num,show=False):
    """
    --> Calcula o fatorial de um número
    :param num: o número a ser calculado o fatorial
    :param show: opcional, se você quer ou não mostrar o processo de calculo fatorial
    :return: o valor do ftorial de um número, o número n
    """
    soma = 1
    for c in range(num, 0, -1):
        soma = soma * c
        if show is True:
            print(f' {c} x' if c > 1 else f' {c} = ', end='')
    return soma


print(fatorial(5))



