# Implement depth first search algorithm and breadth first search algorithm, Use an undirected graph and develop a recursive algorithm for 
# searching all the vertices of a graph or tree data structure

from collections import defaultdict, deque
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def add_edge(self, v, w):
        """Add an undirected edge between v and w"""
        self.graph[v].append(w)
        self.graph[w].append(v)
    def dfs_recursive(self, start, visited=None):
        """Recursive Depth First Search (DFS)"""
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=' ')
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)
    def bfs(self, start):
        """Breadth First Search (BFS)"""
        visited = set()
        queue = deque([start])
        visited.add(start)
        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
if __name__ == "__main__":
    g = Graph()
    # Adding edges
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(2, 6)
    print("DFS Recursive starting from vertex 0:")
    g.dfs_recursive(0)
    print("\nBFS starting from vertex 0:")
    g.bfs(0)
