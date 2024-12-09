from itertools import combinations,groupby
from operator import itemgetter as ig
from utils import coords

class Group:
    def __init__(self, h = False):
        self.h = h
        self.f = coords(8, regex=r'\.\d\w')
        self.groups = sorted([[k,v] for k, v in self.f.items() if v != '.'], key=ig(1))
        self.groups = groupby(self.groups, key=ig(1))
        self.groups = {k: list(map(ig(0), v)) for k, v in self.groups}

    def solve(self):
        nodes = set()
        for g in self.groups.values():
            for p1, p2 in combinations(g, 2):
                if self.h:
                    nodes.add(p1)
                    nodes.add(p2)
                d = p2 - p1
                node = p1 - d
                repeat = True
                while repeat and node in self.f.keys():
                    nodes.add(node)
                    node -= d
                    if not self.h:
                        repeat = False
                node = p2 + d
                repeat = True
                while repeat and node in self.f.keys():
                    nodes.add(node)
                    node += d
                    if not self.h:
                        repeat = False
        return len(nodes)
