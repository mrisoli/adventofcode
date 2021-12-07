from utils import int_row

def solve(n):
    s = [0] * 9
    for p in int_row(6):
        s[p] += 1
    for i in range(n):
        n,s = s[0],s[1:]
        s[6] += n
        s.append(n)

    print(sum(s))
