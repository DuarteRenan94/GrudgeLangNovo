from Grudge import *
import sys

code = input('Olá, seja bem vindo ao compilador d\'O Grito. Para começar, insira o código da linguagem. Para encerrar o prigrama, digite x. \n>')
if code == 'x':
  sys.exit(0)
g = Grudge(code)
g.compile()
g.show_memory()