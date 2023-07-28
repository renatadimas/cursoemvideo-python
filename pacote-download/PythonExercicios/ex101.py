def voto(nasc):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if 65 >= idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATORIO'
    elif idade > 65 or 18 > idade >= 16:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: NÃO VOTA'


ano = int(input('Em qual ano você nasceu? '))
print(voto(ano))

