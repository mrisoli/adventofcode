from utils import fopen

def solve(n):
    l = fopen(6).read().strip()
    for i in range(n,len(l)):
        if len(set(l[i - n:i])) == n:
            return i
