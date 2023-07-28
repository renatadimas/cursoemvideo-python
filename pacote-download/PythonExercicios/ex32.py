from datetime import date
a = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O ano {} é bissexto'.format(a))
else:
    print('O ano {} NÃO é bissexto'.format(a))
