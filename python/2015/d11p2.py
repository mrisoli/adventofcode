from d11 import check, increment, get_seed
s = get_seed()
for i in range(2):
    s = increment(s)
    while not check(s):
        s = increment(s)
print(''.join(map(chr, s)))
