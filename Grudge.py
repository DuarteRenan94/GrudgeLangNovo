class Grudge:
  def __init__(self):
    self.memory = [0 for _ in range(100)]
    self.p = 0
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
  
  def get_code(self, code):
    for t in range(0, len(code),3):
      self.code.append(code[t:(t+3)])
  
  def bf_to_gdg(self, bf_code):
    for c in bf_code:
      self.code.append(self._bf[c])
    
  def _increase(self):
    self.memory[self.p] += 1
  
  def _decrease(self):
    self.memory[self.p] -= 1
  
  def _current(self):
    return self.memory[self.p]
  
  def _position(self):
    return self.p
  
  def _inp(self, c):
    self.memory[self.p] = ord(c)
  
  def _out(self):
    print(self.memory[self.p])

  def _next(self):
    self.p+=1
  
  def _prev(self):
    self.p-=1
  
  def show_memory(self):
    print(self.memory)
    
  def compile(self):
    c = 0
    while c < len(self.code):
      if self.code[c] == 'aaa':
        self._increase()
      if self.code[c] == 'aaA':
        self._decrease()
      if self.code[c] == 'aAa':
        self._next()
      if self.code[c] == 'aAA':
        self._prev()
      if self.code[c] == 'Aaa': # inicio loop
        self.abrt = c
        if self._current() == 0:
          for i in range(c, len(self.code)):
            if self.code[c] != 'AaA':
              c = i
          c = i
          self.abrt = None
      if self.code[c] == 'AaA':
        if self._current() > 0:
          c = self.abrt
      if self.code[c] == 'AAa':
        self._inp(input('>'))
      if self.code[c] == 'AAA':
        self._out()
      c += 1
