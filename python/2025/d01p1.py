from d01 import make

def rotate(dial, r):
    d, v = r
    if d == 'R':
        return (dial + v) % 100
    return (dial - v) % 100

l = make()
dial,z = 50,0

for r in l:
    dial = rotate(dial, r)
    if dial == 0:
        z += 1
print(z)
