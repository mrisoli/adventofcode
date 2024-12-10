from d10 import score
from utils import coords
f = coords(10, parse=int, regex=r'\d')
print(sum(len(set(score(f,k))) for k,v in f.items() if v == 0))
