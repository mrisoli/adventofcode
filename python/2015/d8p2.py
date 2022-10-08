from utils import str_list
import re

def pr(s):
    hx = len(re.findall(r'\\x[0-9a-f][0-9a-f]', s))
    es = 2 * len(re.findall(r'\\(\"|\\)', s))
    return  4 + hx + es + len(s)

f = str_list(8)
print(sum(map(pr, f)) - sum(map(len, f)))
