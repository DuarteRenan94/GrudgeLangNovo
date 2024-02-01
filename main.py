from grudge_lang import *
import sys

opt = input('Olá, seja bem vindo ao interpretador d\'O Grito.\n Aperte: \ni para inserir código.\nb insira código brainfuck a ser traduzido e interpretado\n x para sair.\n$ ')
g = Grudge()
if opt == 'i':
  code = input('\n$ ')
  g.get_code(code)
if opt == 'b':
  c = input('\n$ ')
  g.bf_to_gdg(c)
if opt == 'x':
  sys.exit()
g.compile()
g.show_memory()