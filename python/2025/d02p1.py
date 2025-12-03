from utils import fopen

def is_invalid(v):
    s1 = str(v)
    s2, s3 = s1[:len(s1)//2 + len(s1)%2], s1[len(s1)//2 + len(s1)%2:]
    return s2 == s3
l = fopen(2).readlines()
l = [x for x in ''.join(l).split(',') if x]
s = 0
for line in l:
    start,end = [int(x) for x in line.split('-')]
    for v in range(start, end + 1):
        if is_invalid(v):
            s += v
print(s)
