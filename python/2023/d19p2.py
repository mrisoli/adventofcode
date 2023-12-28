from d19 import gen_workflows, Workflow
from utils import obj_list

def combinations(ws: Workflow, key: str = 'in') -> int:
    for v,r in ws[key]:
        print(v,r)
    return 1

ws, _ = obj_list(19)
ws = gen_workflows(ws)
print(ws)
print(combinations(ws))
