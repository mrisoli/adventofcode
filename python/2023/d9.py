from utils import rows_of_int

def gen(r):
    return [b - a for a,b in zip(r, r[1:])]

def solve(seq):
    return sum(map(seq, rows_of_int(9)))
