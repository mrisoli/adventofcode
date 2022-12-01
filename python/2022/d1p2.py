from d1 import get_list
from heapq import nlargest

print(sum(nlargest(3, get_list())))
