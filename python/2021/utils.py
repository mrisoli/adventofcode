def int_list(path):
    with open(path) as f:
        l = [int(x) for x in f.read().split()]
    return l
