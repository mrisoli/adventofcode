from utils import str_list

def snafu_to_decimal(s):
    return sum(int('=-012'.index(c) - 2) * 5**i for i,c in enumerate(reversed(s)))

def decimal_to_snafu(n):
    s = []
    while n:
        r = ((n + 2) % 5)
        n = (n + 2) // 5
        s.append('=-012'[r])
    return ''.join(reversed(s))

print(decimal_to_snafu(sum(map(snafu_to_decimal, str_list(25)))))
