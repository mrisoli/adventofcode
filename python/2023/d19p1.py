import re
from d19 import gen_workflows, Workflow
from utils import obj_list

def gen_parts(parts: str) -> [[str]]:
    return [[*map(int, re.findall(r'\d+', p))] for p in parts.split('\n')]

def check(part: [str], workflows: Workflow) -> bool:
    x,m,a,s = part
    c = 'in'
    while True:
        for v,t in workflows[c]:
            if eval(v):
                if t == 'A':
                    return True
                if t == 'R':
                    return False
                c = t
                break

w,p = obj_list(19)
w = gen_workflows(w)
print(sum(map(sum, ([p for p in gen_parts(p) if check(p, w)]))))
