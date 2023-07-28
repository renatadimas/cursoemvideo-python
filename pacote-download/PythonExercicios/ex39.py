from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual-ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, atual))
if idade > 18:
    print('Voce já deveria ter se alistado há {} anos'.format(idade-18))
    print('O seu alistamento foi em {}'.format(atual-(idade-18)))
elif idade == 18:
    print('Voce tem que se alistar imediatamente')
else:
    print('Voce deverá se alistar em {} anos'.format(18 - idade))
    print('O seu alistamento será em {}'.format(atual + (18 - idade)))


