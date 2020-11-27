def next_point(p,d):
  (x, y) = p
  if d == 'U':
    return (x, y + 1)
  elif d == 'D':
    return (x, y - 1)
  elif d == 'R':
    return (x + 1, y)
  elif d == 'L':
    return (x - 1, y)

def get_points(w):
  c, ps, l = (0,0), {}, 0
  for s in w:
    n = int(s[1:])
    for _ in range(n):
      l += 1
      c = next_point(c, s[0])
      if c not in ps:
        ps[c] = l
  return ps

[a,b] = [x.split(',') for x in (open("day3input.txt").read().splitlines())]

pa = get_points(a)
pb = get_points(b)

pi = set(pa.keys()) & set(pb.keys())
print(min([abs(x) + abs(y) for (x,y) in pi]))
print(min([pa[p] + pb[p] for p in pi]))
