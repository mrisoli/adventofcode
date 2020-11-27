from intcode import Intcode
def solve(a, x):
  intc = Intcode(a)
  intc.input([x])
  intc.run()
  while intc.o == 0:
    intc.run()
  print(intc.o)

a = list(map(int,open("day5input.txt").read().split(",")))
solve(a, 1)
print('---')
solve(a, 5)
