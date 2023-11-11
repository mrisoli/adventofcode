from itertools import permutations
from operator import lt, gt
from utils import str_list

def make_graph():
    f = str_list(9)
    m = {}
    for l in f:
        p,d = l.split(' = ')
        s,f = p.split(' to ')
        if s not in m:
            m[s] = {}
        if f not in m:
            m[f] = {}
        m[s][f] = int(d)
        m[f][s] = int(d)
    return m

def calculate_total_distance(path, distances):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distances[path[i]][path[i + 1]]
    return total_distance

def find_path(ln):
    op,base = (lt, 'inf') if ln == 'lt' else (gt,'-inf')
    graph = make_graph()
    nodes = list(graph.keys())
    all_paths = list(permutations(nodes))
    shortest_path = None
    min_distance = float(base)

    for path in all_paths:
        distance = calculate_total_distance(path, graph)
        if op(distance, min_distance):
            min_distance = distance
            shortest_path = path

    return min_distance
