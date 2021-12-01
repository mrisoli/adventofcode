with open("i.in") as f:
    d = [int(x) for x in f.read().split()]
    t = 0
    for i in range(len(d) - 1):
        if d[i + 1] > d[i]:
            t += 1
    print(t)
