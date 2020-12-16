from math import prod

def crt(n):
    p = prod([x[0] for x in n])
    total = sum(y * pow(p // x, -1, x) * (p // x) for x, y in n)
    return total % p

f = open('p.in')
b = f.read().splitlines()[1]
b = [(int(x), int(x) - i) for i,x in enumerate(b.split(',')) if x != 'x']
print(crt(b))
