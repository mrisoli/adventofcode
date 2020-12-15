def solve(total):
    f = open('p.in')
    n = list(map(int, f.read().split(',')))
    s = {}
    last = 0
    idx = 1
    for v in n:
        s[v] = {'last': idx, 'recent': idx}
        last = v
        idx += 1
    while idx <= total:
        last = s[last]['last'] - s[last]['recent']
        if last in s:
            s[last] = {'last': idx, 'recent': s[last]['last']}
        else:
            s[last] = {'last': idx, 'recent': idx}
        idx += 1

    print(last)
