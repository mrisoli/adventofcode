from d24 import Blizzard,run

b = Blizzard()
s,g = -1, complex(b.h, b.w - 1)
print(run(b,s,g) + run(b,g,s) + run(b,s,g))
