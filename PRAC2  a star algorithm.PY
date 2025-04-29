# Implement A star algorithm for any game search problem.

import heapq
class Node:
    def __init__(self, position, parent=None):
        self.position = position  # (x, y)
        self.parent = parent
        self.g = 0  # Cost from start to current node
        self.h = 0  # Heuristic cost to goal
        self.f = 0  # Total cost
    def __lt__(self, other):
        return self.f < other.f
def heuristic(a, b):
    """Manhattan distance as the heuristic."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
def a_star_search(grid, start, goal):
    open_list = []
    closed_set = set()
    start_node = Node(start)
    goal_node = Node(goal)
    heapq.heappush(open_list, start_node)
    while open_list:
        current_node = heapq.heappop(open_list)
        if current_node.position == goal_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path
        closed_set.add(current_node.position)
        x, y = current_node.position
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor_pos = (x + dx, y + dy)
            if (0 <= neighbor_pos[0] < len(grid) and
                0 <= neighbor_pos[1] < len(grid[0]) and
                grid[neighbor_pos[0]][neighbor_pos[1]] == 0 and
                neighbor_pos not in closed_set):
                neighbor = Node(neighbor_pos, current_node)
                neighbor.g = current_node.g + 1
                neighbor.h = heuristic(neighbor_pos, goal)
                neighbor.f = neighbor.g + neighbor.h
                if any(open_node.position == neighbor.position and open_node.f <= neighbor.f for open_node in open_list):
                    continue
                heapq.heappush(open_list, neighbor)
    return None  
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
goal = (4, 4)
path = a_star_search(grid, start, goal)
if path:
    print("Path found:")
    print(path)
else:
    print("No path found.")