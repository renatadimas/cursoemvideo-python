from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep
arquivo = 'cursoemvideo.txt'
if not arquivoExite(arquivo):
    criarAquivo(arquivo)
while True:
    resposta = menu(['Ver Pessoa Cadastrada', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        '''VER PESSOAS CADASTRADAS'''
        leiaArquivo(arquivo)
    elif resposta == 2:
        cabeçalho('CADASTRAR NOVA PESSOA')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('Digite uma opção valida')
    sleep(2)