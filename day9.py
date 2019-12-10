from intcode import Intcode

def solve(a, i):
  intc = Intcode(a)
  intc.input([i])
  intc.run()
  return intc.o

a = list(map(int,open("in9.txt").read().split(",")))
a += [0 for _ in range(10000)]
print(solve(a, 1))
print('---')
print(solve(a, 2))
