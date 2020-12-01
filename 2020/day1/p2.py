from common import find_pair
with open('puzzle.in') as f:
        a = map(int, f.readlines())
        for i in range(len(a)):
            res = find_pair(a[i:], 2020 - a[i])
            if res:
                print(res * a[i])
                break
