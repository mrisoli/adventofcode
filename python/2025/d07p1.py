from utils import coords


def filter_row(f, c):
    points = set()
    for k,v in f.items():
        if k.real == c and v in '|S':
            points.add(k)
    return points

f = coords(7, tokens='S^')
bottom_row = round(max(map(lambda x: x.real, f)))
t = 0
g = dict(f)
print(g)
for c in range(0, bottom_row + 1):
    points = filter_row(f, c)
    for p in points:
        if p + 1 in g.keys() and g[p + 1] == '^':
            f[p + 1 -1j] = '|'
            f[p + 1 +1j] = '|'
            t += 1
        else:
            f[p + 1] = '|'
print(t)
