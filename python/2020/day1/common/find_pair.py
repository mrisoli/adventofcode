def find_pair(a, n):
    s = set()
    for i in a:
        if i in s:
            return ((n - i) * i)
        else:
            s.add(n - i)
    return None
