from math import atan2

def sats(a, i, j):
  sight = {}
  for ii in range(len(a)):
    for jj in range(len(a[i])):
      if a[ii][jj] == '#':
        ri = ii - i
        rj = jj - j
        h = hash(atan2(ri, rj))
        if not h in sight:
          sight[h] = [(ii, jj)]
        else:
          sight[h].append((ii, jj))
  return ((i, j), sight)

def map_visible(a):
  return [[sats(a, i, j) for j in range(len(a[i])) if a[i][j] == '#'] for i in range(len(a))]

def solve(a):
  v = map_visible(a)
  m = 0
  for i in v:
    for j in v:
      k = max(j, key=lambda x: len(x[1].keys()))
      s = len(k[1].keys())
      if s > m:
        m = s
  return m

a = [list(i) for i in open("in10.txt").read().splitlines()]
print(solve(a))
