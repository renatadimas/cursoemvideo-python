vel = float(input('Qual a velocidade do carro? '))
'''Condição simples só tem um if, sem o else'''
if vel > 80:
    print('Você foi multado, a sua multa é de {:.2f} reais'.format((vel-80)*7))
print('Tenha um bom dia! Dirija com segurança')
