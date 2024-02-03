from d20 import Solver

s = Solver()
for _ in range(1000):
    s.solve()
print(s.count())
