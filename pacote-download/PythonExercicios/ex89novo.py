lista = list()
while True:
    nome = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    lista.append([nome, [n1,n2], media])
    resp = input('Quer continuar?[S/N]')
    if resp in 'Nn':
        break
print('=-'*30)
print(f'{"No.":<4}',f'{"NOME":<10}',f'{"MEDIA":>8}')
print('-'*26)
for i,l in enumerate(lista):
    print(f'{i:<4}',f'{l[0]:<10}',f'{l[2]:>8.1f}')
while True:
    num = int(input('Mostrar a nota de qual aluno? (999 interrompe) '))
    if num <= len(lista)-1:
        print(f'As notas de {lista[num][0]} são {lista[num][1]}')
    if num == 999:
        break
print('>>>>>>>>>VOLTE SEMPRE')