from d19 import Solver, Parts
from utils import obj_list

rules, _ = obj_list(19)

parts = Parts(
    x=range(1, 4001),
    m=range(1, 4001),
    a=range(1, 4001),
    s=range(1, 4001),
)

s = Solver(rules)

print(s.solve(parts, 'in'))
