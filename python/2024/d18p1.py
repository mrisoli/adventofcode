import heapq
from utils import points_list
from coordinates import dijkstra

f = points_list(18)
f = f[:1024]
mx = int(max(map(lambda x: x.real, f)))
my = int(max(map(lambda y: y.imag, f)))
start = 0
end = mx + my * 1j
shortest_path_length = dijkstra((mx, my), f, start, end)
print(shortest_path_length)
