from utils import str_list
from collections import Counter

l = str_list(3)

def rt(o, ty):
    s = 0 if ty == '1' else 1
    for i in range(len(l[0])):
        tt = [list(r) for r in zip(*o)]
        n = tt[i]
        c = Counter(n)
        mc = c.most_common(2)
        if mc[0][1] == mc[1][1]:
            o = [f for f in o if f[i] == ty]
        else:
            o = [f for f in o if f[i] == mc[s][0]]
        if len(o) == 1:
            o = int(o[0],2)
            break
    return o

print(rt(l[:], '1') * rt(l[:], '0'))
