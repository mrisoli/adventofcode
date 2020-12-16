def solve(total):
    f = open('p.in')
    n = list(map(int, f.read().split(',')))
    s = [None] * 50000000
    last = 0
    idx = 1
    for v in n:
        s[v] = {'last': idx, 'recent': idx}
        last = v
        idx += 1
    while idx <= total:
        last = s[last]['last'] - s[last]['recent']
        if s[last]:
            s[last] = {'last': idx, 'recent': s[last]['last']}
        else:
            s[last] = {'last': idx, 'recent': idx}
        idx += 1

    print(last)
