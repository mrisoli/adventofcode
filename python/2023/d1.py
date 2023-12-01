def two_digits(l):
    l = [[x for x in v if x.isdigit()] for v in l]
    l = [int(v[0] + v[-1]) for v in l]
    print(sum(l))
