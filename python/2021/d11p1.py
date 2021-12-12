from utils import int_grid
from queue import Queue

g = int_grid(11)

def get_neighbors(g, i, j):
    neighbors = [
        (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
        (i + 1, j - 1), (i + 1, j + 1), (i + 1, j),
        (i, j - 1), (i, j + 1)
    ]
    return [(ix,jx) for ix, jx in neighbors if ix >= 0 and ix < len(g) and jx >= 0 and jx < len(g[i])]

t = 0
for _ in range(100):
    q = Queue()
    visited = set()
    for i in range(len(g)):
        for j in range(len(g[i])):
            g[i][j] += 1
            if g[i][j] > 9:
                g[i][j] = 9
                visited.add(tuple([i,j]))
                q.put(tuple([i,j]))
    while not q.empty():
        i,j = q.get()
        t += 1
        n = get_neighbors(g, i , j)
        for ix, jx in n:
            g[ix][jx] += 1
            if g[ix][jx] > 9 and (ix, jx) not in visited:
                visited.add(tuple([ix,jx]))
                q.put(tuple([ix,jx]))

    for i,j in visited:
        g[i][j] = 0
print(t)
