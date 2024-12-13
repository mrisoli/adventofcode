from utils import coords

NEIGHBORS = [-1, -1j, 1, 1j]
def neighbors(f, k, v):
    return [k + n for n in NEIGHBORS if f.get(k + n) == v]

def area(f, p):
    k,v = p
    q = [k]
    a = set([k])
    while q:
        i = q.pop()
        n = neighbors(f, i, v)
        for p in n:
            if p not in a:
                q += n
                a.update(n)
    return a

def border(f, k, v):
    return [k + n for n in NEIGHBORS if f.get(k + n) != v ]

def solve(func):
    f = coords(12)
    s = 0
    while f.keys():
        i = next(iter(f.items()))
        a = area(f, i)
        p =  func(f, a, i[1])
        s += len(a) * p
        f = {k:v for k,v in f.items() if k not in a}
    print(s)
