from math import ceil

class Tree:
    def __init__(self, value=None, branches=None):
        self.value = None
        self.left = None
        self.right = None
        if value is not None:
            self.value = value
        if branches and len(branches) == 2:
            left, right = branches
            if isinstance(left, int):
                self.left = Tree(value=left)
            elif left is not None:
                self.left = Tree(branches=left)
            if isinstance(right, int):
                self.right = Tree(value=right)
            elif right is not None:
                self.right = Tree(branches=right)


    def tprint(self):
        cl = [self]
        while cl:
            nl = list()
            for n in cl:
                s = '-' if n.value is None else n.value
                print(s, end=' '),
                if n.left: nl.append(n.left)
                if n.right: nl.append(n.right)
            print()
            cl = nl

    def split(self):
        l = self.value // 2
        r = ceil(self.value / 2)
        self.value = None
        self.left = Tree(value=l)
        self.right = Tree(value=r)

    def explode(self):
        self.value = 0
        t = (self.left.value, self.right.value)
        self.left = None
        self.right = None
        return t

    def update(self, v):
        t,e = next((i,x) for i,x in enumerate(v) if isinstance(x, tuple))
        l,r = e
        if t - 1 >= 0:
            v[t - 1].value += l
        if t + 1 < len(v):
            v[t + 1].value += r

    def traverse(self):
        current = self
        stack = []
        visited = []
        depth = 0
        found = None
        while True:
            if current is not None and found != current:
                if not found and current.value is None and depth == 4:
                    visited.append(current.explode())
                    found = current
                else:
                    stack.append(tuple([current, depth]))
                    depth += 1
                    current = current.left
            elif stack:
                current, d = stack.pop()
                depth = d + 1
                if current.value is not None:
                    visited.append(current)
                current = current.right
            else:
                break
        if found:
            self.update(visited)
        return found

    def find_split(self):
        if self.value is None:
            v = self.left.find_split()
            if v:
                return True
        if self.value is not None:
            if self.value >= 10:
                self.split()
                return True
            else:
                return False
        if self.value is None:
            v = self.right.find_split()
            if v:
                return True
        return False



    def parse(self):
        expl = self.traverse()
        spl = False
        while expl or spl:
            expl = self.traverse()
            if not expl:
                spl = self.find_split()
        return self


    def magnitude(self):
        if isinstance(self.value, int):
            return self.value
        return (3 * self.left.magnitude()) + (2 * self.right.magnitude())

    def combine_trees(self, r):
        t = Tree()
        t.left = self
        t.right = r
        t = t.parse()
        return t
