from utils import int_grid
from d9 import get_neighbors

g,t = int_grid(9),0
for i in range(len(g)):
    for j in range(len(g[i])):
        v,n = g[i][j], get_neighbors(g, i, j)
        if all(map(lambda x: x > v, n)):
            t += v + 1
print(t)
