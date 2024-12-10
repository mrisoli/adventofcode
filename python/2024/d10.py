NEIGHBORS = [-1, -1j, 1, 1j]

def get_neighbors(f, k):
    v = f[k]
    return [k + kk for kk in NEIGHBORS if k + kk in f and f[k + kk] == v + 1]

def score(f,k):
    visit = get_neighbors(f, k)
    t = []
    while len(visit) > 0:
        current = visit.pop(0)
        if f[current] == 9:
            t.append(current)
        else:
            visit += get_neighbors(f, current)
    return t
