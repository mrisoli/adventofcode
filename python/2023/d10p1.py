from utils import coords

def parse():
    return dict(coords(10, '|-LJ7FS'))

def neighbors(g, n):
    v = g[n]
    match(v):
        case 'S':
            return [n - 1, n + 1, n + 1j, n - 1j]
        case 'L':
            return [n - 1, n + 1j]
        case 'J':
            return [n - 1, n - 1j]
        case '7':
            return [n + 1, n - 1j]
        case 'F':
            return [n + 1, n + 1j]
        case '|':
            return [n + 1, n - 1]
        case '-':
            return [n + 1j, n - 1j]

def is_reachable(g, n, m):
    if m not in g:
        return False
    return n in neighbors(g, m)

def bfs(g, s):
    v,q,d = set({s}),[s],{s:0}
    while q:
        n = q.pop(0)
        for m in neighbors(g, n):
            if is_reachable(g, n, m) and m not in v:
                d[m] = d[n] + 1
                v.add(m)
                q.append(m)
    return d

g = parse()
s = list(g.keys())[list(g.values()).index('S')]
r = bfs(g, s)
print(max(r.values()))
