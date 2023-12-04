from d4 import generate

def scoring(n):
    return int(2 ** (n - 1))

print(sum(map(scoring, generate().values())))
