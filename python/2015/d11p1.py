from d11 import check, increment, get_seed
s = get_seed()
while not check(s):
    s = increment(s)
print(''.join(map(chr, s)))
