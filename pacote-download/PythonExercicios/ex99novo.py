def maior(*num):
    print('Analisando os valores passados...')
    cont = m = 0
    for v in num:
        print(f'{v} ',end='')
        if cont == 0:
            m = v
        if v > m:
            m = v
        cont = cont + 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi o {m}')




maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
