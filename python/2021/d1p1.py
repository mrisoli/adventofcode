from utils import int_list
d = int_list('i1.in')
t = sum(map(int.__gt__, d[1:], d))
print(t)
