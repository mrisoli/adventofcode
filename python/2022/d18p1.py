from utils import int_tuples
from d18 import sides

f = int_tuples(18)
print(sum((s not in f) for c in f for s in sides(*c)))
