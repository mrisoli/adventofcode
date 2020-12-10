with open('puzzle.in', 'r') as f:
    l = list(map(int, f.readlines()))
    list.sort(l)
    l.insert(0, 0)
    l.append(l[-1] + 3)
    m = l[-1]
    s = set(l)
    a = [0] * (m + 1)
    a[0] = 1
    for i in l:
        for j in range(1,4):
            if i + j < len(a):
                a[i + j] += a[i]
    print(a[m])
