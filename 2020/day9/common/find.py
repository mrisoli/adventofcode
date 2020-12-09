def pair(a, n):
    s = set()
    for i in a:
        if i in s:
            return ((n - i) * i)
        else:
            s.add(n - i)
    return None

def invalid(a, p=25):
    for i in range(p, len(a)):
        if not pair(a[i-p:i], a[i]):
            ans = i
            break
    return ans
