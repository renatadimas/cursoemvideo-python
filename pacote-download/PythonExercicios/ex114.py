'''
Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
TESTAR A CONEXÃO DA INTERNET USANDO PYTHON
'''
import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except urllib.error.URLError:
    print('O site pudim não está acessivel no momento')
else:
    print('Consegui acessar o site Pudim com sucesso')