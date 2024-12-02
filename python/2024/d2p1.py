from utils import rows_of_int

def safe(r):
    variation = [y - x for x,y in zip(r, r[1:])]
    return all(x in {1,2,3} for x in variation) or all(x in {-1,-2,-3} for x in variation)

print(sum(map(safe, rows_of_int(2))))
