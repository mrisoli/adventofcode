class Intcode:
  def __init__(self, a, inputs):
    self.a = a[:]
    self.inputs = inputs
    self.i = 0
    self.o = None
    self.instructions = {
        1: self.add,
        2: self.multiply,
        3: self.modify,
        4: self.output,
        5: self.jump_if_true,
        6: self.jump_if_false,
        7: self.less_than,
        8: self.equals,
        99: self.halt  }

  def add(self, args):
    self.a[self.a[self.i + 3]] = self.value(self.i + 1, args[0]) + self.value(self.i + 2, args[1])
    self.i += 4

  def multiply(self, args):
    self.a[self.a[self.i + 3]] = self.value(self.i + 1, args[0]) * self.value(self.i + 2, args[1])
    self.i += 4

  def modify(self, _args):
    self.a[self.a[self.i + 1]] = self.inputs.pop(0)
    self.i += 2

  def output(self, args):
    val = self.value(self.i + 1, args[0])
    self.o = val
    print(val)
    self.i += 2

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

  def halt(self, _args):
    return self.a

  def read_instruction(self):
    opcode = self.get_opcode() % 100
    st = str(self.get_opcode() // 100)
    while len(st) < 3:
      st = "0" + st
    return self.instructions[opcode](list(map(int, reversed(st))))

  def value(self, i, n):
    if n == 0:
      return self.a[self.a[i]]
    else:
      return self.a[i]

  def get_opcode(self):
    return self.a[self.i]
