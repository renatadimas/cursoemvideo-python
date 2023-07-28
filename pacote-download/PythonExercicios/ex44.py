print('{:=^40}'.format(' Lojas Guanabará '))
preco = float(input('Preço da compras: R$'))
print('Formas de pagamento')
print('[1]à vista dinheiro/cheque')
print('[2]à vista no cartão')
print('[3]em até 2x no cartão')
print('[4]3x ou mais no cartão')
n = int(input('Qual é a opção '))
if n == 1:
    total = preco - (preco*0.10)
    print('Sua compra de {:.2f} vai custar {:.2f} no final'.format(preco, total))
elif n == 2:
    total = preco - (preco * 0.05)
    print('Sua compra de {:.2f} vai custar {:.2f} no final'.format(preco, total))
elif n == 3:
    total = preco
    print('Sua compra será parcelada em 2x de {:.2f} com juros'.format(preco/2))
    print('Sua compra de {:.2f} vai custar {:.2f} no final'.format(preco, total))
elif n == 4:
    parc = int(input('Quantas parcelas: '))
    total = preco + (preco * 0.20)
    parc2 = total/parc
    print('Sua compra será parcelada em {}x de {:.2f} com juros'.format(parc, parc2))
    print('Sua compra de {:.2f} vai custar {:.2f} no final'.format(preco, total))
else:
    print('Opção não valida')

