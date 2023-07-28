'''Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)'''
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        m = str(input(msg))
        if m.isnumeric():
            valor = int(m)
            ok = True
        else:
            print('Erro!Digite um número inteiro válido')
        if ok is True:
            break
    return valor


n = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o número {n}')