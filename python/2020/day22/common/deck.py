def get_hands(f):
    p1 = list(map(int, f[1:len(f) // 2]))
    p2 = list(map(int, f[(len(f) // 2) + 2:]))
    return (p1, p2)

def score(p1,p2):
    d = p1 + p2
    d.reverse()
    return sum([(i + 1) * c for i,c in enumerate(d)])
