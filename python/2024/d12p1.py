from d12 import border, NEIGHBORS, solve

def perimeter(f, a, v):
    return sum([len(border(f, p, v)) for p in a])

solve(perimeter)
