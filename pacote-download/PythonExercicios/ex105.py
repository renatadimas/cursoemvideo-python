'''
Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de
alunos e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)
'''
def notas(*nota, sit=False):
    """
    --> Função para adicionar notas e situação de vários alunos
    :param nota: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    dados = dict()
    dados['total'] = len(nota)
    dados['maior'] = max(nota)
    dados['menor'] = min(nota)
    med = sum(nota)/len(nota)
    dados['media'] = med
    if sit is True:
        if med >= 7:
            dados['situação'] = 'Boa'
        elif 7 > med > 5:
            dados['situação'] = 'Razoavél'
        else:
            dados['situação'] = 'Ruim'
    return dados


resp = notas(5.5,2.5,1.5,sit = True)
print(resp)
help(notas)