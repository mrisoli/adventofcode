from intcode import Intcode

def solve(a):
  intc = Intcode(a)
  intc.input([1])
  intc.run()
  return intc.o

a = list(map(int,open("in9.txt").read().split(",")))
a += [0 for _ in range(1000)]
print(solve(a))
