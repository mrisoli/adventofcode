with open('puzzle.in', 'r') as f:
    l = [0] + list(map(int, f.readlines()))
    list.sort(l)
    l.append(l[-1] + 3)
    a = [1] + ([0] * (l[-1] + 4))
    for i in l:
        for j in range(1,4):
            a[i + j] += a[i]
    print(a[l[-1]])
