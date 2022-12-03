from utils import str_list
from d3 import priority

l = str_list(3)
l = [l[i:i+3] for i in range(0, len(l), 3)]
print(sum(map(priority, l)))
