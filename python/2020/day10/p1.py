with open('puzzle.in', 'r') as f:
    l = list(map(int, f.readlines()))
    list.sort(l)
    c = {1: 0, 3: 0}
    l.insert(0, 0)
    l.append(l[-1] + 3)
    for x,y in zip(l, l[1:]):
        c[y - x] += 1
    print(c[1] * c[3])
