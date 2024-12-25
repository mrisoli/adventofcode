from itertools import combinations
from utils import coords

grid = coords(20, tokens='.SE')
start, = (p for p in grid if grid[p] == 'S')


dist = {start: 0}
todo = [start]

for pos in todo:
    for new in pos-1, pos+1, pos-1j, pos+1j:
        if new in grid and new not in dist:
            dist[new] = dist[pos] + 1
            todo += [new]


a = 0

for (p,i), (q,j) in combinations(dist.items(), 2):
    d = abs((p-q).real) + abs((p-q).imag)
    if d == 2 and j-i-d >= 100: a += 1

print(a)

