memory = [0 for _ in range(100)]
p = 0

def show_memory():
  print(memory)

def decrease():
  global p
  memory[p] -= 1

def increase():
  global p
  memory[p] += 1

def next():
  global p
  p += 1

def prev():
  global 
  
def tokenize(texto):
  cd = []
  for t in range(0, len(texto),3):
    cd.append(texto[t:(t+3)])
  return cd

def convert(code):
  return tokenize(code)

def compile(bytecode):
  global p
  if bytecode[0] == 'aaa':
    memory[p]+=1
    return compile(bytecode[1:])
  if bytecode[0] == 'aaA':
    memory[p]-=1
    return compile(bytecode[1:])
  if bytecode[0] == 'aAa':
    p += 1
    return compile(bytecode[1:])
  if bytecode[0] == 'aAA':
    p -= 1
    return compile(bytecode[1:])
  if bytecode[0] == 'Aaa':
    if memory[p] > 0:
      ind = bytecode.index('AaA')
      return ['Aaa'] + compile(bytecode[1:ind]) + bytecode[ind:]
  if bytecode[0] == 'AaA':
    if memory[p] == 0:
      return compile(bytecode[1:])
  if bytecode[0] == 'AAa':
    memory[p] = ord(input('>'))
    return compile(bytecode[1:])
  if bytecode[0] == 'AAA':
    print(chr(memory[p]))
    return compile(bytecode[0])
  return []


