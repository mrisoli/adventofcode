from common import find

with open('puzzle.in', 'r') as f:
    a = list(map(int, f.readlines()))
    i = find.invalid(a)
    print(a[i])
