from common import graph

def count_colors(g, color):
    c = 0
    for v in g.vertices.keys():
        edges = g.vertices[v].get_edge_names()
        if color in edges:
            c += 1
        else:
            visited = set(v)
            q = list.copy(edges)
            while q:
                vv = q.pop()
                if vv not in visited:
                    visited.add(vv)
                    edges = g.vertices[vv].get_edge_names()
                    if color in edges:
                        c += 1
                        break
                    q.extend(edges)
    return c
with open('puzzle.in', 'r') as f:
    g = graph.Graph(f.read().splitlines())
    print(count_colors(g, 'shiny gold'))
