with open("i.in") as f:
    d = [int(x) for x in f.read().split()]
    t = 0
    w = []
    for i in range(len(d) - 2):
        w.append(sum(d[i:i + 3]))
    for i in range(len(w) - 1):
        if w[i + 1] > w[i]:
            t += 1
    print(t)
