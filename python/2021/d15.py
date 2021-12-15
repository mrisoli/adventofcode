def get_neighbors(g, v):
    i, j = v
    neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    return [(ix,jx) for ix, jx in neighbors if ix >= 0 and ix < len(g) and jx >= 0 and jx < len(g[i])]

def djikstra(g, target):
    current = (0,0)
    dist = {current: 0}
    visited = set()
    q = set()
    q.add(current)
    while len(q) > 0:
        v = min(q, key=lambda x: dist[x])
        q.remove(v)
        visited.add(v)
        if v == target:
            return dist[target]
        for n in get_neighbors(g, v):
            iv, jv = n
            d = dist[v] + g[iv][jv]
            if n not in dist or d < dist[n]:
                dist[n] = d
            if n not in visited:
                q.add(n)
    return dist[target]

def solve(g):
    print(djikstra(g, (len(g) - 1, len(g[len(g) - 1]) - 1)))
