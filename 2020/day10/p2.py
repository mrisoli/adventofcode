f = open('puzzle.in')
l = [0] + list(map(int, f.readlines()))
list.sort(l)
l.append(l[-1] + 3)
a = [1] + ([0] * (l[-1] + 4))
for i in l:
    a[i +1:i + 4] = [x + a[i] for x in a[i +1:i + 4]]
print(a[l[-1]])
