from utils import int_list

l = [x * 811589153 for x in int_list(20)]
idx = list(range(len(l)))

for i in idx * 10:
    idx.pop(j := idx.index(i))
    idx.insert((j+l[i]) % len(idx), i)

z = idx.index(l.index(0))
print(sum(l[idx[(z + (p * 1000)) % len(l)]] for p in range(1,4)))
