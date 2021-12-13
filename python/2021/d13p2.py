from d13 import (fold, read)
from operator import itemgetter

def print_code(c):
    max_x = max(c,key=itemgetter(0))[0]
    max_y = max(c,key=itemgetter(1))[1]
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x,y) in c:
                print('#', end='')
            else:
                print(' ', end='')
        print('')

c,i = read()
for ins in i:
    c = fold(c, ins)

print_code(c)
