from functools import lru_cache


with open('puzzle.in', 'r') as f:
    l = list(map(int, f.readlines()))
    list.sort(l)
    l.insert(0, 0)
    l.append(l[-1] + 3)
    m = l[-1]
    s = set(l)

@lru_cache(maxsize=len(l))
def ways(i):
    if i == m:
        return 1
    if i not in s:
        return 0
    return ways(i + 1) + ways(i + 2) + ways(i + 3)

print(ways(0))
