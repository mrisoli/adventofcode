import re

vp = re.compile(r'(?P<v>\w+\s\w+) bags contain')
ep = re.compile(r'(?P<d>\d+)\s(?P<n>\w+\s\w+)\sbags?(,\s)?')

class Edge:
    def __init__(self, n, name):
        self.n = n
        self.name = name

class Vertex:
    def __init__(self, name, edges):
        self.edges = dict()
        self.name = name
        for e in edges:
            d = int(e['d'])
            self.edges[e['n']] = Edge(d, e['n'])

    def get_edge_names(self):
        return [e for e in self.edges.keys()]

    def get_bags_sum(self):
        return sum([self.edges[e].n for e in self.edges])

class Graph:
    def __init__(self, l):
        self.vertices = dict()
        for s in l:
            name = re.match(vp, s).group('v')
            edges = [er.groupdict() for er in re.finditer(ep, s)]
            self.vertices[name] = Vertex(name, edges)

    def count_colors(self, color):
        c = 0
        for v in self.vertices.keys():
            edges = self.vertices[v].get_edge_names()
            if color in set(edges):
                c += 1
            else:
                visited = set(v)
                q = list.copy(edges)
                while(len(q) > 0):
                    vv = q.pop()
                    if vv not in visited:
                        visited.add(vv)
                        edges = self.vertices[vv].get_edge_names()
                        if color in set(edges):
                            c += 1
                            break
                        q.extend(edges)
        return c

    def count_bags(self, color):
        v = self.vertices[color]
        c = v.get_bags_sum()
        for name in v.edges:
            t = self.vertices[color].edges[name].n
            c += (t * self.count_bags(name))
        return c
