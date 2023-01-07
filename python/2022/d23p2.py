from d23 import get_coords,rnd
f,m = get_coords()
i = 0
while True:
    i += 1
    nf = rnd(f,m)
    if nf == f:
        break
    f = nf
print(i)
