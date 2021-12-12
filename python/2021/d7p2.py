from utils import int_row

l = int_row(7)

def sqn(n):
    return (n * (n - 1)) // 2

print(min([sum([sqn(abs(x - y) + 1) for y in l]) for x in l]))
