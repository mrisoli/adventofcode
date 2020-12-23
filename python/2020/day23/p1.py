from common import ll
n = list(map(int, '496138527'))
(h, d) = ll.make(n)

c = ll.run(h, d, 100, 9)
while c.data != 1:
    c = c.next
s = ''
while c.next.data != 1:
    c = c.next
    s += str(c.data)
print(s)
