from utils import int_row

p1,p2 = int_row(21)
s1,s2,c,d = 0,0,0,1

def inc(x):
    return x + 1 if x + 1 <= 100 else 1

def run(p, x, c):
    t = 0
    for _ in range(3):
        t += x
        x = inc(x)
        c += 1
    p = p + t
    while p > 10:
        p -= 10
    return p,x,c

while True:
    p1,d, c = run(p1, d, c)
    s1 += p1
    if max(s1,s2) >= 1000:
        break
    p2,d, c = run(p2, d, c)
    s2 += p2
    if max(s1,s2) >= 1000:
        break
print(c * min(s1,s2))
