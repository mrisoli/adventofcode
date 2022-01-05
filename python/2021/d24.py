from utils import fopen

def run(p, op, cmp):
    l = [*fopen(24)]
    s = []
    for i in range(14):
        a = int(l[18 * i + 5].split()[-1])
        b = int(l[18 * i + 15].split()[-1])

        if a > 0: s+=[(i, b)]; continue
        j, b = s.pop()

        p = op(p, abs((a + b) * 10 ** (13- [i,j][cmp(a, -b)])))

    print(p)
