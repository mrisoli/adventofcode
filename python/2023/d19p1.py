import re
from d19 import Parts, Solver
from utils import obj_list

def sum_parts(parts: Parts) -> int:
    return parts.x[0] + parts.m[0] + parts.a[0] + parts.s[0]

def gen_parts(parts: str) -> [[str]]:
    parts = list(map(int, re.findall(r'\d+', parts)))
    x,m,a,s = parts
    return Parts(
        x=range(x, x+1),
        m=range(m, m+1),
        a=range(a, a+1),
        s=range(s, s+1),
    )

rules,parts = obj_list(19)
s = Solver(rules)

print(sum(map(sum_parts, filter(lambda p: s.solve(p, 'in'), map(gen_parts, parts.split('\n'))))))
