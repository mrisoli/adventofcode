from utils import str_list
from collections import Counter

l = str_list(3)

def r(ty=0, o=l, i=0):
    if len(o) == 1:
        return int(o[0],2)
    m = Counter([r for r in zip(*o)][i]).most_common(2)
    s = '1' if ty == 0 else '0'
    e = s if m[0][1] == m[1][1] else m[ty][0]
    return r(ty, [f for f in o if f[i] == e], i + 1)

print(r() * r(1))
