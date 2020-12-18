from common import pn
f = open('p.in')
print(sum([pn.solve(s, False) for s in f.read().splitlines()]))
