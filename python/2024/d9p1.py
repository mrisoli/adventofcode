from utils import fopen

def checksum(d):
    return sum(i * v for i, v in enumerate(d) if isinstance(v, int))

s = fopen(9).read().strip()
disk = []
block_id = 0
for i in range(len(s)):
    d = int(s[i])
    if i % 2 == 0:
        disk += ([block_id] * d)
        block_id += 1
    else:
        disk += (['.'] * d)
rd = len(disk) - 1
for i in range(len(disk)):
    if all(x == '.' for x in disk[i:]):
        break
    if disk[i] == '.':
        while disk[rd] == '.':
            rd -= 1
        disk[i], disk[rd] = disk[rd], disk[i]
print(checksum(disk))
