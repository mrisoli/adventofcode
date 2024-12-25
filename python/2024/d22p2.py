from itertools import pairwise
from collections import defaultdict
from utils import int_list

def mix_and_prune(n):
    n ^= n << 6 & 0xFFFFFF
    n ^= n >> 5 & 0xFFFFFF
    return n ^ n << 11 & 0xFFFFFF

def solve(n):
    for i in range(2000):
        n = mix_and_prune(n)
    return n

f = int_list(22)

a = defaultdict(int)
for n in f:
    nums = [n] + [n := mix_and_prune(n) for _ in range(2000)]

    diffs = [b%10-a%10 for a,b in pairwise(nums)]

    seen = set()
    for i in range(len(nums)-4):
        pat = tuple(diffs[i:i+4])
        if pat not in seen:
            a[pat] += nums[i+4] % 10
            seen.add(pat)

print(max(a.values()))
