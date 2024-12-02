from utils import rows_of_int

def safe(r):
    variation = [y - x for x,y in zip(r, r[1:])]
    if sum(x not in {1,2,3} for x in variation) <= 2 or sum(x not in {-1,-2,-3} for x in variation) <= 2:
        for i in range(len(r)):
            n = r[:i] + r[i+1:]
            v = [y - x for x,y in zip(n, n[1:])]
            if all(x in {1,2,3} for x in v) or all(x in {-1,-2,-3} for x in v):
                return True
    return False

print(sum(map(safe, rows_of_int(2))))
