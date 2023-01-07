from d23 import get_coords,rnd

f,m = get_coords()
for _ in range(10):
    f = rnd(f,m)

i = [x.real for x in f]
j = [x.imag for x in f]
a = int((max(i) - min(i) + 1) * (max(j) - min(j) + 1))
print(a - len(f))
