'''Exercício Python 090: Faça um programa que
leia nome e média de um aluno, guardando também a situação em um dicionário.
 No final, mostre o conteúdo da estrutura na tela'''
alunos = dict()
alunos['nome'] = str(input('Nome: '))
alunos['media'] = float(input(f'Média de {alunos["nome"]}: '))
if alunos['media'] >= 7:
    alunos['situação'] = 'Aprovado'
else:
    if alunos['media'] >= 5:
        alunos['situação'] = 'Recuperação'
    else:
        alunos['situação'] = 'Reprovado'
print('=-'*30)
for k, v in alunos.items():
    print(f'-  {k} é igual a {v}')

