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
        node = p1 - ((p2 - p1))
        if node in f.keys():
            nodes.add(node)
        node = p2 - ((p1 - p2))
        if node in f.keys():
            nodes.add(node)
print(len(nodes))
