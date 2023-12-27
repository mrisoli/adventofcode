from operator import itemgetter
from d18 import make,solve

z = make()
z = map(itemgetter(0), z)
print(solve(z))
