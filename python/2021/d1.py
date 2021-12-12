from utils import int_list

def solve(n):
    d = int_list(1)
    print(sum(map(int.__gt__, d[(n):], d)))
