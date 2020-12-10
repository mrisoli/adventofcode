with open('puzzle.in', 'r') as f:
    l = list(map(int, f.readlines()))
    list.sort(l)
    l.insert(0, 0)
    l.append(l[-1] + 3)
    a = [0] * (l[-1] + 4)
    a[0] = 1
    for i in l:
        for j in range(1,4):
            a[i + j] += a[i]
    print(a[l[-1]])
