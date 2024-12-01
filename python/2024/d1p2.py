from utils import rows_of_int
from collections import Counter
left, right = zip(*rows_of_int(1))
right = Counter(right)
print(sum(l * right[l] for l in left))
