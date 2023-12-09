from utils import rows_of_int

def gen(r):
    return [b - a for a,b in zip(r, r[1:])]

def seq(r):
    return r[-1] + seq(gen(r)) if any(r) else r[-1]

def solve(rev=False):
    r = rows_of_int(9)
    if rev:
        r = map(lambda x: list(reversed(x)), r)
    return sum(map(seq, r))
