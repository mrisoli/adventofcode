f = open('p.in')
[t, b] = f.read().splitlines()
b = [int(n) for n in b.split(',') if n != 'x']
t = int(t)
c = min([ (n, n - (t % n)) for n in b], key = lambda x: x[1])
print(c[0] * c[1])
