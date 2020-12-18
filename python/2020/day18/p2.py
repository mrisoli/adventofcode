from common import pn
f = open('p.in')
print(sum([pn.solve(s, True) for s in f.read().splitlines()]))
