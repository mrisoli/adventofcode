class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def make(l):
    head,tail = None, None
    index = [None] * (len(l) + 1)
    for o in l:
        n = Node(o)
        index[o] = n
        if not(head):
            tail = head = n
        else:
            tail.next = n
            tail = tail.next
    tail.next = head
    return (head, index)

def get_cup(x, r, mx):
    d = x - 1
    b = r
    rr = set()
    while b:
        rr.add(b.data)
        b = b.next
    while d in rr or d == 0:
        d -= 1
        if d <= 0:
            d = mx
    return d

def run(h, index, m, mx):
    c = h
    for i in range(m):
        x = c
        r = c.next
        c.next = c.next.next.next.next
        r.next.next.next = None
        d = get_cup(c.data, r, mx)
        c = index[d]
        b = c.next
        c.next = r
        while c.next:
            c = c.next
        c.next = b
        c = x.next
    return c
