peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
IMC = peso/(altura**2)
print('0 IMC dessa pessoa é de {:.1f}'.format(IMC))
if IMC < 18.5:
    status = 'ABAIXO DO PESO'
elif IMC < 25:
    status = 'PESO IDEAL'
elif IMC < 30:
    status = 'SOBREPESO'
elif IMC < 40:
    status = 'OBESIDADE'
else:
    status = 'OBESIDADE MORBIDA'
print('Voce esta na faixa: {}'.format(status))


