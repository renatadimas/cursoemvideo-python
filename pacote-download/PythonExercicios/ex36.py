casa = float(input('Valor da casa:R$ '))
salario = float(input('Salário do comprador:R$ '))
tempo = int(input('Quantos anos de financiamento: '))
p = casa/(tempo*12)
print('Para pagar uma casa de {} em {} anos a prestação será de {:.2f}'.format(casa, tempo, p))
if p > (0.30 * salario):
    print('Emprestimo negado')
else:
    print('Emprestimo aprovado')
