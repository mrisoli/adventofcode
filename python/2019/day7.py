from itertools import permutations
from intcode import Intcode

def solve(a):
  os = []
  for settings in permutations(range(5)):
    intcs = [Intcode(a) for _ in range(5)]
    out = 0
    for intc, setting in zip(intcs, settings):
      intc.input([setting, out]).run()
      out = intc.o
    os.append(out)

  return max(os)

def loop(a):
  os = []
  for settings in permutations(range(5, 10)):
    intcs = [Intcode(a) for _ in range(5)]
    out = 0
    for intc, setting in zip(intcs, settings):
      out = intc.input([setting, out]).run()
    while out:
      for intc in intcs:
        out = intc.input([out]).run()
      if out:
        os.append(out)

  return max(os)

a = list(map(int,open("day7input.txt").read().split(",")))
print(solve(a))
print('---')
print(loop(a))
