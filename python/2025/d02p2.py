from utils import fopen

def is_invalid(num):
    s = str(num)
    length = len(s)

    # Try all possible pattern lengths from 1 to length//2
    for pattern_len in range(1, length // 2 + 1):
        if length % pattern_len == 0:
            pattern = s[:pattern_len]
            repetitions = length // pattern_len

            if pattern * repetitions == s:
                return True

    return False

l = fopen(2).readlines()
l = [x for x in ''.join(l).split(',') if x]
s = 0
for line in l:
    start,end = [int(x) for x in line.split('-')]
    for v in range(start, end + 1):
        if is_invalid(v):
            s += v
print(s)
