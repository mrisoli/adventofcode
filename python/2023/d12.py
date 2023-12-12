from functools import lru_cache

def parse_line(line):
    springs, count = line.split(' ')
    return springs,tuple(map(int, count.split(',')))

@lru_cache
def place(s,c):
    if len(s) == 0:
        return 1 if len(c) == 0 else 0
    if s.startswith('.'):
        return place(s.strip('.'), c)
    if s.startswith('?'):
        return place(s.replace('?', '.', 1), c) + place(s.replace('?', '#', 1), c)
    if len(c) == 0 or len(s) < c[0] or'.' in s[:c[0]]:
        return 0
    if len(c) > 1:
        if (len(s) < c[0] + 1 or s[c[0]] == '#'):
            return 0
        return place(s[c[0] + 1:], c[1:])
    return place(s[c[0]:], c[1:])
