from d12 import (is_small, solve)

def count(g, current, smallvisited={}):
    if current == 'end':
        return 1
    if is_small(current):
        if current not in smallvisited:
            smallvisited[current] = 1
        else:
            smallvisited[current] += 1
    visited = smallvisited.keys() if 2 in smallvisited.values() else set()
    tovisit = g[current] - visited
    if len(tovisit) == 0:
        return 0
    return sum([count(g, v, smallvisited.copy()) for v in tovisit])

solve(count)
