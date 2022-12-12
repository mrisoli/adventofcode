from utils import str_list
from d12 import Grid

g = Grid()

starts = filter(lambda v: g.grid[v] in 'aS', g.grid.keys())
print(min([d for d in map(lambda v: g.run(v), starts) if d]))
