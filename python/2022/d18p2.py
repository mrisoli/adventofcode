from utils import int_tuples
from d18 import sides

f = int_tuples(18)
s = set()
q = [(-1,-1,-1)]
while q:
    h = q.pop()
    q += [v for v in (sides(*h) - f - s) if all(-1<= c <= 25 for c in v)]
    s.add(h)
print(sum((v in s) for c in f for v in sides(*c)))
