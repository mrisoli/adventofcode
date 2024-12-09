from utils import fopen

def checksum(d):
    s = 0
    i = 0
    for el in d:
        for v in el:
            if isinstance(v, int):
                s += i * int(v)
            i += 1
    return s

s = fopen(9).read().strip()
disk = []
block_id = 0
for i in range(len(s)):
    d = int(s[i])
    if i % 2 == 0:
        disk.append([block_id] * d)
        block_id += 1
    else:
        disk.append(['.'] * d)
for i,rd in reversed(list(enumerate(disk))[0::2]):
    for j,arr in enumerate(disk):
        if j >= i:
            break
        if len(rd) <= arr.count('.'):
            dot = arr.index('.')
            for dd in range(len(rd)):
                arr[dot] = rd[0]
                dot += 1
            disk[i] = ['.'] * len(rd)
            break
print(checksum(disk))
