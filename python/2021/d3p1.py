from utils import str_list
from collections import Counter

g = [Counter(n).most_common(1)[0][0] for n in zip(*str_list(3))]
e = ''.join(['1' if i == '0' else '0' for i in g])
print(int(''.join(g),2) * int(e,2))
