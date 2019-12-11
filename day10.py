from intcode import Intcode

def in_sight(a, i, j, s, r):
  for (ii, jj, rr) in s:
    if (r/rr) * ii == i and (r/rr) * jj == j:
      return False
  return True

def is_in_range(i, j, l):
  return  i >= 0 and i < l and j >= 0 and j < l

def sats(a, i, j):
  sight = set()
  visited = set({(i, j)})
  for r in range(1, len(a)):
    for ri in range(-r,r + 1):
      for rj in range(-r,r + 1):
        ii, jj = i + ri, j + rj
        if is_in_range(ii, jj, len(a)):
          if a[ii][jj] == '#' and (ii,jj) not in visited:
            visited.add((ii, jj))
            if in_sight(a, ri, rj, sight, r):
              sight.add((ri, rj, r))
  return len(sight)
def solve(a):
  ans = ({-1, -1}, 0)
  for i in range(len(a)):
    for j in range(len(a[i])):
      if a[i][j] == '#':
        s = sats(a, i, j)
        if s > ans[1]:
          ans = ({i, j}, s)
  return ans

a = [list(i) for i in open("in10.txt").read().splitlines()]
print(solve(a))
