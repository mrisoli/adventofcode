class Intcode:
  def __init__(self, a):
    self.a = a[:]
    self.i = 0
    self.base = 0
    self.inputs = []
    self.o = None

  def add(self, mode):
    self.a[self.value(self.i + 3, mode[2], True)] = self.value(self.i + 1, mode[0]) + self.value(self.i + 2, mode[1])
    self.i += 4

  def multiply(self, mode):
    self.a[self.value(self.i + 3, mode[2], True)] = self.value(self.i + 1, mode[0]) * self.value(self.i + 2, mode[1])
    self.i += 4

  def modify(self, mode):
    self.a[self.value(self.i + 1, mode[0], True)] = self.inputs.pop(0)
    self.i += 2

  def output(self, mode):
    val = self.value(self.i + 1, mode[0])
    self.o = val
    self.i += 2
    print(val)
    return self.o

  def jump(self, mode, c):
    if c:
      self.i = self.value(self.i + 2, mode[1])
    else:
      self.i += 3

  def jump_if_true(self, mode):
    self.jump(mode, self.value(self.i + 1, mode[0]) != 0)

  def jump_if_false(self, mode):
    self.jump(mode, self.value(self.i + 1, mode[0]) == 0)

  def ifc(self, mode, c):
    if c:
      self.a[self.value(self.i + 3, mode[2], True)] = 1
    else:
      self.a[self.value(self.i + 3, mode[2], True)] = 0
    self.i += 4

  def less_than(self, mode):
    self.ifc(mode, self.value(self.i + 1, mode[0]) < self.value(self.i + 2, mode[1]))

  def equals(self, mode):
    self.ifc(mode, self.value(self.i + 1, mode[0]) == self.value(self.i + 2, mode[1]))

  def offset(self, mode):
    self.base += self.value(self.i + 1, mode[0])
    self.i += 2

  def value(self, i, n, w=False):
    if n == 0 and not w:
      return self.a[self.a[i]]
    elif n == 2:
      return self.a[self.base + self.a[i]]
    else:
      return self.a[i]

  def get_opcode(self):
    return self.a[self.i] % 100

  def input(self, inputs):
    self.inputs += inputs
    return self

  def mode(self):
    st = str(self.a[self.i] // 100)
    while len(st) < 3:
      st = "0" + st
    return list(map(int, reversed(st)))

  def run(self):
    while True:
      op = self.get_opcode()
      mode = self.mode()
      if op == 1:
        self.add(mode)
      elif op == 2:
        self.multiply(mode)
      elif op == 3:
        self.modify(mode)
      elif op == 4:
        return self.output(mode)
      elif op == 5:
        self.jump_if_true(mode)
      elif op == 6:
        self.jump_if_false(mode)
      elif op == 7:
        self.less_than(mode)
      elif op == 8:
        self.equals(mode)
      elif op == 9:
        self.offset(mode)
      elif op == 99:
        return None
