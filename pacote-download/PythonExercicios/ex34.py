sal = float(input('Digite o valor do seu salário '))
if sal > 1250:
    total = sal + (0.10*sal)
else:
    total = sal + (0.15*sal)
print('\033[1;31;42mQuem ganhava {:.2f} passa a ganhar {:.2f}\033[m'.format(sal,total))
