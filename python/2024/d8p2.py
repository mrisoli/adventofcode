from itertools import combinations,groupby
from operator import itemgetter as ig
from utils import coords

f = coords(8, regex=r'\.\d\w')
groups = sorted([[k,v] for k, v in f.items() if v != '.'], key=ig(1))
groups = groupby(groups, key=ig(1))
groups = {k: list(map(ig(0), v)) for k, v in groups}
nodes = set()
for g in groups.values():
    for p1, p2 in combinations(g, 2):
        nodes.add(p1)
        nodes.add(p2)
        d = p2 - p1
        node = p1 - d
        while node in f.keys():
            nodes.add(node)
            node -= d
        node = p2 + d
        while node in f.keys():
            nodes.add(node)
            node += d
print(len(nodes))
