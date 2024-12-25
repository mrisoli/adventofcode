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

print(sum(map(solve,f)))
