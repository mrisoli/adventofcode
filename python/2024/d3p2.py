import re
from utils import fopen
from d3 import solve

f = re.sub( r"don't\(\).*?($|do\(\))", '', fopen(3).read(), flags=re.DOTALL)
solve(f)
