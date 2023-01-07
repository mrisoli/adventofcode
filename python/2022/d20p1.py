from collections import deque
from utils import int_list

l = int_list(20)
d = deque(l)
while l:
    v = l.pop(0)
    d.rotate(-d.index(v))
    d.popleft()
    d.insert(v % len(d), v)
d.rotate(-d.index(0))
print(sum(d[(i * 1000) % len(d)] for i in range(1,4)))
