def leiadinheiro(msg):
    ok = False
    while True:
        mensagem = str(input(msg)).strip().replace(',','.')
        if mensagem.isalpha() or mensagem == '':
            print(f'ERRO: {mensagem} é um preço invalido')
        else:
            ok = True
        if ok is True:
            break
    return float(mensagem)

