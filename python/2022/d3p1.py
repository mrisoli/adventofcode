from utils import str_list
from d3 import priority

l = list(map(lambda s: (s[:len(s)//2], s[len(s)//2:]), str_list(3)))
print(sum(map(priority, l)))
