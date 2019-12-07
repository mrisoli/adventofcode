from intcode import Intcode
def solve(a, x):
  intc = Intcode(a, [x])
  i = 0
  while intc.get_opcode() != 99:
    intc.read_instruction()

a = list(map(int,open("day5input.txt").read().split(",")))
solve(a, 1)
print('---')
solve(a, 5)
