from utils import rows_of_int

def gen(r):
    return [b - a for a,b in zip(r, r[1:])]

def seq(op, p, r):
    return op(r[p], seq(op, p, gen(r))) if any(r) else r[p]

def solve(op, p):
    return sum(map(lambda x: seq(op, p, x), rows_of_int(9)))
