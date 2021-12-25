from d19 import align_scanners,dist
from itertools import combinations
def manhattan_distance(s, c):
    p1 = s.position
    p2 = c.position
    return dist(p1,p2)

scanners = align_scanners()
print(max([sum(dist(s.position,c.position)) for s,c in combinations(scanners, 2)]))
