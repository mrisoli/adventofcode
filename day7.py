from itertools import permutations
from intcode import Intcode

def solve(a):
  os = []
  for settings in permutations(range(5)):
    intcs = [Intcode(a) for _ in range(5)]
    out = 0
    for intc, setting in zip(intcs, settings):
      intc.run([setting, out])
      out = intc.o
    os.append(out)

  return max(os)

def loop(a):
  os = []
  for settings in permutations(range(5)):
    intcs = [Intcode(a) for _ in range(5)]
    out = 0
    for intc, setting in zip(intcs, settings):
      intc.run([setting, out])
      out = intc.o
    while out:
      for intc in intcs:
        intc.run([setting, out])
        out = intc.o

      os.append(out)

  return max(os)

a = list(map(int,open("day7input.txt").read().split(",")))
print(solve(a))
print('---')
print(loop(a))
