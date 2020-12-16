from common import find_pair
with open('puzzle.in') as f:
        a = map(int, f.readlines())
        print(find_pair(a, 2020))
