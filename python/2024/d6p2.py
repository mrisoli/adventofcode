from d6 import run, setup, solve

def find_cycle(f,s, el):
    p = -1
    f[el] = '#'
    c = set()
    while s in f:
        t = (s, p)
        if t in c:
            return True
        c.add(t)
        s,p = run(f, s, p)
    return False

f, s = setup()
print(sum(find_cycle(f.copy(), s, el) for el in solve(f, s)))
