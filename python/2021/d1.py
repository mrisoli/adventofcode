from utils import int_list

def solve(n):
    d = int_list(1)
    t = sum(map(int.__gt__, d[(n):], d))
    print(t)
