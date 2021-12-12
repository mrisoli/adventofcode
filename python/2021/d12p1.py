from d12 import (is_small, solve)

def count(g, current, smallvisited=set()):
    if current == 'end':
        return 1
    if is_small(current):
        smallvisited.add(current)
    tovisit = g[current] - smallvisited
    if len(tovisit) == 0:
        return 0
    return sum([count(g, v, smallvisited.copy()) for v in tovisit])

solve(count)
