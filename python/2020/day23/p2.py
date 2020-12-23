from common import ll
n = list(map(int, '496138527'))
n += [e for e in range(10, 1000001)]
(h, index) = ll.make(n)

c = ll.run(h, index, 10000000, 1000000)
c = index[1]
print(c.next.data  * c.next.next.data)
