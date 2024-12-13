from utils import obj_list
from d13 import Machine

print(sum(Machine(m, enlarge=True).solve() for m in obj_list(13)))
