import heapq

class Vertex:
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return False

    def __repr__(self):
        return str(self.val)

def dijkstra(grid_size, walls, start, end):
    rows, cols = grid_size
    walls = set(walls)  # Convert walls to a set for faster lookup

    directions = [
        1,       # Right
        1j,      # Down
        -1,      # Left
        -1j      # Up
    ]

    def neighbors(node):
        for direction in directions:
            neighbor = node + direction
            if 0 <= neighbor.real <= rows and 0 <= neighbor.imag <= cols and neighbor not in walls:
                yield neighbor

    pq = []  # Priority queue
    heapq.heappush(pq, (0, Vertex(start)))  # (distance, node)
    distances = {start: 0}
    visited = set()

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_node.val in visited:
            continue
        visited.add(current_node.val)

        # If we've reached the end node, return the distance
        if current_node.val == end:
            return current_dist

        for neighbor in neighbors(current_node.val):
            if neighbor not in visited:
                new_dist = current_dist + 1
                if neighbor not in distances or new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, Vertex(neighbor)))

    return None
