def add(a, i, args, _v):
  a[a[i + 3]] = value(a, i + 1, args[0]) + value(a, i + 2, args[1])
  return (a, i + 4)

def multiply(a, i, args, _v):
  a[a[i + 3]] = value(a, i + 1, args[0]) * value(a, i + 2, args[1])
  return (a, i + 4)

def modify(a, i, args, v):
  a[a[i + 1]] = v
  return (a,i + 2)

def output(a, i, args, _v):
  print(value(a, i + 1, args[0]))
  return (a,i + 2)

def jump(a, i, args, c):
  if c:
    return (a, value(a, i + 2, args[1]))
  return (a, i + 3)

def jump_if_true(a, i, args, _v):
  return jump(a, i, args, value(a, i + 1, args[0]) != 0)

def jump_if_false(a, i, args, _v):
  return jump(a, i, args, value(a, i + 1, args[0]) == 0)

def ifc(a, i, args, c):
  if c:
    a[a[i + 3]] = 1
  else:
    a[a[i + 3]] = 0
  return (a, i + 4)

def less_than(a, i, args, _v):
  return ifc(a, i, args, value(a, i + 1, args[0]) < value(a, i + 2, args[1]))

def equals(a, i, args, _v):
  return ifc(a, i, args, value(a, i + 1, args[0]) == value(a, i + 2, args[1]))

def halt (a, i, _v):
  return (a,i)

def read_instruction(a, i, x):
  opcode = a[i] % 100
  st = str(a[i] // 100)
  while len(st) < 3:
    st = "0" + st
  return instructions[opcode](a, i, list(map(int, reversed(st))), x)

def value(a, i, n):
  if n == 0:
    return a[a[i]]
  else:
    return a[i]

instructions = {
    1: add,
    2: multiply,
    3: modify,
    4: output,
    5: jump_if_true,
    6: jump_if_false,
    7: less_than,
    8: equals,
    99: halt  }

def solve(a, x):
  i = 0
  while a[i] != 99:
    a, i = read_instruction(a, i, x)

solve(list(map(int,open("day5input.txt").read().split(","))), 1)
print('---')
solve(list(map(int,open("day5input.txt").read().split(","))), 5)
