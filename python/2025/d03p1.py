from utils import int_grid

def joltage(digits):
    p = max(digits[0:-1])
    return (p * 10) + max(digits[(digits.index(p) + 1):])

print(sum(map(joltage, int_grid(3))))
