class Intcode:
  def __init__(self, a):
    self.a = a[:]
    self.i = 0
    self.base = 0
    self.inputs = []
    self.o = None

  def add(self, args):
    self.a[self.value(self.i + 3, args[2], True)] = self.value(self.i + 1, args[0]) + self.value(self.i + 2, args[1])
    self.i += 4

  def multiply(self, args):
    self.a[self.value(self.i + 3, args[2], True)] = self.value(self.i + 1, args[0]) * self.value(self.i + 2, args[1])
    self.i += 4

  def modify(self, args):
    self.a[self.value(self.i + 1, args[0], True)] = self.inputs.pop(0)
    self.i += 2

  def output(self, args):
    val = self.value(self.i + 1, args[0])
    self.o = val
    self.i += 2
    print(val)
    return self.o

  def jump(self, args, c):
    if c:
      self.i = self.value(self.i + 2, args[1])
    else:
      self.i += 3

  def jump_if_true(self, args):
    self.jump(args, self.value(self.i + 1, args[0]) != 0)

  def jump_if_false(self, args):
    self.jump(args, self.value(self.i + 1, args[0]) == 0)

  def ifc(self, args, c):
    if c:
      self.a[self.a[self.i + 3]] = 1
    else:
      self.a[self.a[self.i + 3]] = 0
    self.i += 4

  def less_than(self, args):
    self.ifc(args, self.value(self.i + 1, args[0]) < self.value(self.i + 2, args[1]))

  def equals(self, args):
    self.ifc(args, self.value(self.i + 1, args[0]) == self.value(self.i + 2, args[1]))

  def offset(self, args):
    self.base += self.value(self.i + 1, args[0])
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

  def get_args(self):
    st = str(self.a[self.i] // 100)
    while len(st) < 3:
      st = "0" + st
    return list(map(int, reversed(st)))

  def run(self):
    while True:
      op = self.get_opcode()
      args = self.get_args()
      if op == 1:
        self.add(args)
      elif op == 2:
        self.multiply(args)
      elif op == 3:
        self.modify(args)
      elif op == 4:
        return self.output(args)
      elif op == 5:
        self.jump_if_true(args)
      elif op == 6:
        self.jump_if_false(args)
      elif op == 7:
        self.less_than(args)
      elif op == 8:
        self.equals(args)
      elif op == 9:
        self.offset(args)
      elif op == 99:
        return None
