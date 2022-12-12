from utils import str_list

class Grid:
    def __init__(self):
        self.se = {'E': 'z', 'S': 'a'}
        g = str_list(12)
        self.grid = {}
        for i in range(len(g)):
            for j in range(len(g[i])):
                self.grid[(i,j)] = g[i][j]
                if g[i][j] == 'S':
                    self.start = (i,j)

    def cv(self, v):
        return self.se[v] if v in self.se else v

    def movable(self, c,p):
        return ord(self.cv(self.grid[c])) + 1 >= ord(self.cv(self.grid[p]))

    def neighbours(self, p):
        i, j = p
        return list(filter(lambda v: v in self.grid, [(i - 1, j),(i, j - 1),(i, j + 1),(i + 1, j)]))

    def run(self, start=None):
        if not start:
            start = self.start
        q = [start]
        dist = {start: 0}
        visited = set()
        while q:
            c = q.pop(0)
            visited.add(c)
            if self.grid[c] == 'E':
                return dist[c]
            for p in self.neighbours(c):
                if p not in visited and self.movable(c,p) and p not in q:
                    q.append(p)
                    dist[p] = min(dist[p], dist[c] + 1) if p in dist else dist[c] + 1
        return None
