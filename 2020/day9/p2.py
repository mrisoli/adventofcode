from common import find

with open('puzzle.in', 'r') as f:
    a = list(map(int, f.readlines()))
    i = find.invalid(a)
    l,j = 0,1
    while j < i:
        sub = a[l:j]
        s = sum(sub)
        if s == a[i]:
            print(min(sub) + max(sub))
            break
        elif s > a[i]:
            l += 1
        else:
            j += 1
