from utils import int_list

def solve(n):
    d = int_list('i1.in')
    t = sum(map(int.__gt__, d[(n):], d))
    print(t)
