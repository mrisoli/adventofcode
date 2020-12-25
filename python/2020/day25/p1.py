r = 20201227
def get_loop_size(n):
    v = 1
    loop = 0
    while v != n:
        loop += 1
        v = (v * 7) % r
    return loop

[pcard, pdoor] = list(map(int, open('p.in').read().splitlines()))
cloop = get_loop_size(pcard)
dloop = get_loop_size(pdoor)
a = 1
for _ in range(cloop):
    a = (a * pdoor) % r

print(a)
