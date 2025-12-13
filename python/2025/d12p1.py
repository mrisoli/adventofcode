from utils import str_list
import re
a = 0
for l in str_list(12)[30:]:
    w,h, *n = map(int, re.findall(r'\d+', l))
    a += w//3 * h//3 >= sum(n)
print(a)
