from math import prod

def crt(n, a):
    p = prod(n)
    total = sum(y * pow(p // x, -1, x) * (p // x) for x, y in zip(n, a))
    return total % p

f = open('p.in')
b = f.read().splitlines()[1]
b = [(int(x), int(x) - i) for i,x in enumerate(b.split(',')) if x != 'x']
print(crt([x[0] for x in b], [x[1] for x in b]))
