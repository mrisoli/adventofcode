from math import atan2

def sats(a, i, j):
  sight = set()
  for ii in range(len(a)):
    for jj in range(len(a[i])):
      if a[ii][jj] == '#':
        ri = ii - i
        rj = jj - j
        if not atan2(ri, rj) in sight:
          sight.add(atan2(ri, rj))
  return len(sight)

def solve(a):
  return max([max([sats(a, i, j) for j in range(len(a[i])) if a[i][j] == '#']) for i in range(len(a))])

a = [list(i) for i in open("in10.txt").read().splitlines()]
print(solve(a))
