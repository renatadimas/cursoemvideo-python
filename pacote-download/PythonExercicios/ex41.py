from datetime import date
nasc = int(input('Ano de Nascimento: '))
ano = date.today().year
idade = ano - nasc
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    categoria = 'mirim'
elif 14 >= idade:
    categoria = 'infantil'
elif 19 >= idade:
    categoria = 'junior'
elif 25 >= idade:
    categoria = 'senior'
else:
    categoria = 'master'
print('Classificação: {}'.format(categoria))