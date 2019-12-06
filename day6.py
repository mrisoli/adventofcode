def mapOrbits(f):
  os = {}
  for i in f:
    [c, o] = i.split(')')
    o = o.rstrip()
    if c in os:
      os[c].append(o)
    else:
      os[c] = [o]
  return os

def traverse(os):
  v,q, path = {}, [("COM",None)], {}
  while q:
    (n, p) = q.pop(0)
    if n not in v.keys():
      if p is None:
        v[n] = 0
        path[n] = []
      else:
        v[n] = v[p] + 1
        cp = path[p][:]
        cp.append(p)
        path[n] = cp
      if n in os:
        for i in os[n]:
          q.append((i, n))
  return (v, path)

def find_path(path, orb):
  i=j=0
  y,s = path["YOU"], path["SAN"]
  return len(set(y).symmetric_difference(set(s)))


orbits = mapOrbits(open("day6input.txt").readlines())
(orb, path) = (traverse(orbits))
print(sum(orb.values()))
print(find_path(path, orb))
