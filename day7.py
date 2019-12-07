from itertools import permutations
import intcode

def solve(a):
  os = []
  for settings in permutations(range(5)):
    i = 0
    for s in settings:
      ar = a[:]
      while ar[i] != 99 or ar[i] != 4:
        ar, i = intcode.read_instruction(a, i, s)
      if ar[i] == 4:
        os.append(intcode.value(a, i + 1, a // 100))
  return max(os)

print(solve(list(map(int,open("day7input.txt").read().split(",")))))
