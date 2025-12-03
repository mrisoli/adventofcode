from utils import fopen

pos = 50
count = 0
for line in fopen(1):
    sign = {'L': -1, 'R': 1}[line[0]]
    step = int(line[1:])

    prev = pos
    pos += step * sign

    prev_lo = prev // 100
    curr_lo = pos // 100
    prev_hi = (prev - 1) // 100
    curr_hi = (pos - 1) // 100

    count += abs(prev_lo - curr_lo) + abs(prev_hi - curr_hi)
print(count // 2)
