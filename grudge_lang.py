class Grudge:
  def __init__(self):
    self.memory = [0 for _ in range(100)]
    self.p = 0
    self._c = 0
    self.code = []
    self._bf = {
      '+' : 'aaa',
      '-' : 'aaA',
      '>' : 'aAa',
      '<' : 'aAA',
      '[' : 'Aaa',
      ']' : 'AaA',
      ',' : 'AAa',
      '.' : 'AAA'
    }
    self.sm = []
    self.abrt = None # índice do colchete de abertura
    self._INSTRUCTIONS = {
      'aaa': self._increase,
      'aaA': self._decrease,
      'aAa': self._next,
      'aAA': self._prev,
      'Aaa': self._consume_loop,
      'AaA': self._exit_loop,
      'AAa': self._inp,
      'AAA': self._out
    }
  
  def get_code(self, code):
    for t in range(0, len(code),3):
      self.code.append(code[t:(t+3)])
  
  def bf_to_gdg(self, bf_code):
    for c in bf_code:
      self.code.append(self._bf[c])
    
  def _increase(self):
    self.memory[self.p] += 1
  
  def _decrease(self): self.memory[self.p] -= 1
  
  def _current(self): return self.memory[self.p]
  
  def _position(self): return self.p
  
  def _inp(self): self.memory[self.p] = ord(input('>'))
  
  def _out(self): print(chr(self.memory[self.p]))

  def _next(self): self.p+=1
  
  def _prev(self): self.p-=1

  def _consume_loop(self):
    self.abrt = self._c
    if self._current() == 0:
      for i in range(self._c, len(self.code)):
        if self.code[c] != 'AaA':
          self._c = i
      self._c = i
      self.abrt = None
  
  def _exit_loop(self, ):
    if self._current() > 0:
      self._c = self.abrt

  def show_memory(self): print(self.memory)
    
  def compile(self):
    while self._c < len(self.code):
      self._INSTRUCTIONS[self.code[self._c]]()
      self._c += 1
